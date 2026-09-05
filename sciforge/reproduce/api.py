"""复现线 MCP 接口：异步启动任务 + 查询状态。

因为 MCP 是顺序请求/响应，无法长期阻塞单次调用，故：
- reproduce_paper：创建 Task，启动后台线程跑五步闭环，立即返回 task_id。
- reproduce_status：读取 task.json 返回阶段进度 + 最终结果摘要。
"""

from __future__ import annotations

import json
import threading
import traceback

from sciforge.core import get_layout
from sciforge.core import model
from sciforge.reproduce import pipeline
from sciforge.reproduce.tasks import Task, load_task, new_task, save_task


def _llm_fn():
    """返回可选的 LLM 代码生成函数；未配置则返回 None。"""
    if not model.configured():
        return None

    def _gen(hypers, parse, plan, framework):
        prompt = (
            "你是严谨的论文复现工程师。请为下面的论文生成可独立运行的复现代码，\n"
            "要求：\n"
            "1) 只能导入白名单模块：numpy/scipy/pandas/sklearn/matplotlib/torch(可选)/os等。\n"
            "2) 用 set_metric('name', value) 上报每个数值指标（真实计算结果），\n"
            "   禁止硬编码伪造指标值；loss 用 set_metric('train_loss', ...)\n"
            "3) 用 matplotlib 保存图到当前目录如 convergence.png。\n"
            "4) 数据用合成/可见数据，脚本必须可自跑、有确定性的随机种子。\n"
            f"框架: {framework}\n"
            f"论文结构: {json.dumps(plan.get('structure', []), ensure_ascii=False)}\n"
            f"推断超参: {json.dumps(hypers, ensure_ascii=False)}\n"
            "只输出 Python 代码，不要解释。\n"
        )
        from sciforge.core.model import chat
        return chat(prompt, temperature=0.2, max_tokens=4000)

    return _gen


def reproduce_paper(pdf_path: str, framework: str = "pytorch") -> dict:
    """创建复现任务并后台执行五步闭环。立即返回 task_id。"""
    task = new_task(pdf_path=pdf_path, framework=framework)
    save_task(task)

    def _bg():
        try:
            result = pipeline.run_pipeline(task, get_layout(), llm_fn=_llm_fn())
            # 将最终结果一并写回 task 供 status 读取
            task.results = result  # type: ignore[attr-defined]
            save_task(task)
        except Exception as e:  # noqa: BLE001
            task.set_stage("failed", f"内部错误：{e}")
            task.error = f"{e}\n{traceback.format_exc()}"
            save_task(task)

    t = threading.Thread(target=_bg, daemon=True)
    t.start()

    return {
        "ok": True,
        "task_id": task.task_id,
        "status": task.status,
        "message": "复现任务已创建，后台开始五步闭环。",
    }


def reproduce_status(task_id: str) -> dict:
    task = load_task(task_id)
    if task is None:
        return {"ok": False, "task_id": task_id, "error": f"任务不存在：{task_id}"}
    base = {
        "ok": True,
        "task_id": task.task_id,
        "status": task.status,
        "stage": task.stage,
        "message": task.message,
        "pdf_path": task.pdf_path,
        "framework": task.framework,
        "error": task.error,
        "deliverables_dir": task.deliverables_dir,
    }
    result = getattr(task, "results", None)
    if result:
        base["steps"] = result.get("steps", [])
    else:
        base["steps"] = []
    # 附带 results.json 摘要（若已生成）
    if task.results_path:
        try:
            base["result_summary"] = json.loads(
                __import__("pathlib").Path(task.results_path).read_text(encoding="utf-8")
            )
        except Exception:  # noqa: BLE001
            pass
    return base
