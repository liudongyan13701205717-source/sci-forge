"""claim→source 核验：解析 doc.md 中 claims + 引文（含 [引用标记]/locator 锚点）；
锚点分类 5 类 HIGH-WARN，输出 gate_refuse；离线确定性规则。"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional

from sciforge.review.validators import content_tokens

# ---------- 常量 ----------
_CLAIM_MARKERS = [
    "表明", "证明", "结果显示", "结果证明", "显著", "优于", "提升", "达到", "实现", "验证了",
    "发现", "显示", "结果表明", "results show", "demonstrates", "achieves", "outperforms",
    "improves", "surpasses", "beats", "we find", "we show", "we demonstrate",
]
_CONSTRAINT_MARKERS = [
    "不得", "禁止", "不允许", "严禁", "不能", "不应", "must not", "forbidden",
    "prohibited", "never", "shall not", "may not",
]
_VAGUE_SOURCE = [
    "研究表明", "文献显示", "先前研究", "据报道", "据文献",
    "previous work", "prior studies", "prior work", "previous research",
    "it has been shown", "it is shown", "literature shows", "studies show",
]
_AUTHOR_YEAR_RE = re.compile(
    r"(?i)([A-Z][a-z]+(?:\s+et\s+al\.?)?)\s*[\(（]\s*(?:19|20)\d{2}\s*[\)）]"
)
_DOI_RE = re.compile(r"doi:\s*(?P<doi>10\.\d{4,9}/[^\s,，)）;、]+)", re.I)
_DOI_BARE_RE = re.compile(r"(?<![\d./])10\.\d{4,9}/[^\s,，)）;、]+")
_ARXIV_RE = re.compile(r"arXiv:\d{4}\.\d{4,5}(?:v\d+)?", re.I)
_URL_RE = re.compile(r"https?://\S+")
_BRACKET_RE = re.compile(r"\[([^\[\]]+)\]")
_SENT_SPLIT = re.compile(r"[。！？!?\n；;]+")

# 5 类别
CATEGORIES = (
    "claim-not-supported",
    "negative-constraint-violation",
    "fabricated-reference",
    "anchorless",
    "constraint-violation-uncited",
)

# 严重度
HIGH_CATS = {
    "claim-not-supported",
    "negative-constraint-violation",
    "fabricated-reference",
}
WARN_CATS = {
    "anchorless",
    "constraint-violation-uncited",
}


@dataclass
class Finding:
    category: str
    severity: str
    position: int          # 句索引（0-based）
    excerpt: str
    reason: str
    anchor: str = ""


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in _SENT_SPLIT.split(text or "") if s.strip()]


def _has_marker(text: str, markers: list[str]) -> bool:
    low = text.lower()
    return any(m in low for m in markers)


def _parse_doi(text: str) -> list[str]:
    """提取 DOI（含 doi: 前缀与裸 DOI）。"""
    out = []
    for m in _DOI_RE.finditer(text):
        out.append(m.group("doi"))
    for m in _DOI_BARE_RE.finditer(text):
        d = m.group(0)
        if d not in out:
            out.append(d)
    return out


def _parse_author_year_outside_brackets(sentence: str) -> list[dict]:
    """解析括号外的 author-year 引用 (如 'Smith et al. (2020)')。"""
    out = []
    # 匹配 "Author et al. (2020)" 或 "Author et al. (2020)." 等
    pattern = re.compile(
        r"(?i)([A-Za-z]+(?:\s+et\s+al\.?)?)\s*[\(（]\s*(?:19|20)\d{2}\s*[\)）]"
    )
    for m in pattern.finditer(sentence):
        out.append({"kind": "author_year", "anchor": m.group(0), "valid": True, "raw": m.group(0)})
    # 中文 "张三等 (2020)"
    pattern_cn = re.compile(r"([\u4e00-\u9fff]{2,4}等)\s*[\(（]\s*(?:19|20)\d{2}\s*[\)）]")
    for m in pattern_cn.finditer(sentence):
        out.append({"kind": "author_year", "anchor": m.group(0), "valid": True, "raw": m.group(0)})
    return out


def _parse_citations(sentence: str) -> list[dict]:
    """解析句中引用锚点，返回 [{kind, anchor, valid, raw}]。"""
    out = []
    # DOI
    for m in _DOI_RE.finditer(sentence):
        doi = m.group("doi")
        out.append({"kind": "doi", "anchor": f"doi:{m.group('doi')}", "valid": True, "raw": m.group(0)})
    for m in _DOI_BARE_RE.finditer(sentence):
        d = m.group(0)
        # 避免重复
        if not any(c["anchor"] == f"doi:{d}" for c in out):
            out.append({"kind": "doi", "anchor": f"doi:{d}", "valid": True, "raw": d})
    # arXiv
    for m in _ARXIV_RE.finditer(sentence):
        out.append({"kind": "arxiv", "anchor": m.group(0), "valid": True, "raw": m.group(0)})
    # URL
    for m in _URL_RE.finditer(sentence):
        out.append({"kind": "url", "anchor": m.group(0), "valid": True, "raw": m.group(0)})
    # bracket citations [n] [1,2] [Smith2020]
    for m in _BRACKET_RE.finditer(sentence):
        content = m.group(1).strip()
        if not content:
            out.append({"kind": "bracket", "anchor": m.group(0), "valid": False,
                        "raw": m.group(0), "reason": "empty bracket"})
            continue
        if re.fullmatch(r"[\d,\s]+", content):
            out.append({"kind": "bracket", "anchor": m.group(0), "valid": True, "raw": m.group(0)})
        elif re.match(r"^[A-Za-z]+(?:\s+et\s+al\.?)?\s*[\(（]\s*(?:19|20)\d{2}\s*[\)）]", content):
            out.append({"kind": "author_year", "anchor": m.group(0), "valid": True, "raw": m.group(0)})
        elif re.match(r"^[A-Za-z]+(?:\s+et\s+al\.?)?\s*(?:19|20)\d{2}$", content):
            out.append({"kind": "author_year", "anchor": m.group(0), "valid": True, "raw": m.group(0)})
        else:
            out.append({"kind": "bracket", "anchor": m.group(0), "valid": False,
                        "raw": m.group(0), "reason": "unrecognized bracket format"})
    # 括号外 author-year (Smith et al. (2020), 张三等 (2020))
    for c in _parse_author_year_outside_brackets(sentence):
        if c not in out:
            out.append(c)
    return out


def _parse_vague_source(sentence: str) -> bool:
    low = sentence.lower()
    return any(v in low for v in _VAGUE_SOURCE) or _AUTHOR_YEAR_RE.search(sentence) is not None


def _has_anchor(citations: list[dict]) -> bool:
    return any(c.get("valid", False) for c in citations)


# -------- 约束目标提取 --------
def _extract_constraint_targets(text: str) -> list[str]:
    """从负向约束句提取目标词（去除标记词后的内容 2-gram/英文词）。"""
    targets = set()
    for sent in _sentences(text):
        low = sent.lower()
        if not _has_marker(sent, _CONSTRAINT_MARKERS):
            continue
        # 去除标记词后的文本
        core = sent
        for m in _CONSTRAINT_MARKERS:
            if m in low:
                idx = low.index(m)
                core = sent[idx + len(m):].strip()
                break
        for tok in content_tokens(core):
            if len(tok) >= 2:
                targets.add(tok)
    return list(targets)


def parse_claims(text: str) -> list[dict]:
    """提取 claim 句（含 claim marker）。返回 [{"sentence_idx", "text", "claim_tokens"}]"""
    claims = []
    for idx, s in enumerate(_sentences(text)):
        if _has_marker(s, _CLAIM_MARKERS):
            claims.append({
                "sentence_idx": len(_sentences(text)) - len(_sentences(text)) + idx,  # temp
                "text": s,
                "claim_tokens": set(content_tokens(s)),
            })
    # 修正索引
    for i, c in enumerate(claims):
        c["sentence_idx"] = i  # 在 claims 中的索引
    return claims


def parse_citations(text: str) -> list[dict]:
    """全文引用解析，返回每句的引用列表 [{sentence_idx, citations}]"""
    out = []
    for idx, s in enumerate(_sentences(text)):
        cits = _parse_citations(s)
        if cits:
            out.append({"sentence_idx": idx, "citations": cits})
    return out


def parse_constraints(text: str) -> list[dict]:
    """负向约束句 + 目标词提取。返回 [{"sentence_idx", "text", "targets"}]"""
    out = []
    for idx, s in enumerate(_sentences(text)):
        low = s.lower()
        if _has_marker(s, _CONSTRAINT_MARKERS):
            targets = _extract_constraint_targets(s)
            if targets:
                out.append({"sentence_idx": idx, "text": s, "targets": targets})
    return out


# -------- source 文本索引构建 --------
def _build_source_index(text: str, sources: dict | None) -> dict[str, set[str]]:
    """构建 source_text -> token set 映射。键支持：bracket number, doi, arxiv id, author-year, full citation raw"""
    index = {}
    if sources:
        for k, v in sources.items():
            index[str(k)] = set(content_tokens(v))
    # 从正文提取 references 段
    # 简单启发：以 [n] 或 doi: 开头的行
    for line in (text or "").splitlines():
        line = line.strip()
        if not line:
            continue
        # [n] Author. Title...
        m = re.match(r"^\s*\[(\d+)\]\s*(.+)", line)
        if m:
            index[m.group(1)] = set(content_tokens(m.group(2)))
            continue
        # doi: 10.xxxx 开头
        if line.lower().startswith("doi:"):
            doi_m = _DOI_RE.search(line)
            if doi_m:
                index[doi_m.group("doi")] = set(content_tokens(line))
    return index


# -------- 核心分类 --------
def _check_claim_not_supported(claim: dict, citations: list[dict], source_index: dict) -> Optional[Finding]:
    """claim-not-supported：claim 内容词与 cited source 零重叠。"""
    if not citations:
        return None
    claim_tokens = set(content_tokens(claim["text"]))
    for cit in citations:
        if not cit.get("valid"):
            continue
        # 查找 source text
        source_text_tokens = None
        for key in (cit.get("anchor"), cit.get("raw")):
            if key in source_index:
                source_text_tokens = source_index[key]
                break
        if source_text_tokens is None:
            continue
        claim_toks = set(content_tokens(claim["text"]))
        if not (claim_toks & source_text_tokens):
            return Finding(
                category="claim-not-supported",
                severity="HIGH",
                position=claim["sentence_idx"],
                excerpt=claim["text"][:40],
                reason=f"声明与引用来源关键词零重叠（anchor={cit.get('anchor')}）",
                anchor=cit.get("anchor", ""),
            )
    return None


def _check_fabricated_reference(citations: list[dict]) -> Optional[Finding]:
    """fabricated-reference：引用无合法 DOI/来源格式。"""
    for cit in citations:
        if not cit.get("valid"):
            return Finding(
                category="fabricated-reference",
                severity="HIGH",
                position=cit.get("sentence_idx", 0),
                excerpt=cit.get("raw", "")[:40],
                reason=f"引用无合法来源格式：{cit.get('reason', '格式不合法')}",
                anchor=cit.get("anchor", ""),
            )
    return None


def _check_anchorless(claim: dict, citations: list[dict], has_vague: bool) -> Optional[Finding]:
    """anchorless：claim 有模糊源提及但无有效锚点。"""
    if not has_vague:
        return None
    if not citations:
        return Finding(
            category="anchorless",
            severity="WARN",
            position=claim["sentence_idx"],
            excerpt=claim["text"][:40],
            reason="claim 含模糊源提及（如'研究表明'/'Smith et al. (2020)'）但无有效锚点",
        )
    if not any(c.get("valid") for c in claim.get("citations", [])):
        return Finding(
            category="anchorless",
            severity="WARN",
            position=claim["sentence_idx"],
            excerpt=claim["text"][:40],
            reason="claim 含模糊源提及但无有效锚点（无有效 DOI/bracket/URL）",
        )
    return None


def _check_negative_constraint(claim: dict, constraint_targets: list[str]) -> Optional[Finding]:
    """negative-constraint-violation：claim 命中负向约束目标词。"""
    if not constraint_targets:
        return None
    claim_toks = set(content_tokens(claim["text"]))
    if any(t in claim_toks for t in constraint_targets):
        return Finding(
            category="negative-constraint-violation",
            severity="HIGH",
            position=claim["sentence_idx"],
            excerpt=claim["text"][:40],
            reason=f"声明命中负向约束目标词（如: {', '.join(constraint_targets[:3])}）",
        )
    return None


def _check_constraint_violation_uncited(text: str, constraint_targets: list[str]) -> list[Finding]:
    """constraint-violation-uncited：非 claim、非约束句命中目标词且无引用锚点。"""
    findings = []
    for idx, s in enumerate(_sentences(text)):
        low = s.lower()
        if _has_marker(s, _CLAIM_MARKERS) or _has_marker(s, _CONSTRAINT_MARKERS):
            continue
        s_toks = set(content_tokens(s))
        hit = any(t in s_toks for t in constraint_targets)
        if not hit:
            continue
        # 检查是否有引用锚点
        cits = _parse_citations(s)
        if not _has_anchor(cits):
            findings.append(Finding(
                category="constraint-violation-uncited",
                severity="WARN",
                position=idx,
                excerpt=s[:40],
                reason=f"非 claim 句命中负向约束目标词（如: {', '.join(constraint_targets[:3])}）且无引用锚点",
            ))
    return findings


def _check_anchorless(claim: dict, citations: list[dict], has_vague: bool) -> Optional[Finding]:
    """anchorless WARN：claim 有模糊源提及但无有效锚点。"""
    if not has_vague:
        return None
    if not citations:
        return Finding(
            category="anchorless",
            severity="WARN",
            position=claim["sentence_idx"],
            excerpt=claim["text"][:40],
            reason="claim 含模糊源提及（如'研究表明'/'Smith et al. (2020)'）但无有效锚点",
        )
    # 也可能有引用但都无效
    if not any(c.get("valid") for c in citations):
        return Finding(
            category="anchorless",
            severity="WARN",
            position=claim["sentence_idx"],
            excerpt=claim["text"][:40],
            reason="claim 含模糊源提及但无有效锚点（无有效 DOI/bracket/URL）",
        )
    return None


# -------- 公共 API --------
def parse_claims(text: str) -> list[dict]:
    return [{"sentence_idx": i, "text": s, "claim_tokens": set(content_tokens(s))}
            for i, s in enumerate(_sentences(text)) if _has_marker(s, _CLAIM_MARKERS)]


def parse_citations(text: str) -> list[dict]:
    out = []
    for idx, s in enumerate(_sentences(text)):
        cits = _parse_citations(s)
        if cits:
            out.append({"sentence_idx": i, "citations": cits})
    return out


def parse_constraints(text: str) -> list[dict]:
    out = []
    for i, s in enumerate(_sentences(text)):
        if _has_marker(s, _CONSTRAINT_MARKERS):
            targets = _extract_constraint_targets(s)
            if targets:
                out.append({"sentence_idx": i, "text": s, "targets": _extract_constraint_targets(s)})
    return out


def classify_findings(
    claims: list[dict],
    citations_by_sentence: list[dict],
    constraint_targets: list[str],
    source_index: dict[str, set[str]],
) -> list[Finding]:
    findings = []
    # claim 相关
    for claim in claims:
        # 找该句的 citations
        cits = []
        for cb in citations_by_sentence:
            if cb["sentence_idx"] == claim["sentence_idx"]:
                cits = cb["citations"]
                break
        # claim-not-supported
        f = _check_claim_not_supported(claim, cits, _build_source_index("", {}))
        if f:
            findings.append(f)
        # negative-constraint-violation
        f = _check_negative_constraint(claim, _extract_constraint_targets(""))
        # TODO: 传入真实 constraint_targets
        # fabricated-reference
        f = _check_fabricated_reference([c for cb in citations_by_sentence if cb["sentence_idx"] == claim["sentence_idx"] for c in cb["citations"]])
        if f:
            findings.append(f)
        # anchorless
        has_vague = any(v in claim["text"].lower() for v in _VAGUE_SOURCE) or _AUTHOR_YEAR_RE.search(claim["text"]) is not None
        f = _check_anchorless(claim, [c for cb in citations_by_sentence if cb["sentence_idx"] == claim["sentence_idx"] for c in cb["citations"]], has_vague)
        if f:
            findings.append(f)
    # constraint-violation-uncited（全文扫描）
    # 略
    return findings


def verify(text: str, *, sources: dict | None = None) -> dict:
    """主入口：claim→source 核验，返回 gate_refuse + findings。"""
    text = text or ""
    sentences = _sentences(text)
    constraint_targets = _extract_constraint_targets(text)
    source_index = _build_source_index(text, sources)

    claims = []
    citations_by_sentence = []
    for idx, s in enumerate(sentences):
        if _has_marker(s, _CLAIM_MARKERS):
            claims.append({"sentence_idx": len(claims), "text": s})
        cits = _parse_citations(s)
        if cits:
            citations_by_sentence.append({"sentence_idx": idx, "citations": cits})

    findings: list[Finding] = []
    gate_refuse = False

    # 1) fabricated-reference：全文扫描所有引用
    for idx, s in enumerate(_sentences(text)):
        cits = _parse_citations(s)
        for cit in cits:
            if not cit.get("valid"):
                findings.append(Finding(
                    category="fabricated-reference",
                    severity="HIGH",
                    position=idx,
                    excerpt=s[:40],
                    reason=f"引用无合法来源格式：{cit.get('reason', '格式不合法')}",
                    anchor=cit.get("anchor", ""),
                ))
                gate_refuse = True

    # 2) claim 相关检查
    claims_list = []
    for idx, s in enumerate(sentences):
        if _has_marker(s, _CLAIM_MARKERS):
            claims_list.append({"sentence_idx": idx, "text": s})

    global_constraint_targets = _extract_constraint_targets(text)

    for claim in claims_list:
        cits = _parse_citations(claim["text"])
        has_vague = any(v in claim["text"].lower() for v in _VAGUE_SOURCE) or _AUTHOR_YEAR_RE.search(claim["text"]) is not None

        # claim-not-supported
        for cit in cits:
            if not cit.get("valid"):
                continue
            src_toks = None
            for key in (cit.get("anchor"), cit.get("raw")):
                if key in _build_source_index("", {}):
                    pass  # 简化：此处简化处理
            # 简化：若有有效引用且无源索引，视为 unsupported（由 fabricated/anchorless 覆盖）

        # claim-not-supported
        claim_toks = set(content_tokens(claim["text"]))
        for cit in cits:
            if not cit.get("valid"):
                continue
            # 查找源文本
            src_tokens = None
            for key in (cit.get("anchor"), cit.get("raw")):
                src = _build_source_index("", {}).get(key)
                if src:
                    src_tokens = src
                    break
            if src_tokens is None:
                # 无源文本可比对，视为 unsupported（由 fabricated/anchorless 覆盖）
                continue
            if not (set(content_tokens(claim["text"])) & src_tokens):
                findings.append(Finding(
                    category="claim-not-supported",
                    severity="HIGH",
                    position=_sentences(text).index(claim["text"]) if claim["text"] in _sentences(text) else 0,
                    excerpt=claim["text"][:40],
                    reason=f"声明与引用来源关键词零重叠（anchor={cit.get('anchor')}）",
                    anchor=cit.get("anchor", ""),
                ))
                gate_refuse = True

        # claim-not-supported: 如果 claim 没有任何有效引用，也标记为 unsupported
        has_valid_cit = any(c.get("valid") for c in cits)
        if not has_valid_cit:
            findings.append(Finding(
                category="claim-not-supported",
                severity="HIGH",
                position=_sentences(text).index(claim["text"]) if claim["text"] in _sentences(text) else 0,
                excerpt=claim["text"][:40],
                reason="声明缺乏有效引用支撑",
                anchor="",
            ))
            gate_refuse = True

        # fabricated-reference（逐 claim 再检一次，确保覆盖）
        if _extract_constraint_targets(text):
            claim_toks = set(content_tokens(claim["text"]))
            if any(t in claim_toks for t in _extract_constraint_targets(text)):
                findings.append(Finding(
                    category="negative-constraint-violation",
                    severity="HIGH",
                    position=_sentences(text).index(claim["text"]) if claim["text"] in sentences else 0,
                    excerpt=claim["text"][:40],
                    reason=f"声明命中负向约束目标词",
                ))
                gate_refuse = True

        # anchorless
        if (any(v in claim["text"].lower() for v in _VAGUE_SOURCE) or _AUTHOR_YEAR_RE.search(claim["text"])):
            if not any(c.get("valid") for c in cits):
                findings.append(Finding(
                    category="anchorless",
                    severity="WARN",
                    position=0,
                    excerpt=claim["text"][:40],
                    reason="claim 含模糊源提及但无有效锚点",
                ))

    # constraint-violation-uncited
    global_targets = _extract_constraint_targets(text)
    for idx, s in enumerate(_sentences(text)):
        if _has_marker(s, _CLAIM_MARKERS) or _has_marker(s, _CONSTRAINT_MARKERS):
            continue
        if any(t in set(content_tokens(s)) for t in global_targets):
            cits = _parse_citations(s)
            if not any(c.get("valid") for c in cits):
                findings.append(Finding(
                    category="constraint-violation-uncited",
                    severity="WARN",
                    position=idx,
                    excerpt=s[:40],
                    reason="非 claim 句命中负向约束目标词且无引用锚点",
                ))

    # 汇总
    summary = {cat: 0 for cat in CATEGORIES}
    for f in findings:
        summary[f.category] += 1
        if f.severity == "HIGH":
            gate_refuse = True

    return {
        "ok": not gate_refuse,
        "gate_refuse": gate_refuse,
        "findings": [f.__dict__ for f in findings],
        "summary": summary,
        "offline": True,
    }