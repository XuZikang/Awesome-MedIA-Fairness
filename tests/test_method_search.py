import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from scripts.literature_pipeline.cli import main
from scripts.literature_pipeline.analysis import route

class MethodSearchTests(unittest.TestCase):
    def test_supplement_queries_execute_with_independent_lane_status(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            config={'initial_days':30,'overlap_days':7,'max_records_per_query':20,'max_analyses_per_run':10,
                    'sources':{'pubmed':['method query']},'supplementary_sources':{'pubmed':['review query']}}
            path=root/'config.json';path.write_text(json.dumps(config))
            calls=[]
            def fetch(source,query,*args,**kwargs):
                calls.append(query)
                return {'records':[],'complete':True,'total':0}
            with patch('scripts.literature_pipeline.sources.fetch_source',side_effect=fetch):
                result=main(['--config',str(path),'--db',str(root/'db.sqlite3'),'--state',str(root/'state.json'),
                             '--output',str(root/'reports'),'--metadata-only','--until','2026-11-09'])
            self.assertEqual(result,0)
            self.assertEqual(calls,['method query','review query'])
            status=json.loads((root/'reports/run-status.json').read_text())
            self.assertEqual([r['lane'] for r in status['sources']],['methodology','review_supplement'])
            self.assertEqual(len({r['query_id'] for r in status['sources']}),2)

    def test_published_review_type_lowers_priority_even_with_method_keywords(self):
        p={'title':'Clinical fairness framework','abstract':'We propose a calibration framework and evaluate prediction models on a dataset.'}
        original={**p,'publication_types':['Journal Article']}
        review={**p,'publication_types':['Journal Article','Review']}
        self.assertGreater(route(original)['priority'],route(review)['priority'])
