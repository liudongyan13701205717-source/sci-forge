"""风格校准：从已有 doc.md 文本学习作者声音统计 → style profile；score_text 相似度评分。

- learn_style(text)：句长分布（分桶直方图）、用词频率偏好（top 词）、
  结构习惯（标题密度/列表密度/段落长度）→ profile dict。
- score_text(text, profile)：与作者画像的相似度评分（0-100），
  分量 = 句长分布（余弦）+ 用词重叠（Jaccard）+ 结构习惯。
- learn_doc(paper_id, layout)：读取 projects/{paper_id}/doc.md 后调 learn_style。
"""
from __future__ import annotations

import re

from sciforge.research.quality import _sentences

_BUCKETS = [(0, 30), (31, 60), (61, 90), (91, 120), (121, 10 ** 9)]

_STOP = {
    "the", "and", "for", "with", "this", "that", "are", "not", "but", "you",
    "your", "can", "have", "has", "had", "was", "were", "will", "from",
    "into", "about", "than", "then", "their", "what", "when", "which",
    "while", "also", "our", "its", "one", "two", "使用", "通过", "进行", "方法",
}


def _tokens(text: str) -> list[str]:
    """所有 token（含重复）：英文词（≥3 字符小写，去停用词）+ 中文重叠 2-gram。"""
    out: list[str] = []
    for w in re.findall(r"[a-zA-Z]{3,}", text or ""):
        lw = w.lower()
        if lw not in _STOP:
            out.append(lw)
    for m in re.findall(r"[\u4e00-\u9fff]{2,}", text or ""):
        for j in range(len(m) - 1):
            out.append(m[j:j + 2])
    return out

# 结构习惯：标题行、列表项
_HEADING = re.compile(r"^\s*#{1,6}\s+", re.MULTILINE)
_BULLET = re.compile(r"^\s*[-*]\s+", re.MULTILINE)


def learn_style(text: str) -> dict:
    """从文本学习作者声音统计 → style profile dict。

    Args:
        text: 已有正文（如 doc.md 全文）。

    Returns:
        dict：{ok, n_chars, sentences: {count, mean_len, buckets},
        tokens: {top: [{token, count}]}, structure: {heading_rate,
        bullet_rate, para_mean_len}}。空文本 → ok=False。
    """
    text = text or ""
    sents = _sentences(text)
    if not sents or not text.strip():
        return {"ok": False, "error": "文本为空", "n_chars": 0,
                "sentences": {}, "tokens": {}, "structure": {}}
    lens = [len(s) for s in sents]
    mean_len = sum(lens) / len(lens)
    buckets = [sum(1 for L in lens if lo <= L <= hi) for lo, hi in _BUCKETS]
    freq: dict[str, int] = {}
    for t in _tokens(text):
        freq[t] = freq.get(t, 0) + 1
    top = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:20]
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    para_lens = [len(p.strip()) for p in paras] or [len(text.strip())]
    profile = {
        "ok": True,
        "n_chars": len(text),
        "sentences": {
            "count": len(sents),
            "mean_len": round(mean_len, 1),
            "buckets": buckets,
        },
        "tokens": {"top": [{"token": t, "count": c} for t, c in top]},
        "structure": {
            "heading_rate": round(len(_HEADING.findall(text)) / max(1, len(paras)), 3),
            "bullet_rate": round(len(_BULLET.findall(text)) / max(1, len(sents)), 3),
            "para_mean_len": round(sum(para_lens) / len(para_lens), 1),
        },
    }
    return profile


def learn_doc(paper_id: str, *, layout) -> dict:
    """读取 projects/{paper_id}/doc.md 并学习作者声音画像。"""
    p = layout.project_dir(paper_id) / "doc.md"
    if not p.exists():
        return {"ok": False, "error": "尚无 doc.md", "n_chars": 0,
                "sentences": {}, "tokens": {}, "structure": {}}
    return learn_style(p.read_text(encoding="utf-8", errors="ignore"))


def score_text(text: str, profile: dict) -> dict:
    """文本与作者画像的相似度评分（0-100，越高越接近作者声音）。

    Args:
        text: 待评文本。
        profile: learn_style / learn_doc 产出的画像 dict。

    Returns:
        dict：{ok, score, components: {sentence_sim, token_sim,
        structure_sim}, verdict}。空文本或画像无效 → ok=False。
    """
    sents = _sentences(text)
    if not sents or not (text or "").strip():
        return {"ok": False, "error": "文本为空", "score": 0.0,
                "components": {}, "verdict": ""}
    if not profile or not profile.get("ok"):
        return {"ok": False, "error": "画像无效（先运行 learn_style）",
                "score": 0.0, "components": {}, "verdict": ""}
    lens = [len(s) for s in sents]
    buckets = [sum(1 for L in lens if lo <= L <= hi) for lo, hi in _BUCKETS]
    ref_buckets = profile["sentences"].get("buckets") or [0] * len(_BUCKETS)
    sentence_sim = _cosine(buckets, ref_buckets)

    ref_top = {t["token"] for t in profile["tokens"].get("top", [])}
    # 待评文本也取 top-N token（与画像 top 数量一致），再做 Jaccard
    my_freq: dict[str, int] = {}
    for t in _tokens(text):
        my_freq[t] = my_freq.get(t, 0) + 1
    n_top = len(ref_top) or 20
    my_top = {t for t, _ in sorted(my_freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n_top]}
    token_sim = _jaccard(my_top, ref_top)

    st = profile["structure"]
    my_paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    my_heading = len(_HEADING.findall(text)) / max(1, len(my_paras))
    my_bullet = len(_BULLET.findall(text)) / max(1, len(sents))
    my_para_len = sum(len(p.strip()) for p in my_paras) / max(1, len(my_paras))
    structure_sim = (
        _rel_diff(my_heading, st.get("heading_rate", 0.0))
        + _rel_diff(my_bullet, st.get("bullet_rate", 0.0))
        + _rel_diff(my_para_len, st.get("para_mean_len", 0.0))
    ) / 3.0

    score = round(sentence_sim * 40.0 + token_sim * 35.0
                  + structure_sim * 25.0, 1)
    verdict = ("高度接近作者声音" if score >= 70
               else "部分接近" if score >= 45 else "风格偏离")
    return {
        "ok": True,
        "score": score,
        "components": {
            "sentence_sim": round(sentence_sim, 3),
            "token_sim": round(token_sim, 3),
            "structure_sim": round(structure_sim, 3),
        },
        "verdict": verdict,
    }


def _cosine(a: list[float], b: list[float]) -> float:
    import math
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def _jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def _rel_diff(a: float, b: float) -> float:
    """相对差异 → 0-1 相似度：1 - |a-b|/max(|a|,|b|,eps)。"""
    denom = max(abs(a), abs(b), 1e-9)
    return max(0.0, 1.0 - abs(a - b) / denom)
