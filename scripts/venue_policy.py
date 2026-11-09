"""Evidence-backed CAS/CCF venue eligibility checks.

The policy is deliberately exact: a title or ISSN must match a registry entry
after conservative Unicode/punctuation normalization.  Unknown venues and
ambiguous short aliases remain pending; they are never promoted by fuzzy
similarity or by a parent conference's rank.
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


DEFAULT_POLICY = Path(__file__).resolve().parents[1] / "config" / "venue-policy.json"
KNOWN_FORMAL_CONFIDENCE = {
    "registered_is_preprint_of",
    "explicit_arxiv_doi_and_corroborated_metadata",
    "own_registered_doi",
    "registered_has_preprint",
}
PENDING_TRACKING_STATES = {
    "retry_pending",
    "needs_identity_review",
    "conflicting",
    "unknown",
    "pending",
}
PREPRINT_SOURCES = {"arxiv", "biorxiv", "medrxiv", "preprint", "europepmc_preprints"}
_POLICY_INDEX: Dict[int, Tuple[Mapping[str, Any], List[Mapping[str, Any]], List[Mapping[str, Any]]]] = {}


def _norm_text(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).casefold().strip()
    text = text.replace("&", " and ")
    return re.sub(r"[^\w]+", "", text, flags=re.UNICODE)


def _norm_issn(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).upper()
    text = re.sub(r"[^0-9X]", "", text)
    return text if re.fullmatch(r"[0-9]{7}[0-9X]", text) else ""


def _values(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return list(value)
    return [value]


def _text_values(value: Any) -> List[str]:
    result = []
    for item in _values(value):
        if isinstance(item, Mapping):
            for key in ("title", "name", "full_name", "conference", "journal_title"):
                if item.get(key):
                    result.append(str(item[key]))
        elif str(item).strip():
            result.append(str(item))
    return result


def _registries(policy: Mapping[str, Any]) -> Tuple[List[Mapping[str, Any]], List[Mapping[str, Any]]]:
    registries = policy.get("registries", {})
    cas = registries.get("cas_journals", policy.get("cas_journals", []))
    ccf = registries.get("ccf_venues", policy.get("ccf_venues", []))
    return list(cas or []), list(ccf or [])


def _prepare_policy(policy: Mapping[str, Any]) -> Tuple[List[Mapping[str, Any]], List[Mapping[str, Any]]]:
    """Validate once and cache normalized registry rows for repeated reviews."""
    key = id(policy)
    cached = _POLICY_INDEX.get(key)
    if cached is not None and cached[0] is policy:
        return cached[1], cached[2]
    errors = validate_policy(policy)
    if errors:
        raise ValueError("Invalid venue policy: " + "; ".join(errors[:8]))
    cas, ccf = _registries(policy)

    def indexed(rows):
        result = []
        for row in rows:
            copied = dict(row)
            copied["__aliases_norm"] = set(_record_aliases(row))
            copied["__issns_norm"] = _record_issns(row)
            result.append(copied)
        return result

    prepared = (policy, indexed(cas), indexed(ccf))
    _POLICY_INDEX[key] = prepared
    return prepared[1], prepared[2]


def load_policy(root: Optional[Any] = None) -> Dict[str, Any]:
    """Load and validate ``config/venue-policy.json``.

    ``root`` may be the repository path itself, which keeps callers in the
    pipeline independent of the current working directory.
    """
    base = Path(root) if root is not None else DEFAULT_POLICY.parents[1]
    path = base / "config" / "venue-policy.json"
    policy = json.loads(path.read_text(encoding="utf-8"))
    errors = validate_policy(policy)
    if errors:
        raise ValueError("Invalid venue policy: " + "; ".join(errors[:8]))
    return policy


def validate_policy(policy: Any) -> List[str]:
    """Return schema/registry errors without performing network access."""
    errors: List[str] = []
    if not isinstance(policy, Mapping):
        return ["policy must be an object"]
    rules = policy.get("rules")
    if not isinstance(rules, Mapping):
        errors.append("rules must be an object")
    else:
        for key, expected in (("cas_eligible_zones", {1, 2}), ("cas_ineligible_zones", {3, 4}),
                              ("ccf_eligible_ranks", {"A", "B"}), ("ccf_ineligible_ranks", {"C"})):
            values = rules.get(key)
            if not isinstance(values, list) or set(values) != expected:
                errors.append(f"rules.{key} must be {sorted(expected, key=str)}")
        if rules.get("unknown_status") != "pending":
            errors.append("rules.unknown_status must be pending")
        if rules.get("preprint_status") != "preprint":
            errors.append("rules.preprint_status must be preprint")
        if rules.get("workshop_inherits_parent_rank") is not False:
            errors.append("workshop_inherits_parent_rank must be false")

    sources = policy.get("sources")
    if not isinstance(sources, Mapping):
        errors.append("sources must be an object")
    else:
        for source_name in ("cas", "ccf"):
            source = sources.get(source_name)
            if not isinstance(source, Mapping):
                errors.append(f"sources.{source_name} must be an object")
                continue
            for key in ("edition", "title", "page_url", "download_url", "sha256", "rows"):
                if not source.get(key):
                    errors.append(f"sources.{source_name}.{key} is required")
            if source.get("sha256") and not re.fullmatch(r"[0-9a-f]{64}", str(source["sha256"])):
                errors.append(f"sources.{source_name}.sha256 is not SHA-256")
            if not isinstance(source.get("rows"), int) or source.get("rows", 0) < 1:
                errors.append(f"sources.{source_name}.rows must be positive")

    cas, ccf = _registries(policy)
    if not cas:
        errors.append("CAS journal registry is empty")
    if not ccf:
        errors.append("CCF venue registry is empty")
    if isinstance(sources, Mapping):
        if isinstance(sources.get("cas"), Mapping) and sources["cas"].get("rows") != len(cas):
            errors.append("CAS source row count does not match registry")
        if isinstance(sources.get("ccf"), Mapping) and sources["ccf"].get("rows") != len(ccf):
            errors.append("CCF source row count does not match registry")

    for index, row in enumerate(cas):
        if not isinstance(row, Mapping) or not str(row.get("title", "")).strip():
            errors.append(f"CAS row {index} lacks title")
            continue
        if row.get("zone") not in {1, 2, 3, 4}:
            errors.append(f"CAS row {index} has invalid zone")
        for issn in _values(row.get("issns")):
            if not _norm_issn(issn):
                errors.append(f"CAS row {index} has invalid ISSN")

    for index, row in enumerate(ccf):
        if not isinstance(row, Mapping) or not str(row.get("title", "")).strip():
            errors.append(f"CCF row {index} lacks title")
            continue
        if row.get("kind") not in {"journal", "conference"}:
            errors.append(f"CCF row {index} has invalid kind")
        if row.get("rank") not in {"A", "B", "C", "pending"}:
            errors.append(f"CCF row {index} has invalid rank")
        aliases = row.get("aliases", [])
        if aliases is not None and not isinstance(aliases, list):
            errors.append(f"CCF row {index}.aliases must be a list")
        for issn in _values(row.get("issns")):
            if not _norm_issn(issn):
                errors.append(f"CCF row {index} has invalid ISSN")
    return errors


def _record_aliases(record: Mapping[str, Any]) -> List[str]:
    values = [record.get("title"), record.get("name"), record.get("alias")]
    values.extend(_values(record.get("aliases")))
    result = []
    for value in values:
        if isinstance(value, Mapping):
            value = value.get("title") or value.get("name")
        normalized = _norm_text(value)
        if normalized and normalized not in result:
            result.append(normalized)
    return result


def _record_issns(record: Mapping[str, Any]) -> set:
    values = list(_values(record.get("issns"))) + list(_values(record.get("issn")))
    return {normalized for value in values if (normalized := _norm_issn(value))}


def _paper_journal(paper: Mapping[str, Any]) -> Tuple[List[str], set]:
    title = paper.get("journal_title", paper.get("journal"))
    if isinstance(title, Mapping):
        title = title.get("title") or title.get("name")
    issns = list(_values(paper.get("journal_issns", paper.get("issns"))))
    issns.extend(_values(paper.get("journal_issn")))
    return _text_values(title), {normalized for value in issns if (normalized := _norm_issn(value))}


def _paper_conference(paper: Mapping[str, Any]) -> List[str]:
    values = []
    for key in ("conference", "conference_title", "conference_name", "proceedings"):
        if paper.get(key):
            values.extend(_text_values(paper[key]))
    return values


def _paper_markers(paper: Mapping[str, Any]) -> str:
    values = []
    for key in ("publication_type", "publication_kind", "paper_type", "article_type", "kind", "venue_type", "conference_type"):
        if paper.get(key):
            values.extend(_text_values(paper[key]))
    return " ".join(values).casefold()


def _is_preprint(paper: Mapping[str, Any]) -> bool:
    if paper.get("is_preprint") is True or paper.get("preprint") is True:
        return True
    markers = _paper_markers(paper)
    source = str(paper.get("source", "")).casefold()
    return "preprint" in markers or source in PREPRINT_SOURCES or bool(paper.get("arxiv_id"))


def _formal_publications(paper: Mapping[str, Any]) -> List[Mapping[str, Any]]:
    result: List[Mapping[str, Any]] = []
    for key in ("formal_publications", "linked_formal_publications", "formal_publication"):
        for value in _values(paper.get(key)):
            if isinstance(value, Mapping):
                result.append(value)
            elif isinstance(value, str) and value.strip():
                result.append({"doi": value.strip()})
    return result


def _formal_identity_pending(paper: Mapping[str, Any]) -> bool:
    tracking = paper.get("publication_tracking")
    statuses = []
    if isinstance(tracking, Mapping):
        statuses.extend(_text_values(tracking.get("status")))
    elif tracking:
        statuses.extend(_text_values(tracking))
    if any(any(state in value.casefold() for state in PENDING_TRACKING_STATES) for value in statuses):
        return True
    if paper.get("formal_publication_doi") or paper.get("published_doi"):
        return True
    doi = str(paper.get("doi", "")).casefold()
    if (paper.get("arxiv_id") or str(paper.get("source", "")).casefold()=="arxiv") and doi and "10.48550/arxiv." not in doi and "arxiv.org" not in doi:
        return True
    return False


def _confidence_pending(paper: Mapping[str, Any]) -> bool:
    value = paper.get("confidence")
    if value is None:
        return False
    values = [str(item).casefold() for item in _values(value)]
    return not values or any(item not in KNOWN_FORMAL_CONFIDENCE for item in values)


def _evidence(source: str, record: Mapping[str, Any], policy: Mapping[str, Any]) -> Dict[str, Any]:
    source_meta = policy.get("sources", {}).get(source, {})
    result = {
        "source": source,
        "edition": source_meta.get("edition", ""),
        "kind": record.get("kind", "journal"),
        "title": record.get("title", ""),
        "rank": record.get("zone", record.get("rank", "")),
        "source_url": source_meta.get("page_url", ""),
        "source_document": source_meta.get("download_url", ""),
        "source_row": record.get("source_row"),
        "pdf_page": record.get("pdf_page"),
        "venue_url": record.get("source_url", ""),
    }
    if record.get("issns"):
        result["issns"] = list(record["issns"])
    return result


def _match_records(names: Sequence[str], issns: set, records: Sequence[Mapping[str, Any]]) -> Tuple[List[Mapping[str, Any]], bool]:
    normalized_names = {_norm_text(name) for name in names if _norm_text(name)}
    matches = []
    conflict = False
    for record in records:
        aliases = record.get("__aliases_norm", set()) or set(_record_aliases(record))
        record_issns = record.get("__issns_norm", set()) or _record_issns(record)
        title_match = bool(normalized_names & aliases)
        issn_match = bool(issns & record_issns)
        if title_match and issns and record_issns and not issn_match:
            conflict = True
            continue
        if issn_match and normalized_names and not title_match:
            conflict = True
            continue
        if title_match or issn_match:
            matches.append(record)
    return matches, conflict


def _result(status: str, reason: str, evidence: Iterable[Mapping[str, Any]], **extra: Any) -> Dict[str, Any]:
    value: Dict[str, Any] = {
        "status": status,
        "reason_zh": reason,
        "evidence": list(evidence),
        "eligible_for_human_review": status in {"eligible", "preprint"},
        "automatic_inclusion": False,
    }
    value.update(extra)
    return value


def _assess_non_preprint(
    paper: Mapping[str, Any],
    policy: Mapping[str, Any],
    prepared: Optional[Tuple[List[Mapping[str, Any]], List[Mapping[str, Any]]]] = None,
) -> Dict[str, Any]:
    if prepared is None:
        prepared = _prepare_policy(policy)
    cas, ccf = prepared
    journal_names, journal_issns = _paper_journal(paper)
    conference_names = _paper_conference(paper)
    markers = _paper_markers(paper)
    workshop = "workshop" in markers
    nonregular = any(token in markers for token in ("short", "demo", "technical brief", "summary", "findings"))
    evidence: List[Mapping[str, Any]] = []
    matched: List[Tuple[str, Mapping[str, Any]]] = []
    conflict = False
    if journal_names or journal_issns:
        rows, row_conflict = _match_records(journal_names, journal_issns, cas)
        conflict = conflict or row_conflict
        matched.extend(("cas", row) for row in rows)
        rows, row_conflict = _match_records(journal_names, journal_issns, [r for r in ccf if r.get("kind") == "journal"])
        conflict = conflict or row_conflict
        matched.extend(("ccf", row) for row in rows)
    if conference_names:
        rows, row_conflict = _match_records(conference_names, set(), [r for r in ccf if r.get("kind") == "conference"])
        conflict = conflict or row_conflict
        matched.extend(("ccf", row) for row in rows)

    for source, row in matched:
        evidence.append(_evidence(source, row, policy))

    if not matched:
        reason = "期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。"
        if conflict:
            reason = "题名与 ISSN 或注册表记录不一致，不能据此推断等级，保留待核验。"
        elif not (journal_names or journal_issns or conference_names):
            reason = "缺少可核验的 journal_title/journal_issns/conference 字段，保留待核验。"
        return _result("pending", reason, evidence, venue_fields={
            "journal_title": journal_names,
            "journal_issns": sorted(journal_issns),
            "conference": conference_names,
        })

    grouped_ranks: Dict[Tuple[str, str], set] = {}
    for source, row in matched:
        group = (source, str(row.get("kind", "journal")))
        grouped_ranks.setdefault(group, set()).add(row.get("zone", row.get("rank")))
    if conflict or any(len(ranks) > 1 for ranks in grouped_ranks.values()):
        return _result(
            "pending",
            "多个注册表记录或题名/ISSN证据相互冲突，不能选择较高等级，保留待核验。",
            evidence,
        )

    statuses = []
    for source, row in matched:
        rank = row.get("zone", row.get("rank"))
        if source == "cas":
            if rank in policy["rules"]["cas_eligible_zones"]:
                statuses.append("eligible")
            elif rank in policy["rules"]["cas_ineligible_zones"]:
                statuses.append("ineligible")
            else:
                statuses.append("pending")
        elif row.get("kind") == "journal":
            # The contract uses CCF only for A/B main conferences.  A CCF
            # journal record supplies no CAS partition evidence; A/B/C all
            # remain pending unless an independent CAS record qualifies it.
            statuses.append("pending")
        elif rank in policy["rules"]["ccf_eligible_ranks"]:
            statuses.append("eligible")
        elif rank in policy["rules"]["ccf_ineligible_ranks"]:
            statuses.append("ineligible")
        else:
            statuses.append("pending")

    if conference_names and (workshop or nonregular):
        return _result(
            "ineligible",
            "CCF仅将主会 Full/Regular paper 纳入目录考虑；Workshop 或非Regular形式不继承主会等级。",
            evidence,
            venue_fields={"conference": conference_names},
        )
    if "eligible" in statuses:
        return _result("eligible", "精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。", evidence)
    if "ineligible" in statuses:
        return _result("ineligible", "精确匹配到 CAS 3/4 区或 CCF C 类记录。", evidence)
    return _result("pending", "注册表记录存在，但等级不在当前可判定的范围内。", evidence)


def assess_venue(paper: Mapping[str, Any], policy: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
    """Assess one paper without inferring a rank from fuzzy venue similarity."""
    if not isinstance(paper, Mapping):
        return _result("pending", "文章记录不是对象，无法核验发表场所。", [])
    policy = load_policy() if policy is None else policy
    prepared = _prepare_policy(policy)

    if _is_preprint(paper):
        formal = _formal_publications(paper)
        identity_pending = _formal_identity_pending(paper)
        confidence_pending = _confidence_pending(paper)
        tracking = paper.get("publication_tracking")
        tracking_block = False
        tracking_values = []
        if isinstance(tracking, Mapping):
            tracking_values = _text_values(tracking.get("status"))
        elif tracking:
            tracking_values = _text_values(tracking)
        tracking_block = any(
            any(state in value.casefold() for state in PENDING_TRACKING_STATES)
            for value in tracking_values
        )
        if tracking_block:
            return _result(
                "pending",
                "正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。",
                [{"source": "paper", "kind": "preprint", "tracking_status": tracking_values}],
                formal_assessments=[],
            )
        if (identity_pending or confidence_pending) and not formal:
            return _result(
                "pending",
                "预印本存在待核验的正式发表身份或置信状态，不能绕过正式版本场所门禁。",
                [{"source": "paper", "kind": "preprint", "doi": paper.get("doi", "")}],
                formal_assessments=[],
            )
        assessments = []
        for item in formal:
            if _confidence_pending(item):
                assessments.append(_result(
                    "pending",
                    "正式版本关联置信度未知或冲突，不能据此授予正式发表资格。",
                    [{"source": "paper", "kind": "formal_publication", "confidence": item.get("confidence")}],
                ))
            else:
                assessments.append(_assess_non_preprint(item, policy, prepared))
        if confidence_pending:
            return _result(
                "pending",
                "正式版本关联置信度未知或冲突，不能据此授予正式发表资格。",
                [{"source": "paper", "kind": "preprint", "confidence": paper.get("confidence")}],
                formal_assessments=assessments,
            )
        if formal:
            if any(item["status"] == "pending" for item in assessments):
                return _result(
                    "pending",
                    "正式版本已关联但其场所或身份仍待核验，不能直接纳入。",
                    [{"source": "paper", "kind": "preprint", "doi": paper.get("doi", "")}],
                    formal_assessments=assessments,
                )
            if any(item["status"] == "ineligible" for item in assessments):
                return _result(
                    "ineligible",
                    "关联的正式版本不满足 CAS/CCF 场所门禁，预印本不能绕过该结果。",
                    [{"source": "paper", "kind": "preprint", "doi": paper.get("doi", "")}],
                    formal_assessments=assessments,
                )
            return _result(
                "eligible",
                "关联的正式版本通过 CAS/CCF 场所门禁；预印本仍需人工审核，不能自动纳入。",
                [{"source": "paper", "kind": "preprint", "doi": paper.get("doi", "")}],
                preprint=True,
                formal_assessments=assessments,
            )
        return _result(
            "preprint",
            "预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。",
            [{"source": "paper", "kind": "preprint", "doi": paper.get("doi", "")}],
            formal_assessments=[],
        )

    return _assess_non_preprint(paper, policy, prepared)


__all__ = ["assess_venue", "load_policy", "validate_policy"]
