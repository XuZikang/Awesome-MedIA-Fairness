import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.catalog_editorial import verify_public_code
from scripts.literature_pipeline.analysis import review_fingerprint, validate_review
from scripts.literature_pipeline.cli import connect, ingest, review_pending, supplement_matches
from scripts.review_workflow import read_decisions, write_review_packet
from scripts.literature_pipeline.official_lists import fetch_official_list
from tests.test_literature_pipeline import analysis, record


class TwoStageWorkflowTests(unittest.TestCase):
    def test_abstract_recommendation_is_only_a_shortlist_decision(self):
        abstract = 'A medical model evaluates subgroup disparities.'
        validate_review(analysis(), abstract, 'abstract', initial=True)
        with self.assertRaisesRegex(ValueError, 'full-text'):
            validate_review(analysis(), abstract, 'abstract')

    def test_discovery_model_reads_abstract_without_retrieving_full_text(self):
        with tempfile.TemporaryDirectory() as directory:
            db = connect(Path(directory) / 'state.sqlite3')
            self.addCleanup(db.close)
            ingest(db, {**record(), 'abstract': 'A medical model evaluates subgroup disparities.'}, '2026-11-23')
            with patch.dict('os.environ', {'LITERATURE_LLM_ENDPOINT': 'http://localhost/model',
                                           'LITERATURE_LLM_MODEL': 'fixture-model'}), \
                 patch('scripts.literature_pipeline.cli.fetch_evidence') as fetch, \
                 patch('scripts.literature_pipeline.cli.review', return_value={**analysis(), 'evidence_level': 'abstract'}) as model:
                self.assertEqual(review_pending(db, '2026-11-23', 1, False)['reviewed'], 1)
                fetch.assert_not_called()
                self.assertEqual(model.call_args.args[1]['phase'], 'initial')

    def test_packet_separates_excludes_ineligible_and_pending(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            db = connect(root / 'state.sqlite3')
            self.addCleanup(db.close)
            decisions = [('suggest_include', 'preprint'), ('exclude', 'eligible'),
                         ('hold', 'eligible'), ('suggest_include', 'pending'),
                         ('suggest_include', 'ineligible')]
            ids = []
            for index, (decision, venue) in enumerate(decisions):
                paper = {**record(), 'title': f'Clinical subgroup audit {index}',
                         'doi': f'10.1101/{index}', 'arxiv_id': f'2611.0000{index}',
                         'venue_assessment': {'status': venue, 'reason_zh': '渠道证据'}}
                pid, _ = ingest(db, paper, '2026-11-23')
                ids.append(pid)
                saved = json.loads(db.execute('SELECT payload FROM papers WHERE id=?', (pid,)).fetchone()[0])
                result = {**analysis(), 'decision': decision, 'model': 'fixture',
                          'evidence_level': 'abstract', 'evidence_url': paper['url']}
                db.execute('INSERT INTO analyses VALUES (?,?,?)',
                           (pid, review_fingerprint(saved, 'fixture'), json.dumps(result)))
            reports = root / 'reports'
            write_review_packet(db, reports, '2026-11-23', root / 'README.md')
            self.assertEqual(set(read_decisions(reports / 'review-latest.md')), {ids[0]})
            for index in (1, 4):
                self.assertIn(ids[index], (reports / 'screening-exclusions.md').read_text())
            for index in (2, 3):
                self.assertIn(ids[index], (reports / 'screening-pending.md').read_text())

    def test_code_must_be_public_and_for_this_article(self):
        paper = {'title': 'A Study of Clinical Fairness'}
        url = 'https://github.com/example/research'
        public = {'private': False, 'disabled': False, 'full_name': 'example/research'}
        with patch('scripts.catalog_editorial._github_json', return_value=public) as request:
            code = verify_public_code(paper, [url], f'Our code is available at {url}.')
            self.assertEqual(code['url'], url)
            request.assert_called_once()
        with patch('scripts.catalog_editorial._github_json',
                   side_effect=[public, {'content': 'VW5yZWxhdGVkIHByb2plY3Q='}]):
            self.assertEqual(verify_public_code(paper, [url], f'Baseline: {url}')['status'], 'not_verified')
        with patch('scripts.catalog_editorial._github_json') as request:
            self.assertEqual(verify_public_code(paper, [url], 'No source link here.')['status'], 'not_verified')
            request.assert_not_called()

    def test_supplement_keeps_medical_fairness_not_generic_clinical_hits(self):
        self.assertTrue(supplement_matches({'title':'Subgroup disparity in clinical prediction'}, {}))
        self.assertFalse(supplement_matches({'title':'Clinical treatment outcome prediction'}, {}))
        self.assertFalse(supplement_matches({'title':'Mortgage bias'}, {}))


    def test_official_conference_release_keeps_acceptance_separate_from_publication(self):
        spec = {'provider': 'neurips', 'conference': 'NeurIPS', 'conference_status': 'accepted',
                'event_date': '2026-12-06', 'url': 'https://neurips.cc/Downloads/2026'}
        pages = {
            spec['url']: b'<a href="/virtual/2026/poster/42" class="Poster">Clinical model fairness</a>'
                         b'<a href="/virtual/2026/workshop/10">Health Workshop</a>',
            'https://neurips.cc/virtual/2026/poster/42':
                b'<div class="abstract-text-inner"><p>Evaluation across groups.</p></div>',
        }
        def request(url, source, timeout):
            return pages[url]
        records, complete, total = fetch_official_list('2026-11-19', '2026-11-23', spec,
                                                       lambda p: True, request=request)
        self.assertTrue(complete)
        self.assertEqual(total, 1)
        self.assertEqual(records[0]['conference_status'], 'accepted')
        self.assertEqual(records[0]['abstract'], 'Evaluation across groups.')
        self.assertNotIn('published', records[0])
        self.assertEqual(fetch_official_list('2025-11-19', '2025-11-23', spec,
                                              lambda p: True, request=request), ([], True, 0))
