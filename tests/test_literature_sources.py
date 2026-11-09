from __future__ import annotations

import json
import urllib.error
import urllib.parse
import unittest
from unittest.mock import patch

from scripts.literature_pipeline import sources


class FakeResponse:
    def __init__(self, payload: bytes):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return self.payload


ARXIV_ENTRY = """
<entry xmlns="http://www.w3.org/2005/Atom">
  <id>http://arxiv.org/abs/2601.12345v2</id>
  <title>Medical dynamics</title>
  <summary>A state transition model.</summary>
  <published>2026-01-03T01:02:03Z</published>
  <updated>2026-01-04T01:02:03Z</updated>
  <author><name>Ada Lovelace</name></author>
  <doi>https://doi.org/10.1234/ABC</doi>
</entry>
"""


def arxiv_feed(total: int, entries: str) -> bytes:
    return (
        '<feed xmlns="http://www.w3.org/2005/Atom" '
        'xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">'
        f"<opensearch:totalResults>{total}</opensearch:totalResults>{entries}</feed>"
    ).encode()


class LiteratureSourceTests(unittest.TestCase):
    def test_pubmed_does_not_use_identifiers_from_cited_references(self):
        payload=b'''<PubmedArticleSet><PubmedArticle>
        <MedlineCitation><PMID>123</PMID><Article><ArticleTitle>Fairness audit</ArticleTitle></Article></MedlineCitation>
        <PubmedData><ArticleIdList><ArticleId IdType="doi">10.1000/own</ArticleId></ArticleIdList>
        <ReferenceList><Reference><ArticleIdList><ArticleId IdType="doi">10.1000/cited</ArticleId>
        <ArticleId IdType="pmc">PMC999</ArticleId></ArticleIdList></Reference></ReferenceList></PubmedData>
        </PubmedArticle></PubmedArticleSet>'''
        paper=sources._parse_pubmed(payload)[0]
        self.assertEqual(paper['doi'],'10.1000/own')
        self.assertEqual(paper['pmcid'],'')
        no_own_doi=payload.replace(b'<ArticleId IdType="doi">10.1000/own</ArticleId>',b'')
        self.assertEqual(sources._parse_pubmed(no_own_doi)[0]['doi'],'')

    def setUp(self):
        sources._LAST_REQUEST.clear()

    def test_arxiv_parsing_date_query_and_truncation(self):
        with patch.object(sources.urllib.request, "urlopen", return_value=FakeResponse(arxiv_feed(2, ARXIV_ENTRY))) as mock_urlopen, patch.object(sources.time, "sleep") as sleep:
            result = sources.fetch_source("arxiv", "fairness", "2026-01-01", "2026-01-31", max_records=1)

        self.assertFalse(result["complete"])
        self.assertEqual(result["total"], 2)
        self.assertIn("submittedDate:[202601010000 TO 202601312359]", result["query"])
        paper = result["records"][0]
        self.assertEqual(paper["arxiv_id"], "2601.12345")
        self.assertEqual(paper["version"], "2")
        self.assertEqual(paper["published"], "2026-01-03")
        self.assertEqual(paper["authors"], ["Ada Lovelace"])
        self.assertEqual(paper["url"], "https://arxiv.org/abs/2601.12345")
        request = mock_urlopen.call_args.args[0]
        self.assertEqual(request.get_header("User-agent"), sources.USER_AGENT)
        sleep.assert_not_called()

    def test_arxiv_pagination_reaches_reported_total(self):
        first = arxiv_feed(2, ARXIV_ENTRY)
        second_entry = ARXIV_ENTRY.replace("2601.12345v2", "2601.12346v1").replace("Medical dynamics", "Second")
        second = arxiv_feed(2, second_entry)
        with patch.object(sources.urllib.request, "urlopen", side_effect=[FakeResponse(first), FakeResponse(second)]), patch.object(sources, "_PAGE_SIZE", 1), patch.object(sources.time, "sleep"):
            result = sources.fetch_source("arxiv", "fairness", "2026-01-01", "2026-01-31", max_records=3)
        self.assertTrue(result["complete"])
        self.assertEqual([p["arxiv_id"] for p in result["records"]], ["2601.12345", "2601.12346"])

    def test_europepmc_parsing(self):
        payload = b"""
        <responseWrapper>
          <hitCount>1</hitCount>
          <resultList><result>
            <id>123</id><source>MED</source><pmid>123</pmid><pmcid>PMC999</pmcid>
            <title>Cell state dynamics</title><firstPublicationDate>2026-02-02</firstPublicationDate>
            <firstIndexDate>2026-02-03</firstIndexDate><isOpenAccess>Y</isOpenAccess>
            <authorList><author><fullName>Grace Hopper</fullName></author></authorList>
            <pubTypeList><pubType>Journal Article</pubType></pubTypeList>
            <abstractText>Forecasts cell states.</abstractText>
          </result></resultList>
        </responseWrapper>
        """
        with patch.object(sources.urllib.request, "urlopen", return_value=FakeResponse(payload)):
            result = sources.fetch_source("europepmc", "cell dynamics", "2026-02-01", "2026-02-28", max_records=10)
        self.assertTrue(result["complete"])
        self.assertIn("FIRST_PDATE:[2026-02-01 TO 2026-02-28]", result["query"])
        paper = result["records"][0]
        self.assertEqual(paper["pmid"], "123")
        self.assertEqual(paper["pmcid"], "PMC999")
        self.assertEqual(paper["authors"], ["Grace Hopper"])
        self.assertEqual(paper['publication_types'],['Journal Article'])
        self.assertTrue(paper["is_open_access"])
        self.assertEqual(paper["url"], "https://europepmc.org/article/MED/123")

    def test_europepmc_cursor_pagination_and_source_id(self):
        first = b"""
        <responseWrapper><hitCount>2</hitCount><nextCursorMark>cursor-2</nextCursorMark><resultList><result>
          <id>100</id><source>MED</source><title>First</title><firstPublicationDate>2026-02-01</firstPublicationDate>
          <fullTextUrlList><fullTextUrl><availability>Subscription required</availability></fullTextUrl></fullTextUrlList>
        </result></resultList></responseWrapper>
        """
        second = b"""
        <responseWrapper><hitCount>2</hitCount><resultList><result>
          <id>101</id><source>MED</source><title>Second</title><firstPublicationDate>2026-02-02</firstPublicationDate>
        </result></resultList></responseWrapper>
        """
        with patch.object(sources.urllib.request, "urlopen", side_effect=[FakeResponse(first), FakeResponse(second)]) as mock_urlopen:
            result = sources.fetch_source("europepmc", "cell", "2026-02-01", "2026-02-28", max_records=3)
        self.assertTrue(result["complete"])
        self.assertEqual([paper["pmid"] for paper in result["records"]], ["100", "101"])
        self.assertFalse(result["records"][0]["is_open_access"])
        first_query = urllib.parse.parse_qs(urllib.parse.urlsplit(mock_urlopen.call_args_list[0].args[0].full_url).query)
        second_query = urllib.parse.parse_qs(urllib.parse.urlsplit(mock_urlopen.call_args_list[1].args[0].full_url).query)
        self.assertEqual(first_query["cursorMark"], ["*"])
        self.assertEqual(second_query["cursorMark"], ["cursor-2"])

    def test_pubmed_esearch_efetch_and_date_query(self):
        search = json.dumps({"esearchresult": {"count": "1", "idlist": ["42"]}}).encode()
        fetch = b"""
        <PubmedArticleSet><PubmedArticle>
          <MedlineCitation><PMID>42</PMID><Article>
            <ArticleTitle>Patient trajectories</ArticleTitle>
            <AuthorList><Author><LastName>Curie</LastName><ForeName>Marie</ForeName></Author></AuthorList>
            <Journal><JournalIssue><PubDate><Year>2026</Year><Month>03</Month><Day>04</Day></PubDate></JournalIssue></Journal>
            <ArticleDate><Year>2026</Year><Month>03</Month><Day>04</Day></ArticleDate>
            <DateRevised><Year>2026</Year><Month>03</Month><Day>05</Day></DateRevised>
            <Abstract><AbstractText Label="BACKGROUND">A forecast.</AbstractText></Abstract>
            <PublicationTypeList><PublicationType>Journal Article</PublicationType></PublicationTypeList>
          </Article></MedlineCitation>
          <PubmedData><ArticleIdList><ArticleId IdType="doi">10.1234/test</ArticleId><ArticleId IdType="pmc">PMC42</ArticleId></ArticleIdList></PubmedData>
        </PubmedArticle></PubmedArticleSet>
        """
        with patch.object(sources.urllib.request, "urlopen", side_effect=[FakeResponse(search), FakeResponse(fetch)]) as mock_urlopen:
            result = sources.fetch_source("pubmed", "patient trajectory", "2026-03-01", "2026-03-31", email="a@example.org")
        self.assertTrue(result["complete"])
        self.assertIn('"2026/03/01"[Date - Publication]', result["query"])
        paper = result["records"][0]
        self.assertEqual(paper["pmid"], "42")
        self.assertEqual(paper["doi"], "10.1234/test")
        self.assertEqual(paper["published"], "2026-03-04")
        self.assertEqual(paper["updated"], "2026-03-05")
        self.assertEqual(paper["authors"], ["Marie Curie"])
        self.assertEqual(paper['publication_types'],['Journal Article'])
        self.assertFalse(paper["is_open_access"])
        search_request = mock_urlopen.call_args_list[0].args[0]
        self.assertIn("a%40example.org", search_request.full_url)

    def test_source_errors_are_raised(self):
        arxiv_error = b'<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>Error: bad query</title></entry></feed>'
        with patch.object(sources.urllib.request, "urlopen", return_value=FakeResponse(arxiv_error)):
            with self.assertRaises(sources.SourceError):
                sources.fetch_source("arxiv", "bad", "2026-01-01", "2026-01-02")

        europe_error = b"<responseWrapper><errMsg>bad query</errMsg></responseWrapper>"
        with patch.object(sources.urllib.request, "urlopen", return_value=FakeResponse(europe_error)):
            with self.assertRaises(sources.SourceError):
                sources.fetch_source("europepmc", "bad", "2026-01-01", "2026-01-02")

        pubmed_warning = json.dumps({"esearchresult": {"count": "0", "idlist": [], "warninglist": {"phrasesnotfound": ["bad"]}}}).encode()
        with patch.object(sources.urllib.request, "urlopen", return_value=FakeResponse(pubmed_warning)):
            with self.assertRaises(sources.SourceError):
                sources.fetch_source("pubmed", "bad", "2026-01-01", "2026-01-02")

        no_results = json.dumps({"esearchresult": {"count": "0", "idlist": [], "warninglist": {"outputmessages": ["No items found."]}}}).encode()
        with patch.object(sources.urllib.request, "urlopen", return_value=FakeResponse(no_results)):
            result = sources.fetch_source("pubmed", "none", "2026-01-01", "2026-01-02")
        self.assertTrue(result["complete"])
        self.assertEqual(result["records"], [])

    def test_pubmed_partial_date_preserves_year_without_fabricating_day(self):
        import xml.etree.ElementTree as ET
        article = ET.fromstring('<Article><Journal><JournalIssue><PubDate><Year>2026</Year><Month>Nov</Month></PubDate></JournalIssue></Journal></Article>')
        self.assertEqual(sources._pubmed_date(article), "2026")

    def test_retry_transient_http_error(self):
        error = urllib.error.HTTPError("https://example.org", 503, "busy", {}, None)
        with patch.object(sources.urllib.request, "urlopen", side_effect=[error, FakeResponse(arxiv_feed(0, ""))]), patch.object(sources.time, "sleep") as sleep:
            result = sources.fetch_source("arxiv", "fairness", "2026-01-01", "2026-01-02")
        self.assertTrue(result["complete"])
        self.assertEqual(result["records"], [])
        self.assertGreaterEqual(sleep.call_count, 1)


if __name__ == "__main__":
    unittest.main()
