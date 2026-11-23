"""Read dated main-conference lists from their organizers or publishers."""
from __future__ import annotations

from datetime import date, timedelta
from html import unescape
import re
from urllib.parse import urljoin, urlsplit

from scripts.literature_pipeline.sources import _request

HOSTS = {'miccai': 'papers.miccai.org', 'acl_anthology': 'aclanthology.org', 'neurips': 'neurips.cc'}


def plain(value):
    return ' '.join(unescape(re.sub(r'<[^>]+>', '', value)).split())


def _list_entries(document, provider, year):
    if provider == 'miccai':
        for match in re.finditer(
            rf'<span class="posts-list-item-name[^"]*">\s*&bullet;\s*<b>(.*?)</b>'
            rf'(.*?)href="(/miccai-{year}/\d+-Paper\d+\.html)"',
            document, re.S,
        ):
            title, links, url = match.groups()
            pdf = re.search(r'href="(https://papers\.miccai\.org/[^"]+_paper\.pdf)"', links)
            authors = [plain(name) for name in re.findall(r'<a href="[^"]*/tags#[^"]+">(.*?)</a>', links)]
            yield dict(title=plain(title), path=url, full_text_pdf=pdf[1] if pdf else '', authors=authors)
    elif provider == 'acl_anthology':
        # The volume includes the abstracts and links of its regular proceedings entries.
        article = re.compile(r'<strong><a class=align-middle href=(/\d{4}\.[\w-]+\.\d+/)>(.*?)</a></strong>', re.S)
        matches = list(article.finditer(document))
        for index, match in enumerate(matches):
            path, title = match.groups()
            if not path.startswith('/'+year+'.') or path.endswith('.0/'):
                continue
            end = matches[index+1].start() if index+1 < len(matches) else len(document)
            tail = document[match.end():end]
            abstract = re.search(r'<div class="card-body p-3 small">(.*?)</div>', tail, re.S)
            authors = re.findall(r'<a href=/people/[^>]+>(.*?)</a>', tail.split('abstract-collapse')[0], re.S)
            yield dict(title=plain(title), path=path, full_text_pdf=f'https://aclanthology.org{path[:-1]}.pdf',
                       authors=[plain(name) for name in authors],
                       abstract=plain(abstract[1]) if abstract else '')
    else:
        for path, title in re.findall(
            rf'<a href="(/virtual/{year}/(?:poster|oral|spotlight)/\d+)"[^>]*>(.*?)</a>',
            document, re.S,
        ):
            yield dict(title=plain(title), path=path)


def _details(document, provider):
    if provider == 'miccai':
        abstract = re.search(r'<h1 id="abstract-id">Abstract</h1>\s*<p>(.*?)</p>', document, re.S)
        doi_block = re.search(r'<p[^>]*>[^<]*SpringerLink \(DOI\):(.*?)</p>', document, re.S)
        doi = re.search(r'href="https://doi\.org/(10\.\d{4,9}/[^"\s]+)"', doi_block[1]) if doi_block else None
        abstract_text = plain(abstract[1]) if abstract else ''
        if not abstract_text:
            description = re.search(r'<meta name="description" content="Abstract ([^"]+)"', document)
            abstract_text = plain(description[1]) if description else ''
        return {'abstract': abstract_text, 'doi': unescape(doi[1]) if doi else ''}
    abstract = re.search(r'<div class="abstract-text-inner">\s*(.*?)</div>', document, re.S)
    return {'abstract': plain(abstract[1]) if abstract else ''}


def fetch_official_list(since, until, spec, matches, *, request=_request):
    """Return records, completeness and scanned count for one tracked edition."""
    start, end = (date.fromisoformat(day) for day in (since, until))
    event = date.fromisoformat(spec['event_date'])
    window = timedelta(days=spec.get('event_window_days', 60))
    if not start-window <= event <= end+window:
        return [], True, 0
    provider = spec['provider']
    url = spec['url']
    target = urlsplit(url)
    if target.scheme != 'https' or target.netloc != HOSTS.get(provider):
        raise ValueError('Conference list must use its configured primary source host')
    year = str(event.year)
    document = request(url, 'conference', spec.get('timeout', 25)).decode('utf-8')
    entries = {item["path"]: item for item in _list_entries(document, provider, year)}
    if not entries:
        raise ValueError('Official conference list layout changed or has no public entries')
    records = []
    complete = True
    detail_budget = spec.get('detail_limit', 45)
    for entry in entries.values():
        if not entry['title'] or not matches(entry):
            continue
        paper_url = urljoin(url, entry['path'])
        if not entry.get('abstract') and provider != 'acl_anthology':
            if detail_budget <= 0:
                complete = False
                continue
            detail_budget -= 1
            try:
                detail = request(paper_url, 'conference', spec.get('timeout', 25)).decode('utf-8')
                entry.update(_details(detail, provider))
                if not entry['abstract']:
                    complete = False
            except (OSError, RuntimeError, ValueError):
                complete = False
        record = {key: value for key, value in entry.items() if key != 'path'}
        record.update(url=paper_url, source='conference', source_id=entry['path'],
                      conference=spec['conference'], conference_status=spec['conference_status'], year=year,
                      publication_kind='conference-acceptance' if spec['conference_status'] == 'accepted'
                      else 'proceedings-article')
        # Year is supplied by the proceedings. The meeting date is only a discovery filter.
        if spec['conference_status'] != 'accepted':
            record['published'] = year
        records.append(record)
    return records, complete, len(entries)
