"""Bounded discovery adapters for medRxiv and official conference lists.

These adapters deliberately keep source-specific discovery separate from the
arXiv, PubMed and Europe PMC adapters.  A record is only a discovery lead.  It
does not imply venue eligibility, human approval or inclusion in the catalog.

Configuration examples (the event URLs must be maintained as official source
pages by the caller)::

    {"base_url": "https://api.medrxiv.org/details/medrxiv",
     "page_size": 100, "max_records": 500}

    {"event_window_days": 30, "max_records": 500, "events": [
        {"name": "MICCAI 2026",
         "url": "https://papers.miccai.org/miccai-2026/",
         "format": "html", "event_date": "2026-10-...",
         "conference": "MICCAI", "rank": "B",
         "status": "published", "link_pattern": "/paper/"}
    ]}

medRxiv records keep the preprint DOI in ``doi`` and an independently
reported journal DOI, if provided, in ``published_doi``.  Conference records
distinguish ``conference-paper`` (official proceedings evidence) from
``conference-accepted`` (an acceptance list only).  A conference/event date
is never copied into ``published``; it is only a bounded fallback for finding
undated official lists.
"""

from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from html.parser import HTMLParser
from typing import Any


USER_AGENT = (
    "Awesome-MedIA-Fairness discovery/1.0 "
    "(+https://github.com/XuZikang/Awesome-MedIA-Fairness)"
)
_RETRIES = 2
_RETRY_WAIT = 0.5


class DiscoveryError(RuntimeError):
    """Raised when a configured discovery source is invalid or unavailable."""


def _bounds(since: str, until: str) -> tuple[date, date]:
    try:
        start, end = date.fromisoformat(since), date.fromisoformat(until)
    except (TypeError, ValueError) as exc:
        raise ValueError("dates must use YYYY-MM-DD") from exc
    if start > end:
        raise ValueError("since must not be later than until")
    return start, end


def _iso(value: Any) -> str:
    if isinstance(value, dict):
        for key in ("value", "date", "timestamp", "created"):
            if key in value:
                parsed = _iso(value[key])
                if parsed:
                    return parsed
        return ""
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        try:
            timestamp = float(value)
            if timestamp > 10**11:
                timestamp /= 1000.0
            if timestamp > 10**8:
                return datetime.fromtimestamp(timestamp, tz=timezone.utc).date().isoformat()
        except (OverflowError, OSError, ValueError):
            return ""
    text = str(value or "").strip()
    match = re.search(r"(\d{4})[-/]?(\d{2})[-/]?(\d{2})", text)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    match = re.search(r"\b((?:19|20)\d{2})\b", text)
    return match.group(1) if match else ""


def _authors(value: Any) -> list[str]:
    if isinstance(value, list):
        result = []
        for item in value:
            if isinstance(item, dict):
                name = item.get("name") or item.get("fullName")
                if not name:
                    name = " ".join(str(item.get(k, "")).strip() for k in ("given", "family") if item.get(k))
            else:
                name = str(item)
            if str(name).strip():
                result.append(str(name).strip())
        return result
    text = str(value or "").strip()
    return [part.strip() for part in re.split(r"\s*;\s*|\s*\|\s*", text) if part.strip()]


def _doi(value: Any) -> str:
    text = str(value or "").strip()
    text = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text, flags=re.I)
    text = re.sub(r"^doi:\s*", "", text, flags=re.I).rstrip(".")
    if text.lower() in {"na", "n/a", "none", "null", "not available", "-"}:
        return ""
    return text


def _scalar(value: Any) -> Any:
    """Unwrap OpenReview-style ``{"value": ...}`` fields recursively."""
    while isinstance(value, dict) and set(value) == {"value"}:
        value = value["value"]
    return value


def _conference_kind(raw: dict[str, Any], spec: dict[str, Any]) -> tuple[str, str]:
    explicit = str(_scalar(raw.get("publication_kind") or raw.get("kind") or "")).strip().lower()
    status = str(_scalar(raw.get("conference_status") or raw.get("status") or raw.get("decision") or spec.get("status") or "")).strip()
    status_key = re.sub(r"[\s_]+", "-", status.lower())
    if explicit:
        kind = explicit
    elif status_key in {"published", "proceedings", "official-proceedings", "main-published", "camera-ready", "regular-published"}:
        kind = "conference-paper"
    elif status_key in {"accepted", "accept", "accepted-main", "main", "main-accepted", "oral", "spotlight", "poster"}:
        # An acceptance list is not evidence of a formally published paper.
        kind = "conference-accepted"
    elif status_key in {"submitted", "submission", "under-review", "under-reviewing", "review"}:
        kind = "conference-submitted"
    elif status_key in {"rejected", "reject", "withdrawn", "desk-reject"}:
        kind = "conference-rejected"
    else:
        # An unspecified source status is deliberately left as a paper lead;
        # venue/rank policy decides whether it can be considered downstream.
        kind = "conference-paper"
    if status_key in {"accepted", "accept", "main", "main-accepted"}:
        status = "accepted-main"
    elif status_key in {"published", "proceedings", "official-proceedings", "main-published", "camera-ready", "regular-published"}:
        status = "published-main"
    return kind, status


_PDF_HOSTS = {
    "openaccess.thecvf.com",
    "proceedings.mlr.press",
}


def _allowlisted_pdf(value: Any) -> str:
    candidate = str(_scalar(value) or "").strip()
    if not candidate:
        return ""
    try:
        parsed = urllib.parse.urlparse(candidate)
    except ValueError:
        return ""
    if parsed.scheme not in {"http", "https"} or parsed.hostname not in _PDF_HOSTS:
        return ""
    return candidate


def _record(raw: dict[str, Any], source: str, spec: dict[str, Any], index: int) -> dict[str, Any]:
    title = str(_scalar(raw.get("title") or raw.get("Title") or raw.get("name") or "")).strip()
    if source == "conference":
        # Acceptance/decision/created dates are useful for filtering, but do
        # not establish proceedings publication and therefore stay separate.
        published = _iso(_scalar(raw.get("published") or raw.get("publication_date") or raw.get("date")))
    else:
        # medRxiv's "published" field is the journal DOI or NA, not a date.
        published = _iso(_scalar(raw.get("date") or raw.get("posted") or raw.get("publication_date") or raw.get("created")))
    accepted_date = _iso(_scalar(raw.get("accepted") or raw.get("decision") or raw.get("created")))
    updated = _iso(_scalar(raw.get("updated") or raw.get("modified") or raw.get("last_updated")))
    doi = _doi(_scalar(raw.get("doi") or raw.get("DOI") or raw.get("doi_url") or raw.get("preprint_doi")))
    formal = raw.get("published_doi") or raw.get("rel_doi") or raw.get("related_doi") or raw.get("journal_doi")
    if source == "medrxiv":
        formal = formal or raw.get("published")
        updated = updated or published
    published_doi = _doi(_scalar(formal))
    version = str(_scalar(raw.get("version") or raw.get("Version") or "")).strip()
    url = str(_scalar(raw.get("url") or raw.get("link") or raw.get("paper_url") or "")).strip()
    full_text_pdf = _allowlisted_pdf(raw.get("full_text_pdf") or raw.get("pdf_url") or raw.get("pdf") or raw.get("pdfUrl"))
    if not url and full_text_pdf:
        url = full_text_pdf
    if not url and doi:
        host = "www.medrxiv.org" if source == "medrxiv" else "doi.org"
        url = f"https://{host}/content/{doi}" if source == "medrxiv" else f"https://doi.org/{doi}"
    if source == "medrxiv" and doi and version and "/content/" in url and not re.search(r"v\d+$", url):
        url += f"v{version}"
    if not title or not url:
        raise DiscoveryError(f"{source} record {index} has no title or URL")
    source_id = str(_scalar(raw.get("id") or raw.get("paper_id") or raw.get("forum") or doi or hashlib.sha256(title.encode()).hexdigest()[:20]))
    event = str(_scalar(raw.get("conference") or raw.get("venue") or spec.get("conference") or spec.get("name") or "")).strip()
    if source == "medrxiv":
        publication_kind = "preprint"
        conference_status = ""
    else:
        publication_kind, conference_status = _conference_kind(raw, spec)
    explicit_status = str(_scalar(raw.get("conference_status") or raw.get("status") or raw.get("decision") or "")).strip()
    if explicit_status:
        _, conference_status = _conference_kind({"conference_status": explicit_status}, spec)
    event_date = _iso(_scalar(raw.get("event_date") or spec.get("event_date")))
    return {
        "title": title,
        "abstract": str(_scalar(raw.get("abstract") or raw.get("summary") or raw.get("description") or "")).strip(),
        "authors": _authors(_scalar(raw.get("authors") or raw.get("author"))),
        "published": published,
        "accepted_date": accepted_date,
        "updated": updated,
        "year": published[:4] if published[:4].isdigit() else "",
        "doi": doi,
        "published_doi": published_doi,
        "arxiv_id": "",
        "pmid": "",
        "pmcid": "",
        "url": url,
        "full_text_pdf": full_text_pdf,
        "source": source,
        "source_id": source_id,
        "version": version,
        "is_open_access": True,
        "publication_kind": publication_kind,
        "journal_title": "",
        "journal_issns": [],
        "conference": event,
        "conference_rank": str(raw.get("conference_rank") or spec.get("rank") or ""),
        "conference_status": conference_status,
        "event_date": event_date,
        "discovery_lane": source,
    }


def _request(url: str, timeout: int) -> bytes:
    if not isinstance(timeout, int) or timeout <= 0:
        raise ValueError("timeout must be positive")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json, application/xml, text/html;q=0.9, */*;q=0.8"})
    for attempt in range(_RETRIES + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            if exc.code not in {408, 429} and not 500 <= exc.code <= 599:
                raise DiscoveryError(f"HTTP {exc.code} for {url}") from exc
            if attempt >= _RETRIES:
                raise DiscoveryError(f"HTTP {exc.code} for {url}") from exc
            time.sleep(_RETRY_WAIT * (attempt + 1))
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            if attempt >= _RETRIES:
                raise DiscoveryError(f"request failed for {url}") from exc
            time.sleep(_RETRY_WAIT * (attempt + 1))
    raise DiscoveryError(f"request failed for {url}")


def _json(payload: bytes, source: str) -> Any:
    try:
        return json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise DiscoveryError(f"{source} returned invalid JSON") from exc


def _items(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    if not isinstance(value, dict):
        return []
    for key in ("collection", "records", "papers", "items", "results", "notes"):
        candidate = value.get(key)
        if isinstance(candidate, list):
            return [item for item in candidate if isinstance(item, dict)]
    return [value]


def _openreview_items(value: Any) -> list[dict[str, Any]]:
    """Flatten OpenReview v1/v2 notes into the common record shape."""
    result: list[dict[str, Any]] = []
    for item in _items(value):
        content = item.get("content")
        merged: dict[str, Any] = {}
        if isinstance(content, dict):
            for key, field in content.items():
                merged[key] = _scalar(field)
        for key, field in item.items():
            if key != "content" and key not in merged:
                merged[key] = _scalar(field)
        forum = str(_scalar(item.get("forum") or item.get("id") or merged.get("forum") or "")).strip()
        if forum and not merged.get("url") and not merged.get("link"):
            merged["url"] = f"https://openreview.net/forum?id={urllib.parse.quote(forum, safe='')}"
        if item.get("id") and not merged.get("id"):
            merged["id"] = item["id"]
        result.append(merged)
    return result


class _AtomParser:
    def __init__(self, base_url: str = "") -> None:
        self.records: list[dict[str, Any]] = []
        self.base_url = base_url

    def parse(self, payload: bytes) -> list[dict[str, Any]]:
        try:
            root = ET.fromstring(payload)
        except ET.ParseError as exc:
            raise DiscoveryError("conference source returned invalid XML") from exc
        for entry in [node for node in root.iter() if node.tag.rsplit("}", 1)[-1] in {"entry", "item", "record"}]:
            values: dict[str, Any] = {}
            for child in list(entry):
                key = child.tag.rsplit("}", 1)[-1].lower()
                text = "".join(child.itertext()).strip()
                if key in {"title", "summary", "description", "id", "published", "updated", "doi"}:
                    values[key] = text
                elif key == "author":
                    values.setdefault("authors", []).append(text)
                elif key == "link":
                    href = urllib.parse.urljoin(self.base_url, child.attrib.get("href", text))
                    relation = (child.attrib.get("rel") or "").lower()
                    if not values.get("url") or relation in {"alternate", "related"}:
                        values["url"] = href
            self.records.append(values)
        return self.records


class _HtmlParser(HTMLParser):
    """Small parser for official lists exposing citation metadata or paper links."""
    def __init__(self, base_url: str, link_pattern: str = "", allow_headings: bool = False) -> None:
        super().__init__()
        self.records: list[dict[str, Any]] = []
        self.current: dict[str, Any] | None = None
        self.capture = False
        self.buffer: list[str] = []
        self.base_url = base_url
        self.link_pattern = re.compile(link_pattern) if link_pattern else None
        self.allow_headings = allow_headings
        self.meta_record: dict[str, Any] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        name = (attr.get("name") or attr.get("property") or "").lower()
        if tag == "meta":
            content = attr.get("content", "") or ""
            if name in {"citation_title", "dc.title", "og:title"}:
                self.meta_record["title"] = content
            elif name in {"citation_pdf_url", "citation_fulltext_html_url"}:
                self.meta_record["full_text_pdf"] = content
                self.meta_record["url"] = content
            elif name in {"citation_doi", "dc.identifier"}:
                self.meta_record["doi"] = content
            elif name in {"citation_publication_date", "dc.date"}:
                self.meta_record["published"] = content
            elif name == "citation_author":
                self.meta_record.setdefault("authors", []).append(content)
            return
        if tag == "a" and attr.get("href"):
            href = urllib.parse.urljoin(self.base_url, attr["href"])
            parsed = urllib.parse.urlparse(href)
            if parsed.scheme not in {"http", "https"}:
                return
            if self.link_pattern and not self.link_pattern.search(href):
                return
            # Without an explicit pattern, keep links that look like paper
            # records and ignore site navigation such as /about or /login.
            if not self.link_pattern and not re.search(r"(?:/paper(?:s)?/|/article/|/abs/|/content/|/forum\?|\.pdf(?:$|[?#]))", parsed.path + ("?" + parsed.query if parsed.query else ""), re.I):
                return
            self.current = {"url": href}
            self.capture = True
            self.buffer = []
        elif tag in {"h2", "h3", "h4", "li"}:
            self.capture = True
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.capture and ((tag == "a" and self.current is not None) or tag in {"h2", "h3", "h4", "li"}):
            text = " ".join("".join(self.buffer).split())
            if text and (self.current is not None):
                self.current["title"] = text
                self.records.append(self.current)
            elif text and tag in {"h2", "h3", "h4"} and self.allow_headings:
                self.records.append({"title": text})
            self.current = None
            self.buffer = []
            self.capture = False

    def finish(self) -> list[dict[str, Any]]:
        if self.meta_record.get("title") and self.meta_record.get("url"):
            self.records.insert(0, dict(self.meta_record))
        return self.records


def _parse_conference(payload: bytes, fmt: str, spec: dict[str, Any]) -> list[dict[str, Any]]:
    if fmt == "openreview":
        value = _json(payload, "conference")
        return _openreview_items(value)
    if fmt == "json":
        value = _json(payload, "conference")
        return _items(value)
    if fmt == "atom" or fmt == "xml":
        return _AtomParser(str(spec.get("url", ""))).parse(payload)
    parser = _HtmlParser(
        str(spec.get("url", "")),
        link_pattern=str(spec.get("link_pattern", "")),
        allow_headings=bool(spec.get("allow_headings", False)),
    )
    parser.feed(payload.decode("utf-8", errors="replace"))
    return parser.finish()


def fetch_medrxiv(since: str, until: str, config: dict[str, Any] | None = None) -> tuple[list[dict[str, Any]], bool, int]:
    """Fetch date-bounded medRxiv records using the official details API.

    The API uses a cursor offset rather than a page token.  ``complete`` is
    false when ``max_records`` truncates a reported result set.
    """
    start, end = _bounds(since, until)
    cfg = dict(config or {})
    base = str(cfg.get("base_url", "https://api.medrxiv.org/details/medrxiv")).rstrip("/")
    timeout = int(cfg.get("timeout", 30))
    maximum = int(cfg.get("max_records", 500))
    page_size = int(cfg.get("page_size", 100))
    parsed_base = urllib.parse.urlparse(base)
    if parsed_base.scheme not in {"http", "https"} or not parsed_base.netloc:
        raise ValueError("base_url must be an absolute HTTP(S) URL")
    if maximum <= 0:
        raise ValueError("max_records must be positive")
    if page_size <= 0:
        raise ValueError("page_size must be positive")
    records: list[dict[str, Any]] = []
    total = 0
    cursor = 0
    exhausted = False
    seen_cursors: set[int] = set()
    while len(records) < maximum:
        if cursor in seen_cursors:
            raise DiscoveryError("medRxiv pagination repeated a cursor")
        seen_cursors.add(cursor)
        url = f"{base}/{start.isoformat()}/{end.isoformat()}/{cursor}/json"
        data = _json(_request(url, timeout), "medrxiv")
        batch = _items(data)
        if not batch:
            exhausted = True
            break
        messages = data.get("messages") if isinstance(data, dict) else None
        if isinstance(messages, list):
            for message in messages:
                if isinstance(message, dict):
                    for key in ("total", "total_count", "count"):
                        value = _scalar(message.get(key, ""))
                        if isinstance(value, (int, float)) or str(value).isdigit():
                            total = max(total, int(value))
        for index, raw in enumerate(batch):
            record = _record(raw, "medrxiv", cfg, cursor + index)
            records.append(record)
            if len(records) >= maximum:
                break
        cursor += len(batch)
        if total > 0:
            # The API's ``total`` is authoritative; its page ``count`` may
            # be smaller than the caller's configured page_size (currently
            # the service commonly returns 30 rows per request).
            if cursor >= total:
                exhausted = True
                break
        elif len(batch) < page_size:
            exhausted = True
            break
    if total == 0:
        total = len(records)
    complete = exhausted and (total <= len(records) or len(records) < maximum)
    if total > 0 and len(records) >= total:
        complete = True
    return records, complete, total


def fetch_conference(since: str, until: str, config: dict[str, Any] | None = None) -> tuple[list[dict[str, Any]], bool, int]:
    """Fetch configured official conference paper lists.

    Each ``events`` item must provide an official ``url`` and may specify
    ``format`` as ``json``, ``openreview``, ``atom`` or ``html``.  Event dates
    are metadata only.  Records are filtered by their own publication or
    acceptance date when available, with a configurable event-date window.
    """
    start, end = _bounds(since, until)
    cfg = dict(config or {})
    events = cfg.get("events", [])
    if not isinstance(events, list):
        raise ValueError("conference config events must be a list")
    maximum = int(cfg.get("max_records", 500))
    timeout = int(cfg.get("timeout", 30))
    window = int(cfg.get("event_window_days", 30))
    if maximum <= 0:
        raise ValueError("max_records must be positive")
    records: list[dict[str, Any]] = []
    total = 0
    accepted_total = 0
    seen: set[str] = set()
    for event in events:
        if not isinstance(event, dict) or not event.get("url"):
            raise ValueError("each conference event needs an official url")
        spec = dict(event)
        source_url = str(spec["url"])
        parsed_url = urllib.parse.urlparse(source_url)
        if parsed_url.scheme not in {"http", "https"} or not parsed_url.netloc:
            raise ValueError("each conference event url must be an absolute HTTP(S) URL")
        payload = _request(source_url, timeout)
        fmt = str(spec.get("format", "auto")).lower()
        if fmt == "auto":
            stripped = payload.lstrip()
            fmt = "json" if stripped.startswith((b"{", b"[")) else "xml" if stripped.startswith(b"<") and b"<html" not in stripped[:200].lower() else "html"
        raw_records = _parse_conference(payload, fmt, spec)
        total += len(raw_records)
        for index, raw in enumerate(raw_records):
            raw = dict(raw)
            if spec.get("conference") and not raw.get("conference"):
                raw["conference"] = spec["conference"]
            if spec.get("event_date") and not raw.get("event_date"):
                raw["event_date"] = spec["event_date"]
            candidate_dates = [_iso(_scalar(raw.get(key))) for key in ("published", "publication_date", "date", "accepted", "decision", "created")]
            candidate_dates = [date.fromisoformat(value) for value in candidate_dates if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)]
            event_date = _iso(raw.get("event_date"))
            event_day = date.fromisoformat(event_date) if re.fullmatch(r"\d{4}-\d{2}-\d{2}", event_date) else None
            include = any(start <= day <= end for day in candidate_dates)
            # The event date is only a fallback for undated list entries; it
            # must not rescue a paper whose own date is outside the window.
            if not include and not candidate_dates and event_day is not None:
                include = start - timedelta(days=window) <= event_day <= end + timedelta(days=window)
            if not include and not candidate_dates and event_day is None:
                include = bool(spec.get("include_undated", False))
            if not include:
                continue
            accepted_total += 1
            record = _record(raw, "conference", spec, index)
            identity = record.get("doi") or record.get("url") or re.sub(r"\s+", " ", record["title"].strip().lower())
            if identity in seen:
                continue
            seen.add(identity)
            if len(records) < maximum:
                records.append(record)
    return records, accepted_total <= maximum, total


__all__ = ["DiscoveryError", "fetch_medrxiv", "fetch_conference", "USER_AGENT"]
