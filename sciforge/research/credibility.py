"""引文可信度 / 可靠性评分（backlog #20）。

对一组文献打分（0-100），把多个**可解释信号**合成为单一排序依据：
  - 载体质量（顶会/顶刊白名单、DOI 注册状态）
  - 社区复核度（被引量、跨年引用）
  - 撤稿/更正历史（复用 retraction 模块）
  - 记录完备性（题名/年份/作者/DOI 是否齐全）

分数随 breakdown 一起返回，规则本身可审计；不同权重视为显式常量，
不做玄学「AI 可信度」断言。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

from sciforge.core import Layout

# 载体白名单：公认顶刊/顶会（只作分级信号，不构成学术评价）
TOP_VENUES = {
    "nature": 20, "science": 20, "cell": 20, "pnas": 18,
    "proceedings of the national academy of sciences": 18,
    "nips": 18, "neurips": 18, "neural information processing systems": 18,
    "icml": 16, "international conference on machine learning": 16,
    "iclr": 16, "international conference on learning representations": 16,
    "cvpr": 14, "iccv": 14, "eccv": 14, "acl": 14, "emnlp": 14,
    "aaai": 12, "ijcai": 12, "kdd": 12, "sigir": 12, "www": 12,
    "sigmod": 12, "vldb": 12, "osdi": 12, "sosp": 12,
    "lancet": 20, "new england journal of medicine": 20, "jama": 18,
    "the journal of the american medical association": 18,
    "jmlr": 14, "journal of machine learning research": 14,
    "ieee transactions on pattern analysis and machine intelligence": 16,
    "journal of the acm": 16, "communications of the acm": 14,
    "physical review letters": 16, "physical review x": 16,
}

WEIGHTS = {
    "venue": 30,
    "cited": 25,
    "integrity": 25,
    "completeness": 20,
}


@dataclass
class CredibilityItem:
    title: str = ""
    doi: str = ""
    venue: str = ""
    cited_by: int = 0
    year: int = 0
    status: str = "unknown"      # clean | corrected | retracted | unknown
    score: int = 0
    breakdown: list = field(default_factory=list)
    tier: str = "C"

    def to_dict(self) -> dict:
        return {
            "title": self.title, "doi": self.doi, "venue": self.venue,
            "cited_by": self.cited_by, "year": self.year, "status": self.status,
            "score": self.score, "breakdown": self.breakdown, "tier": self.tier,
        }


@dataclass
class CredibilityReport:
    ok: bool
    paper_id: str = ""
    items: list = field(default_factory=list)
    ranked: list = field(default_factory=list)
    mean_score: int = 0
    notes: list = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "ok": self.ok, "paper_id": self.paper_id, "items": self.items,
            "ranked": self.ranked, "mean_score": self.mean_score,
            "notes": self.notes, "error": self.error,
        }

    def to_markdown(self) -> str:
        rows = []
        for i, it in enumerate(self.ranked, 1):
            rows.append(f"{i}. **{it['score']}**（{it['tier']}） {it['title'] or it['doi']}"
                        f" — {it['venue']}，被引 {it['cited_by']}")
        return "\n\n".join([
            f"# 引文可信度评分：{self.paper_id}",
            f"## 结论\n平均 {self.mean_score} 分（0-100），"
            f"共 {len(self.items)} 条。",
            f"## 排序\n" + ("\n".join(rows) or "- （无）"),
            "## 说明\n" + ("\n".join(f"- {n}" for n in self.notes) or "- （无）"),
        ])


def _venue_points(venue: str, breakdown: list) -> int:
    if not venue:
        breakdown.append("载体未知：0/{}".format(WEIGHTS["venue"]))
        return 0
    low = venue.lower()
    for key, pts in TOP_VENUES.items():
        if key in low:
            breakdown.append(f"载体白名单命中（{key}）：{pts}/{WEIGHTS['venue']}")
            return min(WEIGHTS["venue"], pts)
    breakdown.append(f"非白名单载体（{venue[:40]}）：{WEIGHTS['venue'] // 4}/{WEIGHTS['venue']}")
    return WEIGHTS["venue"] // 4


def _cited_points(cited: int, breakdown: list) -> int:
    cap = WEIGHTS["cited"]
    if cited <= 0:
        breakdown.append(f"无被引记录：0/{cap}")
        return 0
    # 对数标度：10 次=一半，1000 次=满分
    import math

    v = cap * min(1.0, math.log10(cited + 1) / 3.0)
    breakdown.append(f"被引 {cited}（log10 标度）：{int(v)}/{cap}")
    return int(v)


def _integrity_points(status: str, breakdown: list) -> int:
    cap = WEIGHTS["integrity"]
    table = {
        "clean": cap,
        "unknown": int(cap * 0.5),
        "corrected": int(cap * 0.4),
        "retracted": 0,
    }
    v = table.get(status, int(cap * 0.5))
    label = {"clean": "无撤稿/更正记录", "unknown": "诚信状态未知",
             "corrected": "有更正/勘误记录", "retracted": "已撤稿"}.get(status, status)
    breakdown.append(f"诚信信号 {label}：{v}/{cap}")
    return v


def _completeness_points(rec: dict, breakdown: list) -> int:
    cap = WEIGHTS["completeness"]
    keys = ("title", "year", "authors", "doi", "venue")
    have = [k for k in keys if str(rec.get(k) or "").strip()]
    v = int(cap * len(have) / len(keys))
    breakdown.append(f"字段完备 {len(have)}/{len(keys)}（{'/'.join(have) or '无'}）：{v}/{cap}")
    return v


def score_works(*, paper_id: str, layout: Layout, records,
                retraction_index: dict | None = None) -> dict:
    """给一组文献打可信度分并排序。"""
    r = CredibilityReport(ok=False, paper_id=paper_id)
    recs = []
    for rec in records or []:
        if isinstance(rec, str):
            recs.append({"title": rec})
        elif isinstance(rec, dict):
            recs.append(dict(rec))
    if not recs:
        r.error = "records 为空。"
        return r.to_dict()

    idx = retraction_index or {}
    for rec in recs:
        it = CredibilityItem(
            title=str(rec.get("title") or ""),
            doi=str(rec.get("doi") or ""),
            venue=str(rec.get("venue") or ""),
            cited_by=int(rec.get("cited_by") or 0),
            year=int(rec.get("year") or 0),
        )
        key = (it.doi or it.title[:40]).strip().lower()
        it.status = str(idx.get(key, rec.get("status") or "unknown")).lower()
        bd: list = []
        it.score = (_venue_points(it.venue, bd) + _cited_points(it.cited_by, bd)
                    + _integrity_points(it.status, bd)
                    + _completeness_points(rec, bd))
        it.breakdown = bd
        it.tier = "A" if it.score >= 80 else ("B" if it.score >= 55 else "C")
        r.items.append(it.to_dict())

    r.ranked = sorted(r.items, key=lambda x: x["score"], reverse=True)
    r.mean_score = int(sum(x["score"] for x in r.items) / len(r.items))
    r.notes.append("评分为多信号加权（venue/cited/integrity/completeness），"
                   "规则见每项 breakdown，可复算。")
    r.notes.append("载体白名单仅作分级信号，不构成对单篇论文学术价值的判定。")
    if not retraction_index:
        r.notes.append("未提供 retraction_index，诚信信号按 unknown 计（半权）。")

    r.ok = True
    _persist(layout, paper_id, r)
    return r.to_dict()


def _persist(layout: Layout, paper_id: str, r: CredibilityReport) -> None:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "credibility.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "credibility.md").write_text(r.to_markdown(), encoding="utf-8")
