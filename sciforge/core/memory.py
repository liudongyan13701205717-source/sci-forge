"""项目进度记账（memory）：为 projects/{paper_id} 维护一条 timeline，
记录里程碑、状态与备注，形成可回溯的研究日志。

纯本地 JSON，无网络。
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field

from sciforge.core import Layout


@dataclass
class MemoryEntry:
    ts: str
    action: str          # note | milestone | status
    note: str = ""
    milestone: str = ""
    status: str = ""

    def to_dict(self) -> dict:
        return {"ts": self.ts, "action": self.action, "note": self.note,
                "milestone": self.milestone, "status": self.status}


@dataclass
class ProjectMemory:
    ok: bool
    paper_id: str = ""
    entries: list = field(default_factory=list)
    summary: list = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict:
        return {"ok": self.ok, "paper_id": self.paper_id,
                "entries": self.entries, "summary": self.summary, "error": self.error}

    def to_markdown(self) -> str:
        lines = [f"# 项目进度：{self.paper_id}", ""]
        if not self.entries:
            lines.append("- （暂无记录，用 project_memory 添加）")
        for e in self.entries:
            tag = {"note": "备忘", "milestone": "里程碑", "status": "状态"}.get(e["action"], e["action"])
            body = []
            if e.get("note"):
                body.append(e["note"])
            if e.get("milestone"):
                body.append("里程碑：" + e["milestone"])
            if e.get("status"):
                body.append("状态：" + e["status"])
            lines.append(f"- `[{e['ts']}] {tag}` {' ｜ '.join(body) if body else '（空）'}")
        return "\n".join(lines)


def _semver_like(s: str) -> bool:
    s = s.strip()
    try:
        a, b, c = s.split(".")
        int(a); int(b); int(c)
        return a.isdigit() and b.isdigit() and c.isdigit()
    except (ValueError, AttributeError):
        return False


def _milestone_sort(entries: list[dict]) -> list[dict]:
    """把纯 digit 里程碑（如 1.0.0）按版本序排在各自位置。"""
    def ver_key(e):
        ms = (e.get("milestone") or "").strip()
        if _semver_like(ms):
            try:
                return (0, tuple(int(x) for x in ms.split(".")), e["ts"])
            except (ValueError, AttributeError):
                return (1, (0, 0, 0), e["ts"])
        return (1, (0, 0, 0), e["ts"])
    return sorted(entries, key=ver_key)


def _backlog(layout: Layout, paper_id: str) -> list[dict]:
    """把 work_plan 的 breakpoints/checkpoints 变成待跟踪里程碑。"""
    root = layout.project_dir(paper_id) / "research"
    out: list[dict] = []
    for name in ("research_plan.json", "work_plan.json"):
        p = root / name
        if not p.exists():
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        nodes = []
        for key in ("breakpoints", "checkpoints", "milestones"):
            nodes.extend(data.get(key) or [] if isinstance(data, dict) else [])
        for n in nodes:
            if isinstance(n, str):
                out.append({"milestone": n.strip(), "_planned": True})
            elif isinstance(n, dict):
                for k in ("id", "title", "name", "milestone"):
                    v = n.get(k)
                    if v:
                        out.append({"milestone": str(v).strip(), "_planned": True})
                        break
    return out


def project_memory(
    *,
    paper_id: str,
    layout: Layout,
    action: str = "read",
    note: str = "",
    milestone: str = "",
    status: str = "",
    subject: str = "",
) -> ProjectMemory:
    """记账：action∈{read,note,milestone,status,rename}；subject 用于 rename。"""
    root = layout.project_dir(paper_id)
    root.mkdir(parents=True, exist_ok=True)
    db = root / "memory.json"
    entries: list[dict] = []
    if db.exists():
        try:
            entries = json.loads(db.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            entries = []

    if action == "read":
        entries = _milestone_sort(entries)
        return _finalize(layout, paper_id, entries, db, write=False)

    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    if action == "note":
        if not note:
            return _finalize(layout, paper_id, entries, db, error="note 不能为空")
        entry = MemoryEntry(ts=ts, action="note", note=note)
    elif action == "milestone":
        if not milestone:
            return _finalize(layout, paper_id, entries, db, error="milestone 不能为空")
        entry = MemoryEntry(ts=ts, action="milestone", milestone=milestone, note=note)
    elif action == "status":
        entry = MemoryEntry(ts=ts, action="status", status=status, note=note)
    elif action == "rename":
        entries = list(filter(None, entries))  # keep shape
        return _finalize(layout, paper_id, entries, db,
                         error="rename 需要传入新名称（项目目录请用文件系统重命名）")
    else:
        return _finalize(layout, paper_id, entries, db,
                         error=f"未知 action：{action}（可选 read/note/milestone/status）")

    entries.append(entry.to_dict())
    return _finalize(layout, paper_id, entries, db, write=True)


def _finalize(layout, paper_id, entries, db, *, write=True, error=""):
    if write:
        db.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = _summarize(entries)
    return ProjectMemory(ok=not error, paper_id=paper_id,
                         entries=entries, summary=summary, error=error)


def _summarize(entries: list[dict]) -> list[dict]:
    counts: dict[str, int] = {}
    last = {}
    for e in entries:
        counts[e.get("action", "?")] = counts.get(e.get("action", "?"), 0) + 1
    statuses = [e.get("status") for e in entries if e.get("status")]
    milestones = [e.get("milestone") for e in entries if e.get("milestone")]
    return [
        {"entries": len(entries),
         "by_action": counts,
         "last_status": statuses[-1] if statuses else "",
         "milestones": milestones,
         "has_plan_backlog": bool(milestones) or len(entries) >= 3},
    ]