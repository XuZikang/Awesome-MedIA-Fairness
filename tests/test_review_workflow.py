import json
import tempfile
import unittest
from pathlib import Path
from scripts.literature_pipeline.cli import connect,import_state
from scripts.review_workflow import read_decisions,write_review_packet

class ReviewWorkflowTests(unittest.TestCase):
    def test_md_decisions_are_explicit_and_empty_notes_do_not_consume_next_line(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'review.md'
            p.write_text('## p-abc123\n\n审核决定：待审核\n审核备注：\n证据版本：abcdef\n')
            x=read_decisions(p)['p-abc123']
            self.assertEqual(x,{'decision':'pending','note':'','fingerprint':'abcdef'})
            p.write_text(p.read_text().replace('待审核','通过'))
            self.assertEqual(read_decisions(p)['p-abc123']['decision'],'approve')
            p.write_text(p.read_text().replace('通过','自动批准'))
            with self.assertRaises(ValueError):read_decisions(p)

    def test_packet_generation_preserves_same_version_decision_without_touching_catalog(self):
        source=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'data').mkdir();(root/'data/catalog.json').write_text('[]')
            db=connect(root/'db.sqlite3')
            try:
                import_state(db,source/'data/literature-state.json')
                before=(root/'data/catalog.json').read_bytes()
                path=write_review_packet(db,root/'reports','2026-11-04',root/'README.md')
                decisions=read_decisions(path)
                self.assertTrue(decisions)
                self.assertTrue(all(v['decision']=='pending' for v in decisions.values()))
                first=next(iter(decisions))
                original=path.read_text();path.write_text(original.replace('审核决定：待审核','审核决定：排除',1))
                write_review_packet(db,root/'reports','2026-11-04',root/'README.md')
                self.assertEqual(read_decisions(path)[first]['decision'],'reject')
                self.assertEqual((root/'data/catalog.json').read_bytes(),before)
            finally:db.close()
