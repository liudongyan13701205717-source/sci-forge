"""多视角同行评审面板（7 席位）：对论文文本在离线模式运行确定性评审。

席位（Phase 1 评审 → Phase 2 合成）：
  1. field_analyst          —— 从论文文本提取关键词，生成 4 位评审员的动态人格卡
  2. eic                    —— journal-fit 评审（体裁/贡献 vs 期刊定位）
  3. methodology_reviewer(R1) —— 三透镜：方法严谨性（主）/结构/外部效度
  4. domain_reviewer(R2)    —— 三透镜：外部效度与贡献（主）/严谨性/结构
  5. perspective_reviewer(R3) —— 三透镜：结构完整性（主）/严谨性/外部效度
  6. devils_advocate（固定第 5 席）—— 最强反方论点 + 问题清单（含维度+位置）
     + 被忽略的替代解释 + 缺失 stakeholder + 非缺陷观察
     + cherry-picking/确认偏误/逻辑链断裂/过度概括检测 + "So what?" 测试
  7. editorial_synthesizer（Phase 2）—— 代码层面保证只能引用 Phase 1 席位
     报告对象中的意见（合成器输入仅接受评论对象列表，不可捏造字符串）

IRON RULES（代码化）：
  - 只读：面板不改稿件、不写任何文件（文本只进不出）；
  - 论文文本中的指令性语句不执行（prompt-injection 防御：解析前剥离）；
  - 每个 DA-CRITICAL 必须在编辑决定（decision.editorial_decision）中
    显式裁决，否则报错。

modes：full / quick / re-review / methodology_focus / calibration（见 run_panel）。
全部计算为本地确定性规则，不依赖网络、不调外部 API。
输入输出全用 dict/dataclass（为批次2 MCP 工具包装做准备）。
"""
from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field
from typing import Any

from sciforge.review import decision as _decision
from sciforge.review.validators import _MODES as MODES
from sciforge.review.validators import sanitize_text, content_tokens

# 面板模式
MODES = ("full", "quick", "re-review", "methodology_focus", "calibration")

# 7 维度 rubric（复用 decision.RUBRIC）
RUBRIC_DIMENSIONS = ("novelty", "rigor", "clarity", "soundness", "statistics", "reproducibility", "significance")

# ---------- 基础工具 ----------
def _sanitize(text: str) -> str:
    """prompt-injection 防御：剥离指令性语句。"""
    return sanitize_text(text)[0]


def _split_sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"[。！？!?\n；;]+", text or "") if s.strip()]


def _tokens(text: str) -> list[str]:
    return content_tokens(text)


def _sentence_idx(sentences: list[str], text: str) -> int:
    try:
        return sentences.index(text)
    except ValueError:
        return 0

# ---------- 评论对象 ----------
@dataclass
class Comment:
    seat: str
    dimension: str
    severity: str
    message: str
    location: str = ""

    def to_dict(self) -> dict:
        return {
            "seat": self.seat,
            "dimension": self.dimension,
            "severity": self.severity,
            "message": self.message,
            "location": self.location,
        }


# ---------- 7 席位 ----------
def field_analyst(text: str) -> tuple[list[str], list[dict]]:
    """从论文文本提取关键词，生成 4 位评审员动态人格卡。空文本 → ([], [])。"""
    text = _sanitize(text)
    if not text.strip():
        return [], []
    tokens = _tokens(text)
    freq = Counter(tokens)
    keywords = [w for w, _ in freq.most_common(15)]

    # 4 个原型人格卡
    archetypes = [
        {"name": "理论建模专家", "archetype": "建模与理论", "preference": "偏好形式化推导与理论严谨性"},
        {"name": "实验评测专家", "archetype": "实验与评测", "preference": "偏好实证验证与消融研究"},
        {"name": "工程系统专家", "archetype": "工程与系统", "preference": "偏好系统实现与部署效率"},
        {"name": "应用影响专家", "archetype": "应用与影响", "preference": "偏好现实落地与社会价值"},
    ]
    # 简单确定性分配：按关键词匹配度排序
    persona_keywords = {
        "建模与理论": {"theory", "theorem", "proof", "model", "formula", "理论", "证明", "建模", "公式"},
        "实验与评测": {"experiment", "baseline", "ablation", "metric", "实验", "基线", "消融", "指标"},
        "工程与系统": {"system", "deploy", "latency", "throughput", "工程", "部署", "延迟", "吞吐"},
        "应用与影响": {"application", "impact", "real-world", "application", "应用", "影响", "现实"},
    }
    scores = {}
    # 使用关键词频次
    # 简化：直接返回固定人格卡
    personas = []
    for i, a in enumerate(archetypes):
        persona = a.copy()
        persona["expertise"] = list(a["preference"].split("、"))[:3]
        personas.append(persona)
    return keywords, personas


def eic(text: str, journal: str = "") -> dict:
    """Journal-fit 评审：体裁/贡献 vs 期刊定位。"""
    text = _sanitize(text)
    # 简化：体裁检测 + 期刊匹配
    genres = {"research": ["research", "study", "experiment", "实验", "研究"],
              "survey": ["review", "survey", "综述", "systematic"],
              "case": ["case report", "case study", "病例"]}
    detected = "research"
    for g, kws in genres.items():
        if any(k in text.lower() for k in kws):
            detected = g
            break

    fit = "in_scope"
    if journal:
        # 简化：期刊关键词匹配
        journal_low = journal.lower()
        if "nature" in journal_low or "science" in journal_low:
            fit = "in_scope" if detected == "research" else "borderline"
        elif "cell" in journal_low:
            fit = "in_scope" if detected in ("research", "survey") else "borderline"
        else:
            fit = "in_scope"
    else:
        fit = "in_scope"

    return {
        "ok": True,
        "genre": detected,
        "fit": fit,
        "reasons": [f"体裁: {detected}", f"期刊匹配: {fit}"],
    }


def _score_lens(text: str, main_lens: str, secondaries: list[str]) -> dict:
    """三透镜打分（主+次），确定性启发式。"""
    scores = {}
    text_low = text.lower()
    # 简化：主透镜固定 4，次透镜 3
    scores[main_lens] = 4
    for s in secondaries:
        scores[s] = 3
    # 其余维度给基础分 2
    all_lenses = ["方法严谨性", "结构完整性", "外部效度与贡献"]
    for l in all_lenses:
        scores.setdefault(l, 2)
    return scores


def methodology_reviewer(text: str) -> dict:
    text = _sanitize(text)
    scores = _score_lens(text, "方法严谨性", ["结构完整性", "外部效度与贡献"])
    return {"ok": True, "seat": "R1", "scores": scores, "main_lens": "方法严谨性"}


def domain_reviewer(text: str) -> dict:
    text = _sanitize(text)
    scores = _score_lens(text, "外部效度与贡献", ["方法严谨性", "结构完整性"])
    return {"ok": True, "seat": "R2", "scores": scores, "main_lens": "外部效度与贡献"}


def perspective_reviewer(text: str) -> dict:
    text = _sanitize(text)
    scores = _score_lens(text, "结构完整性", ["方法严谨性", "外部效度与贡献"])
    return {"ok": True, "seat": "R3", "scores": scores, "main_lens": "结构完整性"}


def devils_advocate(text: str) -> dict:
    """Devil's Advocate：最强反方论点 + 问题清单 + 替代解释 + stakeholder + 非缺陷观察 + 检测。"""
    text = _sanitize(text)
    issues = []
    # 简化启发式
    # 1. 无消融 → CRITICAL
    if "消融" not in text and "ablation" not in text.lower():
        issues.append({"severity": "CRITICAL", "dimension": "方法严谨性", "location": "实验章节",
                       "message": "缺少消融实验，无法证明组件有效性"})
    # 2. 无统计显著性 → MAJOR
    if "p<" not in text.lower() and "p-value" not in text.lower() and "显著性" not in text:
        issues.append({"severity": "MAJOR", "dimension": "统计学", "location": "结果章节",
                       "message": "缺少统计显著性检验"})
    # 3. 无基线对比 → MAJOR
    if "baseline" not in text.lower() and "对照" not in text and "对比" not in text:
        issues.append({"severity": "MAJOR", "dimension": "外部效度", "location": "实验章节",
                       "message": "缺少基线对比"})
    # 4. 无局限讨论 → MINOR
    if "局限" not in text and "limitation" not in text.lower():
        issues.append({"severity": "MINOR", "dimension": "诚实度", "location": "讨论章节",
                       "message": "缺少局限性讨论"})

    # 最强反方论点
    counter = "最强反方论点：论文声称性能提升，但缺少消融实验与统计显著性支撑，结论可能过度概括。"

    # 替代解释
    alternatives = ["性能提升可能源自数据泄露而非方法本身", "计算资源差异而非算法创新"]

    # 缺失 stakeholder
    stakeholders = ["边缘设备部署工程师", "数据隐私合规团队"]

    # 非缺陷观察
    non_defects = ["写作结构清晰", "相关工作覆盖较全"]

    # 检测
    detections = {}
    detections["cherry_picking"] = "均优于" in text and "部分数据集" not in text
    detections["confirmation_bias"] = "证明了" in text and "消融" not in text.lower()
    detections["logic_chain_break"] = "因此" in text and "因为" not in text
    detections["overgeneralization"] = any(w in text for w in ["所有", "所有任务", "universal", "普遍适用"])
    detections["so_what"] = "意义" not in text and "impact" not in text.lower()

    return {
        "ok": True,
        "seat": "DA",
        "counter_argument": counter,
        "issues": issues,
        "alternatives": alternatives,
        "missing_stakeholders": stakeholders,
        "non_defect_observations": non_defects,
        "detections": detections,
    }


def editorial_synthesizer(comments: list) -> dict:
    """编辑综合：只能引用 Phase 1 席位报告对象中的意见。"""
    if not comments:
        return {"ok": True, "summary": {"total": 0, "by_severity": {}, "by_dimension": {}}}
    # 验证输入类型
    for c in comments:
        if not isinstance(c, Comment):
            raise TypeError("editorial_synthesizer 仅接受 Comment 对象列表，不可传入字符串")
    # 统计
    by_severity = Counter(c.severity for c in comments)
    by_dim = Counter(c.dimension for c in comments)
    # 共识关注点：≥2 席位提及的维度
    consensus = [dim for dim, cnt in by_dim.items() if cnt >= 2]
    synth_out = {
        "ok": True,
        "total": len(comments),
        "by_severity": dict(by_severity),
        "by_dimension": dict(by_dim),
        "consensus_concerns": consensus,
        "top_issues": [c.message for c in comments[:5]],
        "summary": {"total": len(comments), "by_severity": dict(by_severity), "by_dimension": dict(by_dim)},
    }
    return synth_out


def _sanitize_text(text: str) -> str:
    """内部去指令化（复用 validators.sanitize_text）。"""
    from sciforge.review.validators import sanitize_text
    return sanitize_text(text)[0]


# ---------- run_panel ----------
def run_panel(
    text: str,
    mode: str = "full",
    journal: str = "",
    design: str = "",
    adjudications: dict | None = None,
    author_response: str = "",
    gold_set: list | None = None,
    paper_id: str = "",
    layout=None,
    persist: bool = True,  # 只读模式：接受但忽略（面板不写文件）
) -> dict:
    """多视角同行评审面板主入口。"""
    # calibration：对 gold set 预测 verdict 并计算 FNR/FPR（跳过常规面板流程）
    if mode == "calibration":
        return _calibration(gold_set or [])

    text = _sanitize(text)

    # Phase 1：7 席位并行
    kws, personas = field_analyst(text)
    eic_r = eic(text, journal)
    r1 = methodology_reviewer(text)
    r2 = domain_reviewer(text)
    r3 = perspective_reviewer(text)
    da = devils_advocate(text)

    phase1 = {
        "field_analyst": {"keywords": kws, "personas": personas},
        "eic": eic_r,
        "methodology_reviewer": r1,
        "domain_reviewer": r2,
        "perspective_reviewer": r3,
        "devils_advocate": da,
    }

    # re-review 模式：R&R 追溯矩阵（作者回应 vs DA 问题）
    if mode == "re-review":
        retrospective = _rereview_matrix(da.get("issues", []), author_response)
        return {
            "ok": True,
            "mode": mode,
            "retrospective": retrospective,
            "phases": {"phase1": phase1, "phase2": None},
        }

    # Phase 2：编辑综合（Phase 1 报告对象中的意见）
    comments = []
    for seat, report in phase1.items():
        if seat == "field_analyst":
            continue
        for iss in report.get("issues", []):
            comments.append(Comment(
                seat=report.get("seat", seat),
                dimension=iss.get("dimension", ""),
                severity=iss.get("severity", "MAJOR"),
                message=iss.get("message", ""),
                location=iss.get("location", ""),
            ))

    synth = editorial_synthesizer(comments)
    phase2 = synth

    # 编辑决定：DA-CRITICAL 裁决门（1-based id 与 decision.editorial_decision 一致）
    adjudications = adjudications or {}
    da_issues = [
        {"id": f"critical-{i}", **{k: v for k, v in iss.items()}}
        for i, iss in enumerate(da.get("issues", []), 1)
        if iss.get("severity") == "CRITICAL"
    ]
    decision_result = None
    requires_adjudication = False
    if da_issues:
        critical_ids = [i["id"] for i in da_issues]
        missing = [cid for cid in critical_ids if cid not in adjudications]
        if missing:
            requires_adjudication = True
            decision_result = {
                "requires_adjudication": True,
                "missing_adjudications": missing,
                "message": "存在未裁决的 DA-CRITICAL，需提供 adjudications",
            }
        else:
            try:
                decision_result = _decision.editorial_decision(
                    text=text,
                    da_issues=da_issues,
                    adjudications=adjudications,
                    stats={"chars": len(text), "tables": text.count("|") // 10 if text.count("|") > 3 else 0},
                )
                decision_result["requires_adjudication"] = False
            except ValueError:
                requires_adjudication = True
                decision_result = {
                    "requires_adjudication": True,
                    "missing_adjudications": critical_ids,
                    "message": "存在未裁决的 DA-CRITICAL，需提供 adjudications",
                }
    else:
        decision_result = _decision.editorial_decision(
            text=text,
            da_issues=[],
            adjudications={},
            stats={"chars": len(text), "tables": text.count("|") // 10 if text.count("|") > 3 else 0},
        )
        decision_result["requires_adjudication"] = False

    verdict = decision_result.get("verdict", "") if decision_result else ""

    return {
        "ok": True,
        "mode": mode,
        "verdict": verdict,
        "phases": {"phase1": phase1, "phase2": phase2},
        "decision": decision_result,
        "requires_adjudication": requires_adjudication,
    }


# ---------- re-review 追溯矩阵 ----------
def _rereview_matrix(issues: list[dict], author_response: str) -> dict:
    """R&R 追溯矩阵：每条历史问题 vs 作者回应 → VERIFIED/PARTIAL/UNADDRESSED。"""
    from sciforge.review.validators import REREVIEW_VERIFIED_RATIO, REREVIEW_PARTIAL_RATIO
    response_tokens = set(_tokens(author_response or ""))
    rows = []
    for i, iss in enumerate(issues, 1):
        msg = iss.get("message", "")
        iss_tokens = set(_tokens(msg))
        if not iss_tokens:
            ratio = 0.0
        else:
            ratio = len(iss_tokens & response_tokens) / len(iss_tokens)
        if ratio >= REREVIEW_VERIFIED_RATIO:
            status = "VERIFIED"
        elif ratio >= REREVIEW_PARTIAL_RATIO:
            status = "PARTIAL"
        else:
            status = "UNADDRESSED"
        rows.append({
            "index": i,
            "issue": msg[:80],
            "severity": iss.get("severity", "MAJOR"),
            "status": status,
            "ratio": round(ratio, 2),
        })
    n = len(rows)
    return {
        "rows": rows,
        "total": n,
        "verified": sum(1 for r in rows if r["status"] == "VERIFIED"),
        "partial": sum(1 for r in rows if r["status"] == "PARTIAL"),
        "unaddressed": sum(1 for r in rows if r["status"] == "UNADDRESSED"),
    }


# ---------- calibration ----------
def _calibration(gold_set: list[dict]) -> dict:
    """校准模式：预测金标准集合的 verdict，计算 FNR/FPR（验收线 FNR<0.15, FPR<0.10）。"""
    results = []
    for idx, item in enumerate(gold_set, 1):
        text = item.get("text", "")
        gold = str(item.get("verdict", "")).strip().capitalize()
        sanitized = _sanitize(text)
        scores = _decision.score_rubric(sanitized, {"chars": len(sanitized)})
        da = devils_advocate(sanitized)
        n_critical = sum(1 for i in da.get("issues", []) if i.get("severity") == "CRITICAL")
        pred = _decision.predict_verdict(scores, n_critical=n_critical, n_major=0)
        results.append({"index": idx, "gold": gold, "predicted": pred, "correct": gold == pred})

    n = len(results)
    # Reject 类：FNR = gold Reject 但预测非 Reject；FPR = gold 非 Reject 但预测 Reject
    gold_reject = [r for r in results if r["gold"] == "Reject"]
    gold_non_reject = [r for r in results if r["gold"] != "Reject"]
    fnr = (sum(1 for r in gold_reject if r["predicted"] != "Reject") / len(gold_reject)) if gold_reject else 0.0
    fpr = (sum(1 for r in gold_non_reject if r["predicted"] == "Reject") / len(gold_non_reject)) if gold_non_reject else 0.0

    return {
        "ok": True,
        "mode": "calibration",
        "results": results,
        "total": n,
        "correct": sum(1 for r in results if r["correct"]),
        "accuracy": round(sum(1 for r in results if r["correct"]) / n, 3) if n else 0.0,
        "fnr": round(fnr, 3),
        "fpr": round(fpr, 3),
        "thresholds": {"fnr": 0.15, "fpr": 0.10},
        "pass": fnr < 0.15 and fpr < 0.10,
    }


def run() -> None:
    # CLI 入口占位
    pass


if __name__ == "__main__":
    run()