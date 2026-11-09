#!/usr/bin/env python3
"""Validate the structure and controlled metadata of the fairness catalog."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.catalog_schema import ALLOWED, IMAGING_DOMAINS, MAIN_HEADING, RESOURCE_HEADING, TOPICS


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ISSUE_FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "01-paper-suggestion.yml"

METADATA_FIELDS = ("Domain", "Focus", "Stage", "Attributes", "Assets", "Evidence")
# Assets and Evidence remain internal controlled values and issue-form fields,
# but are intentionally hidden from rendered paper entries and taxonomy.
DISPLAY_FIELDS = ("Domain", "Focus", "Stage", "Attributes")
RESOURCE_CATEGORIES = ("Datasets", "Benchmarks", "Toolkits")
METHOD_CATEGORIES = (
    "Fairness Evaluation",
    "Unfairness Mitigation: Pre-processing",
    "Unfairness Mitigation: In-processing",
    "Unfairness Mitigation: Post-processing",
    "Unfairness Mitigation: Stage pending",
)
METHOD_LEGEND_LABELS = (
    "Fairness Evaluation",
    "Pre-processing",
    "In-processing",
    "Post-processing",
)
METHOD_STAGES = {
    "Unfairness Mitigation: Pre-processing": "Pre-processing",
    "Unfairness Mitigation: In-processing": "In-processing",
    "Unfairness Mitigation: Post-processing": "Post-processing",
}
LEGACY_TOPIC_HEADING = "## 🧭 By Topic"

# entries() is also used by seed_catalog() on the archived pre-migration format.
ENTRY_RE = re.compile(r"^- \(\*.*?\*\) \*\*(.*?)\*\*(.*)$", re.MULTILINE)
ENTRY_LINE_RE = re.compile(
    r"^- \(\*(?P<venue>.*?)\*\) \*\*(?P<title>.*?)\*\*(?P<suffix>.*)$"
)
BADGE_WITH_ALT_RE = re.compile(
    r"!\[([^\]]+)\]\((assets/badges/[^)\s]+\.svg)\)"
)
CONTROL_RE = re.compile(
    r"^  (?P<Domain>.*?) · "
    r"(?P<Focus>.*?) · "
    r"(?P<Stage>.*?)<br>"
    r"(?P<Attributes>.*?)"
    r"(?: · (?P<annotation>!\[(?:Survey|Commentary|Perspective)\]\(assets/badges/"
    r"(?:survey-survey|commentary-commentary|perspective-perspective)\.svg\)))?$",
    re.MULTILINE,
)
TLDR_RE = re.compile(r"^  \*\*TLDR:\*\* (.+)$", re.MULTILINE)
DATE_RE = re.compile(r"^  \*\*Date:\*\* (\d{4}(?:-\d{2}(?:-\d{2})?)?)$", re.MULTILINE)
# Ignore Markdown images (the local SVG badges) while collecting paper/resource links.
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
# Accept the current single-link form and the archived double-bracket form.
LINK_LABEL_RE = re.compile(r"(?<!\!)\[\[?([^\]]+)\]\(([^)\s]+)")
PLACEHOLDER_LINKS = {"https://example.org/paper", "https://github.com/org/repo"}


@dataclass(frozen=True)
class Entry:
    title: str
    block: str
    section: str
    category: str = ""
    month: str = ""


def _normal_title(title: str) -> str:
    """Normalize titles only for duplicate detection; preserve display titles."""
    return re.sub(r"[^\w]+", "", title.casefold())


def _parts(raw_value: str) -> list[str]:
    return [part.strip() for part in raw_value.split(" + ")]


def _badge_slug(label: str, family: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", f"{family}-{label}".lower()).strip("-")


def _expected_badge_path(field: str, label: str) -> str:
    # The renderer reuses the methodology family for its three intervention
    # stage badges; all other control values use their field family.
    family = label if field == "Stage" and label in {"Pre-processing", "In-processing", "Post-processing"} else field
    return f"assets/badges/{_badge_slug(label, family)}.svg"


def _line_index(block: str, match: re.Match[str]) -> int:
    return block[: match.start()].count("\n")


def _sentences(text: str) -> list[str]:
    """Split simple English prose at terminal punctuation for the TLDR contract."""
    # Decimal percentages are part of a sentence, not sentence boundaries.
    protected = re.sub(r"(?<=\d)\.(?=\d)", "\ufff0", text.strip())
    return [part.strip().replace("\ufff0", ".") for part in re.findall(r"[^.!?]+[.!?](?=\s|$)", protected)]


class CatalogValidator:
    """Validate a README string without performing network or filesystem writes."""

    def __init__(self, text: str) -> None:
        self.text = text
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def section_between(self, start: str, end: str) -> str:
        start_index = self.text.find(start)
        end_index = self.text.find(end, start_index + len(start)) if start_index >= 0 else -1
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
        """Parse entries under old or new headings while retaining their context.

        The old ``### YYYY`` form is intentionally accepted here for the state
        seeder's migration fixture. Full README validation requires the new
        category/``#### YYYY`` hierarchy.
        """
        entries: list[Entry] = []
        category = ""
        year = ""
        month = ""
        current_lines: list[str] = []

        def flush() -> None:
            nonlocal current_lines
            if not current_lines:
                return
            block = "\n".join(current_lines).strip()
            match = ENTRY_RE.search(block)
            if match:
                entries.append(Entry(match.group(1).strip(), block, year, category, month))
            current_lines = []

        for line in section.splitlines():
            if re.match(r"^###\s+", line):
                flush()
                heading = line[4:].strip()
                if re.fullmatch(r"\d{4}", heading):
                    year, category, month = heading, "", ""
                else:
                    category, year, month = heading, "", ""
                continue
            if re.match(r"^####\s+", line):
                flush()
                year, month = line[5:].strip(), ""
                continue
            if re.match(r"^#####\s+", line):
                flush()
                month = line[6:].strip()
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
        main = self.section_between(MAIN_HEADING, RESOURCE_HEADING)
        resources = self.section_after(RESOURCE_HEADING)
        taxonomy = self.section_between("## 🧬 Taxonomy", MAIN_HEADING)

        main_entries = self.entries(main)
        self.validate_taxonomy(taxonomy)
        self.validate_categories(main)
        self.validate_hierarchy(main)
        self.validate_main_entries(main_entries)
        self.validate_resources(resources)
        self.validate_duplicate_identifiers(main_entries)
        self.validate_links(main_entries)
        return self.errors

    def validate_taxonomy(self, taxonomy: str) -> None:
        rows = re.findall(
            r"^\| \*\*([^|]+)\*\* \| ([^|]+)\|?$",
            taxonomy,
            re.MULTILINE,
        )
        parsed: dict[str, set[str]] = {}
        for field, values in rows:
            field = field.strip()
            if field not in DISPLAY_FIELDS:
                if field in {"Assets", "Evidence"}:
                    self.error(f"Taxonomy must hide the {field} field")
                else:
                    self.error(f"Taxonomy contains unknown field row: {field}")
                continue
            if field in parsed:
                self.error(f"Taxonomy contains duplicate {field} rows")
            labels = self._badge_values(f"Taxonomy {field}", values, field)
            parsed[field] = set(labels)

        for field in DISPLAY_FIELDS:
            allowed = ALLOWED[field]
            if field not in parsed:
                self.error(f"Taxonomy table is missing the {field} row")
            elif parsed[field] != allowed:
                self.error(
                    f"Taxonomy {field} values differ from the schema: "
                    f"README={sorted(parsed[field])}, schema={sorted(allowed)}"
                )

        for label in METHOD_LEGEND_LABELS:
            if label not in taxonomy:
                self.error(f"Taxonomy method legend is missing: {label}")

    def validate_categories(self, main: str) -> None:
        headings = re.findall(r"^### (.+)$", main, re.MULTILINE)
        required = list(METHOD_CATEGORIES[:-1])
        valid = headings == required or (
            len(headings) == len(required) + 1 and headings == required + [METHOD_CATEGORIES[-1]]
        )
        if not valid:
            self.error(
                "Method category headings differ from the required order (Stage pending is optional): "
                f"README={headings}, required={required} or {required + [METHOD_CATEGORIES[-1]]}"
            )
        if LEGACY_TOPIC_HEADING in main:
            self.error("Legacy By Topic section is not allowed in the main catalog")

    def validate_hierarchy(self, main: str) -> None:
        years_by_category: dict[str, list[int]] = defaultdict(list)
        months_by_year: dict[tuple[str, int], list[str]] = defaultdict(list)
        category = ""
        year = 0
        max_year = 0

        for line in main.splitlines():
            match = re.match(r"^### (.+)$", line)
            if match:
                category = match.group(1)
                year = 0
                continue
            match = re.match(r"^#### (\d{4})$", line)
            if match:
                year = int(match.group(1))
                max_year = max(max_year, year)
                if category not in METHOD_CATEGORIES:
                    self.error(f"Year heading {year} is outside a method category")
                years_by_category[category].append(year)
                continue
            match = re.match(r"^##### (.+)$", line)
            if match:
                value = match.group(1)
                if not year:
                    self.error(f"Month heading '{value}' is outside a year heading")
                    continue
                if value != "Month unverified" and not re.fullmatch(r"\d{4}-\d{2}", value):
                    self.error(f"Invalid month heading: {value}")
                if value != "Month unverified" and not value.startswith(f"{year:04d}-"):
                    self.error(f"Month heading '{value}' does not match year {year}")
                months_by_year[(category, year)].append(value)

        all_years = [year for years in years_by_category.values() for year in years]
        if not all_years:
            self.error(f"No four-digit year headings found under {MAIN_HEADING}")
            return
        for category, years in years_by_category.items():
            if years != sorted(years, reverse=True):
                self.error(f"Year headings must be in descending order in '{category}': {years}")
            if len(years) != len(set(years)):
                self.error(f"Duplicate year heading in '{category}': {years}")

        for (category, heading_year), months in months_by_year.items():
            if heading_year != max(all_years):
                self.error(
                    f"Month headings are allowed only under latest global year {max(all_years)}: "
                    f"'{category}' {heading_year}"
                )
            numeric = [month for month in months if month != "Month unverified"]
            if numeric != sorted(numeric, reverse=True):
                self.error(f"Month headings must be in descending order in '{category}' {heading_year}: {months}")
            if "Month unverified" in months and months[-1] != "Month unverified":
                self.error(f"Month unverified must be last in '{category}' {heading_year}: {months}")

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
            if entry.category not in METHOD_CATEGORIES:
                self.error(f"{entry.title}: entry is not under a method category")
            self.validate_entry_year(entry)
            self.validate_control_values(entry)
            self.validate_entry_layout(entry)
            self.validate_tldr(entry)
            self.validate_date(entry)
            self.validate_category_stage(entry)

    def validate_entry_year(self, entry: Entry) -> None:
        if not re.fullmatch(r"\d{4}", entry.section):
            self.error(f"{entry.title}: entry is not under a four-digit year heading")
            return
        first_line = entry.block.splitlines()[0] if entry.block.splitlines() else ""
        match = ENTRY_LINE_RE.match(first_line)
        if not match:
            self.error(f"{entry.title}: malformed entry title line")
            return
        venue_year = re.search(r"(?:19|20)\d{2}|\b\d{2}\b", match.group("venue"))
        if not venue_year:
            self.error(f"{entry.title}: venue label must include a publication year")
            return
        value = venue_year.group(0)
        expected = entry.section if len(value) == 4 else entry.section[-2:]
        if value != expected:
            self.error(f"{entry.title}: venue year '{value}' does not match section {entry.section}")

    def validate_entry_layout(self, entry: Entry) -> None:
        lines = entry.block.splitlines()
        if not lines:
            self.error(f"{entry.title}: empty entry")
            return
        title_line = ENTRY_LINE_RE.match(lines[0])
        if not title_line:
            self.error(f"{entry.title}: malformed entry title line")
        elif title_line.group("suffix").strip():
            self.error(f"{entry.title}: title must not contain inline badges or control values")

        if len(lines) < 9 or lines[1] != "":
            self.error(f"{entry.title}: title and control values must be separated by a blank line")
        elif not CONTROL_RE.match(lines[2]):
            self.error(f"{entry.title}: expected one five-field control-values line after the title")
        if len(lines) < 9 or lines[3] != "":
            self.error(f"{entry.title}: control values and links must be separated by a blank line")
        elif not lines[4].startswith("  "):
            self.error(f"{entry.title}: links line must start with two spaces")
        elif not LINK_LABEL_RE.search(lines[4]):
            self.error(f"{entry.title}: links line is missing paper/resource links")

        if len(lines) >= 7 and lines[5] != "":
            self.error(f"{entry.title}: links and TLDR must be separated by a blank line")
        if len(lines) >= 7 and not TLDR_RE.match(lines[6]):
            self.error(f"{entry.title}: expected TLDR immediately after the links")
        if len(lines) >= 3:
            if re.search(r"\*\*(?:Domain|Focus|Stage|Attributes|Assets|Evidence):\*\*", lines[2]):
                self.error(f"{entry.title}: control values must not contain bold field labels")
            visible_badges = {label for label, _ in BADGE_WITH_ALT_RE.findall(lines[2])}
            hidden_assets = visible_badges & ALLOWED["Assets"]
            hidden_evidence = visible_badges & ALLOWED["Evidence"]
            if hidden_assets:
                self.error(f"{entry.title}: Assets badges must remain hidden: {sorted(hidden_assets)}")
            if hidden_evidence:
                self.error(f"{entry.title}: Evidence badges must remain hidden: {sorted(hidden_evidence)}")
        if "Provenance" in entry.block or "Why it qualifies" in entry.block:
            self.error(f"{entry.title}: legacy Provenance/Why it qualifies text is not allowed")
        if re.search(r"^\s*\*\*Metadata:\*\*", entry.block, re.MULTILINE):
            self.error(f"{entry.title}: legacy Metadata line is not allowed")
        if re.search(r"^\s*\*\*Evidence:\*\*", entry.block, re.MULTILINE):
            self.error(f"{entry.title}: Evidence must remain hidden from paper entries")

    def _badge_values(self, context: str, raw_value: str, field: str = "") -> list[str]:
        """Return alt labels from a badge-only group and report inline text."""
        matches = list(BADGE_WITH_ALT_RE.finditer(raw_value))
        residual = BADGE_WITH_ALT_RE.sub("", raw_value)
        if not matches:
            self.error(f"{context}: value must contain one or more local SVG badges")
            return []
        # Spaces and punctuation are separators; all semantic text must come
        # from image alt labels so values are not duplicated inline.
        if re.search(r"[^\s,;]", residual):
            self.error(f"{context}: value cell must contain badges only, without repeated inline text")
        values = [match.group(1).strip() for match in matches]
        if field:
            for match, value in zip(matches, values):
                if match.group(2) != _expected_badge_path(field, value):
                    self.error(
                        f"{context}: badge path {match.group(2)!r} does not match "
                        f"{field} value {value!r}"
                    )
        if any(not value for value in values):
            self.error(f"{context}: badge alt labels must not be empty")
        if len(values) != len(set(values)):
            self.error(f"{context}: duplicate badge value")
        return values

    def validate_control_values(self, entry: Entry) -> None:
        matches = list(CONTROL_RE.finditer(entry.block))
        if len(matches) != 1:
            self.error(f"{entry.title}: expected one exact five-field control-values line, found {len(matches)}")
            return

        match = matches[0]
        lines = entry.block.splitlines()
        index = _line_index(entry.block, match)
        if index == 0 or lines[index - 1] != "" or index + 1 >= len(lines) or lines[index + 1] != "":
            self.error(f"{entry.title}: control values must be on their own line with blank lines around them")

        values: dict[str, list[str]] = {}
        for field in DISPLAY_FIELDS:
            labels = self._badge_values(f"{entry.title}: {field}", match.group(field), field)
            values[field] = labels
            invalid = set(labels) - ALLOWED[field]
            if invalid:
                self.error(f"{entry.title}: invalid {field} values: {sorted(invalid)}")
            if not labels:
                self.error(f"{entry.title}: empty {field} value")

        domains = values["Domain"]
        if len(domains) > 1 and (not set(domains).issubset(IMAGING_DOMAINS) or "Medical imaging (modality unspecified)" in domains):
            self.error(f"{entry.title}: multiple domains must be concrete imaging modalities")

        annotation = match.group("annotation")
        if annotation:
            annotation_match = BADGE_WITH_ALT_RE.fullmatch(annotation)
            annotation_label = annotation_match.group(1)  # type: ignore[union-attr]
            if annotation_label not in {"Survey", "Commentary", "Perspective"}:
                self.error(f"{entry.title}: invalid annotation badge")
            expected_path = {
                "Survey": "assets/badges/survey-survey.svg",
                "Commentary": "assets/badges/commentary-commentary.svg",
                "Perspective": "assets/badges/perspective-perspective.svg",
            }.get(annotation_label)
            if annotation_match and annotation_match.group(2) != expected_path:
                self.error(f"{entry.title}: annotation badge path does not match its label")

        labels = [label for label, _ in LINK_LABEL_RE.findall(entry.block)]
        if not any(re.search(r"\bPaper\b", label) for label in labels):
            self.error(f"{entry.title}: entry must include a Paper link")

    def validate_tldr(self, entry: Entry) -> None:
        matches = list(TLDR_RE.finditer(entry.block))
        if len(matches) != 1:
            self.error(f"{entry.title}: expected one TLDR line, found {len(matches)}")
            return
        match = matches[0]
        lines = entry.block.splitlines()
        index = _line_index(entry.block, match)
        if index == 0 or lines[index - 1] != "":
            self.error(f"{entry.title}: TLDR must follow a blank line")
        text = match.group(1).strip()
        if re.search(r"[\u3400-\u9fff]", text):
            self.error(f"{entry.title}: TLDR must be English prose")
        sentences = _sentences(text)
        if len(sentences) != 3 or " ".join(sentences) != text:
            self.error(f"{entry.title}: TLDR must contain exactly three complete English sentences")
        if index + 1 >= len(lines) or lines[index + 1] != "":
            self.error(f"{entry.title}: Date must be separated from TLDR by a blank line")

    def validate_date(self, entry: Entry) -> None:
        matches = list(DATE_RE.finditer(entry.block))
        if len(matches) != 1:
            self.error(f"{entry.title}: expected one Date line, found {len(matches)}")
            return
        value = matches[0].group(1)
        if value[:4] != entry.section:
            self.error(f"{entry.title}: Date '{value}' does not match section {entry.section}")
        if entry.month == "Month unverified" and len(value) != 4:
            self.error(f"{entry.title}: Month unverified entries must use year-only Date precision")
        if re.fullmatch(r"\d{4}-\d{2}", entry.month) and not value.startswith(entry.month):
            self.error(f"{entry.title}: Date '{value}' does not match month heading {entry.month}")

    def validate_category_stage(self, entry: Entry) -> None:
        match = CONTROL_RE.search(entry.block)
        if not match:
            return
        stage = set(self._badge_values(f"{entry.title}: Stage", match.group("Stage"), "Stage"))
        if entry.category == "Unfairness Mitigation: Stage pending":
            if not stage.intersection({"Not verified", "Not applicable"}):
                self.error(f"{entry.title}: Stage pending entries require Not verified or Not applicable stage")
            return
        expected = METHOD_STAGES.get(entry.category)
        if expected and not stage.intersection({expected, "Multi-stage", "Not verified", "Not applicable"}):
            self.error(f"{entry.title}: stage metadata does not match category {entry.category}")

    def validate_duplicate_identifiers(self, entries: list[Entry]) -> None:
        owners: dict[str, set[str]] = defaultdict(set)
        patterns = {
            "arXiv": re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE),
            "DOI": re.compile(r"(?:doi\.org/|doi:\s*)(10\.\d{4,9}/[-._;()/:A-Z0-9]+)", re.IGNORECASE),
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
    MULTISELECT_FIELDS = {"domain", "focus", "stage", "attributes", "topics"}
    SINGLE_SELECT_FIELDS = {"evidence", "publication_status"}
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
                self.error(f"field '{field_id}' has type '{actual_type}', expected '{expected_type}'")
            if field_id not in self.OPTIONAL_FIELDS and field_id != "confirmation":
                if not re.search(r"^    validations:\n      required: true$", block, re.MULTILINE):
                    self.error(f"field '{field_id}' must be required")

        for field_id in self.MULTISELECT_FIELDS:
            if field_id in fields and not re.search(r"^      multiple: true$", fields[field_id][1], re.MULTILINE):
                self.error(f"field '{field_id}' must allow multiple selections")

        for field_id in self.SINGLE_SELECT_FIELDS:
            if field_id in fields and re.search(r"^      multiple: true$", fields[field_id][1], re.MULTILINE):
                self.error(f"field '{field_id}' must be single-select")

        # Topics are a controlled internal routing vocabulary, not a README
        # section: removing the old By Topic index must not break the form.
        expected_options = {
            "domain": ALLOWED["Domain"],
            "focus": ALLOWED["Focus"],
            "stage": ALLOWED["Stage"],
            "attributes": ALLOWED["Attributes"],
            "evidence": ALLOWED["Evidence"],
            "topics": set(TOPICS),
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

        if "confirmation" in fields and not re.search(r"^          required: true$", fields["confirmation"][1], re.MULTILINE):
            self.error("confirmation checkbox must be required")

        return self.errors

    # Kept as a compatibility helper for callers that used the old API; it no
    # longer inspects README headings.
    def readme_topics(self) -> set[str]:
        return set(TOPICS)


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

    main_text = text.split(MAIN_HEADING, 1)[1].split(RESOURCE_HEADING, 1)[0]
    entries = CatalogValidator.entries(main_text)
    categories = {entry.category for entry in entries}
    print(
        f"Catalog validation passed: {len(entries)} papers across "
        f"{len(categories)} method categories and a synchronized paper-suggestion form."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
