"""实验数据并入论文：把复现任务的真实产物注入写作线章节。

对齐 Phase E(实验执行) → Phase G(论文写作)：读取
  tasks/{tid}/results.json   -- 真实指标
  tasks/{tid}/deliverables/*.png -- 图
  tasks/{tid}/parse.json     -- 原文标题/结构
  tasks/{tid}/plan.json      -- 超参/方案
把它转成写作线 results 章节的真实 markdown（数字/表格/图引用），
写入 DocStore（paper_id 关联），实现"实验数据直接进论文"。
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from sciforge.core import Layout
from sciforge.write.doc import DocStore

# 复现产物路径常量（与 reproduce/pipeline._task_paths 对齐）
_RESULTS = "results.json"
_PARSE = "parse.json"
_PLAN = "plan.json"
_DELIV = "deliverables"


class InjectError(Exception):
    pass


def _load(root: Path, name: str) -> dict:
    p = root / name
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _find_plots(root: Path) -> list[Path]:
    out = []
    for pat in ("*.png", "deliverables/*.png"):
        out += sorted(root.glob(pat))
    # 去重（同一文件不同路径）
    seen = set()
    uniq = []
    for p in out:
        k = p.name
        if k in seen:
            continue
        seen.add(k)
        uniq.append(p)
    return uniq


def build_results_markdown(task_root: Path, *, images_dir: str | None = None) -> str:
    """由复现产物生成 results 章节 markdown。无产物即返回空。"""
    data = _load(task_root, _RESULTS)
    metrics = data.get("metrics", [])
    parse = _load(task_root, _PARSE)
    plan = _load(task_root, _PLAN)

    lines: list[str] = []
    title = data.get("paper_title") or parse.get("title") or "本研究"
    lines.append(f"针对原论文《{title}》，我们在本地沙箱完成了复现实验，结果如下。")

    # 指标表
    real_metrics = [m for m in metrics if m.get("ptype", "real") == "real"]
    if metrics:
        lines.append("")
        lines.append("| 指标 | 值 | 类型 | 可信 |")
        lines.append("| --- | --- | --- | --- |")
        for m in metrics:
            val = m.get("value")
            try:
                val = f"{float(val):.4f}"
            except (TypeError, ValueError):
                val = str(val)
            lines.append(
                f"| {m.get('tag','')} | {val} | {m.get('ptype','real')} | "
                f"{'是' if m.get('conf', True) else '否'} |"
            )
        lines.append("")
        lines.append("> 指标来源：沙箱内生成代码实际运行上报（防伪校验已启用）。")

    # 图
    plots = data.get("plots", [])
    if plots or _find_plots(task_root):
        lines.append("")
        lines.append("### 收敛曲线")
        for pl in plots:
            fname = Path(pl).name
            lines.append(f"![{fname}]({images_dir or ''}{fname})" if images_dir is not None
                         else f"- 图：`{fname}`")
        lines.append("")

    # 超参与设置
    hyp = plan.get("inferred_hyperparams") or {}
    if hyp:
        lines.append("")
        lines.append("### 复现设置（推断超参）")
        for k, v in hypotized(hyp).items():
            lines.append(f"- `{k}` = {v}")

    if not metrics and not plots and not hyp:
        return ""
    return "\n".join(lines).strip()


def hypotized(hyp) -> dict:
    if isinstance(hyp, dict):
        return hyp
    return {}


def inject_results(
    *,
    layout: Layout,
    paper_id: str,
    task_id: str,
    section: str = "results",
) -> dict:
    """把复现任务 task_id 的产物注入 paper_id 的 results/experiments 章节。"""
    task_root = layout.task_dir(task_id)
    results_md = build_results_markdown(task_root, images_dir=f"{task_id}/deliverables/")

    if task_id and not task_root.exists():
        try:
            task_root.mkdir(parents=True, exist_ok=True)
        except OSError:
            pass

    if not results_md:
        raise InjectError(
            f"任务 {task_id} 无可用复现结果（results.json/metrics 为空）。"
            "请先完成复现闭环。"
        )

    store = DocStore(layout, paper_id)
    if section not in ("results", "experiments"):
        raise InjectError(f"不支持的注入章节：{section}（可选 results/experiments）")

    existing = store.read_section(section) or ""
    combined = existing.strip() + "\n\n" + results_md if existing.strip() else results_md
    store.write_section(section, combined.strip(), fmt="markdown")

    return {
        "ok": True,
        "paper_id": paper_id,
        "task_id": task_id,
        "section": section,
        "markdown": results_md,
        "metrics_count": _load(task_root, _RESULTS).get("metrics", []).__len__(),
    }
