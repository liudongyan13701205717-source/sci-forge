"""写作质量检查：机器生成文风检测 + claim-strength ladder。

- detect_style(text)：hedging 密度、模板化句式、空洞连接词占比 → 0-100 分数
  + 证据列表（每项 {type, count, examples}）。
- claim_strength(text)：三档强度阶梯 associated with < predicts < causes，
  检测无授权的强度上移（如仅有关联证据却用因果表述）。
"""
from __future__ import annotations

import re

# ---- 机器文风信号词 ----

_HEDGING = [
    "may", "might", "possibly", "perhaps", "likely", "could", "seems",
    "appears", "tends to", "approximately", "arguably", "somewhat",
    "可能", "或许", "也许", "似乎", "大约", "大致", "倾向于", "有望", "往往",
]

_TEMPLATED = [
    "it is worth noting", "in conclusion", "overall,", "furthermore,",
    "moreover,", "additionally,", "in summary", "notably,",
    "plays a crucial role", "in today's",
    "值得注意的是", "需要注意的是", "总的来说", "总而言之", "综上所述",
    "众所周知", "综上所述", "不言而喻",
]

_FILLERS = [
    "however", "therefore", "thus", "hence", "moreover", "furthermore",
    "additionally", "in addition", "overall", "meanwhile",
    "然而", "因此", "所以", "此外", "总之", "但是", "同时", "另外", "总体而言",
]

# ---- claim-strength 阶梯 ----

_LADDER = [
    ("associated", [
        "is associated with", "are associated with", "associated with",
        "correlate", "correlation", "correlated", "link",
        "相关", "关联", "与……相关",
    ]),
    ("predicts", [
        "predict", "predicts", "predicting", "forecast",
        "预测", "预示", "预判",
    ]),
    ("causes", [
        "causes", "cause", "caused", "causal effect", "proves that",
        "results in", "leads to", "drives",
        "导致", "引发", "造成", "证明了", "决定了",
    ]),
]

# 因果表述的授权证据标记（出现则视为有授权）
_CAUSAL_EVIDENCE = [
    "randomized", "controlled trial", "ablation", "causal inference",
    "instrumental variable", "did ", "difference-in-differences",
    "对照实验", "随机对照", "消融", "因果推断", "工具变量", "双重差分",
]

_SENT_SPLIT = re.compile(r"[.!?。！？]+|\n+")


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in _SENT_SPLIT.split(text or "") if s.strip()]


def detect_style(text: str) -> dict:
    """机器生成文风检测：hedging 密度 + 模板化句式 + 空洞连接词占比。

    Args:
        text: 待检文本（论文正文或章节）。

    Returns:
        dict：{ok, score (0-100, 越高越像机器生成), sentences, metrics:
        {hedging_density, templated_ratio, filler_ratio}, evidence: [...]}。
        空文本 → ok=False。
    """
    sents = _sentences(text)
    if not sents:
        return {"ok": False, "error": "文本为空", "score": 0.0,
                "sentences": 0, "metrics": {}, "evidence": []}
    n = len(sents)
    hed_hits = _hits(text, _HEDGING)
    tpl_hits = _hits(text, _TEMPLATED)
    fill_hits = _hits(text, _FILLERS)
    metrics = {
        "hedging_density": round(hed_hits / n, 3),
        "templated_ratio": round(tpl_hits / n, 3),
        "filler_ratio": round(fill_hits / n, 3),
    }
    score = min(100.0, metrics["hedging_density"] * 40.0
                + metrics["templated_ratio"] * 30.0
                + metrics["filler_ratio"] * 30.0)
    evidence = _evidence("hedging", _HEDGING, sents, hed_hits)
    evidence += _evidence("templated", _TEMPLATED, sents, tpl_hits)
    evidence += _evidence("filler", _FILLERS, sents, fill_hits)
    return {"ok": True, "score": round(score, 1), "sentences": n,
            "metrics": metrics, "evidence": evidence}


def _hits(text: str, phrases: list[str]) -> int:
    low = text.lower()
    return sum(low.count(p) for p in phrases)


def _evidence(kind: str, phrases: list[str], sents: list[str],
              count: int) -> list[dict]:
    examples = [s for s in sents if any(p in s.lower() for p in phrases)][:3]
    return [{"type": kind, "count": count, "examples": examples}]


def claim_strength(text: str) -> dict:
    """claim-strength ladder：检测表述强度与无授权的强度上移。

    阶梯：associated with（关联）< predicts（预测）< causes（因果）。
    强度上移 = 仅有关联证据却使用预测/因果表述；因果表述需出现
    授权证据标记（随机对照/消融/因果推断等），否则标记为无授权。

    Args:
        text: 待检文本。

    Returns:
        dict：{ok, max_level ('associated'|'predicts'|'causes'|'none'),
        claims: [{sentence, level, escalated}], escalations: [...]}。
        空文本 → ok=False。
    """
    sents = _sentences(text)
    if not sents:
        return {"ok": False, "error": "文本为空", "max_level": "none",
                "claims": [], "escalations": []}
    has_evidence = any(m in text.lower() for m in _CAUSAL_EVIDENCE)
    claims: list[dict] = []
    escalations: list[dict] = []
    max_rank = -1
    for s in sents:
        low = s.lower()
        ranks = [i for i, (_lvl, words) in enumerate(_LADDER) if any(w in low for w in words)]
        if not ranks:
            continue
        rank = max(ranks)
        max_rank = max(max_rank, rank)
        escalated = rank >= 1 and 0 in ranks and max(ranks) > 0
        # 仅含因果表述但全文无授权证据 → 强度上移
        if rank == 2 and not has_evidence:
            escalated = True
        if escalated:
            escalations.append({
                "sentence": s,
                "level": _LADDER[rank][0],
                "reason": "关联/预测证据不足却使用更高强度表述"
                if rank >= 1 and 0 in ranks
                else "因果表述缺少授权证据标记（随机对照/消融/因果推断等）",
            })
        claims.append({"sentence": s, "level": _LADDER[rank][0],
                       "escalated": escalated})
    return {
        "ok": True,
        "max_level": _LADDER[max_rank][0] if max_rank >= 0 else "none",
        "claims": claims,
        "escalations": escalations,
    }
