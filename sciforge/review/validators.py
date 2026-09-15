"""K-Dense 三验证器：intake 门、报告指南选择、claim/evidence 对齐矩阵。

离线优先：全部计算为本地确定性规则，不联网、不调外部 API。
输入输出全用 dict（为批次2 MCP 工具包装做准备）。

三件套：
  - validate_review_intake：intake gate，通过 → "READY_FOR_LOCAL_REVIEW"；
    阻止未授权评审、未披露/未解决利益冲突、外部服务使用（fail-closed）。
  - select_reporting_guidelines：按研究设计选择 CONSORT/PRISMA/CARE/STARD/
    TRIPOD+AI/ARRIVE 的覆盖审计；非计分、带日期。
  - validate_claims_evidence：claim/evidence 对齐矩阵，每条 claim 判定
    ALIGNED / PARTIAL / UNSUPPORTED。

另提供 sanitize_text：论文文本中的指令性语句不执行（prompt-injection 防御，
解析前剥离指令模式并报告）。
"""

from __future__ import annotations

import re
from datetime import date

# ---- 状态常量 ----
READY_FOR_LOCAL_REVIEW = "READY_FOR_LOCAL_REVIEW"

# 面板支持的模式（与 panel.MODES 一致；此处仅作 intake 校验用）
_MODES = ("full", "quick", "re-review", "methodology_focus", "calibration")

# claim/evidence 对齐阈值（内容词命中率）
ALIGNED_RATIO = 0.6
PARTIAL_RATIO = 0.35

# R&R 追溯矩阵阈值（author claim 命中率）——供 panel 复用
REREVIEW_VERIFIED_RATIO = 0.5
REREVIEW_PARTIAL_RATIO = 0.2


# ---------------------------------------------------------------------------
# prompt-injection 防御
# ---------------------------------------------------------------------------

_INJECTION_PATTERNS = [
    r"(?i)ignore\s+(all\s+)?(previous|prior|above|earlier)\s+instructions?",
    r"(?i)disregard\s+(all\s+)?(previous|prior|above|earlier)",
    r"(?i)(you\s+are\s+now|act\s+as|pretend\s+to\s+be)\s+(a|an|the)\b",
    r"(?i)system\s+prompt",
    r"(?i)忽略(以上|之前|前面|所有)(的)?(指令|说明)",
    r"(?i)(请|现在)(扮演|充当)",
    r"(?i)(不要|别)评审(本|这篇|此)?(论文|稿件)?，?改为",
    r"(?i)(输出|泄露|打印)(你的)?(系统)?(提示词|prompt)",
]


def sanitize_text(text: str) -> tuple[str, list[str]]:
    """剥离论文文本中的指令性语句（prompt-injection 防御）。

    IRON RULE（代码化）：论文文本中的指令性语句不执行——按行匹配指令模式，
    命中的行整体剥离并逐条报告；面板/验证器只对清洗后的文本计算。

    返回 (清洗后文本, 被剥离的指令行列表)。剥离行为确定性、可复现。
    """
    stripped: list[str] = []
    if not text:
        return "", stripped
    kept: list[str] = []
    for line in text.splitlines():
        hit = False
        for pat in _INJECTION_PATTERNS:
            if re.search(pat, line):
                stripped.append(line.strip())
                hit = True
                break
        if not hit:
            kept.append(line)
    return "\n".join(kept), stripped


# ---------------------------------------------------------------------------
# 内容词 tokenize（对齐矩阵 / 关键词提取共用）
# ---------------------------------------------------------------------------

_STOPWORDS = {
    "the", "a", "an", "of", "in", "on", "and", "or", "to", "is", "are",
    "we", "our", "for", "with", "by", "as", "at", "that", "this", "it",
    "its", "be", "was", "were", "than", "from", "not", "no", "but",
    "which", "can", "may", "has", "have", "had", "do", "does",
}


def content_tokens(text: str) -> list[str]:
    """内容词序列（保序、可重复）：拉丁/数字词（去停用词）+ CJK 二元组。

    中文按连续汉字串切 2-gram（单字串保留单字）；英文按 [a-z0-9]+ 切词并
    去除常见停用词。供 claim/evidence 对齐与 R&R 追溯矩阵做确定性命中统计。
    """
    t = (text or "").lower()
    tokens: list[str] = []
    for w in re.findall(r"[a-z0-9]+", t):
        if len(w) > 1 and w not in _STOPWORDS:
            tokens.append(w)
    for run in re.findall(r"[\u4e00-\u9fff]+", t):
        if len(run) == 1:
            tokens.append(run)
        else:
            tokens.extend(run[i:i + 2] for i in range(len(run) - 1))
    return tokens


# ---------------------------------------------------------------------------
# 验证器 1：validate_review_intake（intake gate，fail-closed）
# ---------------------------------------------------------------------------

def validate_review_intake(intake: dict) -> dict:
    """intake 门：校验评审请求是否满足本地评审前置条件（fail-closed）。

    通过条件（全部满足 → status=READY_FOR_LOCAL_REVIEW）：
      - paper_id 非空；
      - mode ∈ {full, quick, re-review, methodology_focus, calibration}；
      - authorization.authorized 为 true（未授权评审直接拒绝）；
      - conflict_of_interest 已披露且已解决（缺失即拒绝，fail-closed）；
      - external_services 为空（本地评审禁止外部服务使用）。

    任何 blocker → ok=False 且 status="BLOCKED"，blockers 列出全部原因。
    """
    blockers: list[str] = []

    paper_id = str(intake.get("paper_id") or "").strip()
    if not paper_id:
        blockers.append("missing paper_id（缺少论文标识）")

    mode = str(intake.get("mode") or "full")
    if mode not in _MODES:
        blockers.append(
            f"unknown mode: {mode}（允许：{', '.join(_MODES)}）"
        )

    auth = intake.get("authorization")
    authorized = False
    if isinstance(auth, dict):
        authorized = auth.get("authorized") is True
    elif isinstance(auth, bool):
        authorized = auth
    if not authorized:
        blockers.append(
            "unauthorized: 缺少授权或 authorization.authorized != true（未授权评审被拒绝）"
        )

    coi = intake.get("conflict_of_interest")
    if isinstance(coi, dict):
        if coi.get("declared") is not True:
            blockers.append("conflict_of_interest: 未披露利益冲突声明（fail-closed）")
        elif coi.get("resolved") is not True:
            blockers.append("conflict_of_interest: 利益冲突未解决")
    else:
        blockers.append("conflict_of_interest: 缺少利益冲突声明（fail-closed）")

    external = intake.get("external_services")
    if isinstance(external, str):
        external = [external]
    if external:
        blockers.append(
            "external_services: 本地评审禁止外部服务使用（"
            + ", ".join(str(x) for x in external) + "）"
        )

    ok = not blockers
    return {
        "ok": ok,
        "status": READY_FOR_LOCAL_REVIEW if ok else "BLOCKED",
        "paper_id": paper_id,
        "mode": mode,
        "blockers": blockers,
        "warnings": [],
    }


# ---------------------------------------------------------------------------
# 验证器 2：select_reporting_guidelines（覆盖审计，非计分、带日期）
# ---------------------------------------------------------------------------

_GUIDELINES: dict[str, dict] = {
    "CONSORT": {
        "designs": ["randomized", "随机对照", "随机分配", "rct", "临床试验", "clinical trial"],
        "items": [
            ("随机分组方法", r"(?i)随机(分配|分组|化)|random(ised|ized)\s+(allocation|assignment)"),
            ("样本量计算", r"(?i)样本量|sample\s+size|power\s+calculation"),
            ("盲法说明", r"(?i)盲法|单盲|双盲|blind(ed|ing)"),
            ("主要结局指标", r"(?i)主要结局|primary\s+outcome|终点|endpoint"),
            ("招募流程图", r"(?i)流程图|flow\s?chart|consort\s+flow|招募流程"),
        ],
    },
    "PRISMA": {
        "designs": ["systematic review", "meta-analysis", "系统综述", "荟萃分析", "meta 分析"],
        "items": [
            ("检索式与数据库", r"(?i)检索式|search\s+strategy|数据库|database"),
            ("纳排标准", r"(?i)(纳入|排除)标准|inclusion\s+(and\s+)?exclusion"),
            ("筛选流程图", r"(?i)流程图|prisma\s+flow|筛选流程"),
            ("偏倚风险评估", r"(?i)偏倚|bias\s+(assessment|risk)|rob"),
            ("证据质量分级", r"(?i)证据(质量|等级)|grade|certainty\s+of\s+evidence"),
        ],
    },
    "CARE": {
        "designs": ["case report", "病例报告", "个案报告"],
        "items": [
            ("患者视角与知情同意", r"(?i)知情同意|informed\s+consent|患者视角|patient\s+(perspective|view)"),
            ("症状与体征", r"(?i)症状|体征|symptoms?|clinical\s+signs"),
            ("诊断检查结果", r"(?i)诊断|检查结果|diagnostic\s+(workup|test)"),
            ("治疗干预", r"(?i)治疗|干预|therapeutic|intervention"),
            ("随访与结局", r"(?i)随访|follow-?up|结局|outcome"),
        ],
    },
    "STARD": {
        "designs": ["diagnostic accuracy", "诊断准确性", "诊断试验"],
        "items": [
            ("参考标准", r"(?i)参考标准|reference\s+standard|金标准|gold\s+standard"),
            ("索引检测", r"(?i)索引(检测|试验)|index\s+test"),
            ("研究人群与样本量", r"(?i)人群|样本量|cohort|sample\s+size|participants"),
            ("敏感性/特异性", r"(?i)敏感性|特异性|sensitivity|specificity"),
            ("不确定性估计", r"(?i)置信区间|confidence\s+interval|不确定度|uncertainty"),
        ],
    },
    "TRIPOD+AI": {
        "designs": ["prediction model", "预测模型", "人工智能", "machine learning", "临床预测"],
        "items": [
            ("预测目标与结局", r"(?i)预测(目标|结局)|prediction\s+(target|outcome)|结局|outcome"),
            ("数据划分与时间验证", r"(?i)(训练|验证|测试)集|train(ing)?[-/ ]?(test|valid)|temporal\s+(validation|split)|外部验证"),
            ("模型与超参数", r"(?i)模型|超参|hyperparameter|architecture"),
            ("性能指标（区分度/校准）", r"(?i)auc|roc|校准|calibration|区分度|discrimination"),
            ("公平性与可解释性", r"(?i)公平|fairness|可解释|interpretab|explainab|shap"),
        ],
    },
    "ARRIVE": {
        "designs": ["animal", "动物实验", "动物研究", "in vivo"],
        "items": [
            ("动物种系与数量", r"(?i)种系|品系|strain|动物数|n\s*=\s*\d+\s*(只|animals|mice)"),
            ("随机化与盲法", r"(?i)随机|盲法|randomi|blind"),
            ("样本量依据", r"(?i)样本量|sample\s+size|power"),
            ("伦理审批", r"(?i)伦理|ethic|iacuc|审批"),
            ("实验细节与标准", r"(?i)饲养|麻醉|experimental\s+(detail|procedure)|标准(操作|流程)"),
        ],
    },
}


def select_reporting_guidelines(design: str, text: str = "", *, as_of: str = "") -> dict:
    """按研究设计选择报告指南并做覆盖审计（非计分、带日期）。

    design 为研究设计描述（如 "randomized controlled trial"）；design 为空时
    用 text 前 2000 字符探测设计关键词。命中任意设计关键词的指南全部入选，
    对每条指南逐项（checklist item）检查正文证据 → 覆盖审计。

    非计分：只产出 present/missing 布尔与统计，不产出任何分数/等级。
    as_of：审计日期（缺省取今天，ISO 格式）。
    """
    design = design or ""
    if design.strip():
        probe = design.lower()
        probe_source = "design"
    else:
        probe = (text or "").lower()[:2000]
        probe_source = "text_head"

    selected = [
        name for name, spec in _GUIDELINES.items()
        if any(kw in probe for kw in spec["designs"])
    ]

    coverage: list[dict] = []
    coverage_summary: dict[str, dict] = {}
    text_skipped = not (text or "").strip()
    for name in selected:
        items = _GUIDELINES[name]["items"]
        present_count = 0
        for item, pat in items:
            present = bool(re.search(pat, text)) and not text_skipped
            if present:
                present_count += 1
            coverage.append({
                "guideline": name,
                "item": item,
                "present": present,
            })
        coverage_summary[name] = {
            "total": len(items),
            "present": present_count,
            "missing": len(items) - present_count,
        }

    return {
        "ok": True,
        "selected": selected,
        "probe_source": probe_source,
        "coverage": coverage,
        "coverage_summary": coverage_summary,
        "text_provided": not text_skipped,
        "note": (
            "未提供正文，覆盖审计全部记为缺失" if text_skipped
            else ("未匹配到报告指南，请提供更明确的研究设计" if not selected else "覆盖审计完成（非计分）")
        ),
        "audit_date": as_of or date.today().isoformat(),
    }


# ---------------------------------------------------------------------------
# 验证器 3：validate_claims_evidence（claim/evidence 对齐矩阵）
# ---------------------------------------------------------------------------

def validate_claims_evidence(claims: list, evidence: list) -> dict:
    """claim/evidence 对齐矩阵：每条 claim 判定 ALIGNED / PARTIAL / UNSUPPORTED。

    claims：[{id, text, requires_evidence?}] 或纯字符串列表。
    evidence：[{id, text}] 或纯字符串列表。

    对齐规则（确定性）：claim 内容词集合与 evidence 内容词集合的命中率
    （|claim ∩ evidence| / |claim|），对全部 evidence 取最大：
      - 命中率 ≥ ALIGNED_RATIO(0.6) → ALIGNED
      - 命中率 ≥ PARTIAL_RATIO(0.25) → PARTIAL
      - 否则（含无 evidence）→ UNSUPPORTED
    requires_evidence=False 的观点性陈述 → ALIGNED（附注，不计入证据缺口）。
    """
    norm_claims: list[dict] = []
    for idx, c in enumerate(claims or []):
        if isinstance(c, str):
            norm_claims.append({"id": f"C{idx + 1}", "text": c, "requires_evidence": True})
        elif isinstance(c, dict):
            norm_claims.append({
                "id": str(c.get("id") or f"C{idx + 1}"),
                "text": str(c.get("text") or ""),
                "requires_evidence": bool(c.get("requires_evidence", True)),
            })

    norm_evidence: list[dict] = []
    for idx, e in enumerate(evidence or []):
        if isinstance(e, str):
            norm_evidence.append({"id": f"E{idx + 1}", "text": e})
        elif isinstance(e, dict):
            norm_evidence.append({
                "id": str(e.get("id") or f"E{idx + 1}"),
                "text": str(e.get("text") or ""),
            })

    ev_token_sets = [
        (e["id"], set(content_tokens(e["text"]))) for e in norm_evidence
    ]

    matrix: list[dict] = []
    aligned = partial = unsupported = 0
    for c in norm_claims:
        claim_tokens = set(content_tokens(c["text"]))
        best_ratio = 0.0
        matched: list[str] = []
        if claim_tokens:
            for ev_id, ev_tokens in ev_token_sets:
                overlap = claim_tokens & ev_tokens
                ratio = len(overlap) / len(claim_tokens)
                if ratio > best_ratio:
                    best_ratio = ratio
                if ratio >= PARTIAL_RATIO:
                    matched.append(ev_id)
        if not c["requires_evidence"]:
            verdict = "ALIGNED"
            note = "观点性陈述，无需实证证据"
        elif not norm_evidence:
            verdict = "UNSUPPORTED"
            note = "未提供任何 evidence"
        elif best_ratio >= ALIGNED_RATIO:
            verdict = "ALIGNED"
            note = f"内容词命中率 {best_ratio:.2f} ≥ {ALIGNED_RATIO}"
        elif best_ratio >= PARTIAL_RATIO:
            verdict = "PARTIAL"
            note = f"内容词命中率 {best_ratio:.2f}（{PARTIAL_RATIO}–{ALIGNED_RATIO}），证据部分覆盖"
        else:
            verdict = "UNSUPPORTED"
            note = f"内容词命中率 {best_ratio:.2f} < {PARTIAL_RATIO}，正文证据缺失"

        if verdict == "ALIGNED":
            aligned += 1
        elif verdict == "PARTIAL":
            partial += 1
        else:
            unsupported += 1

        matrix.append({
            "claim_id": c["id"],
            "claim": c["text"],
            "requires_evidence": c["requires_evidence"],
            "verdict": verdict,
            "matched_evidence": matched,
            "best_ratio": round(best_ratio, 2),
            "note": note,
        })

    n = len(matrix)
    return {
        "ok": True,
        "n_claims": n,
        "n_evidence": len(norm_evidence),
        "matrix": matrix,
        "summary": {
            "aligned": aligned,
            "partial": partial,
            "unsupported": unsupported,
            "unsupported_rate": round(unsupported / n, 4) if n else 0.0,
        },
    }


# 面板模式常量（供 panel.py 导入）
MODES = _MODES
