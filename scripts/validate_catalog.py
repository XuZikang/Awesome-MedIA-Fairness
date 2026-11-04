#!/usr/bin/env python3
"""Validate the structure and controlled metadata of the fairness catalog."""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.catalog_schema import ALLOWED, MAIN_HEADING, RESOURCE_HEADING, TOPIC_HEADING, TOPICS


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ISSUE_FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "01-paper-suggestion.yml"

METADATA_FIELDS = ("Domain", "Focus", "Stage", "Attributes", "Assets", "Evidence")
RESOURCE_CATEGORIES = ("Datasets", "Benchmarks", "Toolkits")

ENTRY_RE = re.compile(r"^- \(\*.*?\*\) \*\*(.*?)\*\*", re.MULTILINE)
METADATA_RE = re.compile(
    r"^  \*\*Metadata:\*\* "
    r"`Domain: ([^`]+)` · "
    r"`Focus: ([^`]+)` · "
    r"`Stage: ([^`]+)` · "
    r"`Attributes: ([^`]+)` · "
    r"`Assets: ([^`]+)` · "
    r"`Evidence: ([^`]+)`$",
    re.MULTILINE,
)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
PLACEHOLDER_LINKS = {"https://example.org/paper", "https://github.com/org/repo"}


@dataclass(frozen=True)
class Entry:
    title: str
    block: str
    section: str


def _normal_title(title: str) -> str:
    """Normalize titles only for duplicate detection; preserve display titles."""
    return re.sub(r"[^\w]+", "", title.casefold())


def _parts(raw_value: str) -> list[str]:
    return [part.strip() for part in raw_value.split(" + ")]


class CatalogValidator:
    """Validate a README string without performing network or filesystem writes."""

    def __init__(self, text: str) -> None:
        self.text = text
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def section_between(self, start: str, end: str) -> str:
        start_index = self.text.find(start)
        end_index = self.text.find(end)
        if start_index < 0:
            self.error(f"Missing section heading: {start}")
            return ""
        if end_index < 0 or end_index <= start_index:
            self.error(f"Missing or misplaced section heading: {end}")
            return ""
        return self.text[start_index + len(start) : end_index]

    def section_after(self, heading: str) -> str:
        start_index = self.text.find(heading)
        if start_index < 0:
            self.error(f"Missing section heading: {heading}")
            return ""
        rest = self.text[start_index + len(heading) :]
        next_heading = re.search(r"^##\s+", rest, re.MULTILINE)
        return rest[: next_heading.start()] if next_heading else rest

    @staticmethod
    def entries(section: str) -> list[Entry]:
        """Parse complete entries while retaining their nearest ``###`` heading."""
        entries: list[Entry] = []
        current_heading = ""
        current_lines: list[str] = []

        def flush() -> None:
            if not current_lines:
                return
            block = "\n".join(current_lines).strip()
            match = ENTRY_RE.search(block)
            if match:
                entries.append(Entry(match.group(1).strip(), block, current_heading))
            current_lines.clear()

        for line in section.splitlines():
            if re.match(r"^###\s+", line):
                flush()
                current_heading = line[4:].strip()
                continue
            if ENTRY_RE.match(line):
                flush()
                current_lines.append(line)
                continue
            if current_lines:
                current_lines.append(line)
        flush()
        return entries

    def validate(self) -> list[str]:
        main = self.section_between(MAIN_HEADING, TOPIC_HEADING)
        topics = self.section_between(TOPIC_HEADING, RESOURCE_HEADING)
        resources = self.section_after(RESOURCE_HEADING)
        taxonomy = self.section_between("## 🧬 Taxonomy", MAIN_HEADING)

        main_entries = self.entries(main)
        topic_entries = self.entries(topics)

        self.validate_taxonomy(taxonomy)
        self.validate_years(main)
        self.validate_main_entries(main_entries)
        self.validate_topics(main_entries, topic_entries, topics)
        self.validate_resources(resources)
        self.validate_duplicate_identifiers(main_entries)
        self.validate_links(main_entries + topic_entries)
        return self.errors

    def validate_taxonomy(self, taxonomy: str) -> None:
        rows = re.findall(
            r"^\| \*\*(Domain|Focus|Stage|Attributes|Assets|Evidence)\*\* \| ([^|]+)",
            taxonomy,
            re.MULTILINE,
        )
        parsed: dict[str, set[str]] = {}
        for field, values in rows:
            if field in parsed:
                self.error(f"Taxonomy contains duplicate {field} rows")
            parsed[field] = set(re.findall(r"`([^`]+)`", values))

        for field in METADATA_FIELDS:
            allowed = ALLOWED[field]
            if field not in parsed:
                self.error(f"Taxonomy table is missing the {field} row")
            elif parsed[field] != allowed:
                self.error(
                    f"Taxonomy {field} values differ from the schema: "
                    f"README={sorted(parsed[field])}, schema={sorted(allowed)}"
                )

    def validate_years(self, main: str) -> None:
        years = [int(year) for year in re.findall(r"^### (\d{4})$", main, re.MULTILINE)]
        if not years:
            self.error(f"No year headings found in {MAIN_HEADING}")
            return
        if len(years) != len(set(years)):
            self.error(f"Duplicate year headings: {years}")
        if years != sorted(years, reverse=True):
            self.error(f"Year headings must be in descending order: {years}")

    def validate_main_entries(self, entries: list[Entry]) -> None:
        if not entries:
            self.error(f"No entries found in {MAIN_HEADING}")
            return

        owners: dict[str, set[str]] = defaultdict(set)
        for entry in entries:
            owners[_normal_title(entry.title)].add(entry.title)
        for normalized, titles in owners.items():
            if len(titles) > 1 or sum(_normal_title(e.title) == normalized for e in entries) > 1:
                self.error(f"Duplicate main-list title: {sorted(titles)}")

        for entry in entries:
            self.validate_entry_year(entry)
            self.validate_metadata(entry)
            qualification_count = entry.block.count("> **Why it qualifies:**")
            if qualification_count != 1:
                self.error(
                    f"{entry.title}: expected one Why it qualifies note, found {qualification_count}"
                )

    def validate_entry_year(self, entry: Entry) -> None:
        if len(entry.section) != 4 or not entry.section.isdigit():
            self.error(f"{entry.title}: entry is not under a four-digit year heading")
            return
        first_line = entry.block.splitlines()[0] if entry.block.splitlines() else ""
        venue_year = re.search(r"(?:19|20)\d{2}|\b\d{2}\b", first_line)
        if not venue_year:
            self.error(f"{entry.title}: venue label must include a publication year")
            return
        value = venue_year.group(0)
        expected = entry.section if len(value) == 4 else entry.section[-2:]
        if value != expected:
            self.error(
                f"{entry.title}: venue year '{value}' does not match section {entry.section}"
            )

    def validate_metadata(self, entry: Entry) -> None:
        matches = list(METADATA_RE.finditer(entry.block))
        if len(matches) != 1:
            self.error(f"{entry.title}: expected one exact Metadata line, found {len(matches)}")
            return

        values = dict(zip(METADATA_FIELDS, matches[0].groups()))
        for field, raw_value in values.items():
            parts = _parts(raw_value)
            if not parts or any(not part for part in parts):
                self.error(f"{entry.title}: empty {field} value")
                continue
            if len(parts) != len(set(parts)):
                self.error(f"{entry.title}: duplicate {field} value in '{raw_value}'")
            invalid = set(parts) - ALLOWED[field]
            if invalid:
                self.error(f"{entry.title}: invalid {field} values: {sorted(invalid)}")
            if field in {"Domain", "Evidence"} and len(parts) != 1:
                self.error(f"{entry.title}: {field} must contain exactly one value")

        expected_assets: list[str] = []
        for asset in ("Code", "Weights", "Project", "Data"):
            if re.search(rf"\[[^\]]*\b{re.escape(asset)}\]", entry.block):
                expected_assets.append(asset)
        if not expected_assets:
            expected_assets.append("Paper only")
        expected = " + ".join(expected_assets)
        if values["Assets"] != expected:
            self.error(
                f"{entry.title}: Assets is '{values['Assets']}', expected '{expected}' from links"
            )

    def validate_topics(
        self, main_entries: list[Entry], topic_entries: list[Entry], topics: str
    ) -> None:
        headings = set(re.findall(r"^### (.+)$", topics, re.MULTILINE))
        if headings != set(TOPICS):
            self.error(
                "By Topic headings differ from the schema: "
                f"README={sorted(headings)}, schema={sorted(TOPICS)}"
            )

        main_titles = {_normal_title(entry.title) for entry in main_entries}
        topic_titles = {_normal_title(entry.title) for entry in topic_entries}
        for title in sorted(main_titles - topic_titles):
            self.error(f"Main-list paper missing from By Topic: {title}")
        for title in sorted(topic_titles - main_titles):
            self.error(f"By Topic paper missing from main list: {title}")

        by_section: dict[str, list[str]] = defaultdict(list)
        for entry in topic_entries:
            by_section[entry.section].append(_normal_title(entry.title))
            if "**Metadata:**" in entry.block or "Why it qualifies" in entry.block:
                self.error(f"{entry.title}: topic entries must stay concise")

        for section, titles in by_section.items():
            duplicates = [title for title, count in Counter(titles).items() if count > 1]
            for title in duplicates:
                self.error(f"Duplicate title in topic '{section}': {title}")

    def validate_duplicate_identifiers(self, entries: list[Entry]) -> None:
        owners: dict[str, set[str]] = defaultdict(set)
        patterns = {
            "arXiv": re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE),
            "DOI": re.compile(
                r"(?:doi\.org/|doi:\s*)(10\.\d{4,9}/[-._;()/:A-Z0-9]+)", re.IGNORECASE
            ),
            "PubMed": re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", re.IGNORECASE),
        }
        for entry in entries:
            title = _normal_title(entry.title)
            for kind, pattern in patterns.items():
                for value in pattern.findall(entry.block):
                    value = unquote(value).lower().rstrip(".,;:)")
                    owners[f"{kind}:{value}"].add(title)

        for identifier, titles in sorted(owners.items()):
            if len(titles) > 1:
                self.error(f"Duplicate identifier {identifier} appears in: {sorted(titles)}")

    def validate_links(self, entries: list[Entry]) -> None:
        for entry in entries:
            links = LINK_RE.findall(entry.block)
            if not links:
                self.error(f"{entry.title}: entry has no links")
            for link in links:
                if not link.startswith("https://"):
                    self.error(f"{entry.title}: link must use HTTPS: {link}")
                if link in PLACEHOLDER_LINKS:
                    self.error(f"{entry.title}: placeholder link found: {link}")

    def validate_resources(self, resources: str) -> None:
        headings = set(re.findall(r"^### (.+)$", resources, re.MULTILINE))
        if headings != set(RESOURCE_CATEGORIES):
            self.error(
                "Resource categories differ from the required set: "
                f"README={sorted(headings)}, required={sorted(RESOURCE_CATEGORIES)}"
            )

        for category in RESOURCE_CATEGORIES:
            match = re.search(
                rf"^### {re.escape(category)}\n(.*?)(?=^### |\Z)",
                resources,
                re.MULTILINE | re.DOTALL,
            )
            if not match or not re.search(r"^\| \*\*.+\*\* \|", match.group(1), re.MULTILINE):
                self.error(f"Resource category '{category}' has no entries")

        for link in LINK_RE.findall(resources):
            if not link.startswith("https://"):
                self.error(f"Resource link must use HTTPS: {link}")
            if link in PLACEHOLDER_LINKS:
                self.error(f"Resource placeholder link found: {link}")


class IssueFormValidator:
    """Check that the GitHub issue form exposes the same controlled vocabulary."""

    REQUIRED_FIELDS = {
        "paper_title": "input",
        "paper_url": "input",
        "venue_year": "input",
        "publication_status": "dropdown",
        "domain": "dropdown",
        "focus": "dropdown",
        "stage": "dropdown",
        "attributes": "dropdown",
        "evidence": "dropdown",
        "qualification": "textarea",
        "topics": "dropdown",
        "resources": "textarea",
        "confirmation": "checkboxes",
    }
    OPTIONAL_FIELDS = {"resources"}
    MULTISELECT_FIELDS = {"focus", "stage", "attributes", "topics"}
    SINGLE_SELECT_FIELDS = {"domain", "evidence", "publication_status"}
    FIELD_RE = re.compile(
        r"^  - type: ([^\n]+)\n    id: ([^\n]+)\n(.*?)(?=^  - type:|\Z)",
        re.MULTILINE | re.DOTALL,
    )

    def __init__(self, readme: str, form: str) -> None:
        self.readme = readme
        self.form = form
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(f"Issue form: {message}")

    def validate(self) -> list[str]:
        fields = {
            field_id.strip(): (field_type.strip(), block)
            for field_type, field_id, block in self.FIELD_RE.findall(self.form)
        }

        for field_id in sorted(set(fields) - set(self.REQUIRED_FIELDS)):
            self.error(f"unexpected field '{field_id}'")

        for field_id, expected_type in self.REQUIRED_FIELDS.items():
            if field_id not in fields:
                self.error(f"missing field '{field_id}'")
                continue
            actual_type, block = fields[field_id]
            if actual_type != expected_type:
                self.error(
                    f"field '{field_id}' has type '{actual_type}', expected '{expected_type}'"
                )
            if field_id not in self.OPTIONAL_FIELDS and field_id != "confirmation":
                if not re.search(r"^    validations:\n      required: true$", block, re.MULTILINE):
                    self.error(f"field '{field_id}' must be required")

        for field_id in self.MULTISELECT_FIELDS:
            if field_id in fields and not re.search(
                r"^      multiple: true$", fields[field_id][1], re.MULTILINE
            ):
                self.error(f"field '{field_id}' must allow multiple selections")

        for field_id in self.SINGLE_SELECT_FIELDS:
            if field_id in fields and re.search(
                r"^      multiple: true$", fields[field_id][1], re.MULTILINE
            ):
                self.error(f"field '{field_id}' must be single-select")

        expected_options = {
            "domain": ALLOWED["Domain"],
            "focus": ALLOWED["Focus"],
            "stage": ALLOWED["Stage"],
            "attributes": ALLOWED["Attributes"],
            "evidence": ALLOWED["Evidence"],
            "topics": self.readme_topics(),
        }
        for field_id, expected in expected_options.items():
            if field_id not in fields:
                continue
            options = set(re.findall(r"^        - ([^\n]+)$", fields[field_id][1], re.MULTILINE))
            if options != expected:
                self.error(
                    f"field '{field_id}' options differ from the schema: "
                    f"form={sorted(options)}, schema={sorted(expected)}"
                )

        if "confirmation" in fields and not re.search(
            r"^          required: true$", fields["confirmation"][1], re.MULTILINE
        ):
            self.error("confirmation checkbox must be required")

        return self.errors

    def readme_topics(self) -> set[str]:
        try:
            topic_section = self.readme.split(TOPIC_HEADING, 1)[1].split(
                RESOURCE_HEADING, 1
            )[0]
        except IndexError:
            self.error("cannot read topic headings from README")
            return set()
        return set(re.findall(r"^### (.+)$", topic_section, re.MULTILINE))


def main() -> int:
    if not README.exists():
        print(f"ERROR: README not found at {README}", file=sys.stderr)
        return 1
    if not ISSUE_FORM.exists():
        print(f"ERROR: issue form not found at {ISSUE_FORM}", file=sys.stderr)
        return 1

    text = README.read_text(encoding="utf-8")
    form = ISSUE_FORM.read_text(encoding="utf-8")
    errors = CatalogValidator(text).validate()
    errors.extend(IssueFormValidator(text, form).validate())
    if errors:
        print(f"Catalog validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    main_entries = CatalogValidator.entries(
        text.split(MAIN_HEADING, 1)[1].split(TOPIC_HEADING, 1)[0]
    )
    topic_entries = CatalogValidator.entries(
        text.split(TOPIC_HEADING, 1)[1].split(RESOURCE_HEADING, 1)[0]
    )
    print(
        f"Catalog validation passed: {len(main_entries)} main-list papers, "
        f"{len({_normal_title(entry.title) for entry in topic_entries})} unique topic entries, "
        "and a synchronized paper-suggestion form."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
