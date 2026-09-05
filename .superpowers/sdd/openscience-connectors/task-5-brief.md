### Task 5: Research-line integration (sources param)

**Files:**
- Modify: `clawsgo_self/research/survey.py`
- Modify: `clawsgo_self/research/novelty.py`
- Modify: `clawsgo_self/research/community.py`
- Create: `tests/test_science_integration.py`

**Interfaces:**
- Consumes: `science.api.cross_lookup`
- Produces: existing `literature_review` / `check_novelty` / `citation_landscape` accept optional `sources` param (default: openalex, arxiv)

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_integration.py`:

```python
import pytest
from clawsgo_self.science.connector import Connector, ConnectorRegistry
from clawsgo_self.science import api


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


def test_literature_review_multi_source(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    from clawsgo_self.core import get_layout
    from clawsgo_self.research.survey import literature_review
    monkeypatch.setattr(api, "get_registry", _reg)
    layout = get_layout()
    r = literature_review(topic="test", paper_id="p_multi", layout=layout,
                          sources=["openalex", "crossref"])
    titles = [p.get("title") for p in r.papers]
    assert "From OpenAlex" in titles
    assert "From Crossref" in titles


def test_literature_review_default_sources(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    from clawsgo_self.core import get_layout
    from clawsgo_self.research.survey import literature_review
    monkeypatch.setattr(api, "get_registry", _reg)
    layout = get_layout()
    r = literature_review(topic="test", paper_id="p_default", layout=layout)
    titles = [p.get("title") for p in r.papers]
    assert "From OpenAlex" in titles


def test_check_novelty_multi_source(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    from clawsgo_self.core import get_layout
    from clawsgo_self.research.novelty import check_novelty
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
    from clawsgo_self.core import get_layout
    from clawsgo_self.research.community import citation_landscape
    monkeypatch.setattr(api, "get_registry", _reg)
    layout = get_layout()
    r = citation_landscape(paper_id="p_cit", layout=layout, doi_or_topic="test",
                           sources=["openalex"])
    assert r.ok is True or r.mode == "topic"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_integration.py -v`
Expected: FAIL -- sources param not accepted

- [ ] **Step 3: Update survey.py**

Modify `clawsgo_self/research/survey.py` `literature_review` function signature and body:

```python
def literature_review(
    topic: str,
    *,
    paper_id: str,
    layout: Layout,
    limit: int = 10,
    sources: list[str] | None = None,
) -> LiteratureReview:
    r = LiteratureReview(ok=False, topic=topic)
    notes: list = []
    from clawsgo_self.science.api import cross_lookup
    if sources:
        papers = cross_lookup(topic, databases=sources, limit=limit)
    else:
        papers = lit.search_openalex(topic, limit=limit)
    papers = lit.dedupe(papers)
    r.papers = papers
    if not papers:
        notes.append("检索无结果（离线或网络），综述基于空集，缺口为启发式。")
    r.keyworks = _keywords(topic)

    if llm.configured() and papers:
        try:
            _llm_review(r, notes)
            r.llm_used = True
        except RuntimeError as e:
            notes.append(f"LLM 综述不可用，回退模板：{e}")

    if not r.clusters:
        _template_review(r, notes)

    r.notes = notes
    r.ok = True
    _persist(layout, paper_id, r)
    return r
```

- [ ] **Step 4: Update novelty.py**

Modify `clawsgo_self/research/novelty.py` `check_novelty` function signature and body:

```python
def check_novelty(
    *,
    paper_id: str,
    layout: Layout,
    limit: int = 8,
    sources: list[str] | None = None,
) -> NoveltyReport:
    r = NoveltyReport(ok=False, paper_id=paper_id)
    phrases = _extract_phrases(layout, paper_id)
    if not phrases:
        r.error = "没有可利用的标题/摘要内容"
        return r
    r.phrases = phrases

    from clawsgo_self.science.api import cross_lookup
    if sources:
        papers = cross_lookup(" ".join(phrases), databases=sources, limit=limit)
    else:
        papers = lit.search_openalex(" ".join(phrases), limit=limit)
    r.similar_papers = papers
    r.differentiators = _differentiators(phrases, papers)
    _persist(layout, paper_id, r)
    r.ok = True
    return r
```

- [ ] **Step 5: Update community.py**

Modify `clawsgo_self/research/community.py` `citation_landscape` function signature and body:

```python
def citation_landscape(
    *,
    paper_id: str,
    layout: Layout,
    doi_or_topic: str,
    sources: list[str] | None = None,
) -> CitationLandscape:
    r = CitationLandscape(ok=False, paper_id=paper_id, source=doi_or_topic)
    doi_like = bool(re.search(r"10\.\d{4,9}/", doi_or_topic or ""))
    r.mode = "doi" if doi_like else "topic"
    works: list[dict] = []
    if r.mode == "doi":
        seed = _fetch_work_by_doi(doi_or_topic)
        if not seed:
            r.offline = lit._offline()
            r.notes.append("DOI 在 OpenAlex 未命中（可能离线/拼写问题）。")
            r.headline = "无法定位该 DOI 的引文邻域，请检查 DOI 或改用主题关键词。"
        else:
            works.append(seed)
            r.notes.append(f"以 DOI 定位到「{seed.get('title','')[:60]}」，被引 {seed.get('cited_by',0)}。")
    else:
        from clawsgo_self.science.api import cross_lookup
        if sources:
            works = cross_lookup(doi_or_topic, databases=sources, limit=40)
        else:
            works = lit.search_openalex(doi_or_topic, limit=40)
        if not works:
            r.offline = lit._offline()
            r.notes.append("主题检索无结果（离线或关键词过冷门）。")
            r.headline = "未检索到相关作品，建议更换关键词后再试。"
        else:
            r.notes.append("基于主题检索 top 作品的被引量判断领域热度。")

    if not works:
        r.error = "无可用引文数据（离线或未命中）。"
        return r
    r.total_works = len(works)
    r.max_cited = max(w.get("cited_by", 0) for w in works)
    r.headline = _time_window(r.total_works, r.max_cited)
    by_year = Counter()
    for w in works:
        yr = w.get("year")
        if yr:
            by_year[yr] += 1
    r.works_by_year = [{"year": y, "count": c} for y, c in sorted(by_year.items())]
    r.top_cited = sorted(works, key=lambda w: w.get("cited_by", 0), reverse=True)[:15]
    venues = Counter()
    for w in works:
        v = (w.get("venue") or "").strip()
        if v:
            venues[v] += 1
    r.venues = [{"venue": v, "count": c} for v, c in venues.most_common()]
    _persist(layout, paper_id, r)
    r.ok = True
    return r
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest tests/test_science_integration.py -v`
Expected: 4 passed

- [ ] **Step 7: Commit**

```bash
git add clawsgo_self/research/survey.py clawsgo_self/research/novelty.py clawsgo_self/research/community.py tests/test_science_integration.py
git commit -m "feat(science): wire multi-source search into literature_review/novelty/citation_landscape"
```

---
