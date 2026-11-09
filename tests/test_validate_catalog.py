from __future__ import annotations

import re
import unittest

from scripts.catalog_schema import ALLOWED, MAIN_HEADING, RESOURCE_HEADING, TOPICS
from scripts.validate_catalog import CatalogValidator, IssueFormValidator, _sentences


def _slug(label: str, family: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", f"{family}-{label}".lower()).strip("-")


def _badge(label: str, family: str) -> str:
    return f"![{label}](assets/badges/{_slug(label, family)}.svg)"


def _taxonomy() -> str:
    rows = []
    for field in ("Domain", "Focus", "Stage", "Attributes"):
        values = " ".join(
            _badge(value, value if field == "Stage" and value in {"Pre-processing", "In-processing", "Post-processing"} else field)
            for value in sorted(ALLOWED[field])
        )
        rows.append(f"| **{field}** | {values} |")
    legend = "\n".join(
        [
            "Directory categories:",
            f"| {_badge('Fairness Evaluation', 'Fairness Evaluation')} | Evaluation and subgroup auditing. |",
            f"| {_badge('Pre-processing', 'Pre-processing')} | Data and sampling interventions. |",
            f"| {_badge('In-processing', 'In-processing')} | Training and representation interventions. |",
            f"| {_badge('Post-processing', 'Post-processing')} | Output and calibration interventions. |",
        ]
    )
    return "\n".join(
        [
            "## 🧬 Taxonomy",
            "",
            "| Method | Definition |",
            "|---|---|",
            f"| {_badge('Fairness Evaluation', 'Fairness Evaluation')} | Evaluation. |",
            f"| {_badge('Pre-processing', 'Pre-processing')} | Pre-processing. |",
            f"| {_badge('In-processing', 'In-processing')} | In-processing. |",
            f"| {_badge('Post-processing', 'Post-processing')} | Post-processing. |",
            "",
            "| Field | Controlled values |",
            "|---|---|",
            *rows,
            "",
            legend,
            "",
        ]
    )


def _control_line(stage: str, assets: str, annotation: str | None = None, domains: tuple[str, ...] = ("MRI",)) -> str:
    focus = "Evaluation" if stage == "Evaluation" else "Mitigation"
    values = {
        "Domain": list(domains),
        "Focus": [focus],
        "Stage": [stage],
        "Attributes": ["Sex and gender"],
    }
    groups = [
        " ".join(
            _badge(value, value if field == "Stage" and value in {"Pre-processing", "In-processing", "Post-processing"} else field)
            for value in field_values
        )
        for field, field_values in values.items()
    ]
    line = "  " + " · ".join(groups[:3]) + "<br>" + groups[3]
    if annotation:
        line += " · " + _badge(annotation, annotation)
    return line


def _entry(
    title: str,
    year: int,
    doi: str,
    stage: str,
    assets: str = "Paper only",
    date: str | None = None,
    annotation: str | None = None,
) -> str:
    links = [f"[📝 Paper](https://doi.org/{doi})"]
    if "Code" in assets:
        links.append("[💻 Code](https://github.com/example/code)")
    if "Weights" in assets:
        links.append("[🌐 Weights](https://example.org/weights)")
    if "Project" in assets:
        links.append("[🌐 Project](https://example.org/project)")
    if "Data" in assets:
        links.append("[📊 Data](https://example.org/data)")
    return "\n".join(
        [
            f"- (*Journal'{str(year)[-2:]}*) **{title}**",
            "",
            _control_line(stage, assets, annotation),
            "",
            "  " + " ".join(links),
            "",
            "  **TLDR:** This paper studies a medical fairness method. It compares subgroup outcomes. It reports an evaluated result.",
            "",
            f"  **Date:** {date or str(year)}",
        ]
    )


def _readme(include_pending: bool = True) -> str:
    evaluation = "\n\n".join(
        [
            "### Fairness Evaluation\n\n#### 2025\n\n##### 2025-11\n\n"
            + _entry("Fairness Evaluation Example", 2025, "10.1000/fairness-a", "Evaluation", "Code + Data", "2025-11-04"),
            "##### 2025-10\n\n"
            + _entry("Fairness Evaluation Second", 2025, "10.1000/fairness-b", "Evaluation", date="2025-10"),
        ]
    )
    preprocessing = "### Unfairness Mitigation: Pre-processing\n\n#### 2024\n\n" + _entry(
        "Pre-processing Example", 2024, "10.1000/fairness-c", "Pre-processing", date="2024"
    )
    inprocessing = "### Unfairness Mitigation: In-processing\n\n#### 2023\n\n" + _entry(
        "In-processing Example", 2023, "10.1000/fairness-d", "In-processing", date="2023"
    )
    postprocessing = "### Unfairness Mitigation: Post-processing\n\n#### 2022\n\n" + _entry(
        "Post-processing Example", 2022, "10.1000/fairness-e", "Post-processing", date="2022"
    )
    pending = "### Unfairness Mitigation: Stage pending\n\n#### 2025\n\n##### Month unverified\n\n" + _entry(
        "Stage Pending Example", 2025, "10.1000/fairness-f", "Not verified", date="2025"
    )
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
        + f"\n{MAIN_HEADING}\n\n"
        + "\n\n".join([evaluation, preprocessing, inprocessing, postprocessing] + ([pending] if include_pending else []))
        + f"\n\n{RESOURCE_HEADING}\n\n"
        + resources
        + "\n"
    )


def _issue_form() -> str:
    def options(values: set[str] | list[str]) -> str:
        return "\n".join(f"        - {value}" for value in sorted(values))

    fields = [
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
    ]
    for field_id, field_type, multiple, required in [
        ("paper_title", "input", False, True),
        ("paper_url", "input", False, True),
        ("venue_year", "input", False, True),
        ("publication_status", "dropdown", False, True),
    ]:
        fields += [f"  - type: {field_type}", f"    id: {field_id}", "    attributes:", f"      label: {field_id}"]
        if field_id == "publication_status":
            fields += [
                "      options:",
                "        - Peer-reviewed and published",
                "        - Accepted or in press",
                "        - Public conference or workshop submission",
                "        - Preprint",
            ]
        if required:
            fields += ["    validations:", "      required: true"]
        fields.append("")
    for field_id, schema_field in [
        ("domain", "Domain"),
        ("focus", "Focus"),
        ("stage", "Stage"),
        ("attributes", "Attributes"),
        ("evidence", "Evidence"),
    ]:
        multiple = field_id in {"domain", "focus", "stage", "attributes"}
        fields += [
            "  - type: dropdown",
            f"    id: {field_id}",
            "    attributes:",
            f"      label: {schema_field}",
        ]
        if multiple:
            fields.append("      multiple: true")
        fields += ["      options:", options(ALLOWED[schema_field]), "    validations:", "      required: true", ""]
    fields += [
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
        "      label: Internal topic routing",
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
    return "\n".join(fields)


class CatalogValidatorTests(unittest.TestCase):
    def test_valid_fixture(self) -> None:
        self.assertEqual(CatalogValidator(_readme()).validate(), [])

    def test_pending_category_is_optional_when_no_pending_entry_exists(self) -> None:
        self.assertEqual(CatalogValidator(_readme(include_pending=False)).validate(), [])

    def test_legacy_entries_parser_remains_available_for_seed_fixtures(self) -> None:
        entries = CatalogValidator.entries(
            "### 2022\n\n- (*Journal'22*) **Legacy**\n  [[📝 Paper](https://doi.org/10.1000/legacy)]\n"
        )
        self.assertEqual([(entry.title, entry.section) for entry in entries], [("Legacy", "2022")])

    def test_title_has_no_inline_badge(self) -> None:
        main = _readme().split(MAIN_HEADING, 1)[1].split(RESOURCE_HEADING, 1)[0]
        title_line = next(line for line in main.splitlines() if line.startswith("- (*"))
        self.assertNotIn("![", title_line)
        self.assertEqual(CatalogValidator(_readme()).validate(), [])

    def test_control_line_has_four_badge_groups_and_no_labels(self) -> None:
        main = _readme().split(MAIN_HEADING, 1)[1].split(RESOURCE_HEADING, 1)[0]
        entry = CatalogValidator.entries(main)[0]
        control = entry.block.splitlines()[2]
        self.assertIn("![MRI](assets/badges/domain-mri.svg)", control)
        self.assertIn("![Evaluation](assets/badges/focus-evaluation.svg)", control)
        self.assertIn("![Evaluation](assets/badges/stage-evaluation.svg)<br>", control)
        self.assertIn("![Sex and gender](assets/badges/attributes-sex-and-gender.svg)", control)
        self.assertNotIn("**", control)
        self.assertNotIn("assets-badges", control)

    def test_missing_control_values_are_reported(self) -> None:
        mutated = _readme().replace(
            "  ![MRI](assets/badges/domain-mri.svg)",
            "  **Domain:** ![MRI](assets/badges/domain-mri.svg)",
            1,
        )
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("bold field labels" in error for error in errors))

    def test_invalid_controlled_value_is_reported(self) -> None:
        mutated = _readme().replace(
            "  ![MRI](assets/badges/domain-mri.svg)",
            "  ![Galaxy](assets/badges/domain-galaxy.svg)",
            1,
        )
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("invalid Domain values" in error for error in errors))

    def test_badge_family_must_match_control_field(self) -> None:
        mutated = _readme().replace(
            "  ![MRI](assets/badges/domain-mri.svg)",
            "  ![MRI](assets/badges/focus-mri.svg)",
            1,
        )
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("does not match Domain value" in error for error in errors))

    def test_multiple_imaging_modalities_are_allowed(self) -> None:
        mutated = _readme().replace(
            "  ![MRI](assets/badges/domain-mri.svg) · ![Evaluation](assets/badges/focus-evaluation.svg)",
            "  ![MRI](assets/badges/domain-mri.svg) ![CT](assets/badges/domain-ct.svg) · ![Evaluation](assets/badges/focus-evaluation.svg)",
            1,
        )
        self.assertEqual(CatalogValidator(mutated).validate(), [])

    def test_mixed_modality_and_nonimaging_domain_is_rejected(self) -> None:
        mutated = _readme().replace(
            "  ![MRI](assets/badges/domain-mri.svg) ·",
            "  ![MRI](assets/badges/domain-mri.svg) ![EHR and clinical prediction](assets/badges/domain-ehr-and-clinical-prediction.svg) ·", 1)
        self.assertTrue(any("multiple domains must be concrete" in e for e in CatalogValidator(mutated).validate()))

    def test_perspective_annotation_badge_is_allowed(self) -> None:
        mutated = _readme().replace(
            "<br>![Sex and gender](assets/badges/attributes-sex-and-gender.svg)",
            "<br>![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · ![Perspective](assets/badges/perspective-perspective.svg)",
            1,
        )
        self.assertEqual(CatalogValidator(mutated).validate(), [])

    def test_legacy_double_bracket_links_remain_accepted(self) -> None:
        mutated = _readme().replace(
            "[📝 Paper](https://doi.org/10.1000/fairness-a)",
            "[[📝 Paper](https://doi.org/10.1000/fairness-a)]",
            1,
        )
        self.assertEqual(CatalogValidator(mutated).validate(), [])

    def test_assets_badge_is_hidden_from_entries(self) -> None:
        mutated = _readme().replace(
            "  ![MRI](assets/badges/domain-mri.svg) · ![Evaluation](assets/badges/focus-evaluation.svg) · ![Evaluation](assets/badges/stage-evaluation.svg)<br>![Sex and gender](assets/badges/attributes-sex-and-gender.svg)",
            "  ![MRI](assets/badges/domain-mri.svg) · ![Evaluation](assets/badges/focus-evaluation.svg) · ![Evaluation](assets/badges/stage-evaluation.svg)<br>![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · ![Code](assets/badges/assets-code.svg)",
            1,
        )
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Assets badges must remain hidden" in error for error in errors))

    def test_evidence_badge_is_hidden_from_entries(self) -> None:
        mutated = _readme().replace(
            "  ![MRI](assets/badges/domain-mri.svg) · ![Evaluation](assets/badges/focus-evaluation.svg) · ![Evaluation](assets/badges/stage-evaluation.svg)<br>![Sex and gender](assets/badges/attributes-sex-and-gender.svg)",
            "  ![MRI](assets/badges/domain-mri.svg) · ![Evaluation](assets/badges/focus-evaluation.svg) · ![Evaluation](assets/badges/stage-evaluation.svg)<br>![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · ![Primary full text](assets/badges/evidence-primary-full-text.svg)",
            1,
        )
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Evidence badges must remain hidden" in error for error in errors))

    def test_taxonomy_rejects_repeated_inline_value_text(self) -> None:
        mutated = _readme().replace(
            "| **Domain** | ",
            "| **Domain** | MRI ",
            1,
        )
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("value cell must contain badges only" in error for error in errors))

    def test_taxonomy_hides_evidence_row(self) -> None:
        mutated = _readme().replace(
            MAIN_HEADING,
            "| **Evidence** | ![Primary full text](assets/badges/evidence-primary-full-text.svg) |\n\n" + MAIN_HEADING,
            1,
        )
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Taxonomy must hide the Evidence field" in error for error in errors))

    def test_taxonomy_hides_assets_row(self) -> None:
        mutated = _readme().replace(
            MAIN_HEADING,
            "| **Assets** | ![Code](assets/badges/assets-code.svg) |\n\n" + MAIN_HEADING,
            1,
        )
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Taxonomy must hide the Assets field" in error for error in errors))

    def test_year_mismatch_is_reported(self) -> None:
        mutated = _readme().replace("(*Journal'25*)", "(*Journal'24*)", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("does not match section 2025" in error for error in errors))

    def test_duplicate_identifier_is_reported(self) -> None:
        mutated = _readme().replace("10.1000/fairness-f", "10.1000/fairness-a", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Duplicate identifier DOI:10.1000/fairness-a" in error for error in errors))

    def test_required_method_categories_are_reported(self) -> None:
        mutated = _readme().replace("### Fairness Evaluation", "### Legacy category", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Method category headings differ" in error for error in errors))

    def test_legacy_by_topic_is_rejected(self) -> None:
        mutated = _readme().replace(RESOURCE_HEADING, "## 🧭 By Topic\n\n" + RESOURCE_HEADING, 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Legacy By Topic" in error for error in errors))

    def test_badge_must_be_local_svg(self) -> None:
        mutated = _readme().replace(
            "  ![MRI](assets/badges/domain-mri.svg)",
            "  ![MRI](https://example.org/badge.svg)",
            1,
        )
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("local SVG badges" in error for error in errors))

    def test_tldr_requires_three_english_sentences(self) -> None:
        mutated = _readme().replace(" It reports an evaluated result.", "", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("exactly three complete English sentences" in error for error in errors))

    def test_date_must_match_month_precision(self) -> None:
        mutated = _readme().replace("**Date:** 2025-11-04", "**Date:** 2025-10-04", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("does not match month heading 2025-11" in error for error in errors))

    def test_pending_stage_requires_unknown_stage_value(self) -> None:
        mutated = _readme().replace(
            "  ![MRI](assets/badges/domain-mri.svg) · ![Mitigation](assets/badges/focus-mitigation.svg) · ![Not verified](assets/badges/stage-not-verified.svg)<br>![Sex and gender](assets/badges/attributes-sex-and-gender.svg)",
            "  ![MRI](assets/badges/domain-mri.svg) · ![Mitigation](assets/badges/focus-mitigation.svg) · ![Evaluation](assets/badges/stage-evaluation.svg)<br>![Sex and gender](assets/badges/attributes-sex-and-gender.svg)",
            1,
        )
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Stage pending entries require" in error for error in errors))

    def test_missing_resource_category_is_reported(self) -> None:
        mutated = _readme().replace("### Toolkits", "### Tools", 1)
        errors = CatalogValidator(mutated).validate()
        self.assertTrue(any("Resource categories differ" in error for error in errors))
        self.assertTrue(any("Resource category 'Toolkits' has no entries" in error for error in errors))


class IssueFormValidatorTests(unittest.TestCase):
    def test_valid_fixture(self) -> None:
        self.assertEqual(IssueFormValidator("README without topic headings", _issue_form()).validate(), [])

    def test_schema_option_drift_is_reported(self) -> None:
        mutated = _issue_form().replace("        - MRI", "        - Galaxy", 1)
        errors = IssueFormValidator("README without topic headings", mutated).validate()
        self.assertTrue(any("field 'domain' options differ" in error for error in errors))

    def test_domain_issue_field_allows_multiple_modalities(self) -> None:
        form = _issue_form()
        block = form[form.index("    id: domain") : form.index("    id: focus")]
        self.assertIn("      multiple: true", block)

    def test_missing_required_field_is_reported(self) -> None:
        mutated = _issue_form().replace("    id: qualification", "    id: removed_qualification", 1)
        errors = IssueFormValidator("README without topic headings", mutated).validate()
        self.assertTrue(any("missing field 'qualification'" in error for error in errors))


if __name__ == "__main__":
    unittest.main()


class DecimalSummaryTests(unittest.TestCase):
    def test_three_sentences_preserve_decimal_results(self):
        sentences = ["This study audits gender bias.", "It compares clinical predictions.",
                     "It fixes 17.7% of errors while breaking 1.3% of correct predictions."]
        self.assertEqual(_sentences(" ".join(sentences)), sentences)
