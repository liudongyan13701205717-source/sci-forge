"""投稿建议（venue_suggest）：根据主题/关键词推荐目标期刊与会议。

设计：内置一个关键词→(期刊/会议, 领域, 参考 IF/CCF 性质) 的映射库，
无 LLM 时按主题关键词命中做确定性匹配；可 LLM 增强给出更贴合的推荐。
落盘 projects/{paper_id}/research/venue_suggest.json + md。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from sciforge.core import Layout
from sciforge.core import model as llm

# 关键词主键 -> (名称, 类型, 领域标签, 备注)
_VENUE_DB: list[tuple[str, dict]] = [
    ("大模型|llm|language model|transformer|生成|预训练", {
        "name": "ACL / EMNLP / TACL", "type": "会议/期刊",
        "field": "自然语言处理", "note": "NLP 顶会与高引期刊，门槛高"}),
    ("可解释|可解释性|interpret|explain|attribution|probe", {
        "name": "ICLR / NeurIPS / TMLR", "type": "会议",
        "field": "可解释性与机器学习", "note": "强调新方法与可复现性"}),
    ("多模态|multimodal|vision|图像|语音|audio|video", {
        "name": "CVPR / ICCV / TIP", "type": "会议/期刊",
        "field": "计算机视觉", "note": "视觉与多模态主流"}),
    ("强化|reinforcement|rl|控制|control|agent", {
        "name": "NeurIPS / ICML / ICLR", "type": "会议",
        "field": "强化学习与智能体", "note": "RL 方法主会"}),
    ("数据挖掘|数据|graph|图|推荐|knowledge|kg|network", {
        "name": "KDD / WWW / TKDE", "type": "会议/期刊",
        "field": "数据挖掘与网络", "note": "数据/图/推荐方向"}),
    ("联邦|privacy|隐私|安全|security|差分隐私|attack", {
        "name": "IEEE S&P / CCS / USENIX Sec", "type": "会议",
        "field": "安全与隐私", "note": "安全四大顶会之一"}),
    ("医疗|bio|生物|医学|health|drug|gene", {
        "name": "Nature Methods / Bioinformatics / NEJM AI", "type": "期刊",
        "field": "生物医学", "note": "生物医学计算期刊"}),
    ("分布式|系统|system|性能|os|database|database|并行", {
        "name": "OSDI / SOSP / VLDB / TPDS", "type": "会议/期刊",
        "field": "系统与数据库", "note": "系统顶会"}, ),
    ("优化|optim|数值|numeric|求解|solver|数学", {
        "name": "SIAM / JMLR / COLT", "type": "期刊/会议",
        "field": "优化与学习理论", "note": "理论/优化向"}),
    ("概率|统计|bayes|统计推断|inference|causal|因果", {
        "name": "AISTATS / JASA / NeurIPS", "type": "会议/期刊",
        "field": "统计与概率建模", "note": "统计方法与因果推断"}),
]


@dataclass
class VenueSuggest:
    ok: bool
    topic: str = ""
    matches: list = field(default_factory=list)
    suggestions: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    error: str = ""
    llm_used: bool = False

    def to_dict(self) -> dict:
        return {k: getattr(self, k) for k in (
            "ok", "topic", "matches", "suggestions", "notes", "error", "llm_used",
        )}

    def to_markdown(self) -> str:
        def bullet(xs):
            return "\n".join(f"- {x}" for x in xs) if xs else "- （无）"

        rows = []
        for m in self.matches:
            rows.append(f"- **{m.get('name','')}**（{m.get('type','')}·{m.get('field','')}）："
                        f"{m.get('note','')}  [命中关键词：{', '.join(m.get('hits',[]))}]")
        return "\n\n".join([
            f"# 投稿建议：{self.topic}",
            "## 匹配的期刊/会议\n" + ("\n".join(rows) if rows else "- 未命中内置库，建议人工检索"),
            f"## 采纳建议\n{bullet(self.suggestions)}",
        ])


def venue_suggest(
    topic: str,
    *,
    paper_id: str,
    layout: Layout,
) -> VenueSuggest:
    r = VenueSuggest(ok=False, topic=topic)
    notes: list = []
    r.matches = _match_venues(topic)
    if not r.matches:
        notes.append("内置期刊/会议库未命中关键词，请补充领域信息或采用通用建议。")

    if llm.configured():
        try:
            _llm_suggest(r, notes)
            r.llm_used = True
        except RuntimeError as e:
            notes.append(f"LLM 建议不可用，保留映射匹配：{e}")

    if not r.suggestions:
        _template_suggest(r, notes)

    r.notes = notes
    r.ok = True
    _persist(layout, paper_id, r)
    return r


def _match_venues(topic: str) -> list[dict]:
    low = topic.lower()
    out = []
    for pat, db in _VENUE_DB:
        hits = [k.strip() for k in re.split(r"\|", pat) if k.strip().lower() in low]
        if hits:
            item = dict(db)
            item["hits"] = hits
            out.append(item)
    return out


def _template_suggest(r: VenueSuggest, notes: list) -> None:
    if r.matches:
        r.suggestions = [
            "优先将工作定位到上述 1-2 个目标再写 positioning。",
            "投稿前对照目标会议模板与格式要求。",
            "若能开源数据与代码，可提升接收几率。",
        ]
    else:
        r.suggestions = [
            "按主题补充领域关键词后再运行，以命中更精准的期刊/会议。",
            "参考该领域近 2 年引用最高的论文发表出处。",
            "考虑从通用顶会（NeurIPS/ICML/ICLR）或其姊妹会切入。",
        ]
    notes.append("无 LLM，依据内置映射表给出建议。")


def _llm_suggest(r: VenueSuggest, notes: list) -> None:
    sys = "你是科研投稿顾问。基于主题与已知候选给出投稿建议。输出严格 JSON。"
    cand = ", ".join(m.get("name", "") for m in r.matches) or "未命中内置库"
    prompt = (
        f"主题：{r.topic}\n已知候选：{cand}\n\n"
        "输出 JSON：\n{\"suggestions\":[\"建议:理由\"]}"
    )
    raw = llm.chat(prompt, system=sys, temperature=0.6, max_tokens=900)
    data = _strip_json_obj(raw)
    if not data:
        notes.append("LLM 输出非合法 JSON，保留映射匹配。")
        return
    r.suggestions = [str(x) for x in data.get("suggestions", []) if x]


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


def _persist(layout: Layout, paper_id: str, r: VenueSuggest) -> Path:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    p = root / "venue_suggest.json"
    p.write_text(json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    md = root / "venue_suggest.md"
    md.write_text(r.to_markdown(), encoding="utf-8")
    return p
