"""修订教练 / rebuttal 审计：评审意见 → 结构化路线图；rebuttal 草稿覆盖审计。

- revision_coach(comments_text)：评审意见文本 → 路线图列表。每条意见含原文、
  类型（CRITICAL/MAJOR/MINOR）、位置（章节/图表）、回应计划项。
- rebuttal_audit(rebuttal_text, comments)：rebuttal 草稿 vs 评审意见。逐条判断
  是否被回应；未覆盖 → 未回应清单；fail-closed：无法判定时按未回应计。
"""
from __future__ import annotations

import re

# 严重度信号词（确定性关键词分类）
_CRITICAL_HINTS = [
    "wrong", "incorrect", "invalid", "fatal", "reject", "unacceptable",
    "fundamental", "contradict", "fails", "错误", "有误", "不成立", "无法成立",
    "重大缺陷", "致命", "否决",
]
_MINOR_HINTS = [
    "typo", "minor", "suggest", "could", "maybe", "cosmetic", "format",
    "style", "wording", "笔误", "小问题", "建议", "可选", "格式", "措辞",
]
_MAJOR_HINTS = [
    "should", "must", "unclear", "missing", "uncertain", "需要", "必须",
    "补充", "不清楚", "缺失", "存疑",
]

# 位置信号词
_LOCATION_HINTS = [
    "abstract", "introduction", "method", "methods", "experiment", "experiments",
    "result", "results", "conclusion", "figure", "figures", "table", "tables",
    "reference", "references", "related work",
    "摘要", "引言", "方法", "实验", "结果", "结论", "图", "表", "参考文献", "相关工作",
]

_PLAN_TEMPLATES = {
    "CRITICAL": [
        "定位并复现该问题，给出最小反例或错误证据",
        "修正方法/实验并补充新证据（重跑或新增对照）",
        "在回应中给出修改前后对比与影响范围说明",
    ],
    "MAJOR": [
        "逐条回应并说明具体改动位置（章节/页码）",
        "必要时补充实验、文献或数据证据",
    ],
    "MINOR": [
        "直接修正并在回应中列出修改清单",
    ],
}

# 回应覆盖判定用的停用词（不作为锚点）
_STOP = {
    "the", "and", "for", "with", "this", "that", "are", "not", "but", "you",
    "your", "can", "should", "must", "have", "has", "had", "was", "were",
    "will", "would", "could", "from", "into", "about", "more", "also", "than",
    "then", "there", "their", "what", "when", "which", "while", "section",
    "paper", "please", "comment",
}

# 评论起始行：编号/短横/加粗/标题/Comment N/意见 N
# "Reviewer #N" / "Reviewers?" 视为表头，作为前缀合并到下一条编号意见
_HEADER_LINE = re.compile(r"^\s*Reviewer\s*#?\d*\b|^\s*Reviewers?\b", re.IGNORECASE)
_COMMENT_START = re.compile(
    r"^\s*(?:R?\d+\s*[.)、]|[–—-]\s+|\*{1,2}[^*]+\*{1,2}\s*:?\s*$"
    r"|#{1,4}\s+|Comment\s*\d+|意见\s*\d+)",
    re.IGNORECASE,
)


def split_comments(text: str) -> list[str]:
    """把评审意见文本切成逐条意见：结构化行标（编号/短横/加粗/标题）为界，
    "Reviewer #N" 表头行作为前缀合并到下一条编号意见，不单独成条。"""
    if not text or not text.strip():
        return []
    comments: list[str] = []
    cur: list[str] = []
    header_prefix = ""
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            if cur:
                comments.append(" ".join(cur))
                cur = []
            continue
        # 表头行：不单独成条，存为前缀，合并到下一条非表头行
        if _HEADER_LINE.match(line):
            header_prefix = stripped
            continue
        # 遇到编号/标记行时，若有积累先落盘
        if _COMMENT_START.match(line) and cur:
            comments.append(" ".join(cur))
            cur = []
        # 组装：表头前缀 + 当前行
        if header_prefix:
            cur.append(f"{header_prefix} {stripped}")
            header_prefix = ""
        else:
            cur.append(stripped)
    if cur:
        comments.append(" ".join(cur))
    return [c for c in (s.strip() for s in comments) if c]


def classify_severity(comment: str) -> str:
    """按关键词信号分类意见严重度：CRITICAL / MAJOR / MINOR。"""
    low = (comment or "").lower()
    if any(h in low for h in _CRITICAL_HINTS):
        return "CRITICAL"
    if any(h in low for h in _MINOR_HINTS) and not any(h in low for h in _MAJOR_HINTS):
        return "MINOR"
    return "MAJOR"


def locate(comment: str) -> str:
    """检测意见涉及的位置（章节/图表）；无命中时为「全文」。"""
    low = (comment or "").lower()
    hits = [h for h in _LOCATION_HINTS if h in low]
    return "、".join(hits) if hits else "全文"


def revision_coach(comments_text: str, *, paper_id: str = "", layout=None) -> dict:
    """评审意见文本 → 结构化路线图列表。

    Args:
        comments_text: 评审意见原文（多条意见用编号/空行分隔）。
        paper_id / layout: 给定时落盘 projects/{paper_id}/research/rebuttal_plan.json。

    Returns:
        dict：{ok, total, roadmap: [{index, comment, type, location, plan}],
        summary: {critical, major, minor}}。空输入 → ok=False。
    """
    comments = split_comments(comments_text)
    if not comments:
        return {"ok": False, "error": "评审意见为空", "roadmap": [],
                "summary": {"critical": 0, "major": 0, "minor": 0}}
    roadmap = []
    counts = {"critical": 0, "major": 0, "minor": 0}
    for i, c in enumerate(comments, 1):
        sev = classify_severity(c)
        counts[sev.lower()] += 1
        roadmap.append({
            "index": i,
            "comment": c,
            "type": sev,
            "location": locate(c),
            "plan": list(_PLAN_TEMPLATES[sev]),
        })
    out = {"ok": True, "total": len(comments), "roadmap": roadmap,
           "summary": counts}
    if paper_id and layout is not None:
        _persist(layout, paper_id, "rebuttal_plan.json", out)
    return out


def rebuttal_audit(rebuttal_text: str, comments, *, paper_id: str = "",
                   layout=None) -> dict:
    """rebuttal 草稿 vs 评审意见：逐条审计是否被回应，fail-closed。

    Args:
        rebuttal_text: rebuttal 草稿全文。
        comments: 评审意见文本（str）或意见列表（list[str]）。
        paper_id / layout: 给定时落盘 rebuttal_audit.json。

    Returns:
        dict：{ok, total, addressed, unaddressed: [{index, comment, type}],
        coverage, pass}。空意见 → ok=False；空 rebuttal → 全部未回应。
    """
    if isinstance(comments, str):
        comment_list = split_comments(comments)
    else:
        comment_list = [str(c).strip() for c in (comments or []) if str(c).strip()]
    if not comment_list:
        return {"ok": False, "error": "评审意见为空", "total": 0, "addressed": 0,
                "unaddressed": [], "coverage": 0.0, "pass": False}
    rebuttal_low = (rebuttal_text or "").lower()
    addressed, unaddressed = 0, []
    for i, c in enumerate(comment_list, 1):
        sev = classify_severity(c)
        if _covered(c, rebuttal_low):
            addressed += 1
        else:
            # fail-closed：未覆盖/无法判定一律计为未回应
            unaddressed.append({"index": i, "comment": c, "type": sev})
    total = len(comment_list)
    out = {
        "ok": True,
        "total": total,
        "addressed": addressed,
        "unaddressed": unaddressed,
        "coverage": round(addressed / total, 3) if total else 0.0,
        "pass": not unaddressed,
    }
    if paper_id and layout is not None:
        _persist(layout, paper_id, "rebuttal_audit.json", out)
    return out


def _anchors(comment: str) -> list[str]:
    """提取意见的判别锚点：ASCII 长词（≥4 字符，去停用词）+ 中文 2-gram。"""
    out: list[str] = []
    for w in re.findall(r"[a-zA-Z]{4,}", comment):
        lw = w.lower()
        if lw not in _STOP and lw not in out:
            out.append(lw)
    for m in re.findall(r"[\u4e00-\u9fff]{2,}", comment):
        for j in range(len(m) - 1):
            g = m[j:j + 2]
            if g not in out:
                out.append(g)
    return out[:12]


def _covered(comment: str, rebuttal_low: str) -> bool:
    """覆盖判定：锚点命中 ≥1 或逐字引用意见片段 → 已回应。"""
    if not rebuttal_low.strip():
        return False
    norm_comment = " ".join(comment.lower().split())
    if len(norm_comment) <= 40 and norm_comment in " ".join(rebuttal_low.split()):
        return True
    anchors = _anchors(comment)
    if not anchors:
        return False
    return any(a in rebuttal_low for a in anchors)


def _persist(layout, paper_id: str, filename: str, data: dict) -> None:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / filename).write_text(
        _json_dumps(data), encoding="utf-8"
    )


def _json_dumps(data: dict) -> str:
    import json
    return json.dumps(data, ensure_ascii=False, indent=2)
