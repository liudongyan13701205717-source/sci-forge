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
