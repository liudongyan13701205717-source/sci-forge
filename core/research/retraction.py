"""撤稿/更正监测与信任评分（backlog #4）。

围绕一组文献记录（DOI 或标题）检测撤稿（retraction）与更正（correction），
并给出可解释的信任评分。联网时用 Crossref/OpenAlex 的
`update-to` / `type` 等信号；离线时退化为本地启发式（标题关键词 +
记录完备度），并显式标注 `offline=True`，绝不伪装成真实核查结果。

设计原则：
  - 只返回可解释信号，不做硬性断言；
  - 离线结果必须可辨识（offline 标记 + notes），避免误导用户；
  - 信任评分是启发式加权，规则随分数一起返回。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field

from sciforge.core import Layout
from sciforge.research import lit

_RETRACT_TITLE = re.compile(
    r"\b(retract(ed|ion)?|withdrawn|withdrawal|expression\s+of\s+concern)\b",
    re.IGNORECASE,
)
_CORRECT_TITLE = re.compile(
    r"\b(correction|corrected|erratum|corrigendum|publisher'?s\s+note)\b",
    re.IGNORECASE,
)
_DOI = re.compile(r"(10\.\d{4,9}/[^\s\"<>]+)")

# 已知撤稿院所示例（用于离线演示与测试；非完备清单，源码注释说明来源类型）
_KNOWN_RETRACTED_TITLES = (
    # 占位：真实清单应由用户提供或联网同步；此处保持为空避免伪造事实
)


@dataclass
class WorkTrust:
    doi: str = ""
    title: str = ""
    status: str = "unknown"      # retracted | corrected | suspicious | clean | unknown
    signals: list = field(default_factory=list)
    trust_score: int = 50        # 0-100
    score_breakdown: list = field(default_factory=list)
    source: str = ""             # crossref | openalex | local-heuristic

    def to_dict(self) -> dict:
        return {
            "doi": self.doi, "title": self.title, "status": self.status,
            "signals": self.signals, "trust_score": self.trust_score,
            "score_breakdown": self.score_breakdown, "source": self.source,
        }


@dataclass
class RetractionWatch:
    ok: bool
    paper_id: str = ""
    checked: int = 0
    retracted: list = field(default_factory=list)
    corrected: list = field(default_factory=list)
    suspicious: list = field(default_factory=list)
    works: list = field(default_factory=list)
    min_trust_score: int = 100
    verdict: str = ""
    notes: list = field(default_factory=list)
    error: str = ""
    offline: bool = False

    def to_dict(self) -> dict:
        return {
            "ok": self.ok, "paper_id": self.paper_id, "checked": self.checked,
            "retracted": self.retracted, "corrected": self.corrected,
            "suspicious": self.suspicious, "works": self.works,
            "min_trust_score": self.min_trust_score, "verdict": self.verdict,
            "notes": self.notes, "error": self.error, "offline": self.offline,
        }

    def to_markdown(self) -> str:
        def block(rows, empty):
            if not rows:
                return f"- {empty}"
            return "\n".join(
                f"- **{w['trust_score']}** | {w['status']} | {w['title'] or w['doi']}"
                + (f"（{w['doi']}）" if w.get("doi") else "")
                + (f" — 信号：{'；'.join(w['signals'])}" if w.get("signals") else "")
                for w in rows
            )

        return "\n\n".join([
            f"# 撤稿/更正监测：{self.paper_id}",
            f"## 结论\n{self.verdict or '（无）'}",
            f"## 统计\n- 检出文献 {self.checked} 条\n- 撤稿 {len(self.retracted)} | "
            f"更正 {len(self.corrected)} | 可疑 {len(self.suspicious)}\n"
            f"- 最低信任分：{self.min_trust_score}",
            f"## 撤稿\n{block(self.retracted, '未检出')}",
            f"## 更正\n{block(self.corrected, '未检出')}",
            f"## 可疑\n{block(self.suspicious, '未检出')}",
            f"## 说明\n" + ("\n".join(f"- {n}" for n in self.notes) or "- （无）"),
        ])


def _norm_inputs(records) -> list[dict]:
    """把 doi/字符串/dict 混合输入规整为 {doi,title}。"""
    out: list[dict] = []
    for rec in records or []:
        if isinstance(rec, str):
            m = _DOI.search(rec)
            out.append({"doi": m.group(1).rstrip(".,;)") if m else "", "title": rec.strip()})
        elif isinstance(rec, dict):
            out.append({
                "doi": str(rec.get("doi") or "").strip(),
                "title": str(rec.get("title") or "").strip(),
            })
    return out


def _online_crossref(doi: str, timeout: int = 15) -> dict:
    """Crossref 作品记录（含 update-to / type 信号）。失败返回 {}。"""
    if not doi or lit._offline():
        return {}
    import urllib.parse
    import urllib.request

    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={"User-Agent": "sciforge/3 (mailto:probe@example.org)"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
            return json.loads(resp.read().decode("utf-8")).get("message", {}) or {}
    except Exception:  # noqa: BLE001
        return {}


def _title_signals(title: str) -> tuple[str, list]:
    """标题关键词信号（离线/兜底）。"""
    if not title:
        return "unknown", []
    if _RETRACT_TITLE.search(title):
        return "retracted", ["标题含撤稿/撤回/关注表达字样"]
    if _CORRECT_TITLE.search(title):
        return "corrected", ["标题含更正/勘误字样"]
    return "clean", []


def _score(status: str, signals: list, has_doi: bool, cited_by: int) -> tuple[int, list]:
    """可解释的启发式信任分（0-100）。"""
    score = 60
    bd: list = []
    if status == "retracted":
        score -= 90
        bd.append("-90 检出撤稿信号")
    elif status == "corrected":
        score -= 15
        bd.append("-15 检出更正/勘误信号")
    elif status == "suspicious":
        score -= 10
        bd.append("-10 存在可疑信号")
    elif status == "clean":
        score += 10
        bd.append("+10 未检出撤稿/更正信号")
    if has_doi:
        score += 10
        bd.append("+10 具备 DOI（可稳定定位）")
    else:
        score -= 10
        bd.append("-10 无 DOI（定位不稳）")
    if cited_by >= 100:
        score += 10
        bd.append(f"+10 被引 {cited_by}（社区复核充分）")
    elif cited_by >= 10:
        score += 5
        bd.append(f"+5 被引 {cited_by}")
    return max(0, min(100, score)), bd


def check_works(
    *,
    paper_id: str,
    layout: Layout,
    records,
    sources: list[str] | None = None,
) -> RetractionWatch:
    """检测一组文献的撤稿/更正状态并给出信任分。"""
    r = RetractionWatch(ok=False, paper_id=paper_id)

    recs = _norm_inputs(records)
    if not recs:
        r.error = "未提供待检文献（records 为空）。"
        r.notes.append("请传入 DOI 或标题列表。")
        return r

    r.checked = len(recs)
    r.offline = lit._offline()

    for rec in recs:
        w = WorkTrust(doi=rec["doi"], title=rec["title"])
        cited = 0
        if not r.offline and w.doi:
            meta = _online_crossref(w.doi)
            if meta:
                w.source = "crossref"
                w.title = (meta.get("title") or [w.title])[0]
                cited = int(meta.get("is-referenced-by-count") or 0)
                # Crossref: 撤稿/更正常以 update-to 表达
                updates = meta.get("update-to") or []
                for u in updates:
                    ut = str(u.get("type", "")).lower()
                    if "retract" in ut or "withdraw" in ut:
                        w.signals.append(f"Crossref update-to: {ut}")
                    elif "correct" in ut or "erratum" in ut:
                        w.signals.append(f"Crossref update-to: {ut}")
                mtype = str(meta.get("type", "")).lower()
                if "retract" in mtype:
                    w.signals.append(f"Crossref type: {mtype}")
                w.status = "suspicious" if w.signals else "clean"
            else:
                w.source = "local-heuristic"
                w.notes.append(f"Crossref 未命中 {w.doi or w.title[:30]}，退回本地启发式。")

        if w.source in ("", "local-heuristic"):
            if w.source == "":
                w.source = "local-heuristic"
            w.status, sig = _title_signals(w.title)
            w.signals.extend(sig)
            for k in _KNOWN_RETRACTED_TITLES:
                if w.title and k.lower() == w.title.lower():
                    w.status = "retracted"
                    w.signals.append("命中本地撤稿示例清单")
            if not w.title and not w.doi:
                w.status = "unknown"
                w.signals.append("既无标题也无 DOI，无法判定")

        w.trust_score, w.score_breakdown = _score(w.status, w.signals, bool(w.doi), cited)
        if w.status == "retracted":
            r.retracted.append(w.to_dict())
        elif w.status == "corrected":
            r.corrected.append(w.to_dict())
        elif w.status == "suspicious":
            r.suspicious.append(w.to_dict())
        r.works.append(w.to_dict())

    r.min_trust_score = min(w["trust_score"] for w in r.works)
    if r.retracted:
        r.verdict = f"检出 {len(r.retracted)} 条撤稿文献，请立即从证据链中剔除并核查引用。"
    elif r.suspicious:
        r.verdict = f"检出 {len(r.suspicious)} 条可疑文献（可能存在撤稿/更正），建议人工复核。"
    elif r.corrected:
        r.verdict = f"检出 {len(r.corrected)} 条有更正记录的文献，建议核对更正内容。"
    else:
        r.verdict = "未检出撤稿或更正信号（启发式判定，非权威注销清单比对）。"

    if r.offline:
        r.notes.append("离线模式：未访问 Crossref/OpenAlex，结果为标题启发式，"
                       "不得作为撤稿权威结论。")
    r.notes.append("信任分为启发式加权（规则见 score_breakdown），不替代机构期刊政策判断。")

    r.ok = True
    _persist(layout, paper_id, r)
    return r


def _persist(layout: Layout, paper_id: str, r: RetractionWatch) -> None:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "retraction_watch.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "retraction_watch.md").write_text(r.to_markdown(), encoding="utf-8")
