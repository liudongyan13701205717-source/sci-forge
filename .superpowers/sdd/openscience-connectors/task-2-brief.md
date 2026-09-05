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
