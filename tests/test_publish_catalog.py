import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.catalog_editorial import validate_annotation
from scripts.literature_pipeline.analysis import review_fingerprint
from scripts.literature_pipeline.cli import connect, ingest
from scripts.publish_catalog import same_record, sync_catalog


class PublicationTests(unittest.TestCase):
    def test_human_approved_abstract_override_preserves_real_evidence_level(self):
        from tests.test_literature_pipeline import record,analysis
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'data').mkdir();(root/'reports').mkdir()
            (root/'data/catalog.json').write_text('[]')
            db=connect(root/'state.sqlite3')
            try:
                pid,_=ingest(db,record(),'2026-11-04')
                p=json.loads(db.execute('SELECT payload FROM papers').fetchone()[0])
                r=analysis();r.update(decision='related',evidence_level='abstract')
                r['metadata']['Evidence']=['Primary abstract']
                fp=review_fingerprint(p)
                db.execute('INSERT INTO analyses VALUES (?,?,?)',(pid,fp,json.dumps(r)));db.commit()
                approval=root/'human.md';approval.write_text('## '+pid+'\n\n审核决定：纳入\n审核备注：确认该具体临床任务的公平性分析。\n证据版本：'+fp+'\n')
                editorial={'tldr_en':['This study audits a clinical prediction task.', 'It compares models across patient subgroups.', 'The abstract reports differences between the groups.'],
                           'method':'Fairness Evaluation','reason_zh':'具体任务的公平性评估。','evidence_quotes':[]}
                with patch('scripts.publish_catalog.fetch_evidence',return_value={'level':'abstract','text':'Original abstract evidence.','url':p['url']}), \
                     patch('scripts.publish_catalog.annotate',return_value=editorial),patch('scripts.publish_catalog.render_catalog'):
                    self.assertEqual(sync_catalog(db,root,approval)['added'],1)
                q=json.loads((root/'data/catalog.json').read_text())[0]
                self.assertEqual(q['metadata']['Evidence'],['Primary abstract'])
                self.assertTrue(q['human_review']['overrides_machine_screening'])
                self.assertNotIn('full-text',q['sources'][0]['section'])
            finally:db.close()

    def test_publication_refuses_missing_human_approval(self):
        with self.assertRaisesRegex(ValueError,'human-reviewed'):
            sync_catalog(None,Path('.'))

    def test_identifier_dedup_preserves_original_title(self):
        self.assertTrue(same_record({'title':'Original title','doi':'10.1/ABC'}, {'title':'Publisher variation','doi':'10.1/abc'}))
        self.assertFalse(same_record({'title':'Different study'}, {'title':'Original study'}))

    def test_annotation_rejects_missing_sentences_and_invented_evidence(self):
        good={'tldr_en':['This paper measures clinical model fairness.', 'It compares explicitly defined patient subgroups.', 'The analysis reports subgroup performance differences.'],
              'method':'Fairness Evaluation','reason_zh':'基于方法证据分类。','evidence_quotes':['patient subgroups']}
        validate_annotation(good,'explicitly defined patient subgroups')
        with self.assertRaises(ValueError):validate_annotation({**good,'tldr_en':good['tldr_en'][:2]},'patient subgroups')
        with self.assertRaises(ValueError):validate_annotation(good,'unrelated abstract')

    def test_publication_requires_explicit_approval_and_current_evidence_and_deduplicates(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'data').mkdir();(root/'reports').mkdir()
            (root/'data/catalog.json').write_text('[]')
            db=connect(root/'state.sqlite3')
            try:
                p={'title':'Clinical subgroup fairness','url':'https://arxiv.org/abs/2601.99999', 'arxiv_id':'2601.99999',
                   'source':'arxiv','published':'2026-01-02','year':'2026','abstract':'Clinical model patient subgroups evaluation'}
                pid,_=ingest(db,p,'2026-11-04')
                paper=json.loads(db.execute('SELECT payload FROM papers').fetchone()[0])
                result={'decision':'suggest_include','evidence_level':'full_text','reason_zh':'具有全文证据。',
                        'metadata':{'Domain':['Medical imaging'],'Focus':['Evaluation'],'Stage':['Evaluation'],
                                    'Attributes':['Sex and gender'],'Evidence':['Primary full text']},
                        'criteria':{k:{'met':True,'quote':'patient subgroups evaluation'} for k in ('medical','algorithm','fairness','groups','evaluation')}}
                approval_file=root/'approved.md'
                approval_file.write_text('## '+pid+'\n\n审核决定：待审核\n审核备注：人工确认测试。\n证据版本：'+review_fingerprint(paper)+'\n')
                def save(r,fp=None):
                    db.execute('INSERT OR REPLACE INTO analyses VALUES (?,?,?)',(pid,fp or review_fingerprint(paper),json.dumps(r)));db.commit()
                editorial={'tldr_en':['This paper measures clinical model fairness.', 'It compares explicitly defined patient subgroups.', 'The analysis reports subgroup performance differences.'],
                           'method':'Fairness Evaluation','reason_zh':'分类依据为亚组评估。','evidence_quotes':[]}
                with patch('scripts.publish_catalog.fetch_evidence',return_value={'level':'full_text','text':'paper text','url':p['url']}), \
                     patch('scripts.publish_catalog.annotate',return_value=editorial), patch('scripts.publish_catalog.render_catalog'):
                    save({**result,'evidence_level':'abstract'})
                    self.assertEqual(sync_catalog(db,root,approval_file)['added'],0)
                    approval_file.write_text(approval_file.read_text().replace('审核决定：待审核','审核决定：通过'))
                    save(result,fp='stale')
                    self.assertEqual(sync_catalog(db,root,approval_file)['added'],0)
                    save(result)
                    approval_file.write_text(approval_file.read_text().replace('审核决定：通过','审核决定：暂缓'))
                    self.assertEqual(sync_catalog(db,root,approval_file)['added'],0)
                    approval_file.write_text(approval_file.read_text().replace('审核决定：暂缓','审核决定：通过'))
                    self.assertEqual(sync_catalog(db,root,approval_file),{'added':1,'failures':0})
                    self.assertEqual(sync_catalog(db,root,approval_file)['added'],0)
                published=json.loads((root/'data/catalog.json').read_text())
                self.assertEqual(published[0]['title'],p['title'])
                self.assertEqual(published[0]['metadata']['Domain'],['Medical imaging (modality unspecified)'])
                self.assertEqual(len(published[0]['tldr_en']),3)
                self.assertNotIn('abstract',published[0])
                self.assertIn('全文证据',(root/'reports/catalog-screening.md').read_text())
            finally:db.close()
