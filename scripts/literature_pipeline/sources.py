"""Small standard-library adapters for date-bounded literature searches.

The adapters deliberately return a common record shape so that discovery,
deduplication and later human screening can be kept independent of a source's
API.  They do not make any claims about a paper's eligibility for the catalog.
"""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from typing import Any


USER_AGENT = (
    "Awesome-MedIA-Fairness literature pipeline/1.0 "
    "(+https://github.com/XuZikang/Awesome-MedIA-Fairness)"
)
_RETRIES = 3
_RETRY_WAIT = 1.0
_PAGE_SIZE = 100
_SOURCE_INTERVAL = {"arxiv": 3.0, "pubmed": 0.35, "europepmc": 0.0}
_LAST_REQUEST: dict[str, float] = {}


class SourceError(RuntimeError):
    """Raised when a source rejects a request or returns an invalid response."""


def _date(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except (TypeError, ValueError) as exc:
        raise ValueError(f"date must be YYYY-MM-DD: {value!r}") from exc


def _date_bounds(since: str, until: str) -> tuple[str, str]:
    start, end = _date(since), _date(until)
    if start > end:
        raise ValueError("since must not be later than until")
    return start, end


def _bounded_query(source: str, query: str, since: str, until: str) -> str:
    start, end = _date_bounds(since, until)
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a non-empty string")
    if source == "arxiv":
        return (
            f"({query.strip()}) AND submittedDate:["
            f"{start.replace('-', '')}0000 TO {end.replace('-', '')}2359]"
        )
    if source == "europepmc":
        return f"({query.strip()}) AND FIRST_PDATE:[{start} TO {end}]"
    if source == "pubmed":
        return (
            f'({query.strip()}) AND ("{start.replace("-", "/")}"[Date - Publication] : '
            f'"{end.replace("-", "/")}"[Date - Publication])'
        )
    raise ValueError(f"unknown source: {source!r}")


def _text(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return "".join(node.itertext()).strip()


def _strip_doi(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value, flags=re.I)
    value = re.sub(r"^doi:\s*", "", value, flags=re.I)
    return value.strip().rstrip(".")


def _iso_date(value: str) -> str:
    value = value.strip()
    match = re.search(r"(\d{4})[-/]?(\d{2})[-/]?(\d{2})", value)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    year = re.search(r"\b(19|20)\d{2}\b", value)
    return year.group(0) if year else ""


def _year(published: str) -> str:
    return published[:4] if published[:4].isdigit() else ""


def _record(**values: Any) -> dict[str, Any]:
    required = {
        "title": "",
        "abstract": "",
        "authors": [],
        "published": "",
        "updated": "",
        "year": "",
        "doi": "",
        "arxiv_id": "",
        "pmid": "",
        "pmcid": "",
        "url": "",
        "source": "",
        "source_id": "",
        "version": "",
        "is_open_access": False,
    }
    required.update(values)
    required["authors"] = [str(author).strip() for author in required["authors"] if str(author).strip()]
    required["title"] = str(required["title"]).strip()
    required["abstract"] = str(required["abstract"]).strip()
    required["published"] = str(required["published"])
    required["updated"] = str(required["updated"])
    required["year"] = required["year"] or _year(required["published"])
    required["doi"] = _strip_doi(str(required["doi"])) if required["doi"] else ""
    required["url"] = str(required["url"])
    required["source"] = str(required["source"])
    required["source_id"] = str(required["source_id"])
    required["version"] = str(required["version"])
    required["is_open_access"] = bool(required["is_open_access"])
    return required


def _throttle(source: str) -> None:
    interval = _SOURCE_INTERVAL[source]
    if interval <= 0:
        return
    now = time.monotonic()
    previous = _LAST_REQUEST.get(source)
    if previous is not None and now - previous < interval:
        time.sleep(interval - (now - previous))
    _LAST_REQUEST[source] = time.monotonic()


def _request(url: str, source: str, timeout: int) -> bytes:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/xml, application/json;q=0.9, */*;q=0.8"}
    for attempt in range(_RETRIES + 1):
        _throttle(source)
        request = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            transient = exc.code == 429 or 500 <= exc.code <= 599
            if not transient or attempt >= _RETRIES:
                raise SourceError(f"{source} HTTP {exc.code} for {url}") from exc
            time.sleep(_RETRY_WAIT * (2**attempt))
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            if attempt >= _RETRIES:
                raise SourceError(f"{source} request failed for {url}: {exc}") from exc
            time.sleep(_RETRY_WAIT * (2**attempt))
    raise SourceError(f"{source} request failed for {url}")


def _xml(payload: bytes, source: str) -> ET.Element:
    try:
        return ET.fromstring(payload)
    except ET.ParseError as exc:
        raise SourceError(f"{source} returned invalid XML") from exc


def _json(payload: bytes, source: str) -> dict[str, Any]:
    try:
        value = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SourceError(f"{source} returned invalid JSON") from exc
    if not isinstance(value, dict):
        raise SourceError(f"{source} returned a non-object JSON response")
    return value


def _tag(node: ET.Element) -> str:
    return node.tag.rsplit("}", 1)[-1]


def _children(node: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in node.iter() if _tag(child) == name]


def _first(node: ET.Element, *names: str) -> ET.Element | None:
    for name in names:
        for child in node.iter():
            if _tag(child) == name:
                return child
    return None


def _arxiv_id(raw: str) -> tuple[str, str]:
    value = raw.rsplit("/", 1)[-1].strip()
    match = re.match(r"(.+?)(v(\d+))?$", value, flags=re.I)
    if not match:
        return value, ""
    # Keep the version as digits: downstream full-text adapters add the ``v``
    # prefix when constructing an arXiv HTML URL.
    return match.group(1), (match.group(3) or "")


def _parse_arxiv(payload: bytes) -> tuple[list[dict[str, Any]], int]:
    root = _xml(payload, "arxiv")
    feed_title = _text(_first(root, "title")).lower()
    entries = [child for child in list(root) if _tag(child) == "entry"]
    for entry in entries:
        entry_id = _text(_first(entry, "id"))
        title = _text(_first(entry, "title"))
        if "/api/errors/" in entry_id.lower() or title.lower().startswith("error"):
            raise SourceError(f"arxiv API error: {title or entry_id}")
    if "error" in feed_title and not entries:
        raise SourceError(f"arxiv API error: {feed_title}")
    records: list[dict[str, Any]] = []
    for entry in entries:
        identifier, version = _arxiv_id(_text(_first(entry, "id")))
        if not identifier or not _text(_first(entry, "title")):
            raise SourceError("arxiv returned an entry without an id or title")
        published = _iso_date(_text(_first(entry, "published")))
        updated = _text(_first(entry, "updated"))
        records.append(
            _record(
                title=_text(_first(entry, "title")),
                abstract=_text(_first(entry, "summary")),
                authors=[_text(author) for author in _children(entry, "author")],
                published=published,
                updated=updated,
                year=_year(published),
                doi=_text(_first(entry, "doi")),
                arxiv_id=identifier,
                url=f"https://arxiv.org/abs/{identifier}",
                source="arxiv",
                source_id=identifier,
                version=version,
                is_open_access=True,
            )
        )
    total_node = _first(root, "totalResults")
    if total_node is None:
        raise SourceError("arxiv response is missing totalResults")
    try:
        total = int(_text(total_node))
    except ValueError as exc:
        raise SourceError("arxiv returned an invalid totalResults value") from exc
    return records, total


def _parse_europepmc(payload: bytes) -> tuple[list[dict[str, Any]], int, str]:
    root = _xml(payload, "europepmc")
    errors = [_text(node) for node in _children(root, "errMsg") + _children(root, "error") if _text(node)]
    if errors:
        raise SourceError(f"Europe PMC API error: {'; '.join(errors)}")
    records: list[dict[str, Any]] = []
    result_nodes = [node for node in root.iter() if _tag(node) == "result"]
    for result in result_nodes:
        raw_id = _text(_first(result, "id"))
        source_name = _text(_first(result, "source")).upper() or "MED"
        pmid = _text(_first(result, "pmid"))
        pmcid = _text(_first(result, "pmcid"))
        if source_name == "MED" and not pmid:
            pmid = raw_id
        if source_name == "PMC" and not pmcid and raw_id:
            pmcid = raw_id if raw_id.upper().startswith("PMC") else "PMC" + raw_id
        source_id = pmid or pmcid or raw_id
        title = _text(_first(result, "title"))
        if not source_id or not title:
            raise SourceError("Europe PMC returned a result without an id or title")
        doi = _text(_first(result, "doi"))
        published = _iso_date(
            _text(_first(result, "firstPublicationDate", "electronicPublicationDate", "publicationDate"))
        )
        updated = _text(_first(result, "firstIndexDate", "dateOfCompletion"))
        authors: list[str] = []
        for author in _children(result, "author"):
            authors.append(_text(_first(author, "fullName")) or _text(author))
        oa = _text(_first(result, "isOpenAccess")).lower() in {"y", "yes", "true", "1"}
        if not oa:
            for url_node in _children(result, "fullTextUrl"):
                availability = _text(_first(url_node, "availability")).lower()
                if availability in {"open access", "free", "oa"}:
                    oa = True
                    break
        canonical_id = pmid or pmcid or source_id
        records.append(
            _record(
                title=title,
                abstract=_text(_first(result, "abstractText", "abstract")),
                authors=authors,
                published=published,
                updated=updated,
                year=_year(published),
                doi=doi,
                pmid=pmid,
                pmcid=pmcid,
                url=f"https://europepmc.org/article/{source_name}/{canonical_id}",
                source="europepmc",
                source_id=source_id,
                is_open_access=oa,
            )
        )
    total_node = _first(root, "hitCount")
    if total_node is None:
        raise SourceError("Europe PMC response is missing hitCount")
    try:
        total = int(_text(total_node))
    except ValueError as exc:
        raise SourceError("Europe PMC returned an invalid hitCount value") from exc
    next_cursor = _text(_first(root, "nextCursorMark"))
    return records, total, next_cursor


def _pubmed_warning(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, dict):
        result: list[str] = []
        for key, item in value.items():
            result.extend(f"{key}: {message}" for message in _pubmed_warning(item))
        return result
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def _pubmed_search(payload: bytes, source: str) -> tuple[list[str], int]:
    data = _json(payload, source)
    result = data.get("esearchresult")
    if not isinstance(result, dict):
        raise SourceError("PubMed response has no esearchresult object")
    if result.get("ERROR") or result.get("Error"):
        raise SourceError(f"PubMed query error: {result.get('ERROR') or result.get('Error')}")
    errors = _pubmed_warning(result.get("ErrorList") or result.get("errorlist"))
    if errors:
        raise SourceError(f"PubMed query error: {'; '.join(errors)}")
    warnings = _pubmed_warning(result.get("WarningList") or result.get("warninglist"))
    fatal_warnings = [item for item in warnings if "outputmessages: no items found" not in item.lower()]
    if fatal_warnings:
        raise SourceError(f"PubMed query warning: {'; '.join(fatal_warnings)}")
    if "count" not in result:
        raise SourceError("PubMed response is missing count")
    if "idlist" not in result:
        raise SourceError("PubMed response is missing idlist")
    try:
        total = int(result["count"])
    except (TypeError, ValueError) as exc:
        raise SourceError("PubMed returned an invalid count") from exc
    ids = result["idlist"]
    if not isinstance(ids, list) or any(not isinstance(item, str) for item in ids):
        raise SourceError("PubMed returned an invalid idlist")
    return ids, total


_MONTHS = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


def _pubmed_structured_date(node: ET.Element | None) -> str:
    if node is None:
        return ""
    year = _text(_first(node, "Year"))
    month_text = _text(_first(node, "Month"))
    day_text = _text(_first(node, "Day"))
    if not year.isdigit() or not month_text or not day_text.isdigit():
        return ""
    month = int(month_text) if month_text.isdigit() else _MONTHS.get(month_text[:3].lower(), 0)
    try:
        return date(int(year), month, int(day_text)).isoformat() if month else ""
    except ValueError:
        return ""


def _pubmed_date(article: ET.Element) -> str:
    date_node = _first(article, "ArticleDate")
    value = _pubmed_structured_date(date_node)
    if value:
        return value
    pub_date = _first(article, "PubDate")
    value = _pubmed_structured_date(pub_date)
    if value:
        return value
    year = _text(_first(pub_date, "Year")) if pub_date is not None else ""
    if re.fullmatch(r"\d{4}", year):
        return year  # Do not invent a day when PubMed only supplies an issue month/year.
    return _iso_date(_text(pub_date)) if pub_date is not None else ""


def _parse_pubmed(payload: bytes) -> list[dict[str, Any]]:
    root = _xml(payload, "pubmed")
    errors = [_text(node) for node in root.iter() if _tag(node).upper() == "ERROR" and _text(node)]
    if errors:
        raise SourceError(f"PubMed fetch error: {'; '.join(errors)}")
    records: list[dict[str, Any]] = []
    for article in [node for node in root.iter() if _tag(node) == "PubmedArticle"]:
        citation = _first(article, "MedlineCitation") or article
        article_meta = _first(citation, "Article") or citation
        pmid = _text(_first(citation, "PMID"))
        pmcid = ""
        for identifier in _children(article, "ArticleId"):
            if (identifier.attrib.get("IdType") or "").lower() == "pmc":
                pmcid = _text(identifier)
                break
        doi = ""
        for identifier in _children(article, "ArticleId"):
            if (identifier.attrib.get("IdType") or "").lower() == "doi":
                doi = _text(identifier)
                break
        published = _pubmed_date(article_meta)
        title = _text(_first(article_meta, "ArticleTitle"))
        if not pmid or not title:
            raise SourceError("PubMed returned an article without a PMID or title")
        updated_node = _first(article, "DateRevised", "DateCompleted")
        updated = _pubmed_structured_date(updated_node) or _text(updated_node)
        authors: list[str] = []
        for author in _children(article_meta, "Author"):
            name = _text(_first(author, "CollectiveName"))
            if not name:
                name = " ".join(
                    part for part in (_text(_first(author, "ForeName")), _text(_first(author, "LastName"))) if part
                )
            if name:
                authors.append(name)
        abstract_parts = []
        for node in _children(article_meta, "AbstractText"):
            label = node.attrib.get("Label")
            text = _text(node)
            abstract_parts.append(f"{label}: {text}" if label and text else text)
        oa_values = [
            _text(node).lower()
            for node in article.iter()
            if _tag(node).lower() in {"isopenaccess", "openaccess", "oastatus", "availability"}
        ]
        is_open_access = any(value in {"y", "yes", "true", "1", "open access", "free", "oa"} for value in oa_values)
        records.append(
            _record(
                title=title,
                abstract=" ".join(part for part in abstract_parts if part),
                authors=authors,
                published=published,
                updated=updated,
                year=_year(published),
                doi=doi,
                pmid=pmid,
                pmcid=pmcid,
                url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
                source="pubmed",
                source_id=pmid,
                is_open_access=is_open_access,
            )
        )
    return records


def _url(base: str, params: dict[str, Any]) -> str:
    return f"{base}?{urllib.parse.urlencode(params)}"


def _fetch_arxiv(query: str, since: str, until: str, max_records: int, timeout: int) -> dict[str, Any]:
    final_query = _bounded_query("arxiv", query, since, until)
    records: list[dict[str, Any]] = []
    total = 0
    start = 0
    while len(records) < max_records:
        page_size = min(_PAGE_SIZE, max_records - len(records))
        url = _url(
            "https://export.arxiv.org/api/query",
            {"search_query": final_query, "start": start, "max_results": page_size, "sortBy": "submittedDate", "sortOrder": "descending"},
        )
        page, reported_total = _parse_arxiv(_request(url, "arxiv", timeout))
        total = reported_total
        records.extend(page[: max_records - len(records)])
        if not page or len(page) < page_size or start + len(page) >= reported_total:
            break
        start += len(page)
    complete = len(records) < max_records and (total == 0 or len(records) >= total)
    if len(records) >= max_records and total > len(records):
        complete = False
    return {"records": records, "complete": complete, "total": total, "query": final_query}


def _fetch_europepmc(query: str, since: str, until: str, max_records: int, timeout: int) -> dict[str, Any]:
    final_query = _bounded_query("europepmc", query, since, until)
    records: list[dict[str, Any]] = []
    total = 0
    cursor = "*"
    while len(records) < max_records:
        page_size = min(_PAGE_SIZE, max_records - len(records))
        url = _url(
            "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
            {"query": final_query, "format": "xml", "resultType": "core", "pageSize": page_size, "cursorMark": cursor},
        )
        batch, reported_total, next_cursor = _parse_europepmc(_request(url, "europepmc", timeout))
        total = reported_total
        records.extend(batch[: max_records - len(records)])
        if not batch or len(records) >= max_records or len(records) >= reported_total:
            break
        if not next_cursor or next_cursor == cursor:
            break
        cursor = next_cursor
    complete = len(records) < max_records and (total == 0 or len(records) >= total)
    if len(records) >= max_records and total > len(records):
        complete = False
    return {"records": records, "complete": complete, "total": total, "query": final_query}


def _fetch_pubmed(query: str, since: str, until: str, max_records: int, timeout: int, email: str) -> dict[str, Any]:
    final_query = _bounded_query("pubmed", query, since, until)
    records: list[dict[str, Any]] = []
    total = 0
    start = 0
    while len(records) < max_records:
        page_size = min(_PAGE_SIZE, max_records - len(records))
        params: dict[str, Any] = {"db": "pubmed", "term": final_query, "retmode": "json", "retstart": start, "retmax": page_size}
        if email:
            params["email"] = email
        ids, reported_total = _pubmed_search(_request(_url("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", params), "pubmed", timeout), "pubmed")
        total = reported_total
        if ids:
            fetch_params: dict[str, Any] = {"db": "pubmed", "id": ",".join(ids), "retmode": "xml"}
            if email:
                fetch_params["email"] = email
            batch = _parse_pubmed(_request(_url("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", fetch_params), "pubmed", timeout))
            if len(batch) < len(ids):
                raise SourceError("PubMed returned fewer articles than requested")
            records.extend(batch[: max_records - len(records)])
        if not ids or len(ids) < page_size or start + len(ids) >= reported_total:
            break
        start += len(ids)
    complete = len(records) < max_records and (total == 0 or len(records) >= total)
    if len(records) >= max_records and total > len(records):
        complete = False
    return {"records": records, "complete": complete, "total": total, "query": final_query}


def fetch_source(
    source: str,
    query: str,
    since: str,
    until: str,
    *,
    max_records: int = 500,
    timeout: int = 30,
    email: str = "",
) -> dict[str, Any]:
    """Fetch one date-bounded source and return a common, truncation-aware result."""

    if source not in {"arxiv", "europepmc", "pubmed"}:
        raise ValueError(f"unknown source: {source!r}")
    if not isinstance(max_records, int) or max_records <= 0:
        raise ValueError("max_records must be a positive integer")
    if not isinstance(timeout, int) or timeout <= 0:
        raise ValueError("timeout must be a positive integer")
    _date_bounds(since, until)
    if source == "arxiv":
        return _fetch_arxiv(query, since, until, max_records, timeout)
    if source == "europepmc":
        return _fetch_europepmc(query, since, until, max_records, timeout)
    return _fetch_pubmed(query, since, until, max_records, timeout, email)


__all__ = ["SourceError", "fetch_source", "USER_AGENT"]
