from __future__ import annotations

import json
import unittest
from unittest.mock import patch

from scripts.literature_pipeline import discovery


class FakeResponse:
    def __init__(self, payload: bytes):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return self.payload


def medrxiv_payload(records: list[dict], total: int | None = None) -> bytes:
    messages = [{"status": "ok"}]
    if total is not None:
        messages[0]["total"] = str(total)
    return json.dumps({"messages": messages, "collection": records}).encode()


class DiscoveryTests(unittest.TestCase):
    def test_medrxiv_single_page_preserves_preprint_and_published_doi(self):
        payload = medrxiv_payload(
            [{
                "title": "A medical fairness preprint",
                "authors": "Ada Lovelace; Grace Hopper",
                "doi": "10.64898/2026.11.01.123456",
                "rel_doi": "10.1000/formal-version",
                "date": "2026-11-02",
                "published": "NA",
                "version": "2",
                "abstract": "A bounded analysis.",
            }],
            total=1,
        )
        with patch.object(discovery.urllib.request, "urlopen", return_value=FakeResponse(payload)) as opener:
            records, complete, total = discovery.fetch_medrxiv(
                "2026-11-01", "2026-11-30", {"max_records": 10}
            )
        self.assertTrue(complete)
        self.assertEqual(total, 1)
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(record["doi"], "10.64898/2026.11.01.123456")
        self.assertEqual(record["published_doi"], "10.1000/formal-version")
        self.assertEqual(record["publication_kind"], "preprint")
        self.assertEqual(record["published"], "2026-11-02")
        self.assertEqual(
            record["url"],
            "https://www.medrxiv.org/content/10.64898/2026.11.01.123456v2",
        )
        self.assertEqual(record["authors"], ["Ada Lovelace", "Grace Hopper"])
        self.assertEqual(opener.call_args.args[0].get_header("User-agent"), discovery.USER_AGENT)

    def test_medrxiv_paginates_by_cursor(self):
        first = medrxiv_payload(
            [{"title": "First", "doi": "10.64898/2026.11.01.1", "date": "2026-11-01"}],
            total=2,
        )
        second = medrxiv_payload(
            [{"title": "Second", "doi": "10.64898/2026.11.01.2", "date": "2026-11-02"}],
            total=2,
        )
        with patch.object(
            discovery.urllib.request,
            "urlopen",
            side_effect=[FakeResponse(first), FakeResponse(second)],
        ) as opener:
            records, complete, total = discovery.fetch_medrxiv(
                # The service may return fewer rows than a caller's nominal
                # page_size while ``total`` still reports more pages.
                "2026-11-01", "2026-11-30", {"page_size": 100, "max_records": 5}
            )
        self.assertTrue(complete)
        self.assertEqual(total, 2)
        self.assertEqual([record["title"] for record in records], ["First", "Second"])
        self.assertIn("/0/json", opener.call_args_list[0].args[0].full_url)
        self.assertIn("/1/json", opener.call_args_list[1].args[0].full_url)

    def test_medrxiv_max_records_is_incomplete(self):
        payload = medrxiv_payload(
            [
                {"title": "First", "doi": "10.64898/2026.11.01.1", "date": "2026-11-01"},
                {"title": "Second", "doi": "10.64898/2026.11.01.2", "date": "2026-11-02"},
            ],
            total=3,
        )
        with patch.object(discovery.urllib.request, "urlopen", return_value=FakeResponse(payload)):
            records, complete, total = discovery.fetch_medrxiv(
                "2026-11-01", "2026-11-30", {"page_size": 2, "max_records": 1}
            )
        self.assertFalse(complete)
        self.assertEqual(total, 3)
        self.assertEqual(len(records), 1)

    def test_medrxiv_unknown_total_uses_short_page_as_complete(self):
        payload = medrxiv_payload(
            [{"title": "One", "doi": "10.64898/2026.11.01.1", "date": "2026-11-01"}]
        )
        with patch.object(discovery.urllib.request, "urlopen", return_value=FakeResponse(payload)):
            records, complete, total = discovery.fetch_medrxiv(
                "2026-11-01", "2026-11-30", {"page_size": 10, "max_records": 10}
            )
        self.assertTrue(complete)
        self.assertEqual(total, 1)
        self.assertEqual(len(records), 1)

    def test_date_and_config_validation(self):
        with self.assertRaises(ValueError):
            discovery.fetch_medrxiv("2026-12-01", "2026-11-01")
        with self.assertRaises(ValueError):
            discovery.fetch_medrxiv("2026-11-01", "2026-11-02", {"base_url": "not-a-url"})
        with self.assertRaises(ValueError):
            discovery.fetch_medrxiv("2026-11-01", "2026-11-02", {"max_records": 0})

    def test_conference_json_filters_by_paper_date_and_uses_event_fallback(self):
        payload = json.dumps({
            "papers": [
                {
                    "title": "Published main paper",
                    "published": "2026-11-05",
                    "doi": "10.1234/main",
                    "url": "https://papers.example.org/main",
                    "pdf_url": "https://openaccess.thecvf.com/content/CVPR2026/html/a.pdf",
                },
                {
                    "title": "Outside paper",
                    "published": "2026-01-05",
                    "doi": "10.1234/outside",
                    "url": "https://papers.example.org/outside",
                },
                {
                    "title": "Undated event paper",
                    "doi": "10.1234/undated",
                    "url": "https://papers.example.org/undated",
                },
            ]
        }).encode()
        config = {
            "max_records": 10,
            "event_window_days": 7,
            "events": [{
                "name": "Example 2026",
                "conference": "Example",
                "rank": "B",
                "status": "published",
                "event_date": "2026-11-10",
                "format": "json",
                "url": "https://papers.example.org/list.json",
            }],
        }
        with patch.object(discovery.urllib.request, "urlopen", return_value=FakeResponse(payload)):
            records, complete, total = discovery.fetch_conference("2026-11-01", "2026-11-30", config)
        self.assertTrue(complete)
        self.assertEqual(total, 3)  # raw source count, before date filtering
        self.assertEqual([record["title"] for record in records], ["Published main paper", "Undated event paper"])
        self.assertEqual(records[0]["publication_kind"], "conference-paper")
        self.assertEqual(records[0]["conference_status"], "published-main")
        self.assertEqual(records[0]["full_text_pdf"], "https://openaccess.thecvf.com/content/CVPR2026/html/a.pdf")
        self.assertEqual(records[1]["published"], "")
        self.assertEqual(records[1]["event_date"], "2026-11-10")

    def test_conference_paper_date_takes_precedence_over_event_date(self):
        payload = json.dumps({"papers": [{
            "title": "Outside despite event window",
            "published": "2026-01-01",
            "url": "https://papers.example.org/outside",
        }]}).encode()
        config = {
            "event_window_days": 30,
            "events": [{
                "url": "https://papers.example.org/list.json",
                "format": "json",
                "event_date": "2026-11-10",
            }],
        }
        with patch.object(discovery.urllib.request, "urlopen", return_value=FakeResponse(payload)):
            records, complete, total = discovery.fetch_conference("2026-11-01", "2026-11-30", config)
        self.assertTrue(complete)
        self.assertEqual(total, 1)
        self.assertEqual(records, [])

    def test_openreview_notes_are_flattened_and_accepted_is_not_published(self):
        payload = json.dumps({"notes": [{
            "id": "abc123",
            "forum": "abc123",
            "content": {
                "title": {"value": "An accepted medical paper"},
                "abstract": {"value": "Abstract."},
                "authors": {"value": ["A. Author"]},
                "decision": {"value": "Accept"},
                "created": {"value": 1794000000000},
            },
        }]}).encode()
        config = {
            "events": [{
                "url": "https://openreview.net/group?id=Test",
                "format": "openreview",
                "conference": "TestConf",
                "status": "accepted",
            }],
        }
        with patch.object(discovery.urllib.request, "urlopen", return_value=FakeResponse(payload)):
            records, complete, total = discovery.fetch_conference("2026-11-01", "2026-11-30", config)
        self.assertTrue(complete)
        self.assertEqual(total, 1)
        self.assertEqual(records[0]["title"], "An accepted medical paper")
        self.assertEqual(records[0]["url"], "https://openreview.net/forum?id=abc123")
        self.assertEqual(records[0]["publication_kind"], "conference-accepted")
        self.assertEqual(records[0]["conference_status"], "accepted-main")
        self.assertEqual(records[0]["published"], "")

    def test_medrxiv_published_field_is_related_doi_and_date_is_version_posting_date(self):
        paper = discovery._record({
            "title": "A study of fairness", "doi": "10.1101/2026.11.20.000001",
            "date": "2026-11-20", "published": "10.1234/article", "version": "2",
        }, "medrxiv", {}, 0)
        self.assertEqual(paper["published"], "2026-11-20")
        self.assertEqual(paper["updated"], "2026-11-20")
        self.assertEqual(paper["published_doi"], "10.1234/article")

    def test_conference_atom_resolves_relative_urls(self):
        payload = b"""
        <feed xmlns="http://www.w3.org/2005/Atom"><entry>
          <title>XML paper</title><id>xml-1</id>
          <published>2026-11-03T00:00:00Z</published>
          <author><name>XML Author</name></author>
          <link href="../paper/xml-1" />
        </entry></feed>
        """
        config = {"events": [{
            "url": "https://official.example.org/events/2026/feed.xml",
            "format": "atom",
        }]}
        with patch.object(discovery.urllib.request, "urlopen", return_value=FakeResponse(payload)):
            records, complete, total = discovery.fetch_conference("2026-11-01", "2026-11-30", config)
        self.assertTrue(complete)
        self.assertEqual(total, 1)
        self.assertEqual(records[0]["url"], "https://official.example.org/events/paper/xml-1")
        self.assertEqual(records[0]["authors"], ["XML Author"])

    def test_conference_html_uses_configured_link_pattern_and_real_base(self):
        payload = b"""
        <html><body><nav><a href="/about">About</a></nav>
        <ul><li><a href="../paper/1">A medical paper</a></li></ul></body></html>
        """
        config = {"events": [{
            "url": "https://official.example.org/events/2026/index.html",
            "format": "html",
            "link_pattern": r"/paper/",
            "event_date": "2026-11-10",
        }]}
        with patch.object(discovery.urllib.request, "urlopen", return_value=FakeResponse(payload)):
            records, complete, total = discovery.fetch_conference("2026-11-01", "2026-11-30", config)
        self.assertTrue(complete)
        self.assertEqual(total, 1)
        self.assertEqual(records[0]["url"], "https://official.example.org/events/paper/1")
        self.assertEqual(records[0]["title"], "A medical paper")

    def test_conference_deduplicates_events_and_reports_truncation(self):
        payload = json.dumps({"records": [{
            "title": "Same paper",
            "doi": "10.1234/same",
            "published": "2026-11-03",
            "url": "https://papers.example.org/same",
        }, {
            "title": "Second paper",
            "doi": "10.1234/second",
            "published": "2026-11-04",
            "url": "https://papers.example.org/second",
        }]}).encode()
        config = {
            "max_records": 1,
            "events": [
                {"url": "https://papers.example.org/one.json", "format": "json"},
                {"url": "https://papers.example.org/two.json", "format": "json"},
            ],
        }
        with patch.object(
            discovery.urllib.request,
            "urlopen",
            side_effect=[FakeResponse(payload), FakeResponse(payload)],
        ):
            records, complete, total = discovery.fetch_conference("2026-11-01", "2026-11-30", config)
        self.assertFalse(complete)
        self.assertEqual(total, 4)  # two source lists, each with two rows
        self.assertEqual(len(records), 1)

    def test_conference_rejects_missing_or_non_http_url(self):
        with self.assertRaises(ValueError):
            discovery.fetch_conference("2026-11-01", "2026-11-30", {"events": [{}]})
        with self.assertRaises(ValueError):
            discovery.fetch_conference(
                "2026-11-01", "2026-11-30", {"events": [{"url": "file:///tmp/list"}]}
            )


if __name__ == "__main__":
    unittest.main()
