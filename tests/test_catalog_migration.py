"""Guard against losing original contributions or corrupting bibliographic IDs."""
import json
import re
import unittest
import tempfile
from pathlib import Path
from scripts.build_catalog import identity, apply_primary_links
from scripts.literature_pipeline.cli import connect, seed_catalog

ROOT=Path(__file__).resolve().parents[1]

class MigrationTests(unittest.TestCase):
    def test_primary_link_mapping_requires_reference_and_matching_title(self):
        mapping=json.loads((ROOT/'data/primary-link-resolutions.json').read_text())[0]
        def row(title):
            return {'title':title,'sources':[{'reference':mapping['reference']}],
                    'links':{'Paper':'https://example.org/reference'},
                    'metadata':{'Evidence':['Reviewed source']}}
        valid,wrong=apply_primary_links([row(mapping['title']),row('Different paper')])
        self.assertEqual(valid['doi'],mapping['doi'].lower())
        self.assertEqual(valid['metadata']['Evidence'],['Primary metadata'])
        self.assertNotIn('doi',wrong)

    def test_inventory_kinds_are_explicit(self):
        for row in json.loads((ROOT/'data/catalog.json').read_text()):
            self.assertIn(row.get('kind'),{'main','survey'})

    def test_unknown_mitigation_stage_does_not_claim_in_processing(self):
        for row in json.loads((ROOT/'data/catalog.json').read_text()):
            if row['method']=='Stage pending':
                self.assertEqual(row['metadata']['Stage'],['Not verified'])
            elif row['method'] in {'Pre-processing','In-processing','Post-processing'}:
                self.assertIn(row['method'],row['metadata']['Stage'])

    def test_all_original_occurrences_have_preserved_provenance(self):
        rows=json.loads((ROOT/'data/catalog.json').read_text())
        original=[s for p in rows for s in p['sources'] if s['url']=='docs/legacy-catalog.md']
        self.assertEqual(len(original),35)
        for row in rows:
            self.assertTrue(row['sources'])
            self.assertTrue(row['links'].get('Paper','').startswith('https://'))

    def test_doi_parentheses_are_preserved(self):
        p=identity({'title':'Fixture','links':{'Paper':'https://doi.org/10.1016/S2589-7500(22)00065-1'}})
        self.assertEqual(p['doi'],'10.1016/s2589-7500(22)00065-1')

    def test_original_code_and_data_links_are_preserved(self):
        archive=(ROOT/'docs/legacy-catalog.md').read_text()
        expected={url for role,url in re.findall(r'\[(code|dataset)\]\(([^)]+)\)',archive)}
        actual={url for row in json.loads((ROOT/'data/catalog.json').read_text()) for role,url in row['links'].items() if role in {'Code','Data'}}
        self.assertTrue(expected <= actual)

    def test_dataset_doi_is_not_mistaken_for_the_primary_paper(self):
        p=identity({'title':'Fixture','links':{'Paper':'https://arxiv.org/abs/2306.09264','Data':'https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/A4XMO1'}})
        self.assertEqual(p['arxiv_id'],'2306.09264')
        self.assertNotIn('doi',p)

    def test_seed_parser_keeps_parenthesized_primary_doi(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            catalog=root/'README.md'
            catalog.write_text("## 📝 Fairness Papers\n\n### 2022\n\n- (*Paper'22*) **Fixture**\n  [[📝 Paper](https://doi.org/10.1016/S2589-7500(22)00065-1)]\n\n## 🧭 By Topic\n")
            db=connect(root/'state.sqlite3')
            try:
                seed_catalog(db,catalog,'2026-11-04')
                paper=json.loads(db.execute('SELECT payload FROM papers').fetchone()[0])
                self.assertEqual(paper['doi'].lower(),'10.1016/s2589-7500(22)00065-1')
                self.assertEqual(paper['url'],'https://doi.org/10.1016/S2589-7500(22)00065-1')
            finally:db.close()

if __name__=='__main__':unittest.main()
