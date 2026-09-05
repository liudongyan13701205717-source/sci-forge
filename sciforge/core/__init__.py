"""共享基础设施：项目布局、存储路径、模型连接层。

存储布局（在工作区根下）：
    .sci-forge/
        env                  # 本地配置（含 LLM 端点），不提交
        projects/{paper_id}/ # 写作项目（doc.md, doc.tex, 导出物）
        tasks/{task_id}/     # 复现/交付任务（parse/, code/, runs/, deliverables/）
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def workspace_root() -> Path:
    """工作区根：当前工作目录（opencode 的 cwd 为仓库根）。"""
    return Path(os.getcwd()).resolve()


@dataclass
class Layout:
    root: Path

    @property
    def data_dir(self) -> Path:
        return self.root / ".sci-forge"

    @property
    def projects_dir(self) -> Path:
        return self.data_dir / "projects"

    @property
    def tasks_dir(self) -> Path:
        return self.data_dir / "tasks"

    def ensure(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.projects_dir.mkdir(parents=True, exist_ok=True)
        self.tasks_dir.mkdir(parents=True, exist_ok=True)

    def project_dir(self, paper_id: str) -> Path:
        d = self.projects_dir / _safe(paper_id)
        d.mkdir(parents=True, exist_ok=True)
        return d

    def task_dir(self, task_id: str) -> Path:
        d = self.tasks_dir / _safe(task_id)
        d.mkdir(parents=True, exist_ok=True)
        return d


def _safe(name: str) -> str:
    """清洗路径段，防止路径穿越。"""
    return clean_segment(name)


def clean_segment(name: str) -> str:
    """公开的路径段清洗：非字母数字/`-_.` 统一替换为 `_`。"""
    cleaned = "".join(c if (c.isalnum() or c in "-_.") else "_" for c in name)
    cleaned = cleaned.strip(" .")
    return cleaned or "untitled"


def get_layout() -> Layout:
    return Layout(workspace_root())
