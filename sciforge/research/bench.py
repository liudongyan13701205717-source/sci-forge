"""对比表与显著性检验（bench）：汇总多次任务/基线指标，产出论文可用对比表。

读取各 tasks/{id}/results.json 的指标序列（metrics 为 tag/value 列表），
按 tag 分组得到样本序列；对每个 tag 输出均值±std，
并针对基线做 Welch t 检验与 Mann-Whitney U 检验。纯标准库。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

from sciforge.core import Layout
from sciforge.research import stats

_ALPHA = 0.05


def _lower_is_better(tag: str) -> bool:
    t = tag.lower()
    return any(k in t for k in ("loss", "error", "mse", "mae", "rmse"))


@dataclass
class BenchResult:
    ok: bool
    paper_id: str = ""
    metric_rows: list = field(default_factory=list)
    tests: list = field(default_factory=list)
    errors: list = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "ok": self.ok, "paper_id": self.paper_id,
            "metric_rows": self.metric_rows, "tests": self.tests,
            "errors": self.errors, "error": self.error,
        }

    def to_markdown(self) -> str:
        parts = [f"# 对比表：{self.paper_id}"]
        if not self.metric_rows:
            parts.append("\n（无可用指标，无法生成对比表）")
        else:
            tasks = [r["task"] for r in self.metric_rows]
            tags = []
            for r in self.metric_rows:
                for i in r["items"]:
                    if i["tag"] not in tags:
                        tags.append(i["tag"])
            head = ["指标"] + tasks
            parts.append("\n| " + " | ".join(head) + " |")
            parts.append("|" + "---|" * len(head))
            for tag in tags:
                cells = [tag]
                for r in self.metric_rows:
                    cells.append(_cell(r, tag))
                parts.append("| " + " | ".join(cells) + " |")
        if self.tests:
            parts.append("\n## 显著性检验（对照组：" + (self.tests[0].get("baseline") or "-") + ")")
            for item in self.tests:
                tag = item["tag"]
                e = item["else_group"]
                base = item["baseline_group"]
                g = _sig_cell(item)
                parts.append(
                    f"- `{tag}`：{e} vs {base} → {g}"
                )
        return "\n".join(parts)


def _cell(row: dict, tag: str) -> str:
    for it in row["items"]:
        if it["tag"] == tag:
            return f"{it['mean']:.3f}±{it['std']:.3f} (n={it['n']})"
    return "—"


def _sig_cell(item: dict) -> str:
    t = item["t_test"]
    m = item["mann_whitney"]
    parts = []
    if isinstance(t, dict) and t.get("p") is not None and math_isfinite(t.get("p")):
        parts.append(f"t={t['t']:.3f} p={t['p']:.4f} {'显著' if t['different'] else '不显著'}")
    if isinstance(m, dict) and m.get("p") is not None and math_isfinite(m.get("p")):
        parts.append(f"U={m['u1']:.1f} p={m['p']:.4f} {'显著' if m['different'] else '不显著'}")
    return "; ".join(parts) if parts else "样本不足"


def math_isfinite(v) -> bool:
    import math

    return isinstance(v, (int, float)) and math.isfinite(v)


def _read_metrics(task_root) -> dict:
    """返回 {tag: [values]}。调用方已确保目录存在。"""
    p = task_root / "results.json"
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    out: dict[str, list] = {}
    for m in data.get("metrics", []) or []:
        tag = (m.get("tag") or m.get("name") or "").strip()
        v = m.get("value")
        if not tag or v is None:
            continue
        try:
            v = float(v)
        except (TypeError, ValueError):
            continue
        out.setdefault(tag, []).append(v)
    return out


def compare_metrics(
    *,
    paper_id: str,
    task_ids: list[str],
    layout: Layout,
    baseline: str = "",
    metric: str = "",
) -> BenchResult:
    """对比表：聚合多个 task 的指标并做显著性检验。"""
    r = BenchResult(ok=False, paper_id=paper_id)
    if not task_ids:
        r.error = "请提供至少一个 task_id。"
        return r
    rows: list[dict] = []
    baseline_key = baseline or (task_ids[0] if len(task_ids) > 1 else "")
    for tid in task_ids:
        task_root = layout.task_dir(tid)
        series = _read_metrics(task_root)
        if not series:
            r.errors.append(f"任务 {tid} 没有可用指标。")
            continue
        items = []
        for tag, vals in series.items():
            vals = [v for v in vals if v is not None]
            if not vals:
                continue
            items.append({
                "tag": tag, "mean": stats.mean(vals),
                "std": stats.stddev(vals) if len(vals) > 1 else 0.0,
                "n": len(vals), "lower_better": _lower_is_better(tag),
            })
        if items:
            rows.append({"task": tid, "items": items,
                         "all_tags": sorted(set(i["tag"] for i in items))})
    if metric:
        for row in rows:
            row["items"] = [i for i in row["items"] if metric.lower() in i["tag"].lower()]
            row["all_tags"] = sorted(set(i["tag"] for i in row["items"]))
    rows = [row for row in rows if row["items"]]
    r.metric_rows = rows
    if not rows:
        r.error = "没有可对比的指标序列。"
        return r
    r.ok = True

    # 显著性：逐个非基线 task vs baseline
    tests = []
    base_row = next((row for row in rows if row["task"] == baseline_key), None)
    if base_row is None and len(rows) >= 2:
        base_row = rows[0]
    if base_row is not None:
        base_tags = {i["tag"]: i for i in base_row["items"]}
        for row in rows:
            if row["task"] == base_row["task"]:
                continue
            for item in row["items"]:
                if item["tag"] not in base_tags:
                    continue
                x = _raw_series(task_ids, row["task"], item["tag"], layout)
                y = _raw_series(task_ids, base_row["task"], item["tag"], layout)
                if len(x) < 2 or len(y) < 2:
                    continue
                t = stats.welch_t(x, y)
                m = stats.mann_whitney_u(x, y)
                tests.append({
                    "tag": item["tag"],
                    "else_group": row["task"],
                    "baseline_group": base_row["task"],
                    "t_test": _round_dict(t),
                    "mann_whitney": _round_dict(m),
                    "direction": "lower_better" if item["lower_better"] else "higher_better",
                })
    r.tests = tests
    _persist(layout, paper_id, r)
    return r


def _raw_series(task_ids: list[str], tid: str, tag: str, layout: Layout) -> list[float]:
    series = _read_metrics(layout.task_dir(tid))
    return [v for v in series.get(tag, []) if v is not None]


def _round_dict(d: dict) -> dict:
    out = {}
    for k, v in d.items():
        if k == "p":
            out[k] = round(v, 9) if isinstance(v, float) else v
        elif isinstance(v, float):
            out[k] = round(v, 6)
        elif isinstance(v, dict):
            out[k] = _round_dict(v)
        else:
            out[k] = v
    return out


def _persist(layout: Layout, paper_id: str, r: BenchResult):
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "benchmark_compare.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "benchmark_compare.md").write_text(r.to_markdown(), encoding="utf-8")