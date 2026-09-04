"""标题/摘要/关键词提炼（auto_title_abstract）：从已有正文生成投稿所需的元数据。

读取 projects/{paper_id}/doc.md（或 sections/），产出
  - title（若正文无标题，从首行/关键词启发式生成）
  - abstract（若正文已有摘章节则摘录，否则用引言首段拼装）
  - keywords
落盘 projects/{paper_id}/research/metadata.json + md。
无 LLM 时确定性回退。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from clawsgo_self.core import Layout
from clawsgo_self.core import model as llm
from clawsgo_self.write.doc import DocStore


@dataclass
class Metadata:
    ok: bool
    paper_id: str = ""
    title: str = ""
    abstract: str = ""
    keywords: list = field(default_factory=list)
    source: str = ""
    notes: list = field(default_factory=list)
    error: str = ""
    llm_used: bool = False

    def to_dict(self) -> dict:
        return {k: getattr(self, k) for k in (
            "ok", "paper_id", "title", "abstract", "keywords", "source",
            "notes", "error", "llm_used",
        )}

    def to_markdown(self) -> str:
        return "\n\n".join([
            f"# 论文元数据（{self.paper_id}）",
            f"**标题：** {self.title}",
            f"**来源：** {self.source}",
            f"## 摘要\n{self.abstract or '（暂无）'}",
            f"## 关键词\n" + (", ".join(self.keywords) if self.keywords else "（暂无）"),
        ])


def _read_doc(layout: Layout, paper_id: str) -> str:
    doc = DocStore(layout, paper_id)
    parts = []
    if doc.doc_md.exists():
        parts.append(doc.doc_md.read_text(encoding="utf-8"))
    else:
        for f in sorted(doc.sections_dir.glob("*.md")):
            parts.append(f.read_text(encoding="utf-8"))
    return "\n".join(parts)


def auto_title_abstract(
    *,
    paper_id: str,
    layout: Layout,
) -> Metadata:
    r = Metadata(ok=False, paper_id=paper_id)
    notes: list = []
    text = _read_doc(layout, paper_id)
    if not text.strip():
        r.error = f"项目 {paper_id} 尚无正文，请先写入内容。"
        r.ok = False
        return r

    r.title, r.abstract, r.keywords, r.source = _template_meta(text)

    if llm.configured():
        try:
            _llm_meta(r, text, notes)
            r.llm_used = True
        except RuntimeError as e:
            notes.append(f"LLM 提炼不可用，保留模板结果：{e}")

    r.notes = notes
    r.ok = True
    _persist(layout, paper_id, r)
    return r


def _template_meta(text: str) -> tuple[str, str, list, str]:
    source = "正文启发式"
    # 标题：首个 markdown H1
    m = re.search(r"(?m)^#\s+(.+)$", text)
    title = m.group(1).strip() if m else ""

    # 摘要：找 ## 摘要 / ## 摘要（Abstract） 之后的段落
    absm = re.search(r"(?mis)^#+\s*(摘要|abstract)\s*\n+(.*?)(?=\n#+\s|\Z)", text)
    abstract = ""
    if absm:
        abstract = " ".join(absm.group(2).split()).strip()
    elif not abstract:
        # 回退：引言首个实质段落
        intr = re.search(r"(?mis)^#+\s*(引言|introduction|研究问题)\s*\n+(.*?)(?=\n#+\s|\Z)", text)
        if intr:
            para = re.search(r"(?m)([^\n#][^\n]{40,})", intr.group(2))
            abstract = " ".join(para.group(1).strip().split()) if para else ""

    # 关键词：找 关键词/Keywords 行（": " 形式或 "## 关键词" 标题形式）
    kw = re.findall(r"(?im)^\s*(?:关键词|keywords?)\s*[:：]\s*(.+)$", text)
    if not kw:
        kwm = re.search(r"(?mis)^#+\s*(关键词|keywords?)\s*\n+(.+?)(?=\n#+\s|\Z)", text)
        if kwm:
            kw = [kwm.group(2).strip()]
    keywords = []
    if kw:
        keywords = [k.strip() for k in re.split(r"[,，、;；]", kw[0]) if k.strip()][:8]
    if not keywords:
        words = re.findall(r"[A-Za-z][A-Za-z\-]{2,}", text)
        from collections import Counter
        top = [w for w, _ in Counter(w.lower() for w in words).most_common(12) if w not in
               {"the", "and", "for", "with", "this", "that", "from", "are", "was", "use"}]
        keywords = top[:6]
    return title, abstract, keywords, source


def _llm_meta(r: Metadata, text: str, notes: list) -> None:
    sys = "你是论文助手。根据正文提炼标题、摘要、关键词。输出严格 JSON。"
    snippet = text[:3500]
    prompt = (
        "正文节选：\n" + snippet + "\n\n"
        "输出 JSON：\n{\"title\":\"...\",\"abstract\":\"...\",\"keywords\":[\"\",\"\"]}"
    )
    raw = llm.chat(prompt, system=sys, temperature=0.5, max_tokens=1200)
    data = _strip_json_obj(raw)
    if not data:
        notes.append("LLM 输出非合法 JSON，保留启发式结果。")
        return
    if data.get("title"):
        r.title = str(data["title"]).strip() or r.title
    if data.get("abstract"):
        r.abstract = str(data["abstract"]).strip() or r.abstract
    if data.get("keywords"):
        r.keywords = [str(x) for x in data["keywords"] if x][:8]
    r.source = "LLM 提炼（附启发式基线）"


def _strip_json_obj(raw: str) -> dict:
    s = raw.strip()
    if s.startswith("```"):
        s = s.strip("`")
        if s.lower().startswith("json"):
            s = s[4:]
    i, j = s.find("{"), s.rfind("}")
    if i == -1 or j == -1 or j < i:
        return {}
    try:
        d = json.loads(s[i : j + 1])
        return d if isinstance(d, dict) else {}
    except (ValueError, TypeError):
        return {}


def _persist(layout: Layout, paper_id: str, r: Metadata) -> Path:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    p = root / "metadata.json"
    p.write_text(json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    md = root / "metadata.md"
    md.write_text(r.to_markdown(), encoding="utf-8")
    return p
