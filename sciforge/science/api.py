from __future__ import annotations

from sciforge.science import get_registry
from sciforge.science.http import _offline


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
        return {"ok": False, "error": f"{database} fetch not supported"}
    data = c.fetch(id, format)
    return {"ok": True, "database": database, "id": id,
            "format": format, "data": data}


def cross_lookup(query: str, databases: list[str], limit: int = 5) -> list[dict]:
    seen: set[str] = set()
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
