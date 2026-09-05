"""创新性检查（novelty）：从论文标题/摘要/正文抽关键短语，检索最相似已有工作，
分析重叠并给出候选差异点，供作者定位 contribution 与相关研究。

复用 lit.search_openalex（免 key，离线回退模板）。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field

from sciforge.core import Layout
from sciforge.research import lit


@dataclass
class NoveltyResult:
    ok: bool
    paper_id: str = ""
    title: str = ""
    abstract: str = ""
    phrases: list = field(default_factory=list)
    similar_papers: list = field(default_factory=list)
    overlapping_terms: list = field(default_factory=list)
    differentiators: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    error: str = ""
    offline: bool = False

    def to_dict(self) -> dict:
        return {
            "ok": self.ok, "paper_id": self.paper_id, "title": self.title,
            "abstract": self.abstract, "phrases": self.phrases,
            "similar_papers": self.similar_papers,
            "overlapping_terms": self.overlapping_terms,
            "differentiators": self.differentiators,
            "notes": self.notes, "error": self.error, "offline": self.offline,
        }

    def to_markdown(self) -> str:
        def bullet(xs):
            return "\n".join(f"- {x}" for x in xs) if xs else "- （待补充，考虑聚焦更多方法/场景差异）"

        pubs = []
        for p in self.similar_papers:
            score = p.get("score", 0)
            pubs.append(
                f"- 重叠 {score*100:.0f}% — [{p.get('year','?')}] {p.get('title','')} "
                f"({p.get('venue','')}, 被引{p.get('cited_by',0)}) {p.get('doi') or ''}"
            )
        pubs_text = "\n".join(pubs) if pubs else "- （暂无检索到相似工作，可能网络离线或关键词过新）"
        return "\n\n".join([
            f"# 创新性检查：{self.paper_id}",
            f"## 论文信息\n- 标题：{self.title or '（缺省）'}\n- 摘要：{(self.abstract or '（缺省）')[:300]}",
            f"## 关键短语\n{bullet(self.phrases)}",
            f"## 相似已有工作\n{pubs_text}",
            f"## 重叠术语\n{bullet(self.overlapping_terms)}",
            f"## 候选差异点\n{bullet(self.differentiators)}",
        ])


# ---------- 主函数 ----------

def _paper_text(layout: Layout, paper_id: str) -> tuple[str, str]:
    """取论文标题/摘要：优先 metadata.json，回退 doc.md。"""
    title, abstract = "", ""
    meta = layout.project_dir(paper_id) / "research" / "metadata.json"
    if meta.exists():
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
            title = data.get("title") or ""
            abstract = data.get("abstract") or data.get("summary") or ""
        except (OSError, ValueError):
            pass
    if not title:
        doc = layout.project_dir(paper_id) / "doc.md"
        if doc.exists():
            try:
                txt = doc.read_text(encoding="utf-8")
            except OSError:
                txt = ""
            m = re.search(r"^#\s+(.+)$", txt, re.M)
            if m:
                title = m.group(1).strip()
            if not abstract:
                body = re.sub(r"^#.*$", "", txt, flags=re.M)[:1200]
                abstract = body.strip()
    return title, abstract


_CONTENT_WORDS = {
    "模型", "方法", "框架", "算法", "网络", "量化", "剪枝", "蒸馏", "推理",
    "学习", "优化", "训练", "识别", "生成", "增强", "检索", "对齐", "稀疏",
    "边缘", "端侧", "协同", "混合", "可解释", "泛化", "鲁棒", "注意力",
    "编码器", "解码器", "transformer", "bert", "gpt", "llm", "大模型",
}


def _extract_phrases(title: str, abstract: str) -> list[str]:
    src = (title + " " + abstract)[:2000]
    toks = re.split(r"[\s,，。;；、:：()（）\[\]{}<>\"'“”‘’\-—/\\]+", src)
    phrases: list[str] = []
    seen: set[str] = set()
    for t in toks:
        t = t.strip().strip(".")
        if not t or len(t) < 4:
            continue
        low = t.lower()
        if low in seen or low in _CONTENT_WORDS:
            continue
        seen.add(low)
        phrases.append(t)
    return phrases[:8]


def _tokens(s: str) -> set[str]:
    return {t.lower() for t in re.split(r"[\W_]+", s) if len(t) > 1}


def _overlap(peer_title: str, title: str, abstract: str) -> float:
    base = _tokens(title + " " + abstract)
    if not base:
        return 0.0
    n = sum(1 for t in base if t in peer_title.lower())
    return n / len(base)


def _common_terms(title: str, abstract: str, scored: list[dict]) -> list[str]:
    mine = _tokens(title + " " + abstract)
    agg: set[str] = set()
    for p in scored:
        body = (p.get("title") or "") + " " + (p.get("abstract") or "")
        agg |= _tokens(body) & mine
    terms = sorted(agg, key=len, reverse=True)[:10]
    return terms or ["（未检出明显重叠主题词）"]


def _build_differentiators(r: NoveltyResult) -> list[str]:
    if not r.similar_papers:
        return [
            "未见高度相似工作：可作为空白点切入，建议在 related work 中声明首发性。",
            "若为综述性选题，建议说明本工作覆盖范围与已有综述的差异（更细粒度/更新文献）。",
        ]
    top = r.similar_papers[0]
    tname = (top.get("title") or "")[:60]
    lead = r.title or (r.phrases[0] if r.phrases else "本主题")
    return [
        f"相比代表工作「{tname}」：其聚焦 {_focus_of(top)}；本文侧重 {lead}，"
        "可强调资源受限/效率-精度联合优化等不同切入点。",
        "建议在摘要与引言明确列出与上述工作的 2-3 点实质差异（数据规模、方法机制、评测口径）。",
        "补做对照实验：在相同基准上与 Top 相似工作对比，量化收益以支撑 novelty 声明。",
    ]


def _focus_of(p: dict) -> str:
    abs_ = (p.get("abstract") or "")[:80].strip()
    return abs_ or (p.get("title") or "相关方向")[:40]


def check_novelty(
    *,
    paper_id: str,
    layout: Layout,
    limit: int = 8,
    sources: list[str] | None = None,
) -> NoveltyResult:
    """创新性检查：检索相似工作并给出差异点。"""
    r = NoveltyResult(ok=False, paper_id=paper_id)
    title, abstract = _paper_text(layout, paper_id)
    if not (title or abstract):
        r.error = f"项目 {paper_id} 没有可利用的标题/摘要内容（写 doc.md 或先跑 auto_title_abstract）。"
        return r
    r.title, r.abstract = title, abstract
    phrases = _extract_phrases(title, abstract)
    r.phrases = phrases

    from sciforge.science.api import cross_lookup
    if sources:
        papers = cross_lookup(" ".join(phrases), databases=sources, limit=limit)
    else:
        queries = [title] if title else [abstract[:120]]
        if len(phrases) >= 3:
            queries.append(" ".join(phrases[:4]))
        if len(phrases) >= 5:
            queries.append(" ".join(phrases[4:7]))

        papers = []
        for q in queries[:3]:
            hits = lit.search_openalex(q, limit=limit)
            papers.extend(hits)
    papers = lit.dedupe(papers)
    if not papers:
        r.offline = True
        r.notes.append("OpenAlex 无结果（离线或关键词过新），差异点用启发式模板。")
    else:
        scored = []
        for p in papers:
            p["score"] = round(min(1.0, _overlap(p.get("title", "") or "", title, abstract) + 0.15), 3)
            scored.append(p)
        scored.sort(key=lambda p: p.get("score", 0), reverse=True)
        r.similar_papers = scored[:limit]
        r.overlapping_terms = _common_terms(title, abstract, scored)

    r.differentiators = _build_differentiators(r)
    _persist(layout, paper_id, r)
    r.ok = True
    return r


def _persist(layout: Layout, paper_id: str, r: NoveltyResult):
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "novelty.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "novelty.md").write_text(r.to_markdown(), encoding="utf-8")