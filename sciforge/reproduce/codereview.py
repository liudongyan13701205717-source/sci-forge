"""复现代码静态点评（codereview）：对 tasks/{id}/ 下的 .py 生成可维护
但无批判性他造错误的风格与风险清单，支撑论文复现的代码质量声明。

纯静态规则 + 轻量模式匹配；无需运行代码/网络。
"""

from __future__ import annotations

import ast
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from sciforge.core import Layout, clean_segment


@dataclass
class FileNote:
    path: str
    stats: dict
    issues: list
    ok: bool

    def to_dict(self) -> dict:
        return {"path": self.path, "stats": self.stats,
                "issues": self.issues, "ok": self.ok}


@dataclass
class CodeReviewResult:
    ok: bool
    task_id: str = ""
    files: list = field(default_factory=list)
    scores: dict = field(default_factory=dict)
    checklist: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict:
        return {"ok": self.ok, "task_id": self.task_id, "files": self.files,
                "scores": self.scores, "checklist": self.checklist,
                "warnings": self.warnings, "error": self.error}

    def to_markdown(self) -> str:
        lines = [f"# 复现代码点评：{self.task_id}", ""]
        if self.files:
            lines.append(f"共 {len(self.files)} 个 Python 文件。总分 "
                         f"`{self.scores.get('total','-')}/100`，结构 "
                         f"`{self.scores.get('structure','-')}`，数值 "
                         f"`{self.scores.get('numeric','-')}`，后端 "
                         f"`{self.scores.get('backend','-')}`，风险 "
                         f"`{self.scores.get('risk','-')}`")
            lines.append("")
            for f in self.files:
                lines.append(f"### {f['path']}（{f['stats']['loc']} 行 / "
                             f"{f['stats']['functions']} 函数 / {f['stats']['classes']} 类）")
                if f["issues"]:
                    for it in f["issues"][:20]:
                        lines.append(f"- [{it['category']}] {it['line']}: {it['message']}")
                else:
                    lines.append("- 无明显问题")
                lines.append("")
        else:
            lines.append("（未发现可点评的 Python 文件）")
        if self.checklist:
            lines.append("## 论文可信度检查")
            lines.extend(f"- [{('x' if c['pass'] else ' ')}] {c['text']}" for c in self.checklist)
        if self.warnings:
            lines.append("## 提示")
            lines.extend(f"- {w}" for w in self.warnings)
        return "\n".join(lines)


_NUMERIC_RE = re.compile(r"(seed|epochs?|batch_?size|lr|learning_rate|dropout|layers?|"
                         r"hidden|dim(?:ension)?s?|num_|best|score|acc(?:uracy)?|"
                         r"f1|recall|precision|result|metric)", re.I)
_BACKEND_RE = re.compile(r"(torch|tensorflow|keras|tf\.|flax|jax|paddle|sklearn)", re.I)
_DANGER = [
    ("pandas", "pd.read_csv"),
    ("panic", "raise NotImplementedError"),
    ("rand", "np.random.seed"),
    ("rand", "torch.manual_seed"),
    ("hardcode", "best_hyper"),
    ("temp", "tempfile"),
]
_SMELLS = [
    (re.compile(r"\bprint\("), "debug", "包含 print 调试；建议统一日志"),
    (re.compile(r"\bpass\b"), "stub", "存在 pass 占位，疑似未完成逻辑"),
    (re.compile(r"\bexcept\s*[^:]*:\s*$", re.M), "catch", "裸 except 吞异常"),
    (re.compile(r"\btodo\b", re.I), "todo", "遗留 TODO"),
    (re.compile(r"\bassert\s"), "assert", "断言混入数据路径，发布时建议移除"),
]

_MAGIC_HYPER = ["best", "magic", "secret", "acc=", "acc=", "=0.9", "=0.99"]


def _scan_py(path: Path) -> FileNote:
    txt = path.read_text(encoding="utf-8", errors="replace")
    lines = txt.splitlines()
    issues: list[dict] = []

    def add(cat, line, msg):
        issues.append({"category": cat, "line": line, "message": msg})

    try:
        tree = ast.parse(txt)
    except SyntaxError as e:
        add("syntax", e.lineno or 1, f"语法错误：{e.msg}")
        tree = None

    funcs = classes = 0
    imports: set[str] = set()
    seed_lines: list[int] = []
    if tree is not None:
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                funcs += 1
            elif isinstance(node, ast.ClassDef):
                classes += 1
            elif isinstance(node, ast.Import):
                imports.update(a.name.split(".")[0] for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split(".")[0])
            elif isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        if _NUMERIC_RE.search(t.id) and isinstance(node.value, ast.Constant):
                            v = node.value.value
                            if isinstance(v, (int, float)):
                                if t.id in ("best_acc", "best_loss") or "magic" in t.id:
                                    add("hardcode", node.lineno,
                                        f"超参 {t.id}={v} 疑似硬编码；建议写入配置")
                    if t.id in ("seed", "random_seed"):
                        seed_lines.append(node.lineno)
    else:
        # AST 失败时退回简单的行级扫描
        for i, ln in enumerate(lines, 1):
            m = _NUMERIC_RE.search(ln)
            if m and re.search(r"=\s*\d", ln) and " " not in ln.strip()[:3]:
                add("hardcode", i, "疑似魔法数，建议常量化")

    has_seed = len(seed_lines) > 0 or "seed" in txt.lower()
    has_backend = bool(_BACKEND_RE.search(txt))

    loc = len([ln for ln in lines if ln.strip() and not ln.strip().startswith("#")])
    for pat, cat, msg in _SMELLS:
        for i, ln in enumerate(lines, 1):
            if pat.search(ln):
                add(cat, i, msg)

    # DANGER 关键词检查
    for label, kw in _DANGER:
        if kw.lower() in txt.lower():
            add("risk", 0, f"包含 {label} 特征（{kw}）：请复核随机性与复现一致性")

    if not has_seed and has_backend:
        add("repro", 0, "未发现随机种子设置，多次运行结果可能不可复现")

    return FileNote(
        path=path.name,
        stats={"loc": loc, "functions": funcs, "classes": classes,
               "imports": sorted(imports),
               "has_seed": has_seed, "has_backend": has_backend},
        issues=issues,
        ok=not any(i["category"] in ("syntax",) for i in issues),
    )


def review_code(*, task_id: str, layout: Layout) -> CodeReviewResult:
    safe = clean_segment(task_id)
    root = layout.tasks_dir / safe
    if not root.exists():
        return CodeReviewResult(ok=False, task_id=task_id,
                                error=f"任务 {task_id} 不存在。")
    pys = [p for p in sorted(root.rglob("*.py")) if p.name != "__init__.py"]
    notes = [_scan_py(p) for p in pys]
    r = CodeReviewResult(ok=True, task_id=task_id,
                         files=[n.to_dict() for n in notes])

    # 评分
    n = len(notes)
    structure = 0.0
    numeric = 0.0
    backend = 0.0
    risk = 0.0
    for note in notes:
        st = note.stats
        if st["functions"] >= 2 or st["classes"] >= 1:
            structure += 100 / n
        else:
            structure += 40 / n
        if st["has_seed"]:
            numeric += 100 / n
        else:
            numeric += 0.0
        if st["has_backend"]:
            backend += 100 / n
        else:
            backend += 80 / n
        bad = sum(1 for i in note.issues if i["category"] in ("syntax", "repro", "hardcode", "risk"))
        risk += max(0.0, 100 - 25 * bad) / n
    r.scores = {
        "total": round(structure * 0.35 + numeric * 0.25 + backend * 0.2 + risk * 0.2, 1),
        "structure": round(structure, 1),
        "numeric": round(numeric, 1),
        "backend": round(backend, 1),
        "risk": round(risk, 1),
    }

    # 论文可信度 checklist
    any_seed = any(n.stats["has_seed"] for n in notes)
    r.checklist = [
        {"text": "含随机种子设置（结果可复现）", "pass": any_seed},
        {"text": "每项超参有对应配置/文档", "pass": not any(
            i["category"] == "hardcode" for f in r.files for i in f["issues"])},
        {"text": "无裸 except / panic 占位", "pass": not any(
            i["category"] in ("catch", "panic") for f in r.files for i in f["issues"])},
        {"text": "无残留 TODO / debug print", "pass": not any(
            i["category"] in ("debug", "todo") for f in r.files for i in f["issues"])},
    ]

    # 提示
    if n == 0:
        r.warnings.append("任务内无 Python 文件：请确认复现产物已生成。")
    if not any_seed:
        r.warnings.append("无随机种子：若指标是多次均值，请在论文中注明。")

    r.ok = True
    _persist(layout, task_id, r)
    return r


def _persist(layout: Layout, task_id: str, r: CodeReviewResult):
    root = layout.task_dir(task_id)
    root.mkdir(parents=True, exist_ok=True)
    (root / "code_review.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "code_review.md").write_text(r.to_markdown(), encoding="utf-8")