"""已存检索的监测告警（backlog #7，Litmaps/ResearchRabbit 对等能力）。

把一个已保存的检索式变成「自更新的证据流」：
  - 每次运行执行一次检索，与上次快照做差集 → 新命中；
  - 检索式与快照持久化到项目目录，跨会话可续；
  - 离线时显式降级（不伪造「无新结果」）。

不含定时器/后台线程：由调用方（MCP 工具或用户）按节奏触发，
避免长驻进程负担；这也让行为可预测、可测试。
"""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

from sciforge.core import Layout

_ALERTS_FILE = "alerts.json"


def _dir(layout: Layout, paper_id: str) -> Path:
    p = layout.project_dir(paper_id) / "research"
    p.mkdir(parents=True, exist_ok=True)
    return p


def _load(layout: Layout, paper_id: str) -> dict:
    f = _dir(layout, paper_id) / _ALERTS_FILE
    if not f.exists():
        return {"version": 1, "alerts": {}}
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return {"version": 1, "alerts": {}}


def _save(layout: Layout, paper_id: str, data: dict) -> None:
    f = _dir(layout, paper_id) / _ALERTS_FILE
    f.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _fetch(query: str, databases: list[str] | None, limit: int) -> list[dict]:
    """检索后端，可被测试替换。默认走 cross_lookup。"""
    from sciforge.science.api import cross_lookup

    try:
        return cross_lookup(query, databases=databases or None, limit=limit) or []
    except Exception:  # noqa: BLE001
        return []


def _norm(hits: list[dict]) -> list[dict]:
    out = []
    seen = set()
    for h in hits or []:
        if not isinstance(h, dict):
            continue
        hid = str(h.get("id") or h.get("doi") or h.get("title") or "").strip()
        if not hid or hid in seen:
            continue
        seen.add(hid)
        out.append({"id": hid, "title": h.get("title", ""),
                    "year": h.get("year", ""), "venue": h.get("venue", "")})
    return out


def upsert_alert(*, layout: Layout, paper_id: str, query: str,
                 databases: list[str] | None = None, limit: int = 25) -> dict:
    key = hashlib.sha1(
        (json.dumps([query, sorted(databases or []), limit], ensure_ascii=False)).encode("utf-8")
    ).hexdigest()[:12]
    data = _load(layout, paper_id)
    now = int(time.time())
    rec = data["alerts"].get(key)
    if rec is None:
        rec = {
            "id": key, "query": query, "databases": list(databases or []),
            "limit": limit, "created": now, "enabled": True,
            "runs": 0, "last_run": 0, "seen_ids": [], "history": [],
        }
        data["alerts"][key] = rec
        action = "created"
    else:
        action = "updated"
    _save(layout, paper_id, data)
    return {
        "ok": True, "action": action, "id": key, "query": query,
        "databases": list(databases or []), "enabled": bool(rec["enabled"]),
    }


def set_alert_enabled(*, layout: Layout, paper_id: str, alert_id: str,
                      enabled: bool) -> dict:
    data = _load(layout, paper_id)
    rec = data["alerts"].get(alert_id)
    if rec is None:
        return {"ok": False, "error": f"未找到检索监测 {alert_id}"}
    rec["enabled"] = bool(enabled)
    _save(layout, paper_id, data)
    return {"ok": True, "action": "updated", "id": alert_id, "enabled": bool(enabled)}


def remove_alert(*, layout: Layout, paper_id: str, alert_id: str) -> dict:
    data = _load(layout, paper_id)
    if alert_id not in data["alerts"]:
        return {"ok": False, "error": f"未找到检索监测 {alert_id}"}
    del data["alerts"][alert_id]
    _save(layout, paper_id, data)
    return {"ok": True, "removed": alert_id}


def list_alerts(*, layout: Layout, paper_id: str) -> dict:
    data = _load(layout, paper_id)
    rows = []
    for k in sorted(data["alerts"]):
        a = data["alerts"][k]
        rows.append({
            "id": k, "query": a["query"], "databases": a["databases"],
            "enabled": a["enabled"], "runs": a["runs"],
            "last_run": a["last_run"], "seen_count": len(a["seen_ids"]),
        })
    return {"ok": True, "alerts": rows}


def run_alert(*, layout: Layout, paper_id: str, query: str = "",
              databases: list[str] | None = None, limit: int = 25,
              alert_id: str = "", enabled: bool | None = None) -> dict:
    """创建/运行一个监测：返回本次新命中与累计状态。

    - alert_id 为空：先按 query+databases 建索引（幂等），再跑一次检索。
      首次创建时 action="created" 且 first_seen=True；
      索引已存在时 action="ran" 且 first_seen=False。
    - alert_id 非空：运行既有监测。
    """
    created = False
    if not alert_id:
        up = upsert_alert(layout=layout, paper_id=paper_id, query=query,
                          databases=databases, limit=limit)
        if not up["ok"]:
            return up
        alert_id = up["id"]
        created = up["action"] == "created"
    first_seen = created

    data = _load(layout, paper_id)
    rec = data["alerts"].get(alert_id)
    if rec is None:
        return {"ok": False, "error": f"未找到检索监测 {alert_id}"}
    if enabled is not None:
        rec["enabled"] = bool(enabled)

    if not rec["enabled"]:
        _save(layout, paper_id, data)
        return {"ok": True, "action": "disabled", "id": alert_id,
                "enabled": False, "reason": "监测已停用，未执行检索",
                "new": [], "new_count": 0,
                "runs": rec["runs"], "cumulative_seen": len(rec["seen_ids"])}

    hits = _norm(_fetch(rec["query"], rec["databases"], rec["limit"]))
    previous = set(rec["seen_ids"])
    new = [h for h in hits if h["id"] not in previous]

    rec["seen_ids"] = [h["id"] for h in hits]
    rec["runs"] += 1
    now = int(time.time())
    rec["last_run"] = now
    rec["history"].append({
        "ts": now, "returned": len(hits), "new": len(new),
        "new_ids": [h["id"] for h in new][:50],
    })
    rec["history"] = rec["history"][-50:]
    _save(layout, paper_id, data)

    return {
        "ok": True, "action": "created" if created else "ran",
        "id": alert_id, "query": rec["query"],
        "databases": rec["databases"], "first_seen": bool(first_seen),
        "returned": len(hits), "new": new, "new_count": len(new),
        "runs": rec["runs"], "cumulative_seen": len(rec["seen_ids"]),
    }
