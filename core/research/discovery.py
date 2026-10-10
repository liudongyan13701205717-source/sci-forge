"""迭代检索的发现曲线与停止判据（backlog #22，竞品普遍缺失项）。

给检索一个**可辩护的终止规则**：逐轮执行同一检索，记录每轮新增唯一
命中数与累计曲线；当连续若干轮新增低于阈值时判定 plateau 并停止，
而不是靠感觉决定「查够了」。

累计曲线同时输出为 JSON，便于在论文方法学部分复现检索终止过程。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from sciforge.core import Layout

MIN_NEW_DEFAULT = 3
MAX_ROUNDS_DEFAULT = 8


def _search(query: str, databases: list[str] | None, limit: int) -> list[dict]:
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


@dataclass
class DiscoveryRun:
    ok: bool
    paper_id: str = ""
    query: str = ""
    rounds: int = 0
    total_unique: int = 0
    curve: list = field(default_factory=list)
    new_per_round: list = field(default_factory=list)
    stop_reason: str = ""
    min_new_per_round: int = MIN_NEW_DEFAULT
    offline: bool = False
    notes: list = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "ok": self.ok, "paper_id": self.paper_id, "query": self.query,
            "rounds": self.rounds, "total_unique": self.total_unique,
            "curve": self.curve, "new_per_round": self.new_per_round,
            "stop_reason": self.stop_reason,
            "min_new_per_round": self.min_new_per_round,
            "offline": self.offline, "notes": self.notes, "error": self.error,
        }

    def to_markdown(self) -> str:
        rows = "\n".join(
            f"- 第 {c['round']} 轮：新增 {c['new']}，累计 {c['cumulative']}"
            for c in self.curve
        ) or "- （无数据）"
        return "\n\n".join([
            f"# 迭代发现曲线：{self.paper_id}",
            f"## 检索式\n`{self.query}`",
            f"## 终止判定\n"
            f"- 轮数：{self.rounds}（上限内）\n"
            f"- 停止原因：{self.stop_reason or '（未说明）'}\n"
            f"- 停止阈值：连续新增 < {self.min_new_per_round}\n"
            f"- 唯一命中总计：{self.total_unique}",
            f"## 逐轮曲线\n{rows}",
            "## 说明\n" + ("\n".join(f"- {n}" for n in self.notes) or "- （无）"),
        ])


def evaluate(*, paper_id: str, layout: Layout, query: str,
             databases: list[str] | None = None,
             max_rounds: int = MAX_ROUNDS_DEFAULT,
             min_new_per_round: int = MIN_NEW_DEFAULT,
             limit: int = 25) -> dict:
    """逐轮检索，输出发现曲线与停止判据。"""
    r = DiscoveryRun(
        ok=False, paper_id=paper_id, query=query,
        min_new_per_round=max(1, int(min_new_per_round)),
    )
    if not (query or "").strip():
        r.error = "query 为空。"
        return r.to_dict()

    import os

    r.offline = os.environ.get("SCI_FORGE_OFFLINE") == "1"

    seen: dict[str, dict] = {}
    low_streak = 0
    for rnd in range(1, max(1, int(max_rounds)) + 1):
        hits = _norm(_search(query, databases, limit))
        new = [h for h in hits if h["id"] not in seen]
        for h in new:
            seen[h["id"]] = h
        r.rounds = rnd
        r.curve.append({"round": rnd, "new": len(new), "cumulative": len(seen)})
        r.new_per_round.append(len(new))
        if len(new) < r.min_new_per_round:
            low_streak += 1
        else:
            low_streak = 0
        if low_streak >= 2:
            r.stop_reason = "plateau"
            r.notes.append(f"连续 {low_streak} 轮新增低于 "
                           f"{r.min_new_per_round}，判定检索饱和。")
            break
    else:
        r.stop_reason = "max_rounds"
        r.notes.append(f"达到轮数上限 {max_rounds}；曲线仍在上升时可提高上限。")

    r.total_unique = len(seen)
    if r.offline:
        r.notes.append("离线模式：检索后端返回空，曲线反映的是离线降级结果，"
                       "不能作为真实检索饱和证据。")
    r.notes.append("停止判据为 heuristics；正式系统综述应另按 PRISMA 文档化检索过程。")

    _persist(layout, paper_id, r)
    r.ok = True
    return r.to_dict()


def _persist(layout: Layout, paper_id: str, r: DiscoveryRun) -> None:
    root: Path = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "discovery_curve.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "discovery_curve.md").write_text(r.to_markdown(), encoding="utf-8")
