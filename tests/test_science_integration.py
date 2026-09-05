import pytest
from sciforge.science.connector import Connector, ConnectorRegistry
from sciforge.science import api


def _reg() -> ConnectorRegistry:
    reg = ConnectorRegistry()
    reg.register(Connector(id="openalex", name="OpenAlex", domain="literature",
                            description="OpenAlex works", search=lambda q, n: [
                                {"title": "From OpenAlex", "year": 2024, "doi": "10/oa",
                                 "url": "http://oa", "venue": "OA Journal", "authors": [],
                                 "cited_by": 5, "abstract": "oa"}]))
    reg.register(Connector(id="crossref", name="Crossref", domain="literature",
                            description="Crossref", search=lambda q, n: [
                                {"title": "From Crossref", "year": 2023, "doi": "10/cr",
                                 "url": "http://cr", "venue": "CR Journal", "authors": [],
                                 "cited_by": 3, "abstract": "cr"}]))
    return reg


def _patch_offline(monkeypatch):
    monkeypatch.setattr("sciforge.science.api._offline", lambda: False)
    monkeypatch.setattr("sciforge.research.lit._offline", lambda: False)
    monkeypatch.setattr("sciforge.research.lit.search_openalex",
                        lambda q, limit=10, timeout=20: [
                            {"title": "From OpenAlex", "year": 2024, "doi": "10/oa",
                             "url": "http://oa", "venue": "OA Journal", "authors": [],
                             "cited_by": 5, "abstract": "oa"}])


def test_literature_review_multi_source(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _patch_offline(monkeypatch)
    from sciforge.core import get_layout
    from sciforge.research.survey import literature_review
    monkeypatch.setattr(api, "get_registry", _reg)
    layout = get_layout()
    r = literature_review(topic="test", paper_id="p_multi", layout=layout,
                          sources=["openalex", "crossref"])
    titles = [p.get("title") for p in r.papers]
    assert "From OpenAlex" in titles
    assert "From Crossref" in titles


def test_literature_review_default_sources(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _patch_offline(monkeypatch)
    from sciforge.core import get_layout
    from sciforge.research.survey import literature_review
    monkeypatch.setattr(api, "get_registry", _reg)
    layout = get_layout()
    r = literature_review(topic="test", paper_id="p_default", layout=layout)
    titles = [p.get("title") for p in r.papers]
    assert "From OpenAlex" in titles


def test_check_novelty_multi_source(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _patch_offline(monkeypatch)
    from sciforge.core import get_layout
    from sciforge.research.novelty import check_novelty
    monkeypatch.setattr(api, "get_registry", _reg)
    layout = get_layout()
    project = layout.project_dir("p_nov")
    (project / "research").mkdir(parents=True, exist_ok=True)
    (project / "research" / "metadata.json").write_text(
        '{"title": "Test", "abstract": "test abstract"}', encoding="utf-8")
    r = check_novelty(paper_id="p_nov", layout=layout, sources=["openalex", "crossref"])
    assert r.ok is True
    all_titles = [s.get("title", "") for s in r.similar_papers]
    assert any("OpenAlex" in t for t in all_titles)


def test_citation_landscape_multi_source(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _patch_offline(monkeypatch)
    from sciforge.core import get_layout
    from sciforge.research.community import citation_landscape
    monkeypatch.setattr(api, "get_registry", _reg)
    layout = get_layout()
    r = citation_landscape(paper_id="p_cit", layout=layout, doi_or_topic="test",
                           sources=["openalex", "crossref"])
    assert r.ok is True
    titles = [p.get("title") for p in r.top_cited]
    assert "From OpenAlex" in titles
    assert "From Crossref" in titles
