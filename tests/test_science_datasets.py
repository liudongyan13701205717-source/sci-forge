import pytest
from sciforge.science import get_registry
from sciforge.science.sources import datasets


def test_datasets_registers_4():
    before = len(get_registry().all())
    datasets.register()
    after = len(get_registry().all())
    assert after - before == 4


def test_zenodo_search_parses(monkeypatch):
    fake = {"hits": {"hits": [
        {"id": 12345, "metadata": {"title": "My Dataset", "description": "desc",
                                    "creators": [{"name": "Lee"}]}}
    ]}}
    monkeypatch.setattr("sciforge.science.sources.datasets.http_get_json",
                        lambda url, **kw: fake)
    datasets.register()
    c = get_registry().get("zenodo")
    hits = c.search("climate", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "My Dataset"
    assert hits[0]["url"] == "https://zenodo.org/record/12345"


def test_doaj_search_parses(monkeypatch):
    fake = {"results": [
        {"bibjson": {"title": "Open Paper", "year": "2022",
                     "journal": {"title": "PLOS ONE"},
                     "author": [{"name": "Kim"}], "abstract": "open science"}}
    ]}
    monkeypatch.setattr("sciforge.science.sources.datasets.http_get_json",
                        lambda url, **kw: fake)
    datasets.register()
    c = get_registry().get("doaj")
    hits = c.search("open", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Open Paper"
    assert "Kim" in hits[0]["authors"]


def test_openaire_search_parses(monkeypatch):
    fake = {"response": {"results": {"result": [
        {"metadata": {"oaf:entity": {"oaf:result":
            {"title": {"$": "EU Project"}}}}}]}}}
    monkeypatch.setattr("sciforge.science.sources.datasets.http_get_json",
                        lambda url, **kw: fake)
    datasets.register()
    c = get_registry().get("openaire")
    hits = c.search("energy", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "EU Project"


def test_huggingface_search_parses(monkeypatch):
    fake = [
        {"id": "squad", "title": "SQuAD", "description": "QA dataset",
         "author": "stanford", "downloads": 100000, "likes": 500}
    ]
    monkeypatch.setattr("sciforge.science.sources.datasets.http_get_json",
                        lambda url, **kw: fake)
    datasets.register()
    c = get_registry().get("huggingface")
    hits = c.search("qa", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "SQuAD"
    assert hits[0]["url"] == "https://huggingface.co/datasets/squad"
