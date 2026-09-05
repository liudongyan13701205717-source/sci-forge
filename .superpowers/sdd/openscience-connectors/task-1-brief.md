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
