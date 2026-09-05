"""写作线文档存储：按 paper_id 管理分章节 markdown，并拼接为 doc.md。"""

from __future__ import annotations

from pathlib import Path

from sciforge.core import Layout


class DocStore:
    """按 paper_id 读写章节内容，维护排序列与 doc.md 产物。"""

    # 章节展示顺序（写作逻辑推进）
    SECTION_ORDER = [
        "abstract",
        "introduction",
        "problem",
        "assumptions",
        "notation",
        "modeling",
        "solution",
        "results",
        "references",
        "appendix",
    ]

    def __init__(self, layout: Layout, paper_id: str) -> None:
        self.root = layout.project_dir(paper_id)
        self.sections_dir = self.root / "sections"
        self.sections_dir.mkdir(parents=True, exist_ok=True)
        self.meta = self.root / "doc.json"
        self.doc_md = self.root / "doc.md"

    # ---- 章节级 ----
    def section_path(self, section: str) -> Path:
        return self.sections_dir / f"{_safe(section)}.md"

    def read_section(self, section: str) -> str | None:
        p = self.section_path(section)
        return p.read_text(encoding="utf-8") if p.exists() else None

    def write_section(self, section: str, content: str, *, fmt: str) -> None:
        self.section_path(section).write_text(content, encoding="utf-8")
        self._update_meta(section, fmt)
        self.rebuild_doc()

    def list_sections(self) -> list[str]:
        return [p.stem for p in sorted(self.sections_dir.glob("*.md"))]

    # ---- meta ----
    def _update_meta(self, section: str, fmt: str) -> None:
        import json

        meta: dict = {}
        if self.meta.exists():
            try:
                meta = json.loads(self.meta.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                meta = {}
        meta.setdefault("sections", {})
        meta["sections"][section] = {"format": fmt}
        meta.setdefault("order", self.SECTION_ORDER)
        self.meta.write_text(
            json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    # ---- 拼接 doc.md ----
    def rebuild_doc(self) -> None:
        parts: list[str] = []
        for sec in self.SECTION_ORDER:
            txt = self.read_section(sec)
            if txt:
                heading = _heading_for(sec)
                parts.append(f"## {heading}\n\n{txt.strip()}\n")
        self.doc_md.write_text("\n".join(parts).strip() + "\n", encoding="utf-8")


def _heading_for(section: str) -> str:
    return {
        "abstract": "摘要",
        "introduction": "引言",
        "problem": "研究问题",
        "assumptions": "假设",
        "notation": "符号说明",
        "modeling": "建模",
        "solution": "求解",
        "results": "结果与分析",
        "references": "参考文献",
        "appendix": "附录",
    }.get(section, section.capitalize())


def _safe(name: str) -> str:
    return "".join(c if (c.isalnum() or c in "-_.") else "_" for c in name) or "untitled"
