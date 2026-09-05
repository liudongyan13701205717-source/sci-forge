# OpenScience 科学数据连接器移植实现计划

# OpenScience 科学数据连接器移植实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** 将 synthetic-sciences/openscience 的科学数据库连接器层移植到 clawsgo-self，新增 41 个免 key 科学数据连接器 + 4 个 MCP 工具 + 研究线多源融合。

**Architecture:** 新建 clawsgo_self/science/ 包，复刻上游 Connector 框架（Connector 协议 + Registry + 共享 HTTP 层）。每个域（literature/proteins/chemistry/genomics/pathways/omics/datasets）一个源模块，统一返回归一化 ConnectorHit。API 层提供 science_list_dbs / science_search / science_fetch / science_cross_lookup 四个工具，注册到 server.py（20→24 工具）。science_cross_lookup 输出与 lit.search_openalex() 同构，供现有 literature_review / check_novelty / citation_landscape 通过可选 sources 参数接入多源。

**Tech Stack:** Python ≥3.10, stdlib (urllib, json, threading, time), pytest, MCP FastMCP（已有）。不新增依赖——HTTP 层复用 lit.py 的 urllib 模式 + 离线开关 + 重试/限速。

**Spec:** 本计划基于的设计已获用户批准（2026-09-05 对话）：① 移植 OpenScience 全部连接器 ② 加数据集/开放获取库（zenodo/doaj/openaire/huggingface）③ 检索工具增强（fetch 原文 + 多库联合）④ 接入现有研究线。

## Global Constraints

- 离线优先：所有连接器受 CLAWSGO_SELF_OFFLINE=1 控制，离线时优雅返回空结果（不抛错），与 lit.py 风格一致
- 不新增依赖：仅 stdlib + 已有 mcp
- 测试必须离线运行：连接器测试走 HTTP seam mock（不碰公网），框架/逻辑测试走确定性数据
- 现有 61 项测试必须全绿：CLAWSGO_SELF_OFFLINE=1 pytest tests/ -q
- 统一输出：ConnectorHit(id, title, summary, url, score, extra)；science_cross_lookup 输出与 lit.search_openalex() 同构（title/year/doi/url/venue/authors/cited_by/abstract）
- 代码风格：无多余注释，dataclass + 纯函数，与现有 research/*.py 一致
- 每批 TDD：先写失败测试 → 实现 → 绿 → commit
- git push 不可达 → 本地 commit，后续走 GitHub API 推送
- 文档同步：README / USAGE 随功能落地同步更新

---
### Task 1: Connector 框架（connector.py + http.py + registry）

**Files:**
- Create: `clawsgo_self/science/__init__.py`
- Create: `clawsgo_self/science/connector.py`
- Create: `clawsgo_self/science/http.py`
- Create: `tests/test_science_framework.py`

**Interfaces:**
- Produces: `science.connector.Connector`, `science.connector.ConnectorHit`, `science.connector.DOMAINS`, `science.connector.ConnectorRegistry`, `science.http.http_get_json`, `science.http.http_get_text`, `science.http._offline`

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_framework.py`:

```python
import pytest
from clawsgo_self.science.connector import (
    Connector, ConnectorHit, ConnectorRegistry, DOMAINS,
)


def test_domains_constant():
    assert "literature" in DOMAINS
    assert "proteins" in DOMAINS
    assert "chemistry" in DOMAINS
    assert "genomics" in DOMAINS


def test_connector_hit_to_dict():
    h = ConnectorHit(id="x", title="T", summary="S", url="http://x", score=1.0)
    d = h.to_dict()
    assert d["id"] == "x" and d["title"] == "T" and d["score"] == 1.0


def test_registry_register_and_get():
    reg = ConnectorRegistry()
    c = Connector(id="demo", name="Demo", domain="literature", description="d", search=None)
    reg.register(c)
    assert reg.has("demo")
    assert reg.get("demo").name == "Demo"
    assert reg.all()[0].id == "demo"


def test_registry_by_domain():
    reg = ConnectorRegistry()
    reg.register(Connector(id="a", name="A", domain="chemistry", description="", search=None))
    reg.register(Connector(id="b", name="B", domain="literature", description="", search=None))
    chem = reg.by_domain("chemistry")
    assert len(chem) == 1 and chem[0].id == "a"


def test_registry_catalog_shape():
    reg = ConnectorRegistry()
    reg.register(Connector(id="x", name="X", domain="genomics", description="desc", search=None))
    cat = reg.catalog()
    assert cat[0]["id"] == "x" and "domain" in cat[0] and "requires_key" in cat[0]


def test_registry_get_missing_returns_none():
    assert ConnectorRegistry().get("nope") is None


def test_registry_has_missing():
    assert ConnectorRegistry().has("nope") is False


def test_registry_duplicate_id_last_wins():
    reg = ConnectorRegistry()
    reg.register(Connector(id="d", name="V1", domain="literature", description="", search=None))
    reg.register(Connector(id="d", name="V2", domain="literature", description="", search=None))
    assert reg.get("d").name == "V2"
    assert len(reg.all()) == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_framework.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write connector.py**

Create `clawsgo_self/science/connector.py`:

```python
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional

DOMAINS = ["literature", "proteins", "chemistry", "genomics", "pathways", "omics", "datasets"]


@dataclass
class ConnectorHit:
    id: str
    title: str
    summary: str = ""
    url: str = ""
    score: float = 1.0
    extra: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {"id": self.id, "title": self.title, "summary": self.summary,
                "url": self.url, "score": self.score, "extra": self.extra}


@dataclass
class Connector:
    id: str
    name: str
    domain: str
    description: str
    search: Callable
    fetch: Optional[Callable] = None
    requires_key: bool = False


class ConnectorRegistry:
    def __init__(self):
        self._connectors: dict[str, Connector] = {}

    def register(self, c: Connector) -> None:
        self._connectors[c.id] = c

    def get(self, cid: str) -> Optional[Connector]:
        return self._connectors.get(cid)

    def has(self, cid: str) -> bool:
        return cid in self._connectors

    def all(self) -> list[Connector]:
        return list(self._connectors.values())

    def by_domain(self, domain: str) -> list[Connector]:
        return [c for c in self._connectors.values() if c.domain == domain]

    def catalog(self) -> list[dict]:
        return [{"id": c.id, "name": c.name, "domain": c.domain,
                 "description": c.description, "requires_key": c.requires_key}
                for c in self._connectors.values()]
```

- [ ] **Step 4: Write http.py**

Create `clawsgo_self/science/http.py`:

```python
from __future__ import annotations

import json
import os
import time
import threading
import urllib.error
import urllib.parse
import urllib.request
from typing import Optional

_USER_AGENT = "clawsgo-science/0.1 (+connector-layer; no-key-public-api)"
_OFFLINE = "CLAWSGO_SELF_OFFLINE"

_rate_limits: dict[str, tuple[threading.Lock, float]] = {}
_rate_holder = threading.Lock()


def _offline() -> bool:
    return os.environ.get(_OFFLINE) == "1"


def _rate_limit(host: str, interval: float) -> None:
    with _rate_holder:
        if host not in _rate_limits:
            _rate_limits[host] = (threading.Lock(), 0.0)
    lock, _ = _rate_limits[host]
    with lock:
        _, last = _rate_limits[host]
        now = time.monotonic()
        wait = last + interval - now
        if wait > 0:
            time.sleep(wait)
        _rate_limits[host] = (lock, time.monotonic())


def http_get_json(url, *, timeout=25, headers=None, rate_interval=1.0, retries=2):
    """GET JSON with offline guard, retry/backoff on 429/5xx, per-host rate limit."""
    if _offline():
        return None
    host = urllib.parse.urlparse(url).netloc
    _rate_limit(host, rate_interval)
    hdrs = {"User-Agent": _USER_AGENT}
    if headers:
        hdrs.update(headers)
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(2 ** attempt)
                continue
            return None
        except (urllib.error.URLError, OSError, ValueError):
            return None
    return None


def http_get_text(url, *, timeout=25, headers=None, rate_interval=1.0):
    """GET text (pdb/fasta/sdf/raw). Offline-guarded, rate-limited."""
    if _offline():
        return None
    host = urllib.parse.urlparse(url).netloc
    _rate_limit(host, rate_interval)
    hdrs = {"User-Agent": _USER_AGENT}
    if headers:
        hdrs.update(headers)
    try:
        req = urllib.request.Request(url, headers=hdrs)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", "ignore")
    except (urllib.error.URLError, urllib.error.HTTPError, OSError):
        return None
```

- [ ] **Step 5: Write __init__.py**

Create `clawsgo_self/science/__init__.py`:

```python
from clawsgo_self.science.connector import Connector, ConnectorHit, ConnectorRegistry, DOMAINS

_REGISTRY = ConnectorRegistry()


def get_registry() -> ConnectorRegistry:
    return _REGISTRY


def register(c: Connector) -> None:
    _REGISTRY.register(c)


__all__ = ["Connector", "ConnectorHit", "ConnectorRegistry", "DOMAINS",
           "get_registry", "register"]
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest tests/test_science_framework.py -v`
Expected: 8 passed

- [ ] **Step 7: Commit**

```bash
git add clawsgo_self/science/connector.py clawsgo_self/science/http.py clawsgo_self/science/__init__.py tests/test_science_framework.py
git commit -m "feat(science): add connector framework (Connector/Registry/HTTP layer)"
```

---
### Task 2: API 层（4 个 MCP 工具 + server.py 注册）

**Files:**
- Create: `clawsgo_self/science/api.py`
- Modify: `clawsgo_self/server.py` (注册 4 工具)
- Create: `tests/test_science_api.py`

**Interfaces:**
- Consumes: `science.connector.*`, `science.http.*`
- Produces: `science.api.science_list_dbs`, `science.api.science_search`, `science.api.science_fetch`, `science.api.science_cross_lookup`, `science.api.cross_lookup` (供研究线复用，输出与 lit.search_openalex() 同构)

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_api.py`:

```python
import pytest
from clawsgo_self.science.connector import Connector, ConnectorRegistry
from clawsgo_self.science import api


def _reg() -> ConnectorRegistry:
    reg = ConnectorRegistry()
    reg.register(Connector(id="openalex", name="OpenAlex", domain="literature",
                            description="OpenAlex works", search=lambda q, n: [
                                {"title": "T", "year": 2024, "doi": "10/x",
                                 "url": "http://x", "venue": "V", "authors": ["A"],
                                 "cited_by": 5, "abstract": "ab"}]))
    reg.register(Connector(id="uniprot", name="UniProt", domain="proteins",
                            description="UniProt KB", search=lambda q, n: [
                                {"id": "P12345", "title": "Protein X",
                                 "summary": "desc", "url": "http://u"}]))
    reg.register(Connector(id="chembl", name="ChEMBL", domain="chemistry",
                            description="ChEMBL", search=lambda q, n: []))
    return reg


def test_science_list_dbs_all(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    r = api.science_list_dbs("")
    assert r["ok"] is True
    assert r["count"] == 3
    assert any(d["id"] == "openalex" for d in r["databases"])


def test_science_list_dbs_by_domain(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    r = api.science_list_dbs("proteins")
    assert r["count"] == 1
    assert r["databases"][0]["id"] == "uniprot"


def test_science_search_hits(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    r = api.science_search("openalex", "test", limit=5)
    assert r["ok"] is True
    assert r["database"] == "openalex"
    assert r["hits"][0]["title"] == "T"


def test_science_search_unknown_db(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    r = api.science_search("nonexistent", "test")
    assert r["ok"] is False
    assert "not found" in r["error"] or "不存在" in r["error"]


def test_science_search_offline(monkeypatch):
    monkeypatch.setenv("CLAWSGO_SELF_OFFLINE", "1")
    reg = _reg()
    reg.register(Connector(id="o", name="O", domain="literature",
                            description="", search=lambda q, n: []))
    monkeypatch.setattr(api, "get_registry", lambda: reg)
    r = api.science_search("o", "test")
    assert r["ok"] is True
    assert r["offline"] is True
    assert r["hits"] == []


def test_science_fetch_not_supported(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    r = api.science_fetch("openalex", "W123")
    assert r["ok"] is False
    assert "not supported" in r["error"] or "不支持" in r["error"]


def test_science_cross_lookup_merges(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    r = api.science_cross_lookup("test", databases=["openalex", "uniprot"], limit=5)
    assert r["ok"] is True
    assert r["total"] >= 2
    titles = [h["title"] for h in r["hits"]]
    assert "T" in titles and "Protein X" in titles


def test_cross_lookup_normal_shape(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    r = api.cross_lookup("test", databases=["openalex"], limit=5)
    assert len(r) == 1
    assert r[0]["title"] == "T"
    assert r[0]["year"] == 2024
    assert r[0]["doi"] == "10/x"
    assert r[0]["cited_by"] == 5
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_api.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write api.py**

Create `clawsgo_self/science/api.py`:

```python
from __future__ import annotations

import os
from clawsgo_self.science import get_registry
from clawsgo_self.science.http import _offline


def science_list_dbs(domain: str = "") -> dict:
    reg = get_registry()
    if not domain:
        dbs = reg.catalog()
    else:
        dbs = [{"id": c.id, "name": c.name, "domain": c.domain,
                "description": c.description, "requires_key": c.requires_key}
               for c in reg.by_domain(domain)]
    return {"ok": True, "count": len(dbs), "databases": dbs, "offline": _offline()}


def _normalize_hit(h) -> dict:
    if hasattr(h, "to_dict"):
        h = h.to_dict()
    return {
        "title": h.get("title", ""),
        "year": h.get("year"),
        "doi": h.get("doi"),
        "url": h.get("url", ""),
        "venue": h.get("venue", ""),
        "authors": h.get("authors", []),
        "cited_by": h.get("cited_by", 0),
        "abstract": h.get("abstract", ""),
    }


def science_search(database: str, query: str, limit: int = 5) -> dict:
    reg = get_registry()
    c = reg.get(database)
    if not c:
        return {"ok": False, "error": f"Database {database} not found", "hits": []}
    offline = _offline()
    hits = c.search(query, limit) if not offline else []
    return {"ok": True, "database": database, "query": query,
            "offline": offline, "count": len(hits),
            "hits": [_normalize_hit(h) for h in hits]}


def science_fetch(database: str, id: str, format: str = "") -> dict:
    reg = get_registry()
    c = reg.get(database)
    if not c:
        return {"ok": False, "error": f"Database {database} not found"}
    if not c.fetch:
        return {"ok": False, "error": f"{database} does not support fetch"}
    data = c.fetch(id, format)
    return {"ok": True, "database": database, "id": id,
            "format": format, "data": data}


def cross_lookup(query: str, databases: list[str], limit: int = 5) -> list[dict]:
    seen: set = set()
    out = []
    for db in databases:
        r = science_search(db, query, limit=limit)
        for h in r.get("hits", []):
            key = (h.get("doi") or h.get("url") or h.get("title", "")).lower().strip()
            if key in seen:
                continue
            seen.add(key)
            out.append(h)
    return out


def science_cross_lookup(query: str, databases: list[str] | None = None,
                         limit: int = 5) -> dict:
    reg = get_registry()
    dbs = databases or [c.id for c in reg.all() if not c.requires_key]
    hits = cross_lookup(query, dbs, limit=limit)
    return {"ok": True, "query": query, "databases": dbs,
            "total": len(hits), "hits": hits}
```

- [ ] **Step 4: Register tools in server.py**

Add to `clawsgo_self/server.py` after the `review_code` tool (before `def run()`):

```python
@mcp.tool()
def science_list_dbs(domain: str = "") -> dict:
    from clawsgo_self.science.api import science_list_dbs as _impl
    return _impl(domain=domain)


@mcp.tool()
def science_search(database: str, query: str, limit: int = 5) -> dict:
    from clawsgo_self.science.api import science_search as _impl
    return _impl(database=database, query=query, limit=limit)


@mcp.tool()
def science_fetch(database: str, id: str, format: str = "") -> dict:
    from clawsgo_self.science.api import science_fetch as _impl
    return _impl(database=database, id=id, format=format)


@mcp.tool()
def science_cross_lookup(query: str, databases: list[str] | None = None,
                        limit: int = 5) -> dict:
    from clawsgo_self.science.api import science_cross_lookup as _impl
    return _impl(query=query, databases=databases, limit=limit)
```

- [ ] **Step 5: Run test to verify it passes**

Run: `pytest tests/test_science_api.py -v`
Expected: 10 passed

- [ ] **Step 6: Commit**

```bash
git add clawsgo_self/science/api.py clawsgo_self/server.py tests/test_science_api.py
git commit -m "feat(science): add 4 MCP tools (list_dbs/search/fetch/cross_lookup)"
```

---
### Task 3: Literature Sources (7 connectors)

**Files:**
- Create: `clawsgo_self/science/sources/__init__.py`
- Create: `clawsgo_self/science/sources/literature.py`
- Create: `tests/test_science_literature.py`

**Interfaces:**
- Produces: `sources.literature.register()` registering openalex, arxiv, biorxiv, crossref, europepmc, pubmed, semantic-scholar

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_literature.py`:

```python
import pytest
from clawsgo_self.science import register, get_registry
from clawsgo_self.science.connector import Connector
from clawsgo_self.science.sources import literature


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
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
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
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_text",
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
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
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
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
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
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
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
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
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
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("semantic-scholar")
    hits = c.search("attention", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Attention Nets"
    assert hits[0]["cited_by"] == 500
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_literature.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write sources/__init__.py**

Create `clawsgo_self/science/sources/__init__.py`:

```python
```

- [ ] **Step 4: Write literature.py**

Create `clawsgo_self/science/sources/literature.py`:

```python
from __future__ import annotations

import urllib.parse
import xml.etree.ElementTree as ET
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _truncate(inv_index) -> str:
    if not inv_index:
        return ""
    pos = {}
    for word, idxs in inv_index.items():
        for i in idxs:
            pos[i] = word
    s = " ".join(pos[i] for i in sorted(pos))
    return s[:600]


def _openalex_search(query, limit):
    params = {"search": query, "per-page": str(limit), "mailto": "research@localhost"}
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for w in data.get("results", []):
        auths = [a.get("author", {}).get("display_name", "")
                 for a in (w.get("authorships") or [])[:12]]
        auths = [x for x in auths if x]
        out.append({
            "title": w.get("title") or "",
            "year": w.get("publication_year"),
            "doi": w.get("doi"),
            "url": w.get("id", ""),
            "venue": (w.get("primary_location") or {}).get("display_name", ""),
            "authors": auths,
            "cited_by": w.get("cited_by_count") or 0,
            "abstract": _truncate(w.get("abstract_inverted_index")),
        })
    return out


def _arxiv_search(query, limit):
    q = urllib.parse.quote(query)
    url = (f"https://export.arxiv.org/api/query?search_query=all:{q}"
           f"&max_results={limit}&sortBy=submittedDate&sortOrder=descending")
    body = sci_http.http_get_text(url)
    if not body:
        return []
    ns = {"a": "http://www.w3.org/2005/Atom"}
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return []
    out = []
    for e in root.findall("a:entry", ns):
        title = (e.findtext("a:title", "", ns) or "").strip().replace("\n", " ")
        link = ""
        for l_ in e.findall("a:link", ns):
            if l_.get("rel") == "alternate":
                link = l_.get("href", "")
                break
        out.append({"title": title, "url": link, "authors": [], "year": None,
                    "doi": None, "venue": "", "cited_by": 0, "abstract": ""})
    return out


def _biorxiv_search(query, limit):
    url = f"https://api.biorxiv.org/details/biorxiv/0/{limit}"
    data = sci_http.http_get_json(url + "?q=" + urllib.parse.quote(query))
    if not data:
        return []
    out = []
    for item in data.get("collection", []):
        doi = item.get("doi", "")
        out.append({
            "title": item.get("title", ""),
            "year": None,
            "doi": doi,
            "url": f"https://biorxiv.org/content/{doi}" if doi else "",
            "venue": item.get("category", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": item.get("abstract", ""),
        })
    return out


def _crossref_search(query, limit):
    params = {"query": query, "rows": str(limit), "mailto": "research@localhost"}
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("message", {}).get("items", []):
        authors = []
        for a in item.get("author", [])[:12]:
            name = " ".join(filter(None, [a.get("given"), a.get("family")]))
            if name:
                authors.append(name)
        year = None
        dp = item.get("published", {}).get("date-parts", [[]])
        if dp and dp[0]:
            year = dp[0][0]
        out.append({
            "title": (item.get("title") or [""])[0],
            "year": year,
            "doi": item.get("DOI"),
            "url": item.get("URL", ""),
            "venue": (item.get("container-title") or [""])[0],
            "authors": authors,
            "cited_by": 0,
            "abstract": item.get("abstract", ""),
        })
    return out


def _europepmc_search(query, limit):
    params = {"query": query, "format": "json", "pageSize": str(limit)}
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("resultList", {}).get("result", []):
        out.append({
            "title": r.get("title", ""),
            "year": r.get("pubYear"),
            "doi": r.get("doi"),
            "url": f"https://europepmc.org/article/MED/{r.get('id','')}" if r.get("id") else "",
            "venue": (r.get("journalInfo", {}).get("journal", {}).get("title", "")),
            "authors": [r.get("authorString", "")] if r.get("authorString") else [],
            "cited_by": r.get("citedByCount") or 0,
            "abstract": r.get("abstractText", ""),
        })
    return out


def _pubmed_search(query, limit):
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = sci_http.http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "pubmed", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = sci_http.http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        doi = ""
        for aid in s.get("articleids", []):
            if aid.get("idtype") == "doi":
                doi = aid.get("value", "")
                break
        out.append({
            "title": s.get("title", ""),
            "year": s.get("pubdate", "").split(" ")[0] if s.get("pubdate") else None,
            "doi": doi,
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{uid}/",
            "venue": s.get("fulljournalname", ""),
            "authors": [a.get("name", "") for a in s.get("authors", [])[:12]],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _semantic_scholar_search(query, limit):
    params = {"query": query, "limit": str(limit),
              "fields": "title,year,url,citationCount,venue,externalIds"}
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for p in data.get("data", []):
        doi = (p.get("externalIds") or {}).get("DOI", "")
        out.append({
            "title": p.get("title", ""),
            "year": p.get("year"),
            "doi": doi,
            "url": p.get("url", ""),
            "venue": p.get("venue", ""),
            "authors": [],
            "cited_by": p.get("citationCount") or 0,
            "abstract": "",
        })
    return out


def register():
    specs = [
        ("openalex", "OpenAlex", "OpenAlex works catalog", _openalex_search),
        ("arxiv", "arXiv", "arXiv preprints", _arxiv_search),
        ("biorxiv", "bioRxiv", "bioRxiv preprints", _biorxiv_search),
        ("crossref", "Crossref", "Crossref metadata", _crossref_search),
        ("europepmc", "Europe PMC", "Europe PMC literature", _europepmc_search),
        ("pubmed", "PubMed", "PubMed biomedical literature", _pubmed_search),
        ("semantic-scholar", "Semantic Scholar", "Semantic Scholar papers", _semantic_scholar_search),
    ]
    for cid, name, desc, fn in specs:
        register(Connector(id=cid, name=name, domain="literature",
                           description=desc, search=fn))
```

- [ ] **Step 5: Run test to verify it passes**

Run: `pytest tests/test_science_literature.py -v`
Expected: 9 passed

- [ ] **Step 6: Commit**

```bash
git add clawsgo_self/science/sources/__init__.py clawsgo_self/science/sources/literature.py tests/test_science_literature.py
git commit -m "feat(science): add 7 literature connectors (openalex/arxiv/biorxiv/crossref/europepmc/pubmed/semantic-scholar)"
```

---
### Task 4: Dataset / Open-Access Sources (4 extra connectors)

**Files:**
- Create: `clawsgo_self/science/sources/datasets.py`
- Create: `tests/test_science_datasets.py`

**Interfaces:**
- Produces: `sources.datasets.register()` registering zenodo, doaj, openaire, huggingface

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_datasets.py`:

```python
import pytest
from clawsgo_self.science import get_registry
from clawsgo_self.science.sources import datasets


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
    monkeypatch.setattr("clawsgo_self.science.sources.datasets.http_get_json",
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
    monkeypatch.setattr("clawsgo_self.science.sources.datasets.http_get_json",
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
            {"title": {"$": "EU Project"}}}}
    ]}}}
    monkeypatch.setattr("clawsgo_self.science.sources.datasets.http_get_json",
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
    monkeypatch.setattr("clawsgo_self.science.sources.datasets.http_get_json",
                        lambda url, **kw: fake)
    datasets.register()
    c = get_registry().get("huggingface")
    hits = c.search("qa", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "SQuAD"
    assert hits[0]["url"] == "https://huggingface.co/datasets/squad"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_datasets.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write datasets.py**

Create `clawsgo_self/science/sources/datasets.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _zenodo_search(query, limit):
    params = {"q": query, "size": str(limit), "type": "dataset"}
    url = "https://zenodo.org/api/records?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for h in data.get("hits", {}).get("hits", []):
        meta = h.get("metadata", {})
        out.append({
            "title": meta.get("title", ""),
            "year": None,
            "doi": meta.get("doi"),
            "url": h.get("links", {}).get("html", f"https://zenodo.org/record/{h.get('id','')}"),
            "venue": "Zenodo",
            "authors": [c.get("name", "") for c in meta.get("creators", [])[:12]],
            "cited_by": 0,
            "abstract": meta.get("description", ""),
        })
    return out


def _doaj_search(query, limit):
    url = f"https://doaj.org/api/v2/search/articles/{urllib.parse.quote(query)}?pageSize={limit}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", []):
        bib = r.get("bibjson", {})
        doi = (bib.get("identifier") or [{}])[0].get("id") if bib.get("identifier") else None
        link = (bib.get("link") or [{}])[0].get("url", "") if bib.get("link") else ""
        out.append({
            "title": bib.get("title", ""),
            "year": bib.get("year"),
            "doi": doi,
            "url": link,
            "venue": (bib.get("journal", {}) or {}).get("title", ""),
            "authors": [a.get("name", "") for a in bib.get("author", [])[:12]],
            "cited_by": 0,
            "abstract": bib.get("abstract", ""),
        })
    return out


def _openaire_search(query, limit):
    params = {"keywords": query, "format": "json", "pageSize": str(limit)}
    url = "https://api.openaire.eu/search/publications?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("response", {}).get("results", {}).get("result", []):
        meta = r.get("metadata", {}).get("oaf:entity", {}).get("oaf:result", {})
        title_obj = meta.get("title", {})
        title = title_obj.get("$", "") if isinstance(title_obj, dict) else ""
        out.append({
            "title": title,
            "year": None,
            "doi": "",
            "url": "",
            "venue": "",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _huggingface_search(query, limit):
    params = {"search": query, "limit": str(limit)}
    url = "https://huggingface.co/api/datasets?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for d in data:
        did = d.get("id", "")
        out.append({
            "title": d.get("title") or did,
            "year": None,
            "doi": None,
            "url": f"https://huggingface.co/datasets/{did}" if did else "",
            "venue": "Hugging Face",
            "authors": [d.get("author", "")] if d.get("author") else [],
            "cited_by": d.get("downloads") or 0,
            "abstract": d.get("description", ""),
        })
    return out


def register():
    specs = [
        ("zenodo", "Zenodo", "Zenodo research data", _zenodo_search),
        ("doaj", "DOAJ", "Directory of Open Access Journals", _doaj_search),
        ("openaire", "OpenAIRE", "OpenAIRE research graph", _openaire_search),
        ("huggingface", "Hugging Face", "Hugging Face datasets", _huggingface_search),
    ]
    for cid, name, desc, fn in specs:
        register(Connector(id=cid, name=name, domain="datasets",
                           description=desc, search=fn))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_science_datasets.py -v`
Expected: 5 passed

- [ ] **Step 5: Commit**

```bash
git add clawsgo_self/science/sources/datasets.py tests/test_science_datasets.py
git commit -m "feat(science): add 4 dataset/open-access connectors (zenodo/doaj/openaire/huggingface)"
```

---
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
### Task 6: Protein Sources (6 connectors)

**Files:**
- Create: `clawsgo_self/science/sources/proteins.py`
- Create: `tests/test_science_proteins.py`

**Interfaces:**
- Produces: `sources.proteins.register()` registering uniprot, rcsb-pdb, pdbe, alphafold, interpro, sifts

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_proteins.py`:

```python
import pytest
from clawsgo_self.science import get_registry
from clawsgo_self.science.sources import proteins


def test_proteins_registers_6():
    before = len(get_registry().all())
    proteins.register()
    after = len(get_registry().all())
    assert after - before == 6


def test_uniprot_search_parses(monkeypatch):
    fake = {"results": [
        {"primaryAccession": "P12345",
         "proteinDescription": {"recommendedName": {"fullName": {"value": "Kinase X"}}},
         "organism": {"scientificName": "Homo sapiens"}}
    ]}
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("uniprot")
    hits = c.search("kinase", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Kinase X"
    assert hits[0]["url"] == "https://www.uniprot.org/uniprotkb/P12345"


def test_uniprot_fetch_fasta(monkeypatch):
    fake = ">sp|P12345|KINH_HUMAN\nMKWVTFISLL"
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_text",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("uniprot")
    data = c.fetch("P12345", "fasta")
    assert data["format"] == "fasta"
    assert "MKWVTFISLL" in data["data"]


def test_rcsb_pdb_search_parses(monkeypatch):
    fake = {"result_set": [{"identifier": "1ABC", "score": 1.0}]}
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("rcsb-pdb")
    hits = c.search("hemoglobin", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "1ABC"


def test_alphafold_search_parses(monkeypatch):
    fake = [{"entryId": "AF-P12345-F1",
             "uniprotDescription": "Protein structure",
             "organismScientificName": "Human",
             "pdbUrl": "http://pdb/1abc"}]
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("alphafold")
    hits = c.search("P12345", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Protein structure"


def test_interpro_search_parses(monkeypatch):
    fake = {"results": [
        {"metadata": {"accession": "IPR000001", "name": "Kinase dom",
                       "source_database": "Pfam", "protein_count": 500}}
    ]}
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("interpro")
    hits = c.search("kinase", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Kinase dom"


def test_pdbe_search_parses(monkeypatch):
    fake = {"1abc": {"title": "Heme binding protein"}}
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("pdbe")
    hits = c.search("heme", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Heme binding protein"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_proteins.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write proteins.py**

Create `clawsgo_self/science/sources/proteins.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _uniprot_search(query, limit):
    params = {"query": query, "format": "json", "size": str(limit)}
    url = "https://rest.uniprot.org/uniprotkb/search?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", []):
        acc = r.get("primaryAccession", "")
        desc = r.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {})
        title = desc.get("value", acc) if isinstance(desc, dict) else acc
        out.append({
            "id": acc,
            "title": title,
            "year": None,
            "doi": None,
            "url": f"https://www.uniprot.org/uniprotkb/{acc}" if acc else "",
            "venue": r.get("organism", {}).get("scientificName", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _uniprot_fetch(id, format):
    if format == "fasta":
        url = f"https://rest.uniprot.org/uniprotkb/{id}.fasta"
        text = sci_http.http_get_text(url)
        return {"format": "fasta", "data": text or ""}
    url = f"https://rest.uniprot.org/uniprotkb/{id}.json"
    data = sci_http.http_get_json(url)
    return {"format": "json", "data": data}


def _rcsb_pdb_search(query, limit):
    q = urllib.parse.quote(query)
    url = f"https://search.rcsb.org/rcsbsearch/v2/query?json=%7B%22query%22%3A%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22full_text%22%2C%22parameters%22%3A%7B%22value%22%3A%22{q}%22%7D%7D%2C%22return_type%22%3A%22entry%22%7D"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("result_set", []):
        ident = r.get("identifier", "")
        out.append({
            "id": ident,
            "title": f"PDB {ident}",
            "year": None,
            "doi": None,
            "url": f"https://www.rcsb.org/structure/{ident}" if ident else "",
            "venue": "RCSB PDB",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _pdbe_search(query, limit):
    url = f"https://www.ebi.ac.uk/pdbe/api/search/pdb/entry_details/{urllib.parse.quote(query)}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for pdb_id, info in data.items():
        title = info.get("title", "") if isinstance(info, dict) else ""
        out.append({
            "id": pdb_id,
            "title": title or f"PDB {pdb_id}",
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/pdbe/entry-files/download/pdb{pdb_id}.ent",
            "venue": "PDBe",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _alphafold_search(query, limit):
    url = f"https://alphafold.ebi.ac.uk/api/prediction/{urllib.parse.quote(query)}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for entry in data:
        out.append({
            "id": entry.get("entryId", ""),
            "title": entry.get("uniprotDescription", ""),
            "year": None,
            "doi": None,
            "url": entry.get("pdbUrl", ""),
            "venue": entry.get("organismScientificName", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _interpro_search(query, limit):
    params = {"search": query, "page_size": str(limit)}
    url = "https://www.ebi.ac.uk/interpro/api/search/all/?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", []):
        meta = r.get("metadata", {})
        out.append({
            "id": meta.get("accession", ""),
            "title": meta.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/interpro/entry/{meta.get('accession','')}",
            "venue": meta.get("source_database", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _sifts_search(query, limit):
    url = f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{urllib.parse.quote(query)}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for pdb_id in data:
        out.append({
            "id": pdb_id,
            "title": f"SIFTS mapping {pdb_id}",
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{pdb_id}",
            "venue": "PDBe SIFTS",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def register():
    specs = [
        ("uniprot", "UniProt", "UniProt protein knowledgebase", _uniprot_search),
        ("rcsb-pdb", "RCSB PDB", "Protein Data Bank", _rcsb_pdb_search),
        ("pdbe", "PDBe", "Protein Data Bank in Europe", _pdbe_search),
        ("alphafold", "AlphaFold DB", "AlphaFold protein structures", _alphafold_search),
        ("interpro", "InterPro", "Protein families and domains", _interpro_search),
        ("sifts", "PDBe SIFTS", "Structure integration with function", _sifts_search),
    ]
    for cid, name, desc, fn in specs:
        c = Connector(id=cid, name=name, domain="proteins", description=desc, search=fn)
        if cid == "uniprot":
            c.fetch = _uniprot_fetch
        register(c)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_science_proteins.py -v`
Expected: 7 passed

- [ ] **Step 5: Commit**

```bash
git add clawsgo_self/science/sources/proteins.py tests/test_science_proteins.py
git commit -m "feat(science): add 6 protein connectors (uniprot/rcsb-pdb/pdbe/alphafold/interpro/sifts)"
```

---
### Task 7: Chemistry Sources (6 connectors)

**Files:**
- Create: `clawsgo_self/science/sources/chemistry.py`
- Create: `tests/test_science_chemistry.py`

**Interfaces:**
- Produces: `sources.chemistry.register()` registering chembl, pubchem, chebi, bindingdb, gtopdb, surechembl

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_chemistry.py`:

```python
import pytest
from clawsgo_self.science import get_registry
from clawsgo_self.science.sources import chemistry


def test_chemistry_registers_6():
    before = len(get_registry().all())
    chemistry.register()
    after = len(get_registry().all())
    assert after - before == 6


def test_chembl_search_parses(monkeypatch):
    fake = {"molecules": [
        {"molecule_chembl_id": "CHEMBL123", "pref_name": "Aspirin",
         "molecule_structures": {"canonical_smiles": "CC(=O)OC1=CC=CC=C1C(O)=O"}}
    ]}
    monkeypatch.setattr("clawsgo_self.science.sources.chemistry.http_get_json",
                        lambda url, **kw: fake)
    chemistry.register()
    c = get_registry().get("chembl")
    hits = c.search("aspirin", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Aspirin"
    assert hits[0]["id"] == "CHEMBL123"


def test_pubchem_search_parses(monkeypatch):
    fake_cids = {"IdentifierList": {"CID": [2244]}}
    fake_prop = {"PropertyTable": {"Properties": [{"CID": 2244, "Title": "Acetaminophen"}]}}
    call = [0]
    def fake_json(url, **kw):
        call[0] += 1
        if "cids" in url:
            return fake_cids
        return fake_prop
    monkeypatch.setattr("clawsgo_self.science.sources.chemistry.http_get_json", fake_json)
    chemistry.register()
    c = get_registry().get("pubchem")
    hits = c.search("acetaminophen", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Acetaminophen"


def test_chebi_search_parses(monkeypatch):
    fake = {"List": {"item": [{"chebiId": "CHEBI:12345", "chebiAsciiName": "Caffeine"}]}}
    monkeypatch.setattr("clawsgo_self.science.sources.chemistry.http_get_json",
                        lambda url, **kw: fake)
    chemistry.register()
    c = get_registry().get("chebi")
    hits = c.search("caffeine", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Caffeine"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_chemistry.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write chemistry.py**

Create `clawsgo_self/science/sources/chemistry.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _chembl_search(query, limit):
    params = {"q": query, "format": "json", "limit": str(limit)}
    url = "https://www.ebi.ac.uk/chembl/api/data/molecule/search?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for m in data.get("molecules", []):
        out.append({
            "id": m.get("molecule_chembl_id", ""),
            "title": m.get("pref_name", "") or m.get("molecule_chembl_id", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/chembl/compound_report_card/{m.get('molecule_chembl_id','')}",
            "venue": "ChEMBL",
            "authors": [],
            "cited_by": 0,
            "abstract": (m.get("molecule_structures") or {}).get("canonical_smiles", ""),
        })
    return out


def _pubchem_search(query, limit):
    params = {"name": query, "operation": "cids", "format": "JSON"}
    url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/" + urllib.parse.quote(query) + "/cids/JSON"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    cids = data.get("IdentifierList", {}).get("CID", [])[:limit]
    if not cids:
        return []
    prop_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{','.join(map(str, cids))}/property/Title/JSON"
    prop_data = sci_http.http_get_json(prop_url)
    if not prop_data:
        return []
    out = []
    for p in prop_data.get("PropertyTable", {}).get("Properties", []):
        out.append({
            "id": str(p.get("CID", "")),
            "title": p.get("Title", ""),
            "year": None,
            "doi": None,
            "url": f"https://pubchem.ncbi.nlm.nih.gov/compound/{p.get('CID','')}",
            "venue": "PubChem",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _chebi_search(query, limit):
    params = {"q": query, "maxRows": str(limit)}
    url = "https://www.ebi.ac.uk/chebi/ws/rest/search?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("List", {}).get("item", []):
        out.append({
            "id": item.get("chebiId", ""),
            "title": item.get("chebiAsciiName", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/chebi/searchId.do?chebiId={item.get('chebiId','')}",
            "venue": "ChEBI",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _bindingdb_search(query, limit):
    params = {"q": query, "limit": str(limit)}
    url = "https://www.bindingdb.org/bind/webservices/v1/homologySearch?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("results", []):
        out.append({
            "id": item.get("ligand_id", ""),
            "title": item.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.bindingdb.org/bind/ligand/{item.get('ligand_id','')}",
            "venue": "BindingDB",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _gtopdb_search(query, limit):
    params = {"q": query, "limit": str(limit)}
    url = "https://www.guidetopharmacology.org/services/ligands?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("ligands", []):
        out.append({
            "id": item.get("ligandId", ""),
            "title": item.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.guidetopharmacology.org/GRAC/LigandDisplayForward?ligandId={item.get('ligandId','')}",
            "venue": "GuideToPharmacology",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _surechembl_search(query, limit):
    params = {"q": query, "limit": str(limit)}
    url = "https://www.surechembl.org/api/chemical?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("results", []):
        out.append({
            "id": item.get("surechembl_id", ""),
            "title": item.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.surechembl.org/chemical/{item.get('surechembl_id','')}",
            "venue": "SureChEMBL",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def register():
    specs = [
        ("chembl", "ChEMBL", "Bioactive drug-like compounds", _chembl_search),
        ("pubchem", "PubChem", "Chemical molecules and bioactivities", _pubchem_search),
        ("chebi", "ChEBI", "Chemical entities of biological interest", _chebi_search),
        ("bindingdb", "BindingDB", "Protein-ligand binding affinities", _bindingdb_search),
        ("gtopdb", "GuideToPharmacology", "Drug targets and ligands", _gtopdb_search),
        ("surechembl", "SureChEMBL", "Patent chemistry", _surechembl_search),
    ]
    for cid, name, desc, fn in specs:
        register(Connector(id=cid, name=name, domain="chemistry",
                           description=desc, search=fn))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_science_chemistry.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add clawsgo_self/science/sources/chemistry.py tests/test_science_chemistry.py
git commit -m "feat(science): add 6 chemistry connectors (chembl/pubchem/chebi/bindingdb/gtopdb/surechembl)"
```

---

﻿### Task 8: Genomics Sources (7 connectors)

**Files:**
- Create: `clawsgo_self/science/sources/genomics.py`
- Create: `tests/test_science_genomics.py`

**Interfaces:**
- Produces: `sources.genomics.register()` registering ensembl, eutils, mygene, myvariant, clinvar, dbsnp, gnomad

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_genomics.py`:

```python
import pytest
from clawsgo_self.science import get_registry
from clawsgo_self.science.sources import genomics


def test_genomics_registers_7():
    before = len(get_registry().all())
    genomics.register()
    after = len(get_registry().all())
    assert after - before == 7


def test_ensembl_search_parses(monkeypatch):
    fake = [{"id": "ENSG00000139618", "display_name": "BRCA2", "species": "homo_sapiens",
             "biotype": "protein_coding"}]
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json",
                        lambda url, **kw: fake)
    genomics.register()
    c = get_registry().get("ensembl")
    hits = c.search("BRCA2", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "BRCA2"
    assert hits[0]["id"] == "ENSG00000139618"


def test_eutils_search_parses(monkeypatch):
    search_fake = {"esearchresult": {"idlist": ["12345"]}}
    summ_fake = {"result": {"12345": {"name": "TP53", "description": "tumor protein"}}}
    def fake_json(url, **kw):
        if "esearch" in url:
            return search_fake
        return summ_fake
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json", fake_json)
    genomics.register()
    c = get_registry().get("eutils")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53"


def test_mygene_search_parses(monkeypatch):
    fake = {"hits": [{"_id": "7157", "symbol": "TP53", "name": "tumor protein p53",
                      "taxid": 9606, "entrezgene": "7157"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json",
                        lambda url, **kw: fake)
    genomics.register()
    c = get_registry().get("mygene")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "tumor protein p53"


def test_myvariant_search_parses(monkeypatch):
    fake = {"hits": [{"_id": "chr17:7577121:G:A", "dbsnp": {"rsid": "rs12345"}}]}
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json",
                        lambda url, **kw: fake)
    genomics.register()
    c = get_registry().get("myvariant")
    hits = c.search("BRCA1", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "chr17:7577121:G:A"


def test_clinvar_search_parses(monkeypatch):
    search_fake = {"esearchresult": {"idlist": ["1234"]}}
    summ_fake = {"result": {"1234": {"title": "Pathogenic variant",
                                     "clinical_significance": {"description": "Pathogenic"}}}}
    def fake_json(url, **kw):
        if "esearch" in url:
            return search_fake
        return summ_fake
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json", fake_json)
    genomics.register()
    c = get_registry().get("clinvar")
    hits = c.search("BRCA1", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Pathogenic variant"


def test_dbsnp_search_parses(monkeypatch):
    search_fake = {"esearchresult": {"idlist": ["12345"]}}
    summ_fake = {"result": {"12345": {"title": "rs12345"}}}
    def fake_json(url, **kw):
        if "esearch" in url:
            return search_fake
        return summ_fake
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json", fake_json)
    genomics.register()
    c = get_registry().get("dbsnp")
    hits = c.search("rs12345", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "rs12345"


def test_gnomad_search_parses(monkeypatch):
    fake = {"data": {"variant": {"variantId": "1-55516888-G-A", "consequence": "missense"}}}
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json",
                        lambda url, **kw: fake)
    genomics.register()
    c = get_registry().get("gnomad")
    hits = c.search("1-55516888-G-A", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "1-55516888-G-A"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_genomics.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write genomics.py**

Create `clawsgo_self/science/sources/genomics.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _ensembl_search(query, limit):
    url = f"https://rest.ensembl.org/xrefs/symbol/homo_sapiens/{urllib.parse.quote(query)}?content-type=application/json"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data[:limit]:
        out.append({
            "id": r.get("id", ""),
            "title": r.get("display_name", "") or r.get("id", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ensembl.org/Homo_sapiens/Gene/Summary?g={r.get('id','')}",
            "venue": r.get("species", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": r.get("biotype", ""),
        })
    return out


def _eutils_search(query, limit):
    params = {"db": "gene", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = sci_http.http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "gene", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = sci_http.http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        out.append({
            "id": uid,
            "title": s.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ncbi.nlm.nih.gov/gene/{uid}",
            "venue": s.get("description", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": s.get("summary", ""),
        })
    return out


def _mygene_search(query, limit):
    params = {"q": query, "size": str(limit), "species": "human"}
    url = "https://mygene.info/v3/query?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for h in data.get("hits", []):
        out.append({
            "id": h.get("_id", ""),
            "title": h.get("name", "") or h.get("symbol", ""),
            "year": None,
            "doi": None,
            "url": f"https://mygene.info/v3/gene/{h.get('_id','')}",
            "venue": str(h.get("taxid", "")),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _myvariant_search(query, limit):
    params = {"q": query, "size": str(limit)}
    url = "https://myvariant.info/v1/query?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for h in data.get("hits", []):
        out.append({
            "id": h.get("_id", ""),
            "title": h.get("_id", ""),
            "year": None,
            "doi": None,
            "url": f"https://myvariant.info/v1/variant/{h.get('_id','')}",
            "venue": "MyVariant",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _clinvar_search(query, limit):
    params = {"db": "clinvar", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = sci_http.http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "clinvar", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = sci_http.http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        out.append({
            "id": uid,
            "title": s.get("title", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ncbi.nlm.nih.gov/clinvar/variation/{uid}",
            "venue": (s.get("clinical_significance") or {}).get("description", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _dbsnp_search(query, limit):
    params = {"db": "snp", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = sci_http.http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "snp", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = sci_http.http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        out.append({
            "id": uid,
            "title": s.get("title", "") or uid,
            "year": None,
            "doi": None,
            "url": f"https://www.ncbi.nlm.nih.gov/snp/rs{uid}",
            "venue": "dbSNP",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _gnomad_search(query, limit):
    params = {"variant": query}
    url = "https://gnomad.broadinstitute.org/api/v2/variant?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    variant = data.get("data", {}).get("variant", {})
    if variant:
        out.append({
            "id": variant.get("variantId", ""),
            "title": variant.get("variantId", ""),
            "year": None,
            "doi": None,
            "url": f"https://gnomad.broadinstitute.org/variant/{variant.get('variantId','')}",
            "venue": "gnomAD",
            "authors": [],
            "cited_by": 0,
            "abstract": variant.get("consequence", ""),
        })
    return out


def register():
    specs = [
        ("ensembl", "Ensembl", "Ensembl genome browser", _ensembl_search),
        ("eutils", "NCBI eutils", "NCBI Entrez utilities", _eutils_search),
        ("mygene", "MyGene.info", "Gene annotation service", _mygene_search),
        ("myvariant", "MyVariant.info", "Variant annotation service", _myvariant_search),
        ("clinvar", "ClinVar", "Clinical variant interpretations", _clinvar_search),
        ("dbsnp", "dbSNP", "Short genetic variations", _dbsnp_search),
        ("gnomad", "gnomAD", "Genome aggregation database", _gnomad_search),
    ]
    for cid, name, desc, fn in specs:
        register(Connector(id=cid, name=name, domain="genomics",
                           description=desc, search=fn))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_science_genomics.py -v`
Expected: 8 passed

- [ ] **Step 5: Commit**

```bash
git add clawsgo_self/science/sources/genomics.py tests/test_science_genomics.py
git commit -m "feat(science): add 7 genomics connectors (ensembl/eutils/mygene/myvariant/clinvar/dbsnp/gnomad)"
```

---
﻿### Task 9: Pathways & Omics Sources (11 connectors)

**Files:**
- Create: `clawsgo_self/science/sources/pathways.py`
- Create: `clawsgo_self/science/sources/omics.py`
- Create: `tests/test_science_pathways_omics.py`

**Interfaces:**
- Produces: `sources.pathways.register()` registering biogrid, intact, kegg, opentargets, reactome
- Produces: `sources.omics.register()` registering arrayexpress, depmap, expression-atlas, geo, gtex, hpa

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_pathways_omics.py`:

```python
import pytest
from clawsgo_self.science import get_registry
from clawsgo_self.science.sources import pathways, omics


def test_pathways_registers_5():
    before = len(get_registry().all())
    pathways.register()
    after = len(get_registry().all())
    assert after - before == 5


def test_omics_registers_6():
    before = len(get_registry().all())
    omics.register()
    after = len(get_registry().all())
    assert after - before == 6


def test_biogrid_search_parses(monkeypatch):
    fake = {"12345": [{"interactor_a": "P12345", "interactor_b": "P67890"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("biogrid")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "P67890"


def test_intact_search_parses(monkeypatch):
    fake = {"data": [{"id": "EBI-12345", "label": "BRCA1-BRCA2"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("intact")
    hits = c.search("BRCA1", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "EBI-12345"


def test_kegg_search_parses(monkeypatch):
    fake = [["hsa:7157\tTP53 tumor protein p53"]]
    monkeypatch.setattr("clawsgo_self.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("kegg")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert "TP53" in hits[0]["title"]


def test_opentargets_search_parses(monkeypatch):
    fake = {"data": [{"id": "ENSG00000141510", "name": "TP53", "symbol": "TP53"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("opentargets")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53"


def test_reactome_search_parses(monkeypatch):
    fake = {"results": [{"dbId": 12345, "displayName": "DNA Repair"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("reactome")
    hits = c.search("DNA repair", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "DNA Repair"


def test_arrayexpress_search_parses(monkeypatch):
    fake = {"hits": [{"accession": "E-MTAB-1234", "title": "RNA-seq of cancer"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("arrayexpress")
    hits = c.search("cancer", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "RNA-seq of cancer"


def test_depmap_search_parses(monkeypatch):
    fake = {"data": [{"DepMap_ID": "ACH-000001", "cell_line_name": "A549"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("depmap")
    hits = c.search("A549", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "ACH-000001"


def test_expression_atlas_search_parses(monkeypatch):
    fake = {"results": [{"experimentAccession": "E-GEOD-12345", "description": "gene expr"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("expression-atlas")
    hits = c.search("cancer", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "E-GEOD-12345"


def test_geo_search_parses(monkeypatch):
    search_fake = {"esearchresult": {"idlist": ["12345"]}}
    summ_fake = {"result": {"12345": {"title": "Breast cancer GEO series"}}}
    def fake_json(url, **kw):
        if "esearch" in url:
            return search_fake
        return summ_fake
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json", fake_json)
    omics.register()
    c = get_registry().get("geo")
    hits = c.search("breast cancer", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Breast cancer GEO series"


def test_gtex_search_parses(monkeypatch):
    fake = {"geneSymbol": "TP53", "tissueSiteDetailId": "Lung", "tpkm": 12.5}
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("gtex")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53 - Lung"


def test_hpa_search_parses(monkeypatch):
    fake = [{"gene": "TP53", "tissue": "Lung", "celltype": "alveolar"}]
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("hpa")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_pathways_omics.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write pathways.py**

Create `clawsgo_self/science/sources/pathways.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _biogrid_search(query, limit):
    params = {"searchNames": "true", "geneList": query, "interSpeciesExcluded": "true"}
    url = "https://webservice.thebiogrid.org/interactions?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    seen = set()
    for int_id, interactions in data.items():
        for ia in interactions:
            ident = ia.get("interactor_b", "")
            if ident and ident not in seen:
                seen.add(ident)
                out.append({
                    "id": ident,
                    "title": f"interactor {ident}",
                    "year": None,
                    "doi": None,
                    "url": f"https://thebiogrid.org/{ident}",
                    "venue": "BioGRID",
                    "authors": [],
                    "cited_by": 0,
                    "abstract": "",
                })
                if len(out) >= limit:
                    break
        if len(out) >= limit:
            break
    return out


def _intact_search(query, limit):
    url = f"https://www.ebi.ac.uk/intact/ws/search/interaction/{urllib.parse.quote(query)}?format=json"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("data", [])[:limit]:
        out.append({
            "id": r.get("id", ""),
            "title": r.get("label", "") or r.get("id", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/intact/details/{r.get('id','')}",
            "venue": "IntAct",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _kegg_search(query, limit):
    url = f"https://rest.kegg.jp/find/genes/{urllib.parse.quote(query)}"
    text = sci_http.http_get_text(url)
    if not text:
        return []
    out = []
    for line in text.split("\n")[:limit]:
        parts = line.split("\t")
        if len(parts) >= 2:
            out.append({
                "id": parts[0],
                "title": parts[1],
                "year": None,
                "doi": None,
                "url": f"https://www.genome.jp/dbget-bin/www_bget?{parts[0]}",
                "venue": "KEGG",
                "authors": [],
                "cited_by": 0,
                "abstract": "",
            })
    return out


def _opentargets_search(query, limit):
    params = {"q": query, "size": str(limit)}
    url = "https://api.platform.opentargets.org/v3/graphql?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for d in data.get("data", [])[:limit]:
        out.append({
            "id": d.get("id", ""),
            "title": d.get("name", "") or d.get("symbol", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.opentargets.org/target/{d.get('id','')}",
            "venue": d.get("symbol", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _reactome_search(query, limit):
    url = f"https://reactome.org/ContentService/data/search/{urllib.parse.quote(query)}?types=Pathway&cluster=true&species=Homo%20sapiens"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", [])[:limit]:
        out.append({
            "id": str(r.get("dbId", "")),
            "title": r.get("displayName", ""),
            "year": None,
            "doi": None,
            "url": f"https://reactome.org/content/detail/{r.get('dbId','')}",
            "venue": "Reactome",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def register():
    specs = [
        ("biogrid", "BioGRID", "Protein-protein interactions", _biogrid_search),
        ("intact", "IntAct", "Molecular interactions", _intact_search),
        ("kegg", "KEGG", "Kyoto Encyclopedia of Genes and Genomes", _kegg_search),
        ("opentargets", "Open Targets", "Target-disease associations", _opentargets_search),
        ("reactome", "Reactome", "Pathway database", _reactome_search),
    ]
    for cid, name, desc, fn in specs:
        register(Connector(id=cid, name=name, domain="pathways",
                           description=desc, search=fn))
```

- [ ] **Step 4: Write omics.py**

Create `clawsgo_self/science/sources/omics.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _arrayexpress_search(query, limit):
    url = f"https://www.ebi.ac.uk/biostudies/api/v1/search?query={urllib.parse.quote(query)}&pageSize={limit}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for h in data.get("hits", [])[:limit]:
        out.append({
            "id": h.get("accession", ""),
            "title": h.get("title", "") or h.get("accession", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/biostudies/studies/{h.get('accession','')}",
            "venue": "ArrayExpress",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _depmap_search(query, limit):
    url = f"https://depmap.org/portal/api/cell_lines?search={urllib.parse.quote(query)}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for cl in data.get("data", [])[:limit]:
        out.append({
            "id": cl.get("DepMap_ID", ""),
            "title": cl.get("cell_line_name", "") or cl.get("DepMap_ID", ""),
            "year": None,
            "doi": None,
            "url": f"https://depmap.org/portal/cell_line/{cl.get('DepMap_ID','')}",
            "venue": "DepMap",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _expression_atlas_search(query, limit):
    url = f"https://www.ebi.ac.uk/gxa/api/v2/search?query={urllib.parse.quote(query)}&limit={limit}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", [])[:limit]:
        out.append({
            "id": r.get("experimentAccession", ""),
            "title": r.get("description", "") or r.get("experimentAccession", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/gxa/experiments/{r.get('experimentAccession','')}",
            "venue": "Expression Atlas",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _geo_search(query, limit):
    params = {"db": "gds", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = sci_http.http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "gds", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = sci_http.http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        out.append({
            "id": uid,
            "title": s.get("title", "") or uid,
            "year": None,
            "doi": None,
            "url": f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={uid}",
            "venue": "GEO",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _gtex_search(query, limit):
    url = f"https://gtexportal.org/api/v2/gene/{urllib.parse.quote(query)}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for d in data.get("data", [])[:limit]:
        tissue = d.get("tissueSiteDetailId", "")
        out.append({
            "id": f"{d.get('geneSymbol','')}-{tissue}",
            "title": f"{d.get('geneSymbol','')} - {tissue}",
            "year": None,
            "doi": None,
            "url": f"https://gtexportal.org/home/gene/{d.get('geneSymbol','')}",
            "venue": "GTEx",
            "authors": [],
            "cited_by": 0,
            "abstract": f"TPM: {d.get('medianTPM', '')}",
        })
    return out


def _hpa_search(query, limit):
    url = f"https://www.proteinatlas.org/api/search_download.php?search={urllib.parse.quote(query)}&format=json&limit={limit}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for d in data.get("data", [])[:limit]:
        out.append({
            "id": d.get("gene", ""),
            "title": d.get("gene", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.proteinatlas.org/{d.get('gene','')}",
            "venue": "Human Protein Atlas",
            "authors": [],
            "cited_by": 0,
            "abstract": f"tissue: {d.get('tissue','')}",
        })
    return out


def register():
    specs = [
        ("arrayexpress", "ArrayExpress", "Functional genomics experiments", _arrayexpress_search),
        ("depmap", "DepMap", "Cancer dependency map", _depmap_search),
        ("expression-atlas", "Expression Atlas", "Gene expression patterns", _expression_atlas_search),
        ("geo", "GEO", "Gene Expression Omnibus", _geo_search),
        ("gtex", "GTEx", "Genotype-Tissue Expression", _gtex_search),
        ("hpa", "Human Protein Atlas", "Tissue protein expression", _hpa_search),
    ]
    for cid, name, desc, fn in specs:
        register(Connector(id=cid, name=name, domain="omics",
                           description=desc, search=fn))
```

- [ ] **Step 5: Run test to verify it passes**

Run: `pytest tests/test_science_pathways_omics.py -v`
Expected: 12 passed

- [ ] **Step 6: Commit**

```bash
git add clawsgo_self/science/sources/pathways.py clawsgo_self/science/sources/omics.py tests/test_science_pathways_omics.py
git commit -m "feat(science): add 11 pathways/omics connectors (biogrid/intact/kegg/opentargets/reactome/arrayexpress/depmap/expression-atlas/geo/gtex/hpa)"
```

---
﻿### Task 10: Documentation and regression

**Files:**
- Modify: `README.md`
- Modify: `USAGE.md`

**Interfaces:**
- Consumes: all science modules (verification only)

- [ ] **Step 1: Update README.md**

Update `README.md` to reflect the new science layer:

1. In the feature table, add a new row for the science data layer:
   ```
   | 科学数据查询 | science_list_dbs / science_search / science_fetch / science_cross_lookup | 41 免 key 连接器（literature/proteins/chemistry/genomics/pathways/omics/datasets） |
   ```

2. Update the tool count from 20 to 24.

3. Add a new section `## 科学数据查询（science）` describing the connector framework:
   ```markdown
   ## 科学数据查询（science）

   移植自 [synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience) 的科学数据库连接器层，提供 41 个免 key 科学数据源的统一检索接口。

   ### 数据域
   - **literature**: openalex, arxiv, biorxiv, crossref, europepmc, pubmed, semantic-scholar
   - **proteins**: uniprot, rcsb-pdb, pdbe, alphafold, interpro, sifts
   - **chemistry**: chembl, pubchem, chebi, bindingdb, gtopdb, surechembl
   - **genomics**: ensembl, eutils, mygene, myvariant, clinvar, dbsnp, gnomad
   - **pathways**: biogrid, intact, kegg, opentargets, reactome
   - **omics**: arrayexpress, depmap, expression-atlas, geo, gtex, hpa
   - **datasets**: zenodo, doaj, openaire, huggingface

   ### 工具
   | 工具 | 说明 |
   | --- | --- |
   | `science_list_dbs(domain?)` | 列出可用数据库 |
   | `science_search(database, query, limit)` | 单库检索 |
   | `science_fetch(database, id, format)` | 按 id 拉取记录 |
   | `science_cross_lookup(query, databases?, limit)` | 多库联合检索 |
   ```

4. Update the architecture tree to include `science/` package.

- [ ] **Step 2: Update USAGE.md**

Add a new section `## 科学数据查询` with usage examples:

```markdown
## 科学数据查询

### 列出数据库
```
science_list_dbs("literature")  # 列出文献类数据库
science_list_dbs()              # 列出全部数据库
```

### 单库检索
```
science_search("openalex", "quantum computing", limit=10)
science_search("uniprot", "kinase", limit=5)
```

### 多库联合检索
```
science_cross_lookup("BRCA1", databases=["uniprot", "mygene", "clinvar"], limit=5)
```

### 拉取原文
```
science_fetch("uniprot", "P12345", format="fasta")  # 拉取 FASTA 序列
science_fetch("rcsb-pdb", "1ABC", format="pdb")     # 拉取 PDB 结构
```
```

- [ ] **Step 3: Run full regression**

Run: `CLAWSGO_SELF_OFFLINE=1 pytest tests/ -q`
Expected: all tests pass (61 existing + new science tests)

- [ ] **Step 4: Commit**

```bash
git add README.md USAGE.md
git commit -m "feat(docs): update README and USAGE for science data layer (24 tools, 41 connectors)"
```