"""系统综述的双盲独立筛选与冲突裁决（backlog #9，Rayyan/Covidence 对等能力）。

两个（或多个）筛选人各自独立对同一批文献给出 include/exclude 决定，
本模块计算：
  - 单人判定的分布
  - 两两间一致性（Cohen's Kappa，含 0 判例的安全处理）
  - 冲突清单（决定不同的文献）
  - 裁决（第三方决定，或 majority 多数决）

冲突裁决**只返回结构，不自行决定纳入**——终裁交回人类或由调用方传入
adjudications，这符合系统综述对人工判断的要求。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

from sciforge.core import Layout

VALID = ("include", "exclude", "maybe")


def _norm_decision(v) -> str:
    s = str(v or "").strip().lower()
    if s in ("in", "include", "i", "yes", "y", "1"):
        return "include"
    if s in ("out", "exclude", "e", "no", "n", "0"):
        return "exclude"
    return "maybe"


def cohens_kappa(a: list[str], b: list[str]) -> float:
    """两名判定者的 Cohen's Kappa；单类别或空输入返回 0.0（不做误导性高值）。"""
    if len(a) != len(b) or not a:
        return 0.0
    n = len(a)
    observed = sum(1 for x, y in zip(a, b) if x == y) / n
    cats = set(a) | set(b)
    if len(cats) < 2:
        return 0.0
    expected = 0.0
    for c in cats:
        pa = sum(1 for x in a if x == c) / n
        pb = sum(1 for y in b if y == c) / n
        expected += pa * pb
    if expected >= 1.0:
        return 0.0
    return (observed - expected) / (1.0 - expected)


def _agreement_label(k: float) -> str:
    if k >= 0.81:
        return "almost_perfect"
    if k >= 0.61:
        return "substantial"
    if k >= 0.41:
        return "moderate"
    if k >= 0.21:
        return "fair"
    if k > 0:
        return "slight"
    return "none"


@dataclass
class ScreeningReport:
    ok: bool
    paper_id: str = ""
    reviewers: list = field(default_factory=list)
    n_items: int = 0
    distributions: dict = field(default_factory=dict)
    pairwise: list = field(default_factory=list)
    conflicts: list = field(default_factory=list)
    majority: list = field(default_factory=list)
    kappa_overall: float = 0.0
    agreement: str = ""
    notes: list = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "ok": self.ok, "paper_id": self.paper_id, "reviewers": self.reviewers,
            "n_items": self.n_items, "distributions": self.distributions,
            "pairwise": self.pairwise, "conflicts": self.conflicts,
            "majority": self.majority,
            "kappa_overall": round(self.kappa_overall, 4),
            "agreement": self.agreement, "notes": self.notes, "error": self.error,
        }

    def to_markdown(self) -> str:
        rows = "\n".join(
            f"- {c['id']}：{c['decisions']} → {c['resolution']}"
            for c in self.conflicts
        ) or "- （无冲突）"
        pw = "\n".join(
            f"- {p['a']} vs {p['b']}：κ={p['kappa']}（{p['agreement']}）"
            for p in self.pairwise
        ) or "- （单人筛选）"
        return "\n\n".join([
            f"# 双盲筛选与冲突裁决：{self.paper_id}",
            f"## 结论\n条目 {self.n_items} | 筛选人 {len(self.reviewers)} | "
            f"冲突 {len(self.conflicts)} | 总体 κ={self.kappa_overall:.3f}"
            f"（{self.agreement or 'n/a'}）",
            f"## 两两一致性\n{pw}",
            f"## 冲突清单\n{rows}",
            "## 说明\n" + ("\n".join(f"- {n}" for n in self.notes) or "- （无）"),
        ])


def screen(*, paper_id: str, layout: Layout, records,
           reviewer_names: list[str] | None = None,
           adjudications: dict | None = None) -> dict:
    """多筛选人盲筛 + κ 一致性 + 冲突裁决。

    records: [{"id":..., "title":..., "decisions": [r1, r2, ...]}]
    或 {"id","title","r1","r2"} 形式（自动折为 decisions）。
    adjudications: {"<id>": "include"|"exclude"} 终裁。
    """
    r = ScreeningReport(ok=False, paper_id=paper_id)
    items = []
    for i, rec in enumerate(records or []):
        if not isinstance(rec, dict):
            continue
        d = rec.get("decisions")
        if d is None:
            d = [rec.get(k) for k in rec.keys()
                 if str(k).lower() not in ("id", "title", "doi", "abstract", "decisions")]
        dec = [_norm_decision(x) for x in d if x is not None and str(x).strip()]
        items.append({
            "id": str(rec.get("id") or f"item-{i}"),
            "title": str(rec.get("title") or ""),
            "decisions": dec,
        })
    if not items:
        r.error = "records 为空或格式不正确（需含 decisions 列表）。"
        return r.to_dict()

    n_rev = max(len(it["decisions"]) for it in items)
    r.reviewers = [str(x) for x in (reviewer_names or [f"r{i+1}" for i in range(n_rev)])][:n_rev]
    r.n_items = len(items)

    adj = {str(k): _norm_decision(v) for k, v in (adjudications or {}).items()}

    for it in items:
        dist = {"include": 0, "exclude": 0, "maybe": 0}
        for d in it["decisions"]:
            dist[d] += 1
        r.distributions[it["id"]] = dist
        distinct = {d for d in it["decisions"]}
        if len(distinct) > 1:
            resolution = adj.get(it["id"])
            if resolution:
                it["resolution"] = f"adjudicated:{resolution}"
                it["adjudicated"] = True
            else:
                it["resolution"] = "conflict:pending"
                it["adjudicated"] = False
            r.conflicts.append(it)
        else:
            only = it["decisions"][0] if it["decisions"] else "maybe"
            it["resolution"] = f"unanimous:{only}"
            it["adjudicated"] = False
            r.majority.append({"id": it["id"], "decision": only, "votes": it["decisions"]})

    # 两两 κ
    kappas = []
    for i in range(n_rev):
        for j in range(i + 1, n_rev):
            a = [it["decisions"][i] if i < len(it["decisions"]) else "maybe" for it in items]
            b = [it["decisions"][j] if j < len(it["decisions"]) else "maybe" for it in items]
            k = cohens_kappa(a, b)
            kappas.append(k)
            r.pairwise.append({
                "a": r.reviewers[i] if i < len(r.reviewers) else f"r{i+1}",
                "b": r.reviewers[j] if j < len(r.reviewers) else f"r{j+1}",
                "kappa": round(k, 4), "agreement": _agreement_label(k),
            })
    r.kappa_overall = sum(kappas) / len(kappas) if kappas else 0.0
    r.agreement = _agreement_label(r.kappa_overall)

    r.notes.append("κ 采用 Landis & Koch 分级标度；单类别判定会退化为 0.0（不做高值误导）。")
    r.notes.append("冲突默认保持 conflict:pending，终裁须由 adjudications 或人工给出。")
    if r.conflicts:
        r.notes.append(f"共 {len(r.conflicts)} 条待裁决；系统综述应在方法学部分报告 "
                       f"冲突数与裁决规则。")

    _persist(layout, paper_id, r)
    r.ok = True
    return r.to_dict()


def _persist(layout: Layout, paper_id: str, r: ScreeningReport) -> None:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "screening.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "screening.md").write_text(r.to_markdown(), encoding="utf-8")


def export_audit_log(*, paper_id: str, layout: Layout, records,
                     reviewer_names: list[str] | None = None,
                     adjudications: dict | None = None,
                     round_id: str = "") -> dict:
    """把一次盲筛压成**可导出的决定审计日志**（backlog #6）。

    输出条目级明细（谁、决定是什么、与谁冲突、如何终裁），可直接作为
    系统综述方法学附录。附带 markdown 便于人工阅读。
    """
    base = screen(paper_id=paper_id, layout=layout, records=records,
                  reviewer_names=reviewer_names, adjudications=adjudications)
    if not base.get("ok"):
        return {"ok": False, "error": base.get("error", "screen 失败"),
                "paper_id": paper_id}

    import time

    by_id = {}
    for it in (base.get("conflicts") or []):
        by_id[it["id"]] = it
    rows = []
    for dist_id, dist in (base.get("distributions") or {}).items():
        conflict = by_id.get(dist_id)
        rows.append({
            "id": dist_id,
            "reviewers": list(base.get("reviewers") or []),
            "distribution": dist,
            "conflict": bool(conflict),
            "resolution": conflict["resolution"] if conflict else "unanimous",
            "adjudicated": bool(conflict["adjudicated"]) if conflict else False,
        })

    ts = int(time.time())
    log = {
        "ok": True,
        "paper_id": paper_id,
        "round_id": round_id or f"round-{ts}",
        "logged_at": ts,
        "reviewers": list(base.get("reviewers") or []),
        "n_items": base.get("n_items"),
        "kappa_overall": base.get("kappa_overall"),
        "agreement": base.get("agreement"),
        "counts": {
            "unanimous": sum(1 for x in rows if not x["conflict"]),
            "conflicts": sum(1 for x in rows if x["conflict"]),
            "adjudicated": sum(1 for x in rows if x["adjudicated"]),
            "pending": sum(1 for x in rows if x["conflict"] and not x["adjudicated"]),
        },
        "decisions": rows,
    }

    lines = [
        f"# 盲筛决定审计日志：{paper_id}",
        f"- 轮次：{log['round_id']}",
        f"- 筛选人：{', '.join(log['reviewers']) or '（未命名）'}",
        f"- 条目：{log['n_items']} | 冲突 {log['counts']['conflicts']} | "
        f"已终裁 {log['counts']['adjudicated']} | 待裁决 {log['counts']['pending']}",
        f"- 总体 κ：{log['kappa_overall']}（{log['agreement'] or 'n/a'}）",
        "",
        "| id | include | exclude | maybe | 冲突 | 裁决 |",
        "|---|---|---|---|---|---|",
    ]
    for x in rows:
        d = x["distribution"]
        lines.append(
            f"| {x['id']} | {d.get('include', 0)} | {d.get('exclude', 0)} | "
            f"{d.get('maybe', 0)} | {'是' if x['conflict'] else '否'} | {x['resolution']} |"
        )
    log["markdown"] = "\n".join(lines)

    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "screening_audit.json").write_text(
        json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    (root / "screening_audit.md").write_text(log["markdown"] + "\n", encoding="utf-8")
    return log
