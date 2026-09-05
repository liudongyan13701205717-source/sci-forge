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

from sciforge.core import Layout
from sciforge.core import model as llm
from sciforge.write.doc import DocStore


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
    # 标题：首个 markdown H1（支持 doc 顶部 `# 标题`）
    m = re.search(r"(?m)^#\s+(.+)$", text)
    title = m.group(1).strip() if m else ""
    if not title:
        # 回退：从 H2 摘要/引言首段生成控制性标题（长度适中、剔除口语化引导词）
        cand = _candidate_title(text)
        title = cand if cand else ""

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
        en_top = [w for w, _ in Counter(w.lower() for w in words).most_common(12) if w not in
                  {"the", "and", "for", "with", "this", "that", "from", "are", "was", "use"}]
        cn_top = _cn_keywords(text)
        # 中文正文优先中文短语（可附专名缩写），纯英文正文才回退英文单词
        if cn_top:
            proper = [w for w in re.findall(r"\b[A-Z][A-Za-z0-9\-]{2,}\b", text)
                      if not any(w in o or o in w for o in cn_top)]
            keywords = (cn_top + proper)[:6]
        else:
            keywords = en_top[:6]
    return title, abstract, keywords, source


def _candidate_title(text: str) -> str:
    """无一级标题时，从摘要/引言首段生成一个控制性标题。"""
    sec = re.search(
        r"(?mis)^#+\s*(摘要|abstract|引言|introduction|研究问题)\s*\n+(.*?)(?=\n#+\s|\Z)",
        text,
    )
    if not sec:
        return ""
    para = re.search(r"(?m)([^\n#][^\n]{20,})", sec.group(2))
    if not para:
        return ""
    line = " ".join(para.group(1).strip().split())
    # 取首句，再去掉口语化引导前缀，保留标题主体
    first = re.split(r"[。！？.!?；;]", line)[0].strip(" ，；;：:")
    for pat in (
        r"^(?:本工作|本文|本研究|本方法|我们|近年来|随着|针对(?:上述)?)",
        r"^(?:提出|所提出|我们提出)",
        r"^(?:一种|一个|了一种)?",
    ):
        first = re.sub(pat, "", first).strip(" ，；;：:")
    if 8 <= len(first) <= 60:
        return first
    return ""


_CN_STOP_SINGLE = frozenset(
    "的一在是和与及了我是你他她它们这那之很并以或而要也不但中上能够对将只过些呢啊吧吗被把给让从向在与和于因"
)
_CN_STOP_SEQ = (
    "提出", "目标", "一种", "一个", "设计", "构建", "找到", "寻找", "定义",
    "针对", "我们", "本文", "研究", "报告", "说明", "计算", "介绍", "采用",
    "类边缘",  # “3 类边缘硬件”里的序数残字
)


_CN_TAIL = "方法模型算法机制框架策略网络探针蒸馏剪枝量化优化评估加速部署优化"  # 学科尾缀，用于加分


def _cn_keywords(text: str) -> list:
    """中文关键词回退：无分词 n-gram 频率统计。

    对中文连读段枚举 2-5 字片段，按「频率×(长度-1)² + 学科尾缀加成」打分：
    让 4-5 字主题词（大语言模型/知识蒸馏）优先，同时丢弃含虚词或叙述词的
    句子碎片，再用包含关系去重，避免产出无意义片段。
    """
    from collections import Counter

    grams: Counter = Counter()
    for run in re.findall(r"[\u4e00-\u9fff]{4,}", text):
        n = len(run)
        for L in range(min(5, n), 1, -1):
            for i in range(n - L + 1):
                g = run[i:i + L]
                # 含虚词（的/了/在/是…）→ 必为碎片
                if any(ch in _CN_STOP_SINGLE for ch in g):
                    continue
                # 含叙述词（提出/一种/设计…）→ 必为句子碎片
                if any(s in g for s in _CN_STOP_SEQ):
                    continue
                grams[g] += 1

    def _score(kv):
        g, c = kv
        return c * (len(g) - 1) ** 2 + (8 if g[-1] in _CN_TAIL else 0)

    out: list[str] = []
    for g, _ in sorted(grams.items(), key=lambda kv: (-_score(kv), -len(kv[0]))):
        if any(g in o or o in g for o in out):
            continue
        out.append(g)
        if len(out) >= 6:
            break
    return out


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
