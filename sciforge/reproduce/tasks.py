"""复现任务状态机与持久化。

状态流转：
    created -> parsing -> planning -> codegen -> running -> done
                                                \\-> failed
                                                  \\-> (self-heal 内部循环，不暴露)
"""

from __future__ import annotations

import json
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Optional

from sciforge.core import get_layout

STAGES = ("created", "parsing", "planning", "codegen", "running", "done", "failed")


@dataclass
class Task:
    task_id: str
    pdf_path: str
    framework: str = "pytorch"
    status: str = "created"
    stage: Optional[str] = None
    message: str = ""
    error: Optional[str] = None
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)
    # 运行进度
    step: int = 0
    total_steps: int = 5
    # 产出引用锚点
    parse_path: Optional[str] = None
    plan_path: Optional[str] = None
    code_path: Optional[str] = None
    results_path: Optional[str] = None
    deliverables_dir: Optional[str] = None
    results: Optional[dict] = None  # 最终闭环结果（steps 等），由后台线程写入

    def touch(self) -> None:
        self.updated_at = time.time()

    def set_stage(self, stage: str, message: str = "") -> None:
        assert stage in STAGES, f"非法状态 {stage}"
        self.status = stage
        self.stage = stage
        if message:
            self.message = message
        self.touch()


def _task_file(layout, task_id: str) -> Path:
    return layout.task_dir(task_id) / "task.json"


def new_task(pdf_path: str, framework: str) -> Task:
    t = Task(task_id=uuid.uuid4().hex[:12], pdf_path=pdf_path, framework=framework)
    t.set_stage("created", "已创建")
    return t


def save_task(t: Task, layout=None) -> None:
    layout = layout or get_layout()
    layout.task_dir(t.task_id)
    _task_file(layout, t.task_id).write_text(
        json.dumps(asdict(t), ensure_ascii=False, indent=2), encoding="utf-8"
    )


def load_task(task_id: str, layout=None) -> Optional[Task]:
    layout = layout or get_layout()
    f = _task_file(layout, task_id)
    if not f.exists():
        return None
    data = json.loads(f.read_text(encoding="utf-8"))
    return Task(**{k: v for k, v in data.items() if k in Task.__dataclass_fields__})
