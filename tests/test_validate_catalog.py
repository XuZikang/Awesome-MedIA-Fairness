from __future__ import annotations

import unittest

from scripts.catalog_schema import ALLOWED, TOPICS
from scripts.validate_catalog import CatalogValidator, IssueFormValidator


def _taxonomy() -> str:
    rows = []
    for field, values in ALLOWED.items():
        rows.append(f"| **{field}** | " + ", ".join(f"`{value}`" for value in sorted(values)) + " |")
    return "\n".join(
        [
            "## 🧬 Taxonomy",
            "",
            "| Field | Values | Meaning |",
            "|---|---|---|",
            *rows,
            "",
        ]
    )


def _entry(title: str, year: int, doi: str, assets: str = "Paper only") -> str:
    links = [f"[[📝 Paper](https://doi.org/{doi})]"]
    if "Code" in assets:
        links.append("[[💻 Code](https://github.com/example/code)]")
    if "Weights" in assets:
        links.append("[[🌐 Weights](https://example.org/weights)]")
    if "Project" in assets:
        links.append("[[🌐 Project](https://example.org/project)]")
    if "Data" in assets:
        links.append("[[🌐 Data](https://example.org/data)]")
    return "\n".join(
        [
            f"- (*Journal'{str(year)[-2:]}*) **{title}**",
            "  " + " ".join(links),
            "  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation + Mitigation` · "
            "`Stage: Evaluation` · `Attributes: Sex and gender` · "
            f"`Assets: {assets}` · `Evidence: Primary abstract`",
            "  > **Why it qualifies:** The paper measures subgroup disparities and evaluates a fairness intervention.",
        ]
    )


def _topic_entry(title: str, year: int, doi: str) -> str:
    return "\n".join(
        [
            f"- (*Journal'{str(year)[-2:]}*) **{title}**",
            f"  [[📝 Paper](https://doi.org/{doi})]",
        ]
    )


def _readme() -> str:
    main_entries = [
        _entry("Fairness Evaluation Example", 2025, "10.1000/fairness-a", "Code + Data"),
        _entry("Bias Mitigation Example", 2024, "10.1000/fairness-b"),
    ]
    topic_blocks = []
    for index, topic in enumerate(TOPICS):
        # The first paper intentionally appears in two topics; cross-topic references are valid.
        titles = [
            _topic_entry("Fairness Evaluation Example", 2025, "10.1000/fairness-a"),
        ]
        if index == 1:
            titles.append(_topic_entry("Bias Mitigation Example", 2024, "10.1000/fairness-b"))
        topic_blocks.append(f"### {topic}\n\n" + "\n\n".join(titles))
    resources = "\n\n".join(
        [
            "### Datasets\n\n| **Example data** | [Data](https://example.org/dataset) |",
            "### Benchmarks\n\n| **Example benchmark** | [Paper](https://example.org/benchmark) |",
            "### Toolkits\n\n| **Example toolkit** | [Code](https://github.com/example/toolkit) |",
        ]
    )
    return (
        "# Fairness catalog\n\n"
        + _taxonomy()
        + "\n## 📝 Fairness Papers\n\n"
        + "> Entries are sorted by year in descending order.\n\n"
        + "### 2025\n\n"
        + main_entries[0]
        + "\n\n### 2024\n\n"
        + main_entries[1]
        + "\n\n## 🧭 By Topic\n\n"
        + "\n\n".join(topic_blocks)
        + "\n\n## 🧰 Datasets, Benchmarks and Toolkits\n\n"
        + resources
        + "\n"
    )


def _issue_form() -> str:
    def options(values: set[str] | list[str]) -> str:
        return "\n".join(f"        - {value}" for value in sorted(values))

    return "\n".join(
        [
            "name: Suggest a fairness paper",
            "description: Propose a paper or resource for the fairness catalog.",
            'title: "[Paper]: "',
            "labels: []",
            "assignees: []",
            "",
            "body:",
            "  - type: markdown",
            "    attributes:",
            "      value: |",
            "        Use primary-source evidence and search for duplicate titles and identifiers.",
            "",
            "  - type: input",
            "    id: paper_title",
            "    attributes:",
            "      label: Paper title",
            "    validations:",
            "      required: true",
            "",
            "  - type: input",
            "    id: paper_url",
            "    attributes:",
            "      label: Primary paper URL",
            "    validations:",
            "      required: true",
            "",
            "  - type: input",
            "    id: venue_year",
            "    attributes:",
            "      label: Venue and year",
            "    validations:",
            "      required: true",
            "",
            "  - type: dropdown",
            "    id: publication_status",
            "    attributes:",
            "      label: Publication status",
            "      options:",
            "        - Peer-reviewed and published",
            "        - Accepted or in press",
            "        - Public conference or workshop submission",
            "        - Preprint",
            "    validations:",
            "      required: true",
            "",
        ]
        + sum(
            [
                [
                    f"  - type: dropdown",
                    f"    id: {field.lower()}",
                    "    attributes:",
                    f"      label: {field}",
                    *(["      multiple: true"] if field not in {"Domain", "Evidence"} else []),
                    "      options:",
                    options(values),
                    "    validations:",
                    "      required: true",
                    "",
                ]
                for field, values in (
                    ("Domain", ALLOWED["Domain"]),
                    ("Focus", ALLOWED["Focus"]),
                    ("Stage", ALLOWED["Stage"]),
                    ("Attributes", ALLOWED["Attributes"]),
                    ("Evidence", ALLOWED["Evidence"]),
                )
            ],
            [],
        )
        + [
            "  - type: textarea",
            "    id: qualification",
            "    attributes:",
            "      label: Why it qualifies",
            "    validations:",
            "      required: true",
            "",
            "  - type: dropdown",
            "    id: topics",
            "    attributes:",
            "      label: Topic sections",
            "      multiple: true",
            "      options:",
            options(set(TOPICS)),
            "    validations:",
            "      required: true",
            "",
            "  - type: textarea",
            "    id: resources",
            "    attributes:",
            "      label: Code, weights, project, or data links",
            "",
            "  - type: checkboxes",
            "    id: confirmation",
            "    attributes:",
            "      label: Submission confirmation",
            "      options:",
            "        - label: I searched for duplicate titles and identifiers and used primary evidence.",
            "          required: true",
        ]
    )


class CatalogValidatorTests(unittest.TestCase):
    def test_valid_fixture(self) -> None:
        self.assertEqual(CatalogValidator(_readme()).validate(), [])

    def test_missing_metadata_is_reported(self) -> None:
        mutated = _readme().replace("  **Metadata:**", "  **Removed metadata:**", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("expected one exact Metadata line" in error for error in errors))

    def test_invalid_controlled_value_is_reported(self) -> None:
        mutated = _readme().replace("`Domain: Medical imaging`", "`Domain: Galaxy`", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("invalid Domain values" in error for error in errors))

    def test_domain_must_be_single_select(self) -> None:
        mutated = _readme().replace(
            "`Domain: Medical imaging`", "`Domain: Medical imaging + Other biomedical`", 1
        )
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Domain must contain exactly one value" in error for error in errors))

    def test_asset_mismatch_is_reported(self) -> None:
        mutated = _readme().replace("`Assets: Code + Data`", "`Assets: Paper only`", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("expected 'Code + Data' from links" in error for error in errors))

    def test_year_mismatch_is_reported(self) -> None:
        mutated = _readme().replace("(*Journal'25*)", "(*Journal'24*)", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("does not match section 2025" in error for error in errors))

    def test_duplicate_identifier_is_reported(self) -> None:
        mutated = _readme().replace("10.1000/fairness-b", "10.1000/fairness-a", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Duplicate identifier DOI:10.1000/fairness-a" in error for error in errors))

    def test_topic_set_drift_is_reported(self) -> None:
        mutated = _readme().replace("Bias Mitigation Example", "Topic-only title", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("missing from By Topic" in error for error in errors))
        self.assertTrue(any("missing from main list" in error for error in errors))

    def test_missing_resource_category_is_reported(self) -> None:
        mutated = _readme().replace("### Toolkits", "### Tools", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Resource categories differ" in error for error in errors))
        self.assertTrue(any("Resource category 'Toolkits' has no entries" in error for error in errors))


class IssueFormValidatorTests(unittest.TestCase):
    def test_valid_fixture(self) -> None:
        self.assertEqual(IssueFormValidator(_readme(), _issue_form()).validate(), [])

    def test_schema_option_drift_is_reported(self) -> None:
        mutated = _issue_form().replace("        - Medical imaging", "        - Galaxy", 1)
        errors = IssueFormValidator(_readme(), mutated).validate()
        self.assertTrue(any("field 'domain' options differ" in error for error in errors))

    def test_missing_required_field_is_reported(self) -> None:
        mutated = _issue_form().replace("    id: qualification", "    id: removed_qualification", 1)
        errors = IssueFormValidator(_readme(), mutated).validate()
        self.assertTrue(any("missing field 'qualification'" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
