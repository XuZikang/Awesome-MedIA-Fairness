from __future__ import annotations

import json
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.literature_pipeline.analysis import TOPICS, fetch_evidence, review, validate_review
from scripts.literature_pipeline.cli import ROOT, connect, export_state, import_state, ingest, main, review_pending, seed_catalog
from scripts.validate_catalog import CatalogValidator

CATALOG_COUNT = len(CatalogValidator.entries((ROOT / "README.md").read_text().split("## 📝 Fairness Papers", 1)[1].split("## 🧭 By Topic", 1)[0]))


def record(**changes):
    paper = {"title": "Fixture medical fairness model", "abstract": "A medical model evaluates subgroup disparities.",
             "url": "https://arxiv.org/abs/2601.99999", "arxiv_id": "2601.99999", "doi": "", "pmid": "", "pmcid": "",
             "source": "arxiv", "source_id": "2601.99999", "published": "2026-01-01", "year": "2026", "updated": "2026-01-01", "version": "1"}
    paper.update(changes)
    return paper


def analysis():
    return {"decision": "suggest_include", "summary_zh": "患者状态预测。", "limitations_zh": "仅为测试数据。", "reason_zh": "有动态预测与评估。",
            "topics": [TOPICS[2]], "metadata": {"Domain": ["Medical imaging"], "Focus": ["Evaluation"], "Stage": ["Evaluation"], "Attributes": ["Sex and gender"]},
            "criteria": {key: {"met": True, "quote": "medical model evaluates subgroup disparities"} for key in ("medical", "algorithm", "fairness", "groups", "evaluation")}}


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.db = connect(self.root / "papers.sqlite3")

    def tearDown(self):
        self.db.close()
        self.directory.cleanup()

    def test_cross_source_dedup_and_revision(self):
        pid, changed = ingest(self.db, record(), "2026-11-01")
        self.assertTrue(changed)
        same, changed = ingest(self.db, record(source="pubmed", pmid="123", doi="10.1000/example"), "2026-11-02")
        self.assertEqual(pid, same)
        self.assertTrue(changed)  # New DOI enriches identity and triggers an evidence recheck.
        _, changed = ingest(self.db, record(source="pubmed", pmid="123", doi="10.1000/example"), "2026-11-02")
        self.assertFalse(changed)
        self.assertEqual(self.db.execute("SELECT count(*) FROM papers").fetchone()[0], 1)
        ingest(self.db, record(version="2", updated="2026-11-03", abstract="Revised medical fairness evaluation."), "2026-11-03")
        paper = json.loads(self.db.execute("SELECT payload FROM papers").fetchone()[0])
        self.assertEqual(paper["first_seen"], "2026-11-01")
        self.assertEqual(paper["last_changed"], "2026-11-03")
        self.assertEqual(paper["version"], "2")

    def test_conflicting_identifiers_do_not_merge_two_papers(self):
        ingest(self.db, record(), "2026-11-01")
        ingest(self.db, record(title="Separate fixture paper", arxiv_id="2601.99998", doi="10.1000/separate"), "2026-11-01")
        with self.assertRaisesRegex(ValueError, "identifier conflict"):
            ingest(self.db, record(doi="10.1000/separate"), "2026-11-02")
        self.assertEqual(self.db.execute("SELECT count(*) FROM papers").fetchone()[0], 2)

    def test_source_abstract_variants_do_not_create_daily_false_updates(self):
        ingest(self.db, record(), "2026-11-01")
        _, changed = ingest(self.db, record(source="pubmed", abstract="Different publisher abstract variant."), "2026-11-02")
        self.assertFalse(changed)
        _, changed = ingest(self.db, record(), "2026-11-02")
        self.assertFalse(changed)

    def test_seed_catalog_is_idempotent(self):
        seed_catalog(self.db, ROOT / "README.md", "2026-11-01")
        before = self.db.execute("SELECT payload FROM papers ORDER BY id").fetchall()
        self.assertEqual(len(before), CATALOG_COUNT)
        seed_catalog(self.db, ROOT / "README.md", "2026-11-02")
        self.assertEqual(before, self.db.execute("SELECT payload FROM papers ORDER BY id").fetchall())

    def test_export_restore_preserves_identity_without_publishing_abstract(self):
        pid, _ = ingest(self.db, record(), "2026-11-01")
        export_state(self.db, self.root / "state.json")
        state_text = (self.root / "state.json").read_text()
        self.assertNotIn(record()["abstract"], state_text)
        other = connect(self.root / "restored.sqlite3")
        try:
            import_state(other, self.root / "state.json")
            same, changed = ingest(other, record(), "2026-11-02")
            self.assertEqual(pid, same)
            self.assertFalse(changed)
        finally:
            other.close()

    def test_fixture_rerun_does_not_duplicate_or_erase_daily_digest(self):
        fixture = self.root / "fixture.json"
        fixture.write_text(json.dumps([record()]))
        arguments = ["--fixture", str(fixture), "--metadata-only", "--db", str(self.root / "cli.sqlite3"),
                     "--state", str(self.root / "state.json"), "--output", str(self.root / "reports"), "--until", "2026-11-04"]
        self.assertEqual(main(arguments), 0)
        report = (self.root / "reports/latest.md").read_text()
        self.assertEqual(main(arguments), 0)
        self.assertEqual(report, (self.root / "reports/latest.md").read_text())
        state = json.loads((self.root / "state.json").read_text())
        self.assertEqual(len(state["papers"]), CATALOG_COUNT + 1)
        self.assertIn("未配置模型接口", report)
        self.assertNotIn(record()["abstract"], report)

    def test_no_model_never_calls_full_text(self):
        ingest(self.db, record(), "2026-11-01")
        with patch.dict("os.environ", {}, clear=True), patch("scripts.literature_pipeline.cli.fetch_evidence") as fetch:
            self.assertEqual(review_pending(self.db, "2026-11-01", 10, True)["mode"], "metadata_only")
            fetch.assert_not_called()

    def test_partial_source_does_not_advance_checkpoint(self):
        # Sources module is imported lazily so fixture-only use has no network dependency.
        import types
        mock_sources = types.ModuleType("scripts.literature_pipeline.sources")
        mock_sources.fetch_source = lambda *a, **k: {"records": [record()], "complete": False, "total": 1000}
        arguments = ["--sources", "arxiv", "--metadata-only", "--db", str(self.root / "cli.sqlite3"),
                     "--state", str(self.root / "state.json"), "--output", str(self.root / "reports"), "--until", "2026-11-04"]
        with patch.dict("sys.modules", {"scripts.literature_pipeline.sources": mock_sources}):
            self.assertEqual(main(arguments), 2)
        state = json.loads((self.root / "state.json").read_text())
        self.assertTrue(all(key.startswith("pending-") for key in state["checkpoints"]))
        self.assertTrue(all(value == "2026-10-05" for key, value in state["checkpoints"].items() if key.startswith("pending-start:")))
        self.assertEqual(len(state["papers"]), CATALOG_COUNT + 1)

    def test_incomplete_initial_window_is_pinned_across_weekly_runs(self):
        import types
        observed = []
        mock_sources = types.ModuleType("scripts.literature_pipeline.sources")
        def fetch(source, query, since, until, **kwargs):
            observed.append((since, until))
            return {"records": [], "complete": False, "total": 1000}
        mock_sources.fetch_source = fetch
        arguments = ["--sources", "arxiv", "--metadata-only", "--db", str(self.root / "cli.sqlite3"),
                     "--state", str(self.root / "state.json"), "--output", str(self.root / "reports")]
        with patch.dict("sys.modules", {"scripts.literature_pipeline.sources": mock_sources}):
            self.assertEqual(main(arguments + ["--until", "2026-11-04"]), 2)
            self.assertEqual(main(arguments + ["--until", "2026-11-11"]), 2)
        self.assertEqual(observed, [("2026-10-05", "2026-11-04")] * 2 + [("2026-10-05", "2026-11-11")] * 2)

    def test_required_model_configuration_cannot_fall_back_to_metadata(self):
        with patch.dict("os.environ", {}, clear=True), self.assertRaises(SystemExit) as caught:
            main(["--require-model"])
        self.assertEqual(caught.exception.code, 2)


class ReviewEvidenceTests(unittest.TestCase):
    def test_invalid_model_quote_is_repaired_by_a_second_real_request(self):
        invalid = analysis()
        invalid["criteria"]["fairness"]["quote"] = "entirely fabricated fairness evaluation evidence"
        def response(value):
            return io.BytesIO(json.dumps({"choices": [{"message": {"content": json.dumps(value)}}]}).encode())
        evidence = {"text": "A medical model evaluates subgroup disparities.", "level": "full_text", "url": record()["url"], "warning": ""}
        with patch("urllib.request.urlopen", side_effect=[response(invalid), response(analysis())]) as http:
            result = review(record(), evidence, "http://localhost/chat/completions", "fixture-model", "")
        self.assertEqual(http.call_count, 2)
        self.assertEqual(result["decision"], "suggest_include")
        last_payload = json.loads(http.call_args.args[0].data)
        self.assertIn("unverifiable evidence", last_payload["messages"][-1]["content"])

    def test_provider_change_invalidates_cached_review(self):
        with tempfile.TemporaryDirectory() as directory:
            db = connect(Path(directory) / "db.sqlite3")
            try:
                ingest(db, record(), "2026-11-04")
                evidence = {"text": "A medical model evaluates subgroup disparities.", "level": "full_text", "url": record()["url"], "warning": ""}
                def response():
                    return io.BytesIO(json.dumps({"choices": [{"message": {"content": json.dumps(analysis())}}]}).encode())
                with patch.dict("os.environ", {"LITERATURE_LLM_ENDPOINT": "http://localhost/one", "LITERATURE_LLM_MODEL": "same-model-name"}, clear=True), \
                        patch("scripts.literature_pipeline.cli.fetch_evidence", return_value=evidence), \
                        patch("urllib.request.urlopen", side_effect=[response(), response()]):
                    self.assertEqual(review_pending(db, "2026-11-04", 10, True)["reviewed"], 1)
                    with patch.dict("os.environ", {"LITERATURE_LLM_ENDPOINT": "http://localhost/two"}):
                        self.assertEqual(review_pending(db, "2026-11-04", 10, True)["reviewed"], 1)
            finally:
                db.close()

    def test_model_http_response_is_validated_and_cached(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            db = connect(root / "db.sqlite3")
            try:
                # Weak keyword routing must not permanently suppress model review.
                pid, _ = ingest(db, record(title="Unlabelled research", abstract="No scope keywords."), "2026-11-04")
                payload = analysis()
                payload["article_text"] = "Provider must not persist this arbitrary text."
                response_json = json.dumps({"choices": [{"message": {"content": json.dumps(payload)}}]}).encode()
                evidence = {"text": "A medical model evaluates subgroup disparities.", "level": "full_text", "url": record()["url"], "warning": ""}
                with patch.dict("os.environ", {"LITERATURE_LLM_ENDPOINT": "http://localhost/chat/completions", "LITERATURE_LLM_MODEL": "fixture-model"}, clear=True), \
                        patch("scripts.literature_pipeline.cli.fetch_evidence", return_value=evidence), \
                        patch("urllib.request.urlopen", return_value=io.BytesIO(response_json)) as http:
                    self.assertEqual(review_pending(db, "2026-11-04", 10, True)["reviewed"], 1)
                    self.assertEqual(review_pending(db, "2026-11-04", 10, True)["reviewed"], 0)
                    http.assert_called_once()
                saved = json.loads(db.execute("SELECT payload FROM analyses WHERE paper_id=?", (pid,)).fetchone()[0])
                self.assertEqual(saved["decision"], "suggest_include")
                self.assertEqual(saved["evidence_level"], "full_text")
                self.assertNotIn("article_text", saved)
            finally:
                db.close()

    def test_full_text_failure_falls_back_and_open_access_xml_is_parsed(self):
        paper = record(pmcid="PMC123", is_open_access=True)
        with patch("urllib.request.urlopen", side_effect=OSError("fixture failure")):
            evidence = fetch_evidence(paper)
        self.assertEqual(evidence["level"], "abstract")
        self.assertTrue(evidence["warning"])
        xml = ("<article><body><sec><p>" + ("Patient states are forecast and evaluated. " * 60) + "</p></sec></body></article>").encode()
        with patch("urllib.request.urlopen", return_value=io.BytesIO(xml)):
            evidence = fetch_evidence(paper)
        self.assertEqual(evidence["level"], "full_text")
        self.assertIn("forecast and evaluated", evidence["text"])

    def test_fabricated_quote_rejected(self):
        with self.assertRaisesRegex(ValueError, "unverifiable"):
            validate_review(analysis(), "Nothing about patient transitions.", "full_text")

    def test_weak_evidence_fragments_are_rejected(self):
        value=analysis()
        value['criteria']['medical']['quote']='medi'
        with self.assertRaisesRegex(ValueError,'too short'):
            validate_review(value,'A medical model evaluates subgroup disparities.','full_text')

    def test_abstract_cannot_be_promoted(self):
        with self.assertRaisesRegex(ValueError, "full-text"):
            validate_review(analysis(), "A medical model evaluates subgroup disparities.", "abstract")

    def test_valid_evidence_and_invalid_stage(self):
        result = analysis()
        validate_review(result, "A medical model evaluates subgroup disparities.", "full_text")
        result["metadata"]["Stage"] = ["Action-conditioned"]
        with self.assertRaisesRegex(ValueError, "invalid metadata"):
            validate_review(result, "A medical model evaluates subgroup disparities.", "full_text")

    def test_missing_evidence_and_invalid_taxonomy_rejected(self):
        result = analysis()
        result["criteria"]["algorithm"]["quote"] = ""
        with self.assertRaisesRegex(ValueError, "missing evidence"):
            validate_review(result, "A medical model evaluates subgroup disparities.", "full_text")
        result = analysis()
        result["metadata"]["Domain"] = ["Unknown"]
        with self.assertRaisesRegex(ValueError, "invalid metadata"):
            validate_review(result, "A medical model evaluates subgroup disparities.", "full_text")


if __name__ == "__main__":
    unittest.main()
