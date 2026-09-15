"""批次1升级模块测试：prisma / styles / rebuttal / quality / stylecal。

全离线（SCI_FORGE_OFFLINE=1 兼容），不依赖 sciforge.claims（prisma 引文核验
验证其优雅降级路径），不依赖 LLM。
"""

from __future__ import annotations

import pytest

from sciforge.core import Layout, get_layout

_HITS = [
    {"title": "Pruning Methods for Edge Inference", "year": 2023,
     "doi": "10.1000/abc", "abstract": "structured pruning for edge devices",
     "authors": ["A"], "cited_by": 10},
    {"title": "Pruning Methods for Edge Inference", "year": 2023,
     "doi": "10.1000/abc", "abstract": "duplicate", "authors": ["A"]},
    {"title": "Unrelated Cooking Recipe", "year": 2024, "doi": "10.1000/xyz",
     "abstract": "how to cook noodles", "authors": ["B"]},
]


def _layout(tmp_path) -> Layout:
    import os

    os.chdir(tmp_path)
    return get_layout()


# ---- prisma ----

def test_prisma_flow_offline_counts_and_persist(tmp_path, monkeypatch):
    from sciforge.research.prisma import flow

    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    layout = _layout(tmp_path)
    r = flow("边缘推理剪枝", paper_id="p_prisma", layout=layout)
    assert r["ok"] is True
    c = r["counts"]
    assert {"identified", "duplicates", "screened", "excluded_title_abstract",
            "full_text_assessed", "full_text_excluded", "included"} <= set(c)
    # 离线检索为空 → 流程基于空集继续，不崩
    assert c["identified"] == 0 and c["included"] == 0
    # 多库要求：查询语句按库记录
    assert len(r["queries"]) >= 3
    assert all(q["query"] for q in r["queries"])
    # 7 阶段齐备
    assert set(r["phases"]) == {
        "planning", "search", "screening", "extraction", "synthesis",
        "verification", "reporting",
    }
    assert (layout.project_dir("p_prisma") / "research" / "prisma.json").exists()
    assert (layout.project_dir("p_prisma") / "research" / "prisma.md").exists()


def test_prisma_flow_with_hits_screening_reasons(tmp_path):
    from sciforge.research.prisma import flow

    r = flow("边缘推理剪枝", hits=_HITS, paper_id="", layout=None,
             include_keywords=["pruning"], persist=False)
    c = r["counts"]
    # 3 条识别 → 1 条重复去重 → 2 条筛选 → 1 条与主题无关排除
    assert c["identified"] == 3
    assert c["duplicates"] == 1
    assert c["excluded_title_abstract"] == 1
    assert c["included"] == 1
    excluded = r["phases"]["screening"]["excluded"]
    assert excluded and all(e["reason"] for e in excluded)  # 排除必须带理由
    assert any("与主题无关" in e["reason"] for e in excluded)
    # 全文评估 rubric：摘要+DOI 齐备 → low
    assert r["included"][0]["risk_of_bias"] == "low"


def test_prisma_verification_degrades_without_claims(tmp_path):
    from sciforge.research.prisma import flow

    r = flow("边缘推理剪枝", hits=_HITS[:1], include_keywords=["pruning"],
             persist=False)
    ver = r["phases"]["verification"]
    if ver["available"]:
        assert ver["verified"] + ver["skipped"] >= 1
    else:
        # claims 包不存在 → 全部 skipped（优雅降级，不崩）
        assert ver["skipped"] == c_included(r)
        assert all(v["status"] == "skipped" for v in r["verification"])


def c_included(r: dict) -> int:
    return r["counts"]["included"]


# ---- styles ----

_FULL_BIB = (
    "@article{ref,\n"
    "  author = {Zhang, Wei and Li, Ming and Smith, John},\n"
    "  title = {Pruning for Edge Inference},\n"
    "  journal = {Journal of ML},\n"
    "  year = {2020},\n"
    "  volume = {12},\n"
    "  number = {3},\n"
    "  pages = {123--145},\n"
    "  doi = {10.1000/abc}\n"
    "}\n"
)


def test_render_bibtex_all_styles():
    from sciforge.research.styles import parse_bibtex, render, render_all

    cit = parse_bibtex(_FULL_BIB)
    assert cit.missing == []
    assert len(cit.authors) == 3
    assert cit.year == "2020" and cit.volume == "12" and cit.pages == "123--145"
    allr = render_all(cit)
    assert allr["ok"] is True
    styles = allr["styles"]
    # 5 个样式族、6 个渲染器（Chicago 两式）
    assert set(styles) == {"apa", "chicago-notes", "chicago-author-date",
                           "mla", "ieee", "vancouver"}
    assert all(s for s in styles.values())
    assert "(2020)" in styles["apa"] and "https://doi.org/10.1000/abc" in styles["apa"]
    assert "Zhang, W." in styles["apa"] and "&" in styles["apa"]
    assert "“Pruning for Edge Inference.”" in styles["chicago-notes"]
    assert "no. 3 (2020): 123–145" in styles["chicago-notes"]
    assert styles["chicago-author-date"].startswith("Zhang, Wei")
    assert "et al." in styles["mla"]  # MLA 3+ 作者 → et al.
    assert styles["ieee"].startswith("[1] ") and "vol. 12" in styles["ieee"]
    assert "Journal of ML. 2020;12(3):123–145" in styles["vancouver"]
    r = render(cit, "apa")
    assert r["ok"] is True and r["missing"] == []


def test_render_missing_fields_degrade():
    from sciforge.research.styles import parse_bibtex, render

    cit = parse_bibtex("@article{x,\n  title = {Only a Title},\n}\n")
    assert "year" in cit.missing and "journal" in cit.missing
    assert "authors" in cit.missing
    r = render(cit, "apa")
    assert r["ok"] is True
    # 缺失字段优雅降级：渲染标注 (missing)
    assert "(missing)" in r["citation"]
    assert r["missing"] == cit.missing


def test_render_empty_and_unknown_style():
    from sciforge.research.styles import Citation, parse_bibtex, render

    assert render("", "apa")["ok"] is False          # 空样式输入
    assert parse_bibtex("").missing                   # 空 BibTeX → 全 missing
    r = render(Citation(), "apa")                     # 空引用
    assert r["ok"] is False and "引用为空" in r["error"]
    r = render(parse_bibtex(_FULL_BIB), "bogus")
    assert r["ok"] is False and "未知样式" in r["error"]


# ---- rebuttal ----

_COMMENTS = (
    "Reviewer #1\n"
    "1. The causal claim in the results section is wrong: the controlled "
    "experiment does not support it.\n"
    "2. Figure 3 is unclear, please explain the axes.\n"
    "3. Minor typo on page 5, wording could be improved.\n"
)


def test_revision_coach_roadmap():
    from sciforge.research.rebuttal import revision_coach

    r = revision_coach(_COMMENTS)
    assert r["ok"] is True and r["total"] == 3
    assert len(r["roadmap"]) == 3
    first = r["roadmap"][0]
    assert first["type"] == "CRITICAL" and first["plan"] and len(first["plan"]) >= 2
    assert "results" in first["location"]
    third = r["roadmap"][2]
    assert third["type"] == "MINOR" and third["plan"] == ["直接修正并在回应中列出修改清单"]
    assert r["summary"] == {"critical": 1, "major": 1, "minor": 1}


def test_revision_coach_empty_error(tmp_path):
    from sciforge.research.rebuttal import revision_coach

    r = revision_coach("   \n")
    assert r["ok"] is False and "评审意见为空" in r["error"]


def test_rebuttal_audit_coverage(tmp_path):
    from sciforge.research.rebuttal import rebuttal_audit

    covered = (
        "We thank the reviewers. Regarding the causal claim: we agree the "
        "wording overstated the evidence; we ran a randomized controlled "
        "trial and reworded the results section. The axes of Figure 3 are "
        "now labeled. The typo on page 5 is fixed."
    )
    r = rebuttal_audit(covered, _COMMENTS)
    assert r["ok"] is True and r["total"] == 3
    assert r["coverage"] > 0
    assert r["unaddressed"] == [] and r["pass"] is True

    partial = "We fixed the typo on page 5."
    r = rebuttal_audit(partial, _COMMENTS)
    assert r["ok"] is True
    assert len(r["unaddressed"]) >= 2 and r["pass"] is False


def test_rebuttal_audit_fail_closed():
    from sciforge.research.rebuttal import rebuttal_audit

    # 空 rebuttal → 全部未回应（fail-closed，不默认已覆盖）
    r = rebuttal_audit("", _COMMENTS)
    assert r["ok"] is True and r["addressed"] == 0
    assert len(r["unaddressed"]) == 3 and r["pass"] is False
    # 空意见 → ok=False
    r = rebuttal_audit("anything", "")
    assert r["ok"] is False and "评审意见为空" in r["error"]


# ---- quality ----

def test_detect_style_flags_templated_prose():
    from sciforge.research.quality import detect_style

    text = (
        "总之，这种方法似乎可能有效。值得注意的是，然而这个结果大约会更好。"
        "众所周知，此外它也许有影响。总的来说，因此这个可能很重要。"
    )
    r = detect_style(text)
    assert r["ok"] is True
    assert r["score"] > 40  # hedging + 模板句 + 连接词密集
    kinds = {e["type"] for e in r["evidence"]}
    assert {"hedging", "templated", "filler"} <= kinds
    assert any(e["examples"] for e in r["evidence"])


def test_detect_style_clean_prose_low_score():
    from sciforge.research.quality import detect_style

    text = (
        "剪枝把延迟降低了 23%。剪枝把精度损失控制在 1% 以内。"
        "剪枝在 3 个数据集上验证。剪枝的代码已开源。"
    )
    r = detect_style(text)
    assert r["ok"] is True
    assert r["score"] < 20  # 无 hedging/模板句/连接词
    assert r["metrics"]["hedging_density"] == 0


def test_detect_style_empty_error():
    from sciforge.research.quality import detect_style

    r = detect_style("   \n")
    assert r["ok"] is False and "文本为空" in r["error"]


def test_claim_strength_escalation_detected():
    from sciforge.research.quality import claim_strength

    text = (
        "剪枝与延迟降低相关。因此剪枝导致精度提升。"
        "剪枝造成部署成本下降。"
    )
    r = claim_strength(text)
    assert r["ok"] is True
    assert r["max_level"] == "causes"
    assert r["escalations"], "应检测到无授权的因果表述"
    assert all("证据" in e["reason"] or "授权" in e["reason"]
               for e in r["escalations"])


def test_claim_strength_association_ok():
    from sciforge.research.quality import claim_strength

    text = "剪枝与延迟降低相关。剪枝与压缩率相关。"
    r = claim_strength(text)
    assert r["ok"] is True
    assert r["max_level"] == "associated"
    assert r["escalations"] == []


def test_claim_strength_hedged_causal_with_evidence():
    from sciforge.research.quality import claim_strength

    text = (
        "在随机对照实验中，剪枝导致延迟下降。该消融实验支持因果推断。"
    )
    r = claim_strength(text)
    assert r["ok"] is True
    # 有授权证据标记（随机对照/消融）→ 不升级
    assert r["escalations"] == [] or all(
        "缺少授权证据" not in e["reason"] for e in r["escalations"]
    )


# ---- stylecal ----

_VOICE_A = (
    "# 引言\n\n"
    "剪枝降低延迟。剪枝保留精度。剪枝部署在边缘设备。剪枝的公式很简单。"
    "剪枝分两步走。剪枝先估计重要性。剪枝再移除通道。剪枝最后微调。"
    "\n\n"
    "# 实验\n\n"
    "剪枝在 ImageNet 验证。剪枝在 COCO 验证。剪枝延迟下降 23%。"
    "剪枝精度损失 1%。剪枝开销可忽略。"
)

_VOICE_B = (
    "本研究提出了一种新颖的、基于多尺度注意力机制的知识蒸馏框架。"
    "首先，我们通过教师网络引导学生网络；其次，我们引入了动态温度调度；"
    "最后，我们在多个基准数据集上进行了广泛的实验评估，结果证明该方法"
    "在精度与效率之间取得了更好的平衡，总体而言优于现有最先进方法。"
)


def test_learn_style_profile_and_score(tmp_path):
    from sciforge.research.stylecal import learn_style, score_text

    profile = learn_style(_VOICE_A)
    assert profile["ok"] is True
    assert profile["sentences"]["count"] > 10
    assert profile["sentences"]["mean_len"] < 15  # 作者偏好短句
    assert len(profile["sentences"]["buckets"]) == 5
    top_tokens = [t["token"] for t in profile["tokens"]["top"]]
    assert "剪枝" in "".join(top_tokens[:6])
    assert "heading_rate" in profile["structure"]

    same = score_text(_VOICE_A, profile)
    assert same["ok"] is True and same["score"] >= 80  # 同文本自比 → 高分
    other = score_text(_VOICE_B, profile)
    assert other["ok"] is True
    assert other["score"] < same["score"]  # 不同文风 → 更低分


def test_learn_style_empty_and_invalid_profile(tmp_path):
    from sciforge.research.stylecal import learn_style, score_text

    r = learn_style("   \n")
    assert r["ok"] is False and "文本为空" in r["error"]
    s = score_text("正文内容。", {})
    assert s["ok"] is False and "画像无效" in s["error"]


def test_learn_doc_reads_doc_md(tmp_path):
    from sciforge.research.stylecal import learn_doc

    layout = _layout(tmp_path)
    r = learn_doc("ghost_doc", layout=layout)
    assert r["ok"] is False and "尚无 doc.md" in r["error"]
    (layout.project_dir("p_doc") / "doc.md").write_text(_VOICE_A, encoding="utf-8")
    r = learn_doc("p_doc", layout=layout)
    assert r["ok"] is True and r["sentences"]["count"] > 10


# ---- 集成：rebuttal 落盘 ----

def test_revision_coach_persists_plan(tmp_path):
    from sciforge.research.rebuttal import revision_coach

    layout = _layout(tmp_path)
    r = revision_coach(_COMMENTS, paper_id="p_rb", layout=layout)
    assert r["ok"] is True
    assert (layout.project_dir("p_rb") / "research" / "rebuttal_plan.json").exists()
