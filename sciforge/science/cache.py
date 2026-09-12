"""SQLite-backed offline cache for science search results.

ponytail: simple single-table cache, no eviction policy. Add per-DB TTL + LRU if
query volume grows beyond dev usage.
"""
from __future__ import annotations

import json
import os
import sqlite3
from typing import Any

_CACHE_PATH = os.path.join(
    os.path.expanduser("~"),
    ".local", "share", "sciforge", "science_cache.db",
)


def _db() -> sqlite3.Connection:
    os.makedirs(os.path.dirname(_CACHE_PATH), exist_ok=True)
    conn = sqlite3.connect(_CACHE_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cache (
            query       TEXT NOT NULL,
            database    TEXT NOT NULL,
            result      TEXT NOT NULL,
            created_at  REAL NOT NULL DEFAULT (strftime('%s', 'now'))
        )
    """)
    conn.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_cache_query_db
        ON cache (query, database)
    """)
    conn.commit()
    return conn


def store_cache(query: str, database: str, hits: list[dict]) -> None:
    try:
        conn = _db()
        conn.execute(
            "INSERT OR REPLACE INTO cache (query, database, result) VALUES (?, ?, ?)",
            (query, database, json.dumps(hits)),
        )
        conn.commit()
        conn.close()
    except Exception:
        pass


def search_cache(query: str, databases: list[str], limit: int) -> list[dict]:
    if not databases:
        return []
    try:
        conn = _db()
        placeholders = ",".join("?" * len(databases))
        rows = conn.execute(
            f"SELECT result FROM cache WHERE query = ? AND database IN ({placeholders})",
            [query, *databases],
        ).fetchall()
        conn.close()
    except Exception:
        return []

    out: list[dict] = []
    seen: set[str] = set()
    for row in rows:
        for hit in json.loads(row[0]):
            key = (hit.get("doi") or hit.get("url") or hit.get("title", "")).lower().strip()
            if key in seen:
                continue
            seen.add(key)
            out.append(hit)
            if len(out) >= limit:
                return out
    return out
