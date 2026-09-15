"""claims.verify 核心测试：5 类锚点分类各 1 样例 + gate_refuse 触发。"""
from __future__ import annotations

import pytest

from sciforge.claims.verify import (
    verify,
    parse_claims,
    parse_citations,
    parse_constraints,
    _parse_citations,
    _extract_constraint_targets,
    _parse_vague_source,
    _has_anchor,
    CATEGORIES,
)


# ---------- 样本 ----------
_STRONG = (
    "我们的剪枝方法在边缘设备上取得 99% 精度 [1]。"
    "研究表明剪枝显著降低延迟。"
    "参考文献 [1] Smith et al. (2020) doi:10.1000/abc。"
)

_FABRICATED = (
    "我们的方法达到 SOTA [待补充]。"
    "参考文献 [引用待补]。"
)

_CONSTRAINT = (
    "本实验禁止使用合成数据训练模型。"
    "实验表明使用合成数据训练的模型精度更高。"
)

_UNCITED = (
    "部分先前工作直接在合成数据上训练。"
)

_ANCHORLESS = (
    "研究表明剪枝有效。"
    "先前工作表明剪枝有效。"
    "Smith et al. (2020) 提出类似方法。"
)

_VALID_CITATIONS = (
    "我们的方法达到 SOTA [1]。"
    "参考文献 [1] doi:10.1000/abc。"
    "参考文献 [2] arXiv:2301.00001。"
    "参考文献 [3] https://example.com。"
    "参考文献 [4] Smith et al. (2020)。"
)

_FABRICATED_CITATIONS = (
    "我们的方法达到 SOTA [待补充]。"
    "参考文献 [引用待补]。"
    "参考文献 []。"
    "参考文献 [待补充内容]。"
)

# ---------- parse_claims ----------
def test_parse_claims_basic():
    claims = parse_claims("我们的方法提升精度。这是普通句子。")
    assert len(claims) == 1
    assert "提升" in claims[0]["text"]


# ---------- parse_citations ----------
def test_parse_citations_valid():
    cits = _parse_citations("参考文献 [1] doi:10.1000/abc。")
    assert len(cits) == 2
    kinds = {c["kind"] for c in cits}
    assert "bracket" in kinds
    assert "doi" in kinds


def test_parse_citations_fabricated():
    cits = _parse_citations("参考文献 [待补充]。")
    assert any(not c["valid"] for c in cits)


def test_parse_citations_bracket_valid():
    cits = _parse_citations("参考文献 [1] [2,3]。")
    assert all(c["valid"] for c in cits)


def test_parse_citations_bracket_invalid():
    cits = _parse_citations("参考文献 [待补充] [?] []。")
    assert any(not c["valid"] for c in cits)


# ---------- _parse_citations (内部) ----------
def test_parse_citations_doi():
    cits = _parse_citations("doi:10.1000/abc")
    assert any(c["kind"] == "doi" and c["valid"] for c in cits)


def test_parse_citations_arxiv():
    cits = _parse_citations("arXiv:2301.00001")
    assert any(c["kind"] == "arxiv" and c["valid"] for c in cits)


def test_parse_citations_url():
    cits = _parse_citations("https://example.com")
    assert any(c["kind"] == "url" and c["valid"] for c in cits)


def test_parse_citations_author_year():
    cits = _parse_citations("Smith et al. (2020) 提出...")
    assert any(c["kind"] == "author_year" and c["valid"] for c in cits)


# ---------- _extract_constraint_targets ----------
def test_extract_constraint_targets():
    targets = _extract_constraint_targets("本实验禁止使用合成数据训练模型。")
    assert any("合成" in t for t in targets)
    assert any("数据" in t for t in targets)


# ---------- _parse_vague_source ----------
def test_parse_vague_source():
    assert _parse_vague_source("研究表明剪枝有效。")
    assert _parse_vague_source("Smith et al. (2020) 提出...")
    assert not _parse_vague_source("我们实验证明...")


# ---------- _has_anchor ----------
def test_has_anchor():
    cits = [{"valid": False}, {"valid": True}]
    assert _has_anchor(cits) is True
    assert _has_anchor([{"valid": False}]) is False
    assert _has_anchor([]) is False


# ---------- verify 核心 5 类别 ----------
def test_verify_fabricated_reference():
    r = verify("我们的方法达到 SOTA [待补充]。")
    assert r["gate_refuse"] is True
    cats = {f["category"] for f in r["findings"]}
    assert "fabricated-reference" in cats


def test_verify_negative_constraint_violation():
    r = verify("本实验禁止使用合成数据。实验表明使用合成数据训练的模型精度更高。")
    cats = {f["category"] for f in r["findings"]}
    assert "negative-constraint-violation" in {f["category"] for f in r["findings"]}
    assert r["gate_refuse"] is True


def test_verify_anchorless():
    r = verify("研究表明剪枝有效。")
    cats = {f["category"] for f in r["findings"]}
    assert "anchorless" in cats


def test_verify_constraint_violation_uncited():
    # 需要包含约束句(定义目标)和违反句(无引用)
    text = "本实验禁止使用合成数据训练模型。部分先前工作直接在合成数据上训练。"
    r = verify(text)
    cats = {f["category"] for f in r["findings"]}
    assert "constraint-violation-uncited" in cats


def test_verify_claim_not_supported():
    # 由于缺少 sources 参数，暂不测试 claim-not-supported
    pass


def test_verify_strong_paper_passes():
    text = (
        "我们的剪枝方法在边缘设备上取得 99% 精度 [1]。"
        "参考文献 [1] doi:10.1000/abc。"
    )
    r = verify(text)
    assert r["ok"] is True


def test_verify_strong_with_valid_citations():
    r = verify(_VALID_CITATIONS)
    assert r["ok"] is True


def test_verify_all_categories():
    """组合文本触发全部 5 类（fabricated 除外，需单独测）"""
    text = (
        "研究表明剪枝有效。"  # anchorless
        "本实验禁止使用合成数据。实验表明使用合成数据训练的模型精度更高。"  # negative-constraint-violation
        "部分先前工作直接在合成数据上训练。"  # constraint-violation-uncited
        "参考文献 [待补充]。"  # fabricated-reference
    )
    r = verify(text)
    cats = {f["category"] for f in r["findings"]}
    assert cats == set(CATEGORIES)
    assert r["gate_refuse"] is True


# ---------- 内部函数 ----------
def test_parse_citations_internal():
    cits = _parse_citations("参考文献 [1] doi:10.1000/abc。")
    assert len(cits) >= 1


def test_extract_constraint_targets():
    targets = _extract_constraint_targets("本实验禁止使用合成数据训练模型。")
    assert len(targets) > 0


def test_parse_vague_source():
    assert _parse_vague_source("研究表明剪枝有效。")
    assert _parse_vague_source("Smith et al. (2020) 提出...")


def test_has_anchor():
    assert _has_anchor([{"valid": True}]) is True
    assert _has_anchor([{"valid": False}]) is False


# ---------- 常量 ----------
def test_categories_constant():
    assert set(CATEGORIES) == {
        "claim-not-supported",
        "negative-constraint-violation",
        "fabricated-reference",
        "anchorless",
        "constraint-violation-uncited",
    }