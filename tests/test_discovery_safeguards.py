import json
import io
import urllib.error
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import recall
from scripts.publication_tracking import resolve,track,confirmed_aliases
from scripts.literature_pipeline.cli import connect,ingest,main,review_pending
from scripts.literature_pipeline.sources import _parse_europepmc,_parse_pubmed
from scripts.publish_catalog import sync_catalog
from scripts.venue_catalog import validate_catalog_venues


def formal(identifier='10.1234/final',title='Renamed clinical study'):
    return {'DOI':identifier,'type':'journal-article','title':[title],
            'author':[{'family':'Xu'}],'container-title':['Medical Image Analysis'],
            'ISSN':['1361-8415'],'published':{'date-parts':[[2026,10,1]]}}


class RecallSafeguards(unittest.TestCase):
    def test_source_timeout_retains_every_query_window_without_claiming_execution(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);config={'initial_days':30,'overlap_days':7,'max_records_per_query':10,'max_analyses_per_run':1,
                                'sources':{'pubmed':['first query','second query']}}
            file=root/'config.json';file.write_text(json.dumps(config))
            with patch('scripts.literature_pipeline.sources.fetch_source',side_effect=TimeoutError()) as fetch:
                result=main(['--config',str(file),'--db',str(root/'db'),'--state',str(root/'state.json'),
                             '--output',str(root/'reports'),'--metadata-only','--until','2026-11-08'])
            self.assertEqual(result,2);self.assertEqual(fetch.call_count,1)
            status=json.loads((root/'reports/run-status.json').read_text())
            self.assertTrue(status['sources'][0]['attempted']);self.assertFalse(status['sources'][1]['attempted'])
            self.assertFalse(any(s['complete'] for s in status['sources']))
            state=json.loads((root/'state.json').read_text())
            self.assertTrue(all(k.startswith('pending-') for k in state['checkpoints']))

    def test_approved_sentinels_and_negative_controls(self):
        result=recall.check();self.assertTrue(result['passed']);self.assertEqual(len(result['cases']),8)

    def test_removing_mechanism_lane_exposes_a_real_recall_gap(self):
        config=recall.load_config();config['groups']=config['groups'][:1]
        result=recall.check(config)
        self.assertFalse(result['passed'])
        self.assertTrue(any(not row['passed'] and 'confounder-free' in row['title'] for row in result['cases']))

    def test_recall_queries_execute_with_independent_watermarks(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            config={'initial_days':30,'overlap_days':7,'max_records_per_query':20,'max_analyses_per_run':5,
                    'sources':{'pubmed':[]},'recall_config':str(recall.ROOT/'config/recall.json')}
            file=root/'config.json';file.write_text(json.dumps(config));calls=[]
            def fetch(source,query,*args,**kwargs):
                calls.append(query);return {'records':[],'total':0,'complete':True}
            with patch('scripts.literature_pipeline.sources.fetch_source',side_effect=fetch):
                self.assertEqual(main(['--config',str(file),'--db',str(root/'db'),'--state',str(root/'state.json'),
                    '--output',str(root/'reports'),'--sources','pubmed','--metadata-only']),0)
            status=json.loads((root/'reports/run-status.json').read_text())
            self.assertEqual(len(calls),2)
            self.assertEqual({row['lane'] for row in status['sources']},{'recall'})
            self.assertEqual(len(set(row['query_id'] for row in status['sources'])),2)
            self.assertFalse(status['human_review']['automatic_inclusion'])


class PublicationIdentitySafeguards(unittest.TestCase):
    def test_ingestion_does_not_fuse_equal_titles_with_unlinked_dois(self):
        with tempfile.TemporaryDirectory() as d:
            db=connect(Path(d)/'db')
            first,_=ingest(db,{'title':'Common clinical study title','doi':'10.1234/a','url':'https://doi.org/10.1234/a'},'2026-11-09')
            second,_=ingest(db,{'title':'Common clinical study title','doi':'10.1234/b','url':'https://doi.org/10.1234/b'},'2026-11-09')
            self.assertNotEqual(first,second)
            again,_=ingest(db,{'title':'Common clinical study title','doi':'10.1234/b','url':'https://doi.org/10.1234/b'},'2026-11-10')
            self.assertEqual(again,second)
            paper=json.loads(db.execute('SELECT payload FROM papers WHERE id=?',(second,)).fetchone()[0])
            self.assertEqual(paper['publication_tracking']['status'],'needs_identity_review')
            self.assertEqual(db.execute('SELECT count(*) FROM papers').fetchone()[0],2);db.close()

    def test_registered_relation_can_preserve_a_renamed_formal_version(self):
        pre={'DOI':'10.1234/preprint','type':'posted-content','relation':{
             'is-preprint-of':[{'id':'10.1234/final','id-type':'doi'}]}}
        result,issues=resolve({'doi':'10.1234/preprint','title':'Original title'},
                              lambda identifier: pre if identifier.endswith('preprint') else formal())
        self.assertEqual(result[0]['title'],'Renamed clinical study');self.assertFalse(issues)
        self.assertEqual(result[0]['confidence'],'registered_is_preprint_of')

    def test_arxiv_doi_requires_correlated_title_and_first_author(self):
        p={'arxiv_id':'2610.12345','title':'Unrelated study','authors':['Zikang Xu'],'doi':'10.1234/final'}
        result,issues=resolve(p,lambda identifier:formal())
        self.assertEqual(result,[]);self.assertTrue(issues)
        p['title']='Renamed clinical study'
        result,issues=resolve(p,lambda identifier:formal())
        self.assertFalse(issues);self.assertEqual(result[0]['doi'],'10.1234/final')

    def test_same_author_without_an_explicit_link_does_not_merge(self):
        with patch('scripts.publication_tracking.crossref_record') as request:
            self.assertEqual(resolve({'arxiv_id':'2610.12345','title':'Study','authors':['Zikang Xu']}),([],[]))
            request.assert_not_called()

    def test_title_search_is_a_pending_counterpart_not_an_automatic_merge(self):
        with tempfile.TemporaryDirectory() as d:
            db=connect(Path(d)/'db')
            pid,_=ingest(db,{'title':'Renamed clinical study','arxiv_id':'2610.12345','authors':['Zikang Xu'],
                            'url':'https://arxiv.org/abs/2610.12345'},'2026-11-09')
            track(db,'2026-11-09',{'max_records_per_run':1},fetch=lambda i:formal(),search=lambda p:[formal()])
            paper=json.loads(db.execute('SELECT payload FROM papers').fetchone()[0])
            self.assertEqual(paper['publication_tracking']['status'],'needs_identity_review')
            self.assertEqual(paper['formal_publications'],[])
            self.assertEqual(confirmed_aliases(paper),[])
            self.assertEqual(paper['formal_publication_candidates'][0]['doi'],'10.1234/final')
            db.close()

    def test_search_result_with_registered_arxiv_predecessor_confirms_identity(self):
        with tempfile.TemporaryDirectory() as d:
            db=connect(Path(d)/'db')
            ingest(db,{'title':'Renamed clinical study','arxiv_id':'2610.12345','url':'https://arxiv.org/abs/2610.12345'},'2026-11-09')
            hit=formal();hit['relation']={'has-preprint':[{'id-type':'doi','id':'10.48550/arxiv.2610.12345'}]}
            track(db,'2026-11-09',{'max_records_per_run':1},fetch=lambda i:hit,search=lambda p:[hit])
            paper=json.loads(db.execute('SELECT payload FROM papers').fetchone()[0])
            self.assertEqual(paper['publication_tracking']['status'],'checked')
            self.assertIn('doi:10.1234/final',confirmed_aliases(paper))
            db.close()

    def test_failure_preserves_confirmed_links_and_success_date(self):
        with tempfile.TemporaryDirectory() as d:
            db=connect(Path(d)/'db');pid,_=ingest(db,{'title':'Study','doi':'10.1234/preprint','url':'https://doi.org/10.1234/preprint',
                'formal_publications':[{'doi':'10.1234/final'}],'publication_tracking':{'checked_on':'2026-10-01'}},'2026-11-09')
            def failed(identifier):raise TimeoutError()
            stats=track(db,'2026-11-09',{'max_records_per_run':1},fetch=failed)
            p=json.loads(db.execute('SELECT payload FROM papers WHERE id=?',(pid,)).fetchone()[0])
            self.assertEqual(stats['failures'],1);self.assertEqual(p['formal_publications'][0]['doi'],'10.1234/final')
            self.assertEqual(p['publication_tracking']['checked_on'],'2026-10-01')
            db.close()

    def test_existing_identity_conflicts_are_not_destructively_merged(self):
        with tempfile.TemporaryDirectory() as d:
            db=connect(Path(d)/'db')
            pid,_=ingest(db,{'title':'Preprint','doi':'10.1234/pre','url':'https://doi.org/10.1234/pre'},'2026-11-09')
            other,_=ingest(db,{'title':'Formal','doi':'10.1234/final','url':'https://doi.org/10.1234/final'},'2026-11-09')
            pre={'DOI':'10.1234/pre','type':'posted-content','relation':{'is-preprint-of':[{'id':'10.1234/final','id-type':'doi'}]}}
            stats=track(db,'2026-11-09',{'max_records_per_run':2},fetch=lambda i:pre if i.endswith('/pre') else formal())
            self.assertGreater(stats['identity_conflicts'],0)
            self.assertEqual(db.execute('SELECT count(*) FROM papers').fetchone()[0],2)
            self.assertEqual(db.execute('SELECT paper_id FROM aliases WHERE alias=?',('doi:10.1234/final',)).fetchone()[0],other)
            db.close()

    def test_confirmed_alias_connects_a_later_formal_record_without_changing_title(self):
        with tempfile.TemporaryDirectory() as d:
            db=connect(Path(d)/'db')
            pid,_=ingest(db,{'title':'Original clinical study','arxiv_id':'2610.12345','doi':'10.1234/final',
                    'authors':['Zikang Xu'],'url':'https://arxiv.org/abs/2610.12345'},'2026-11-09')
            track(db,'2026-11-09',{'max_records_per_run':1},fetch=lambda i:formal(title='Original clinical study'))
            new,_=ingest(db,{'title':'Publisher title variation','doi':'10.1234/final','url':'https://doi.org/10.1234/final'},'2026-11-09')
            self.assertEqual(new,pid)
            self.assertEqual(json.loads(db.execute('SELECT payload FROM papers').fetchone()[0])['title'],'Original clinical study')
            db.close()


class VenueGateIntegration(unittest.TestCase):
    def test_human_approval_does_not_bypass_unverified_venue(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'data').mkdir();(root/'data/catalog.json').write_text('[]')
            db=connect(root/'db');pid,_=ingest(db,{'title':'Unknown clinical fairness','url':'https://doi.org/10.1234/unknown','doi':'10.1234/unknown'},'2026-11-09')
            file=root/'approval.md';file.write_text('## '+pid+'\n\n审核决定：纳入\n审核备注：批准。\n证据版本：manual\n')
            with patch('scripts.venue_policy.assess_venue',return_value={'status':'pending','reason_zh':'分区待核实','evidence':[]}),patch('scripts.publish_catalog.annotate') as model:
                self.assertEqual(sync_catalog(db,root,file),{'added':0,'failures':1});model.assert_not_called()
            db.close()

    def test_existing_139_are_preserved_but_unverified_new_formal_record_is_blocked(self):
        records=json.loads((recall.ROOT/'data/catalog.json').read_text())
        validate_catalog_venues(records)
        with self.assertRaisesRegex(ValueError,'venue not eligible'):
            validate_catalog_venues([{'title':'New unknown clinical fairness result','doi':'10.1234/unknown','venue':'Unknown Journal'}])

    def test_quota_failure_stops_new_model_calls_without_losing_candidates(self):
        with tempfile.TemporaryDirectory() as d:
            db=connect(Path(d)/'db')
            for n in range(2):
                ingest(db,{'title':'Clinical fairness '+str(n),'doi':'10.1234/test'+str(n),
                           'abstract':'A medical model evaluates subgroup disparities.','url':'https://doi.org/10.1234/test'+str(n)},'2026-11-09')
            error=urllib.error.HTTPError('http://127.0.0.1/model',429,'quota',{},io.BytesIO(b'{"error":"usage limit reached"}'))
            with patch.dict('os.environ',{'LITERATURE_LLM_ENDPOINT':'http://127.0.0.1/model','LITERATURE_LLM_MODEL':'test'}),patch('scripts.literature_pipeline.cli.review',side_effect=error) as model:
                status=review_pending(db,'2026-11-09',100,False)
            self.assertEqual(status['provider_status'],'unavailable');self.assertEqual(model.call_count,1)
            self.assertEqual(db.execute('SELECT count(*) FROM papers').fetchone()[0],2)
            self.assertEqual(db.execute('SELECT count(*) FROM analyses').fetchone()[0],0);db.close()


class SourceVenueMetadata(unittest.TestCase):
    def test_journal_metadata_comes_from_article_not_reference(self):
        xml=b'<PubmedArticleSet><PubmedArticle><MedlineCitation><PMID>123</PMID><Article><Journal><ISSN>1361-8415</ISSN><Title>Medical Image Analysis</Title></Journal><ArticleTitle>Fair clinical models</ArticleTitle></Article></MedlineCitation><PubmedData><ArticleIdList><ArticleId IdType="doi">10.1234/own</ArticleId></ArticleIdList><ReferenceList><Reference><Title>Other journal</Title></Reference></ReferenceList></PubmedData></PubmedArticle></PubmedArticleSet>'
        p=_parse_pubmed(xml)[0];self.assertEqual(p['journal_title'],'Medical Image Analysis');self.assertEqual(p['journal_issns'],['1361-8415'])

    def test_preprint_platform_is_not_misclassified_as_a_journal(self):
        xml=b'<response><hitCount>1</hitCount><resultList><result><id>PPR1</id><source>PPR</source><title>Fair clinical models</title><doi>10.1234/pre</doi><journalInfo><journal><title>medRxiv</title></journal></journalInfo></result></resultList></response>'
        p=_parse_europepmc(xml)[0][0];self.assertEqual(p['publication_kind'],'preprint')
