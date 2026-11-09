import copy
import unittest
from pathlib import Path

from scripts.venue_policy import assess_venue, load_policy, validate_policy


ROOT = Path(__file__).resolve().parents[1]


def small_policy():
    return {
        "schema_version": "test",
        "rules": {
            "cas_eligible_zones": [1, 2],
            "cas_ineligible_zones": [3, 4],
            "ccf_eligible_ranks": ["A", "B"],
            "ccf_ineligible_ranks": ["C"],
            "unknown_status": "pending",
            "preprint_status": "preprint",
            "workshop_inherits_parent_rank": False,
        },
        "sources": {
            "cas": {
                "edition": "test-cas",
                "title": "Test CAS",
                "page_url": "https://example.org/cas",
                "download_url": "https://example.org/cas.xls",
                "sha256": "a" * 64,
                "rows": 2,
            },
            "ccf": {
                "edition": "test-ccf",
                "title": "Test CCF",
                "page_url": "https://example.org/ccf",
                "download_url": "https://example.org/ccf.pdf",
                "sha256": "b" * 64,
                "rows": 4,
            },
        },
        "registries": {
            "cas_journals": [
                {"title": "Exact Journal", "zone": 1, "issns": ["1234-5678"]},
                {"title": "Low Journal", "zone": 3},
            ],
            "ccf_venues": [
                {"kind": "conference", "rank": "A", "title": "Good Conference", "aliases": ["GC"]},
                {"kind": "conference", "rank": "C", "title": "C Conference", "aliases": ["CCONF"]},
                {"kind": "journal", "rank": "A", "title": "CCF Journal", "aliases": ["CJ"]},
                {"kind": "journal", "rank": "C", "title": "C Journal", "aliases": ["CJ-C"]},
            ],
        },
    }


class VenuePolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = load_policy(ROOT)

    def test_verified_source_registry_and_common_medical_venues(self):
        self.assertEqual(validate_policy(self.policy), [])
        self.assertEqual(self.policy["sources"]["cas"]["rows"], 21772)
        self.assertEqual(self.policy["sources"]["ccf"]["rows"], 679)
        self.assertEqual(assess_venue({"journal_title": "Medical Image Analysis"}, self.policy)["status"], "eligible")
        self.assertEqual(assess_venue({"conference": "MICCAI"}, self.policy)["status"], "eligible")
        self.assertEqual(assess_venue({"conference": "FSE"}, self.policy)["status"], "pending")
        self.assertEqual(assess_venue({"journal_title": "CC"}, self.policy)["status"], "pending")

    def test_exact_aliases_do_not_use_fuzzy_matching(self):
        policy = small_policy()
        self.assertEqual(assess_venue({"conference": "GC"}, policy)["status"], "eligible")
        self.assertEqual(assess_venue({"conference": "G"}, policy)["status"], "pending")
        self.assertEqual(assess_venue({"journal_title": "Exact Journal"}, policy)["status"], "eligible")
        self.assertEqual(assess_venue({"journal_title": "Exact Journal Extra"}, policy)["status"], "pending")

    def test_issn_title_consistency_is_required_when_both_are_known(self):
        policy = small_policy()
        self.assertEqual(
            assess_venue({"journal_issns": ["1234-5678"]}, policy)["status"],
            "eligible",
        )
        self.assertEqual(
            assess_venue({"journal_title": "Exact Journal", "journal_issns": ["8765-4321"]}, policy)["status"],
            "pending",
        )

    def test_cas_three_four_and_ccf_c_are_ineligible(self):
        policy = small_policy()
        self.assertEqual(assess_venue({"journal_title": "Low Journal"}, policy)["status"], "ineligible")
        self.assertEqual(assess_venue({"conference": "CCONF"}, policy)["status"], "ineligible")
        self.assertEqual(assess_venue({"journal_title": "C Journal"}, policy)["status"], "pending")

    def test_ccf_a_b_applies_to_main_conferences_only(self):
        policy = small_policy()
        self.assertEqual(assess_venue({"conference": "Good Conference"}, policy)["status"], "eligible")
        self.assertEqual(
            assess_venue({"conference": "Good Conference", "publication_type": "Workshop"}, policy)["status"],
            "ineligible",
        )
        self.assertEqual(
            assess_venue({"conference": "Good Conference", "paper_type": "Short paper"}, policy)["status"],
            "ineligible",
        )
        self.assertEqual(
            assess_venue({"journal_title": "Exact Journal", "publication_type": "Short communication"}, policy)["status"],
            "eligible",
        )

    def test_ccf_journal_a_b_does_not_qualify_a_journal(self):
        policy = small_policy()
        self.assertEqual(assess_venue({"journal_title": "CCF Journal"}, policy)["status"], "pending")

    def test_preprint_states_and_formal_gate(self):
        policy = small_policy()
        self.assertEqual(
            assess_venue({"arxiv_id": "2412.12345", "publication_kind": "preprint"}, policy)["status"],
            "preprint",
        )
        self.assertEqual(
            assess_venue({"source": "arxiv", "publication_kind": "preprint", "doi": "10.1234/formal"}, policy)["status"],
            "pending",
        )
        failed = assess_venue(
            {
                "source": "arxiv",
                "publication_kind": "preprint",
                "doi": "10.48550/arXiv.2412.12345",
                "formal_publications": [{"journal_title": "Low Journal"}],
            },
            policy,
        )
        self.assertEqual(failed["status"], "ineligible")
        passed = assess_venue(
            {
                "source": "arxiv",
                "publication_kind": "preprint",
                "doi": "10.48550/arXiv.2412.12345",
                "formal_publications": [{"conference": "Good Conference"}],
            },
            policy,
        )
        self.assertEqual(passed["status"], "eligible")
        self.assertTrue(passed["preprint"])

    def test_preprint_platform_own_doi_is_not_a_formal_publication_claim(self):
        for source,identifier in [('biorxiv','10.1101/2026.01.01.123456'),('medrxiv','10.64898/2026.01.01.123456'),('europepmc','10.21203/rs.3.rs-123/v1')]:
            self.assertEqual(assess_venue({'source':source,'publication_kind':'preprint','doi':identifier},small_policy())['status'],'preprint')

    def test_formal_tracking_and_child_confidence_cannot_be_overridden(self):
        policy = small_policy()
        paper = {
            "source": "arxiv",
            "publication_kind": "preprint",
            "doi": "10.48550/arXiv.2412.12345",
            "publication_tracking": {"status": "retry_pending"},
            "formal_publications": [{"conference": "Good Conference"}],
        }
        self.assertEqual(assess_venue(paper, policy)["status"], "pending")
        paper.pop("publication_tracking")
        paper["formal_publications"][0]["confidence"] = "unknown"
        self.assertEqual(assess_venue(paper, policy)["status"], "pending")

    def test_invalid_policy_rank_is_reported(self):
        policy = small_policy()
        broken = copy.deepcopy(policy)
        broken["registries"]["ccf_venues"][0]["rank"] = "D"
        self.assertTrue(any("invalid rank" in error for error in validate_policy(broken)))


if __name__ == "__main__":
    unittest.main()
