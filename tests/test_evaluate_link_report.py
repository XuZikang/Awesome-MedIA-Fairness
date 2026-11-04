import unittest

from scripts.evaluate_link_report import evaluate


class LinkReportTests(unittest.TestCase):
    def test_empty_report_fails(self):
        code, summary = evaluate({"total": 0, "error_map": {}})
        self.assertEqual(code, 1)
        self.assertIn("no links", summary)

    def test_missing_local_and_remote_404_fail(self):
        report = {
            "total": 2,
            "error_map": {
                "README.md": [
                    {"url": "file:///repo/missing.md", "status": {"text": "File not found"}},
                    {"url": "https://example.org/missing", "status": {"code": 404, "text": "Not Found"}},
                ]
            },
        }
        code, summary = evaluate(report)
        self.assertEqual(code, 1)
        self.assertIn("2 hard failures", summary)

    def test_transient_remote_failures_are_reported_without_failing(self):
        report = {
            "total": 3,
            "error_map": {
                "README.md": [
                    {"url": "https://example.org/blocked", "status": {"code": 403, "text": "Forbidden"}},
                    {"url": "https://example.org/unavailable", "status": {"code": 502, "text": "Bad Gateway"}},
                ]
            },
            "timeout_map": {"README.md": [{"url": "https://example.org/slow"}]},
        }
        code, summary = evaluate(report)
        self.assertEqual(code, 0)
        self.assertIn("3 transient or access warnings", summary)


if __name__ == "__main__":
    unittest.main()
