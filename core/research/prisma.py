"""PRISMA 系统综述协议：7 阶段流程 + 流程计数（identified/duplicates/screened/excluded/included）。

阶段：规划/scoping → 多库检索（记录查询语句，最少 3 个库，走 sciforge/science/api.py
门面，离线降级不崩）→ 筛选（title/abstract → 全文，排除必须带理由）→ 数据提取与
质量评估（risk-of-bias 简易 rubric：low/moderate/high）→ 主题综合（按主题分组）→
引文核验（sciforge.claims 延迟导入，包不存在时优雅降级跳过）→ 文档生成。

落盘 projects/{paper_id}/research/prisma.json + prisma.md（给定 paper_id + layout 时）。
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

# 默认检索库：文献领域免 key 连接器，取 3 个（PRISMA 要求多库，最少 3）
DEFAULT_DATABASES = ["openalex", "crossref", "arxiv"]

PHASES = ["planning", "search", "screening", "extraction", "synthesis",
          "verification", "reporting"]

# 纳入/排除筛选用的关键词由调用方给出；未给出时仅按「缺标题/缺摘要」排除


@dataclass
class PrismaReport:
    ok: bool
    topic: str = ""
    counts: dict = field(default_factory=dict)
    included: list = field(default_factory=list)
    themes: list = field(default_factory=list)
    verification: list = field(default_factory=list)
    queries: list = field(default_factory=list)
    phases: dict = field(default_factory=dict)
    notes: list = field(default_factory=list)
    offline: bool = False
    error: str = ""

    def to_dict(self) -> dict:
        return {k: getattr(self, k) for k in (
            "ok", "topic", "counts", "included", "themes", "verification",
            "queries", "phases", "notes", "offline", "error",
        )}

    def to_markdown(self) -> str:
        c = self.counts
        flow_lines = "\n".join(
            f"- {k}: {c.get(k, 0)}" for k in (
                "identified", "duplicates", "screened",
                "excluded_title_abstract", "full_text_assessed",
                "full_text_excluded", "included",
            )
        )
        themes = "\n".join(
            f"- {t['theme']}（{t['count']} 篇）" for t in self.themes
        ) or "- （无纳入研究）"
        return "\n\n".join([
            f"# PRISMA 系统综述：{self.topic}",
            "## 流程计数（PRISMA flow）\n" + flow_lines,
            "## 主题综合\n" + themes,
        ])


def flow(
    topic: str,
    *,
    paper_id: str = "",
    layout=None,
    hits: list[dict] | None = None,
    databases: list[str] | None = None,
    limit: int = 10,
    include_keywords: list[str] | None = None,
    exclude_keywords: list[str] | None = None,
    full_texts: dict[str, str] | None = None,
    persist: bool = True,
) -> dict:
    """执行 PRISMA 7 阶段协议，返回含流程计数的 dict。

    Args:
        topic: 综述主题（检索查询语句）。
        paper_id: 论文/项目标识；给定 layout 时落盘 prisma.json/md。
        layout: Layout 实例（可选）。
        hits: 预取的检索结果（OpenAlex 精简结构列表）；给定则跳过检索阶段。
        databases: 检索库列表，不足 3 个自动补默认库。
        limit: 每库检索条数上限。
        include_keywords: title/abstract 筛选纳入关键词（未命中即排除）。
        exclude_keywords: title/abstract 筛选排除关键词（命中即排除）。
        full_texts: {doi 或 title: 全文文本}，用于更完整的全文质量评估。
        persist: 是否落盘。

    Returns:
        dict：{ok, topic, counts, included, themes, verification, queries,
        phases, notes, offline}。counts 为 PRISMA 流程计数。
    """
    r = PrismaReport(ok=False, topic=topic)
    notes: list[str] = []
    dbs = list(databases) if databases else list(DEFAULT_DATABASES)
    if len(dbs) < 3:
        for d in DEFAULT_DATABASES:
            if d not in dbs:
                dbs.append(d)
            if len(dbs) >= 3:
                break
        notes.append("检索库不足 3 个，已自动补默认库（PRISMA 多库要求）。")

    # 阶段 1：规划/scoping —— 记录协议与查询语句
    queries = [{"database": db, "query": topic} for db in dbs]
    r.queries = queries
    r.phases["planning"] = {"databases": dbs, "queries": len(queries)}

    # 阶段 2：多库检索（走 science.api 门面，离线降级）
    if hits is None:
        from sciforge.science.api import science_batch_search
        sr = science_batch_search(topic, databases=dbs, limit=limit)
        hits = sr.get("hits", [])
        r.offline = bool(sr.get("offline"))
    else:
        r.offline = False
    if not hits:
        notes.append("检索无结果（离线或网络），流程基于空集继续（离线降级）。")
    r.phases["search"] = {
        "databases": dbs, "identified": len(hits), "offline": r.offline,
    }
    counts = {"identified": len(hits)}

    # 阶段 3：筛选（title/abstract → full-text）
    unique = _dedupe(hits)
    counts["duplicates"] = len(hits) - len(unique)
    screened, excluded_ta = _screen(unique, include_keywords, exclude_keywords)
    counts["screened"] = len(unique)
    counts["excluded_title_abstract"] = len(excluded_ta)
    assessed, ft_excluded = _full_text_assess(screened, full_texts)
    counts["full_text_assessed"] = len(assessed)
    counts["full_text_excluded"] = len(ft_excluded)
    counts["included"] = len(assessed)
    r.counts = counts
    r.included = assessed
    r.phases["screening"] = {
        "screened": len(unique),
        "excluded": excluded_ta + ft_excluded,
    }

    # 阶段 4：数据提取与质量评估（risk-of-bias rubric）
    risk = {"low": 0, "moderate": 0, "high": 0}
    for p in assessed:
        risk[p.get("risk_of_bias", "moderate")] += 1
    r.phases["extraction"] = {"assessed": len(assessed), "risk_distribution": risk}

    # 阶段 5：主题综合（按主题分组）
    r.themes = _synthesis(assessed, include_keywords or [])
    r.phases["synthesis"] = {"themes": [t["theme"] for t in r.themes]}

    # 阶段 6：引文核验（claims 延迟导入，不存在时优雅降级跳过）
    r.verification = _verify_refs(assessed, notes)
    ver = r.phases["verification"] = {
        "available": _claims_available(),
        "verified": sum(1 for v in r.verification if v["status"] == "verified"),
        "skipped": sum(1 for v in r.verification if v["status"] == "skipped"),
    }

    # 阶段 7：文档生成
    r.ok = True
    if persist and paper_id and layout is not None:
        paths = _persist(layout, paper_id, r)
        r.phases["reporting"] = {"json": str(paths[0]), "md": str(paths[1])}
    else:
        r.phases["reporting"] = {"persisted": False}
    r.notes = notes
    return r.to_dict()


def _dedupe(hits: list[dict]) -> list[dict]:
    """按 DOI/标题去重（大小写/空白归一），保留首次出现。"""
    seen: set[str] = set()
    out = []
    for h in hits:
        key = (h.get("doi") or h.get("title") or "").lower().strip()
        key = " ".join(key.split())
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(h)
    return out


def _screen(
    hits: list[dict],
    include_keywords: list[str] | None,
    exclude_keywords: list[str] | None,
) -> tuple[list[dict], list[dict]]:
    """title/abstract 筛选：排除必须带理由。返回（保留, 排除）。"""
    kept, excluded = [], []
    for h in hits:
        text = f"{h.get('title', '')} {h.get('abstract', '')}".lower()
        reason = ""
        if not (h.get("title") or "").strip():
            reason = "缺少标题"
        elif include_keywords and not any(k.lower() in text for k in include_keywords):
            reason = "与主题无关（未命中纳入关键词）"
        elif exclude_keywords and any(k.lower() in text for k in exclude_keywords):
            reason = "命中排除关键词"
        if reason:
            excluded.append({"title": h.get("title", ""), "stage": "title_abstract",
                             "reason": reason})
        else:
            kept.append(h)
    return kept, excluded


def _full_text_assess(
    hits: list[dict], full_texts: dict[str, str] | None,
) -> tuple[list[dict], list[dict]]:
    """全文评估：简易 risk-of-bias rubric（low/moderate/high），高风险排除并带理由。"""
    if full_texts is None:
        full_texts = {}
    kept, excluded = [], []
    for h in hits:
        text = full_texts.get(h.get("doi") or "", full_texts.get(h.get("title") or ""))
        risk, signals = _risk_of_bias(h, text)
        h = {**h, "risk_of_bias": risk}
        if risk == "high":
            excluded.append({"title": h.get("title", ""), "stage": "full_text",
                             "reason": "偏倚风险高：" + "、".join(signals)})
        else:
            kept.append(h)
    return kept, excluded


def _risk_of_bias(h: dict, full_text: str | None) -> tuple[str, list[str]]:
    """按元数据信号评 risk-of-bias：低风险=摘要+DOI 齐备；高风险=两者皆缺。
    仅有「未提供全文」单一信号且摘要+DOI 完备时，仍判 low（全文缺失不单独拉高风险）。
    """
    signals: list[str] = []
    if not (h.get("abstract") or "").strip():
        signals.append("缺摘要")
    if not (h.get("doi") or "").strip():
        signals.append("缺 DOI")
    if full_text is None:
        signals.append("未提供全文")
    else:
        signals = [s for s in signals if s != "未提供全文"]
    # 仅有「未提供全文」单一信号且摘要+DOI 完备 → low
    if not signals:
        return "low", signals
    if len(signals) == 1 and signals[0] == "未提供全文":
        return "low", signals
    if len(signals) >= 2:
        return "high", signals
    return "moderate", signals


def _synthesis(included: list[dict], keywords: list[str]) -> list[dict]:
    """主题综合：按主题关键词分组（不按研究罗列）；无关键词时按标题词分组。"""
    buckets: dict[str, list] = {}
    for p in included:
        text = f"{p.get('title', '')} {p.get('abstract', '')}".lower()
        theme = next((k for k in keywords if k.lower() in text), None)
        if theme is None:
            toks = [t for t in re.split(r"[\s,，、;；]+", p.get("title", "")) if len(t) >= 3]
            theme = toks[0] if toks else "其他"
        buckets.setdefault(theme, []).append(p)
    return [
        {"theme": t, "count": len(ps), "papers": ps}
        for t, ps in sorted(buckets.items(), key=lambda kv: -len(kv[1]))
    ]


def _claims_available() -> bool:
    """sciforge.claims 是否可导入（并行任务 B 创建，可能不存在）。"""
    try:
        import sciforge.claims  # noqa: F401
        return True
    except ImportError:
        return False


def _verify_refs(included: list[dict], notes: list[str]) -> list[dict]:
    """引文核验：优先走 sciforge.claims.verify；不可用时标记 skipped（不崩）。"""
    verify = None
    try:
        from sciforge.claims.verify import verify as _verify
        verify = _verify
    except ImportError:
        notes.append("sciforge.claims 包不可用，引文核验跳过（优雅降级）。")
    out = []
    for p in included:
        ref_text = f"{p.get('title', '')} doi:{p.get('doi') or ''}"
        if verify is None:
            out.append({"ref": ref_text, "status": "skipped",
                        "reason": "claims 包不可用"})
            continue
        try:
            res = verify(ref_text)
            ok = bool(res.get("ok")) if isinstance(res, dict) else bool(res)
            out.append({"ref": ref_text, "status": "verified" if ok else "failed",
                        "reason": "" if ok else "核验未通过"})
        except Exception as e:
            # claims.verify 的签名由并行任务 B 决定，调用失败按 skipped 处理
            out.append({"ref": ref_text, "status": "skipped", "reason": f"调用失败: {e}"})
    return out


def _persist(layout, paper_id: str, r: PrismaReport) -> tuple[Path, Path]:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    p_json = root / "prisma.json"
    p_json.write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    p_md = root / "prisma.md"
    p_md.write_text(r.to_markdown(), encoding="utf-8")
    return p_json, p_md
