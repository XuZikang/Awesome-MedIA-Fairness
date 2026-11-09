import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from scripts.screening_policy import paper_version,content_version,current_human_decision
from scripts.literature_pipeline.analysis import route,validate_review
from scripts.review_workflow import read_decisions,import_human_decisions
from tests.test_literature_pipeline import analysis

class ScreeningPolicyTests(unittest.TestCase):
    def test_metadata_refresh_does_not_reopen_human_rejection(self):
        p={'id':'p-abc','title':'A clinical AI review','abstract_hash':'unchanged','updated':'2026-11-03'}
        ledger={'p-abc':{'decision':'reject','content_version':content_version(p)}}
        self.assertEqual(current_human_decision({**p,'updated':'2026-11-08'},ledger)['decision'],'reject')
        self.assertEqual(current_human_decision({**p,'pmcid':'PMC12345','doi':'10.1000/newidentifier'},ledger)['decision'],'reject')
        self.assertEqual(current_human_decision({**p,'abstract_hash':'new content'},ledger),{})

    def test_cataloged_work_is_not_sent_for_model_review_again(self):
        from scripts.literature_pipeline.cli import connect,ingest,review_pending
        from tests.test_literature_pipeline import record
        with tempfile.TemporaryDirectory() as d:
            db=connect(Path(d)/'state.sqlite3')
            try:
                ingest(db,record(),'2026-11-09')
                catalog=[{'title':'Publisher title variant','arxiv_id':record()['arxiv_id']}]
                with patch.dict('os.environ',{'LITERATURE_LLM_ENDPOINT':'http://127.0.0.1:3425/v1/chat/completions','LITERATURE_LLM_MODEL':'qoder-cn/dfmodel'}),patch('scripts.literature_pipeline.cli.review') as model:
                    self.assertEqual(review_pending(db,'2026-11-09',10,True,catalog_records=catalog)['reviewed'],0)
                    model.assert_not_called()
            finally:db.close()

    def test_original_methods_rank_above_reviews(self):
        method={'title':'A novel fairness calibration algorithm for clinical prediction','abstract':'We propose a subgroup fairness metric and mitigation method.'}
        review={'title':'A review of fairness calibration in clinical prediction','abstract':'This review discusses a subgroup fairness metric and mitigation method.'}
        self.assertGreater(route(method)['priority'],route(review)['priority'])

    def test_incidental_review_is_not_recommended_as_related(self):
        r=analysis();r.update(article_type='review',decision='related')
        with self.assertRaisesRegex(ValueError,'specific medical task'):
            validate_review(r,'A medical model evaluates subgroup disparities.','abstract')

    def test_specific_and_detailed_review_is_eligible_without_new_author_experiments(self):
        r=analysis();r['article_type']='review'
        q='medical model evaluates subgroup disparities'
        r['review_scope']={k:{'met':True,'quote':q} for k in ('specific_task','detailed_fairness')}
        validate_review(r,'A medical model evaluates subgroup disparities.','full_text')
        r['review_scope']['detailed_fairness']={'met':False,'quote':''}
        with self.assertRaises(ValueError):validate_review(r,'A medical model evaluates subgroup disparities.','full_text')

    def test_human_rejection_survives_prompt_change_but_not_article_change(self):
        p={'id':'p-abc','title':'Generic clinical AI review','abstract_hash':'original'}
        ledger={'p-abc':{'decision':'reject','paper_version':paper_version(p)}}
        self.assertEqual(current_human_decision(p,ledger)['decision'],'reject')
        self.assertEqual(current_human_decision({**p,'abstract_hash':'revised'},ledger),{})

    def test_accepts_inclusion_word_and_rejection_without_model_analysis(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);packet=root/'review.md'
            packet.write_text('## p-abc\n\n审核决定：纳入\n审核备注：通过。\n证据版本：fp\n\n## p-def\n\n审核决定：排除\n审核备注：comment\n证据版本：待取得有效分析\n')
            state=root/'state.json';state.write_text(json.dumps({'papers':[{'id':'p-abc','title':'A'},{'id':'p-def','title':'B'}],'analyses':[['p-abc','fp',{}]]}))
            x=import_human_decisions(packet,state,root/'ledger.json')
            self.assertEqual(x['p-abc']['decision'],'approve')
            self.assertEqual(x['p-def']['decision'],'reject')
            self.assertEqual(read_decisions(packet)['p-abc']['decision'],'approve')
