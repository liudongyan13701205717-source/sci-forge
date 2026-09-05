"""复现五步闭环编排：解析→方案→代码生成→沙箱执行(自愈)→交付。

自愈迭代：运行失败(报错/超时/白名单)时，收集错误，重新生成并重跑，
受 MaxAttempts 约束；失败如实记录于 results，绝不虚报成功。
"""

from __future__ import annotations

import json
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional

from sciforge.parse.pdf import parse_pdf
from sciforge.reproduce import codegen, harness
from sciforge.reproduce.tasks import Task

MAX_ATTEMPTS = 3
RUN_TIMEOUT = 180.0


@dataclass
class StepResult:
    step: int
    name: str
    ok: bool
    detail: dict = field(default_factory=dict)
    error: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "step": self.step,
            "name": self.name,
            "ok": self.ok,
            "detail": self.detail,
            "error": self.error,
        }


def _task_paths(task: Task, layout) -> dict:
    """任务目录内的关键文件路径。"""
    d = layout.task_dir(task.task_id)
    return {
        "dir": d,
        "parse": d / "parse.json",
        "plan": d / "plan.json",
        "code": d / "generated.py",
        "code_log": d / "codegen.json",
        "results": d / "results.json",
        "runs": d / "runs",
        "deliverables": d / "deliverables",
    }


def _write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def run_pipeline(
    task: Task,
    layout,
    *,
    llm_fn: Optional[Callable] = None,
    on_progress: Optional[Callable[[str], None]] = None,
) -> dict:
    """执行完整五步闭环，返回 {steps, result_summary}。"""
    paths = _task_paths(task, layout)
    paths["runs"].mkdir(parents=True, exist_ok=True)
    steps: list[StepResult] = []

    # 1) 解析
    task.set_stage("parsing", "解析 PDF")
    try:
        pr = parse_pdf(task.pdf_path)
        prd = pr.to_json()
        _write_json(paths["parse"], prd)
        task.parse_path = str(paths["parse"])
        steps.append(StepResult(1, "解析", True,
                                {"title": prd.get("title", ""), "pages": prd.get("num_pages"),
                                 "sections": len(prd.get("sections", [])),
                                 "figures": len(prd.get("figures", [])),
                                 "tables": len(prd.get("tables", []))}))
    except Exception as e:  # noqa: BLE001
        steps.append(StepResult(1, "解析", False, error=f"{e}"))
        return _finalize(task, layout, steps, failed_reason=f"解析失败：{e}")

    # 2) 复现方案（启发式；LLM 可用时补充，本阶段先启发式）
    task.set_stage("planning", "生成复现方案")
    hypers = codegen._extract_hypers(prd)
    plan = {
        "title": prd.get("title", ""),
        "framework": task.framework,
        "structure": [s["title"] for s in prd.get("sections", [])],
        "figures": prd.get("figures", []),
        "tables": prd.get("tables", []),
        "inferred_hyperparams": hypers,
        "notes": "基于解析产物的启发式复现方案；缺失参数标注为未知。",
    }
    _write_json(paths["plan"], plan)
    task.plan_path = str(paths["plan"])
    steps.append(StepResult(2, "方案", True,
                            {"hyperparams": hypers, "sections": len(plan["structure"])}))

    # 3+4) 代码生成 + 自愈执行
    code, code_log = None, {}
    last_err = ""
    codegen_done = False
    for attempt in range(1, MAX_ATTEMPTS + 1):
        task.set_stage("codegen", f"代码生成第 {attempt} 次")
        try:
            code, code_log = codegen.generate_code(
                prd, plan, framework=task.framework, llm_fn=llm_fn
            )
            _write_json(paths["code_log"], code_log)
            paths["code"].write_text(code, encoding="utf-8")
            task.code_path = str(paths["code"])
            if not codegen_done:
                steps.append(StepResult(3, "代码生成", True,
                                        {"generator": code_log.get("generator"),
                                         "hyperparams": hypers,
                                         "attempt": attempt}))
                codegen_done = True
        except Exception as e:  # noqa: BLE001
            steps.append(StepResult(3, "代码生成", False, error=f"生成失败：{e}"))
            return _finalize(task, layout, steps, failed_reason=f"代码生成失败：{e}")

        # 运行
        task.set_stage("running", f"沙箱执行第 {attempt} 次")
        run_dir = paths["runs"] / f"attempt_{attempt}"
        run_dir.mkdir(parents=True, exist_ok=True)
        res = harness.execute(code, run_dir, timeout=RUN_TIMEOUT, allow_frozen=True)

        if res.ok:
            # 4) 执行成功 → 写结果
            _write_harness_results(paths["results"], res, code_log, prd)
            task.results_path = str(paths["results"])
            steps.append(StepResult(4, "执行", True,
                                    {"metrics": [m.__dict__ for m in res.metrics],
                                     "plots": res.plots,
                                     "generator": code_log.get("generator")}))
            break
        else:
            last_err = res.error or (res.stderr[-600:] if res.stderr else "未知错误")
            steps.append(StepResult(4, "执行", False,
                                    error=f"第 {attempt} 次失败：{last_err}",
                                    detail={"timed_out": res.timed_out,
                                            "whitelist": ("非白名单" in (res.error or ""))}))
            if attempt == MAX_ATTEMPTS:
                _write_json(paths["results"], {
                    "ok": False,
                    "error": f"自愈重试 {MAX_ATTEMPTS} 次后仍失败：{last_err}",
                    "generator": code_log.get("generator"),
                    "metrics": [],
                    "plots": [],
                })
                task.results_path = str(paths["results"])
            # 自愈提示：模板回退时禁用 LLM，避免再次失败（若上轮是 LLM）
            llm_fn = None

    # 5) 交付物
    task.set_stage("done", "生成交付物")
    deliv = _collect_deliverables(task, layout, paths, steps)
    task.deliverables_dir = str(paths["deliverables"])
    steps.append(StepResult(5, "交付", True, {"count": len(deliv), "items": deliv}))

    task.set_stage("done", "复现闭环完成")
    return _finalize(task, layout, steps)


def _write_harness_results(results_path: Path, res: harness.HarnessResult,
                           code_log: dict, prd: dict) -> None:
    obj = {
        "ok": True,
        "metrics": [m.__dict__ for m in res.metrics],
        "plots": res.plots,
        "generator": code_log.get("generator"),
        "framework": code_log.get("framework"),
        "timed_out": res.timed_out,
        "stopped_early": res.stopped_early,
        "reason": res.reason,
        "paper_title": prd.get("title", ""),
    }
    _write_json(results_path, obj)


def _collect_deliverables(task: Task, layout, paths: dict, steps) -> list[dict]:
    """将 runs 中的图、生成的代码、结果汇总到 deliverables/。"""
    out_dir = paths["deliverables"]
    out_dir.mkdir(parents=True, exist_ok=True)
    items: list[dict] = []

    # 源码（最近一次成功/最后）
    code_file = paths["code"]
    if code_file.exists():
        dst = out_dir / "reproduce_source.py"
        dst.write_text(code_file.read_text(encoding="utf-8"), encoding="utf-8")
        items.append({"kind": "source", "name": dst.name, "path": str(dst)})

    # 图：收集所有 runs 下 png
    run_root = paths["runs"]
    for png in sorted(run_root.glob("*/convergence.png")) + sorted(run_root.glob("*.png")):
        dst = out_dir / f"plot_{png.parent.name}_{png.name}" if png.parent != run_root \
            else out_dir / png.name
        try:
            dst.write_bytes(png.read_bytes())
            items.append({"kind": "figure", "name": dst.name, "path": str(dst)})
        except OSError:
            pass

    # 结果
    rp = paths["results"]
    if rp.exists():
        items.append({"kind": "data", "name": rp.name, "path": str(rp)})

    # 简report
    report = _write_report(task, out_dir, steps, rp)
    items.append({"kind": "report", "name": report.name, "path": str(report)})

    # 去重（同名）
    seen, uniq = set(), []
    for it in items:
        if it["path"] not in seen:
            seen.add(it["path"])
            uniq.append(it)
    return uniq


def _write_report(task: Task, out_dir: Path, steps, results_path: Path) -> Path:
    lines = [
        "# 复现报告",
        "",
        f"- 任务: `{task.task_id}`",
        f"- PDF: `{task.pdf_path}`",
        f"- 框架: {task.framework}",
        "",
        "## 步骤",
        "",
    ]
    for s in steps:
        lines.append(f"- [{('OK' if s.ok else 'FAIL')}] 步骤{s.step} {s.name}"
                     + (f" — {s.error}" if s.error else ""))
    lines.append("")
    if results_path.exists():
        rj = json.loads(results_path.read_text(encoding="utf-8"))
        lines.append("## 指标")
        lines.append("")
        for m in rj.get("metrics", []):
            lines.append(f"- `{m['tag']}` = {m['value']} (conf={m.get('conf')})")
        lines.append("")
        lines.append("## 图")
        lines.append("")
        for p in rj.get("plots", []):
            lines.append(f"- {p}")
    report = out_dir / "REPORT.md"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def _finalize(task: Task, layout, steps, failed_reason: Optional[str] = None) -> dict:
    if failed_reason:
        task.set_stage("failed", failed_reason)
        task.error = failed_reason
    return {
        "task_id": task.task_id,
        "status": task.status,
        "stage": task.stage,
        "message": task.message,
        "steps": [s.to_dict() for s in steps],
        "deliverables_dir": task.deliverables_dir,
    }
