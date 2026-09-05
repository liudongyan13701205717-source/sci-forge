"""交付线对外 API：get_deliverables。

给定 task_id（复现）或 paper_id（写作），扫描对应目录并给出分门别类的
交付物清单（源码/数据/报告/图/导出物）。
"""

from __future__ import annotations

from pathlib import Path

from sciforge.core import Layout, get_layout

_SOURCES = {".py"}
_DATA = {".json", ".csv", ".npz", ".txt"}
_REPORTS = {".md", ".tex", ".html", ".pdf"}
_IMAGES = {".png", ".jpg", ".jpeg", ".svg"}


def _classify(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in _SOURCES:
        return "source"
    if ext in _DATA:
        return "data"
    if ext in _REPORTS:
        return "report"
    if ext in _IMAGES:
        return "image"
    return "other"


def _scan(root: Path) -> list[dict]:
    if not root.exists():
        return []
    items: list[dict] = []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        rel = str(p.relative_to(root)).replace("\\", "/")
        if "_generated.py" in rel or "metrics.jsonl" in rel:
            continue
        try:
            size = p.stat().st_size
        except OSError:
            size = 0
        items.append({
            "path": rel,
            "kind": _classify(p),
            "size": size,
        })
    return items


def get_deliverables(
    task_id: str = "",
    paper_id: str = "",
    *,
    layout: Layout | None = None,
) -> dict:
    """列出交付物。task_id 优先查复现任务；paper_id 查写作项目。"""
    layout = layout or get_layout()
    layout.ensure()

    # 复现任务
    if task_id:
        task_root = layout.task_dir(task_id)
        found = _scan(task_root)
        if not found:
            # 任务目录无交付物：回退把 task_id 当 paper_id，查写作项目
            proj = layout.project_dir(task_id)
            found = _scan(proj)
            if found:
                by_kind = {}
                for it in found:
                    by_kind.setdefault(it["kind"], []).append(it["path"])
                return {
                    "ok": True,
                    "kind": "project",
                    "id": task_id,
                    "deliverables": found,
                    "by_kind": by_kind,
                    "count": len(found),
                }
            return {
                "ok": True,
                "kind": "task",
                "id": task_id,
                "deliverables": [],
                "count": 0,
                "message": f"任务 {task_id} 暂无交付物（可能尚未完成复现）。",
            }
        grouped: dict[str, list] = {}
        for it in found:
            grouped.setdefault(it["kind"], []).append(it)
        return {
            "ok": True,
            "kind": "task",
            "id": task_id,
            "deliverables": found,
            "by_kind": {k: [i["path"] for i in v] for k, v in grouped.items()},
            "count": len(found),
        }

    # 写作项目
    if paper_id:
        proj = layout.project_dir(paper_id)
        found = _scan(proj)
        by_kind = {}
        for it in found:
            by_kind.setdefault(it["kind"], []).append(it["path"])
        return {
            "ok": True,
            "kind": "project",
            "id": paper_id,
            "deliverables": found,
            "by_kind": by_kind,
            "count": len(found),
        }

    return {"ok": False, "error": "请提供 task_id 或 paper_id 之一。"}
