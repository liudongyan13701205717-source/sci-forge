"""编辑决策标准：7 维度质量 rubric + Accept/Minor/Major/Reject 判据矩阵 + IRON RULE 裁决。

IRON RULES（代码化）：
  - 只读：本模块不写任何文件、不改稿件；
  - 每个 CRITICAL 问题必须在编辑决定中显式裁决（adjudications 给出裁决值），
    否则 editorial_decision 抛 ValueError（fail-closed）；
  - unaddressed / wontfix 的 CRITICAL → 强制 Reject。

判据矩阵（predict_verdict，按序评估、命中即返回）：
  1. n_critical > 0        → Reject（存在未裁决 CRITICAL）
  2. rubric 均分 < 2.0     → Reject
  3. 均分 < 3.0 或 n_major >= 3 → Major
  4. 均分 < 4.0 或 n_major >= 1 → Minor
  5. 否则                  → Accept

predict_verdict 为裸规则（calibration 预测用，无裁决门）；受治理路径是
editorial_decision（强制 CRITICAL 裁决）。
"""

from __future__ import annotations

import re

# 7 维度质量 rubric：novelty/rigor/clarity/soundness/statistics/reproducibility/significance
# 每维 1-5 分判据文字。
RUBRIC: dict[str, dict[int, str]] = {
    "novelty": {
        1: "无新意：重复已有工作，未声明任何差异点。",
        2: "增量微弱：仅在已有方法上做小改动，差异点模糊。",
        3: "有明确改进：与已有工作可比，但差异点单薄。",
        4: "较清晰的新贡献：差异点明确且与相关工作有对照。",
        5: "显著新贡献：研究缺口明确，贡献超越已有工作并可辨识。",
    },
    "rigor": {
        1: "方法缺失或不可信：无建模/推导，步骤无法追踪。",
        2: "方法粗糙：关键步骤含糊，无公式或形式化。",
        3: "方法基本完整：有建模与步骤，但细节与条件不足。",
        4: "方法扎实：推导/形式化完整，支撑实验设计。",
        5: "方法严密：形式化+条件+推导闭环，可直接追踪验证。",
    },
    "clarity": {
        1: "难以理解：结构缺失、术语混乱、结论与方法脱节。",
        2: "可读性差：缺少结构化章节或大量占位。",
        3: "基本可读：主线清楚但表达与组织有待打磨。",
        4: "清晰：结构完整、表达准确、图表辅助得当。",
        5: "范例级清晰：结构、语言与呈现均无可挑剔。",
    },
    "soundness": {
        1: "结论不成立：证据链断裂或存在逻辑错误。",
        2: "证据薄弱：无基线/对照，结论与证据不匹配。",
        3: "结论部分成立：有基线对比但缺消融/稳健性。",
        4: "结论可信：基线+消融+局限讨论齐备。",
        5: "结论严密：多重证据互证，替代解释已排除。",
    },
    "statistics": {
        1: "无统计支撑：无显著性检验或不确定性报告。",
        2: "统计薄弱：仅有单次结果或均值，无方差。",
        3: "统计基本达标：有显著性检验但缺多重比较校正。",
        4: "统计充分：显著性+方差/置信区间+重复实验。",
        5: "统计严谨：效应量、校准与稳健性检验齐备。",
    },
    "reproducibility": {
        1: "不可复现：无代码/数据，无超参数。",
        2: "复现困难：披露不完整，缺关键细节。",
        3: "可部分复现：有超参数或种子但缺代码/数据。",
        4: "可复现：代码或数据可得，披露完整。",
        5: "完全可复现：代码+数据+种子+环境齐备。",
    },
    "significance": {
        1: "无意义：无法回答 So-what，无应用价值。",
        2: "意义存疑：应用边界不清，影响未被论证。",
        3: "有一定意义：有明确应用场景但影响有限。",
        4: "意义明确：现实影响与应用前景论证充分。",
        5: "影响深远：多领域适用性/部署价值被有力论证。",
    },
}

VERDICT_LABELS = ("Accept", "Minor", "Major", "Reject")

# 裁决值域（editorial_decision adjudications）
_ALLOWED_ADJUDICATIONS = ("addressed", "countered", "unaddressed", "wontfix")

# 裁决为"已解决"的值
_RESOLVED_ADJUDICATIONS = ("addressed", "countered")


def _has(text: str, *pats: str) -> bool:
    return any(re.search(p, text, re.I) for p in pats)


def score_rubric(text: str, stats: dict | None = None) -> dict[str, int]:
    """确定性 1-5 打分（无 LLM、无网络）：按 7 维度从文本特征映射。

    每维基线 2 分，文本中出现对应证据各 +1，封顶 5、保底 1。
    stats：panel._stats() 产出的文本统计（可选；缺省从 text 重算）。
    """
    text = text or ""
    st = stats or {}
    chars = int(st.get("chars") or len(re.sub(r"\s+", "", text)))
    tables = int(
        st.get("tables")
        or (text.count("|") // 10 if text.count("|") > 3 else 0)
    )
    has_formula = bool(
        st.get("has_formula", re.search(r"\$|\\frac|\\sum", text))
    )
    has_refs = bool(
        st.get("has_references", _has(text, r"参考文献|references", r"\[\d+\]", r"\bdoi\b", r"\barxiv\b"))
    )
    has_limits = bool(
        st.get("has_limitations", _has(text, r"局限|limitation", r"威胁效度|threats\s+to\s+validity"))
    )

    # novelty：研究缺口 / 贡献声明 / 与已有工作对照
    n = 2
    if _has(text, r"研究缺口|research\s+gap|尚未(被)?(研究|解决)|open\s+problem|新颖|novel"):
        n += 1
    if _has(text, r"贡献(如下|包括|是)|贡献：|contributions?\s+(are|include|of\s+this)|we\s+propose|我们提出"):
        n += 1
    if _has(text, r"与(已有|现有|先前)工作|related\s+work|prior\s+work|相比"):
        n += 1

    # rigor：公式/形式化、表格、参考文献
    r = 2
    if has_formula:
        r += 1
    if tables:
        r += 1
    if has_refs:
        r += 1

    # clarity：篇幅 + 结构标题
    c = 2
    if chars > 1500:
        c += 1
    if chars > 4000:
        c += 1
    if _has(text, r"#+\s", r"摘要|abstract", r"结论|conclusion"):
        c += 1

    # soundness：基线/对照、消融/敏感性、局限讨论
    s = 2
    if _has(text, r"基线|baseline|对照|control"):
        s += 1
    if _has(text, r"消融|ablation|敏感性分析|sensitivity\s+analysis"):
        s += 1
    if has_limits:
        s += 1

    # statistics：显著性检验、不确定性、重复实验
    t = 2
    if _has(text, r"p\s*[<=]\s*0?\.?\d|p-value|显著性|significance\s+test"):
        t += 1
    if _has(text, r"置信区间|confidence\s+interval|95%|标准差|std|误差条|方差"):
        t += 1
    if _has(text, r"重复(实验|运行|10次)|方差分析|t\s*检验|anova|bootstrap|均值±"):
        t += 1

    # reproducibility：代码/数据可得、超参/种子、复现性表述
    p = 2
    if _has(text, r"代码(已)?(开源|公开)|code\s+(is\s+)?(available|released)|github\.com|开源"):
        p += 1
    if _has(text, r"数据集(已)?(公开|发布)|data\s+(is\s+)?available|超参数|hyperparameter|随机种子|\bseed\b"):
        p += 1
    if _has(text, r"复现|reproduc"):
        p += 1

    # significance：影响/意义、现实适用、部署价值
    g = 2
    if _has(text, r"意义|影响|impact|应用(前景|价值)|部署|deployment"):
        g += 1
    if _has(text, r"推广|泛化|实际(场景|应用)|real[- ]world|工业|临床应用"):
        g += 1
    if _has(text, r"多(数据集|领域|任务)|multi[- ]?(dataset|domain|task)"):
        g += 1

    def clip(x: int) -> int:
        return int(max(1, min(5, x)))

    return {
        "novelty": clip(n),
        "rigor": clip(r),
        "clarity": clip(c),
        "soundness": clip(s),
        "statistics": clip(t),
        "reproducibility": clip(p),
        "significance": clip(g),
    }


def predict_verdict(scores: dict, *, n_critical: int = 0, n_major: int = 0) -> str:
    """裸判据矩阵（calibration 预测用，无裁决门）→ Accept/Minor/Major/Reject。

    按序评估、命中即返回（见模块 docstring 判据矩阵）。
    """
    avg = sum(scores.values()) / len(scores) if scores else 0.0
    if n_critical > 0:
        return "Reject"
    if avg < 2.0:
        return "Reject"
    if avg < 3.0 or n_major >= 3:
        return "Major"
    if avg < 4.0 or n_major >= 1:
        return "Minor"
    return "Accept"


def editorial_decision(
    *,
    text: str,
    da_issues: list,
    adjudications: dict,
    stats: dict | None = None,
) -> dict:
    """受治理的编辑决定（IRON RULE 执行点）。

    - 只读：不写任何文件、不改稿件；
    - 每个 CRITICAL 问题（da_issues 中 severity=CRITICAL）必须在
      adjudications 中显式裁决且裁决值合法，否则抛 ValueError（fail-closed）；
    - 裁决值域：addressed（已落实）/ countered（论点被作者反驳）/
      unaddressed / wontfix；后两者视为未解决 → 强制 Reject；
    - 其余按 predict_verdict 判据矩阵（7 维 rubric 均分 + MAJOR 计数）。

    adjudications：{issue_id: 裁决值}；未引用 CRITICAL 的多余键记入
    unknown_adjudications 警告。
    """
    issues = [i for i in (da_issues or []) if isinstance(i, dict)]
    criticals: list[dict] = []
    for idx, i in enumerate(issues):
        if str(i.get("severity", "")).upper() == "CRITICAL":
            criticals.append({
                "id": str(i.get("id") or f"critical-{idx + 1}"),
                "message": str(i.get("message") or i.get("text") or ""),
            })

    adj = {str(k): str(v).lower() for k, v in (adjudications or {}).items()}
    missing = [c["id"] for c in criticals if c["id"] not in adj]
    invalid = [
        c["id"] for c in criticals
        if c["id"] in adj and adj[c["id"]] not in _ALLOWED_ADJUDICATIONS
    ]
    if missing or invalid:
        raise ValueError(
            "iron rule: 以下 CRITICAL 未在编辑决定中显式裁决或裁决值非法"
            f"（缺失: {missing or '—'} / 非法: {invalid or '—'}；"
            f"允许裁决值: {', '.join(_ALLOWED_ADJUDICATIONS)}）"
        )

    resolved_ids = [
        c["id"] for c in criticals if adj.get(c["id"]) in _RESOLVED_ADJUDICATIONS
    ]
    unresolved_ids = [c["id"] for c in criticals if c["id"] not in resolved_ids]

    scores = score_rubric(text, stats)
    n_major = sum(
        1 for i in issues if str(i.get("severity", "")).upper() == "MAJOR"
    )

    reasons: list[str] = []
    if unresolved_ids:
        verdict = "Reject"
        reasons.append(f"未解决 CRITICAL 强制 Reject: {unresolved_ids}")
    else:
        verdict = predict_verdict(scores, n_critical=0, n_major=n_major)
        if criticals:
            reasons.append(
                f"{len(criticals)} 个 CRITICAL 已裁决（addressed/countered），不再阻塞"
            )

    critical_ids = {c["id"] for c in criticals}
    return {
        "ok": True,
        "verdict": verdict,
        "scores": scores,
        "rubric_text": {k: RUBRIC[k][scores[k]] for k in scores},
        "n_major": n_major,
        "criticals_total": len(criticals),
        "criticals_resolved": len(resolved_ids),
        "adjudications": adj,
        "unknown_adjudications": [k for k in adj if k not in critical_ids],
        "reasons": reasons,
    }
