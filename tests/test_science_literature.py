import pytest
from sciforge.science import register, get_registry
from sciforge.science.connector import Connector
from sciforge.science.sources import literature


def test_literature_registers_7():
    before = len(get_registry().all())
    literature.register()
    after = len(get_registry().all())
    assert after - before == 7


def test_openalex_search_offline(monkeypatch):
    monkeypatch.setenv("CLAWSGO_SELF_OFFLINE", "1")
    literature.register()
    c = get_registry().get("openalex")
    assert c is not None
    hits = c.search("cancer", 5)
    assert hits == []


def test_openalex_search_parses(monkeypatch):
    fake = {"results": [
        {"title": "Deep Learning for Cells", "publication_year": 2023,
         "doi": "10.1234/x", "id": "https://openalex.org/W1",
         "primary_location": {"display_name": "Nature"},
         "authorships": [{"author": {"display_name": "Smith"}}],
         "cited_by_count": 42, "abstract_inverted_index": None}
    ]}
    monkeypatch.setattr("sciforge.science.sources.literature.http_get_json",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("openalex")
    hits = c.search("cells", 5)
    assert len(hits) == 1
    h = hits[0]
    assert h["title"] == "Deep Learning for Cells"
    assert h["year"] == 2023
    assert h["doi"] == "10.1234/x"
    assert h["cited_by"] == 42
    assert h["venue"] == "Nature"
    assert "Smith" in h["authors"]


def test_arxiv_search_parses(monkeypatch):
    fake = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <title>Quantum ML</title>
    <id>http://arxiv.org/abs/2301.00001</id>
    <link rel="alternate" href="http://arxiv.org/abs/2301.00001"/>
  </entry>
</feed>"""
    monkeypatch.setattr("sciforge.science.sources.literature.http_get_text",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("arxiv")
    hits = c.search("quantum", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Quantum ML"


def test_biorxiv_search_parses(monkeypatch):
    fake = {"collection": [
        {"title": "COVID Study", "doi": "10.1101/2023.01.01",
         "abstract": "virus research", "category": "microbiology"}
    ]}
    monkeypatch.setattr("sciforge.science.sources.literature.http_get_json",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("biorxiv")
    hits = c.search("covid", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "COVID Study"


def test_crossref_search_parses(monkeypatch):
    fake = {"message": {"items": [
        {"title": ["Protein Folding"], "DOI": "10.1000/abc",
         "published": {"date-parts": [[2022]]},
         "container-title": ["Science"],
         "author": [{"given": "Jane", "family": "Doe"}]}
    ]}}
    monkeypatch.setattr("sciforge.science.sources.literature.http_get_json",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("crossref")
    hits = c.search("protein", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Protein Folding"
    assert hits[0]["year"] == 2022
    assert "Jane Doe" in hits[0]["authors"]


def test_europepmc_search_parses(monkeypatch):
    fake = {"resultList": {"result": [
        {"title": "Gene Therapy", "id": "12345", "doi": "10.123/xyz",
         "pubYear": "2021", "journalInfo": {"journal": {"title": "Cell"}},
         "authorString": "Lee K", "citedByCount": 10}
    ]}}
    monkeypatch.setattr("sciforge.science.sources.literature.http_get_json",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("europepmc")
    hits = c.search("gene", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Gene Therapy"
    assert hits[0]["cited_by"] == 10


def test_pubmed_search_parses(monkeypatch):
    search_fake = {"esearchresult": {"idlist": ["999888"]}}
    summ_fake = {"result": {"999888": {"title": "Brain Mapping",
                                       "pubdate": "2020 Jan",
                                       "fulljournalname": "Nature Neuro",
                                       "authors": [{"name": "Wu S"}]}}}
    call_count = [0]
    def fake_json(url, **kw):
        call_count[0] += 1
        if "esearch" in url:
            return search_fake
        return summ_fake
    monkeypatch.setattr("sciforge.science.sources.literature.http_get_json",
                        fake_json)
    literature.register()
    c = get_registry().get("pubmed")
    hits = c.search("brain", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Brain Mapping"
    assert hits[0]["venue"] == "Nature Neuro"


def test_semantic_scholar_search_parses(monkeypatch):
    fake = {"data": [
        {"title": "Attention Nets", "year": 2019, "url": "http://s2/1",
         "venue": "NeurIPS", "citationCount": 500,
         "externalIds": {"DOI": "10.1234/attn"}}
    ]}
    monkeypatch.setattr("sciforge.science.sources.literature.http_get_json",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("semantic-scholar")
    hits = c.search("attention", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Attention Nets"
    assert hits[0]["cited_by"] == 500
