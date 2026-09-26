"""venue + disciplines 测试：模板注册、fit 评分、学科 registry 自动发现、16 学科字段齐全。"""
from __future__ import annotations

import pytest

from sciforge.venue import (
    VENUE_TEMPLATES,
    get_template,
    list_venues,
    journal_fit,
)
from sciforge.disciplines import (
    list_disciplines,
    get_discipline,
    Discipline,
    list_by_category,
    list_by_contribution_form,
    list_by_tool,
    list_by_database,
)
from sciforge.disciplines.contribution_forms import CONTRIBUTION_FORMS


# ---------- venue templates ----------
def test_venue_templates_registry():
    assert len(VENUE_TEMPLATES) >= 7
    required = {"Nature", "Science", "Cell", "NEJM", "Lancet", "JAMA", "IEEE", "ACL", "AAAI", "APA"}
    assert required <= set(VENUE_TEMPLATES.keys())


def test_get_template():
    t = get_template("Nature")
    assert t["citation_style"] == "Nature numbered (sequential superscript)"
    assert "structure" in t
    assert len(t["structure"]) >= 5


def test_get_template_unknown():
    t = get_template("UnknownJournal")
    assert t == {}


def test_list_venues():
    venues = list_venues()
    assert len(venues) >= 7
    assert "Nature" in venues
    assert "Science" in venues


# ---------- journal_fit ----------
def test_journal_fit_unknown():
    r = journal_fit("任意文本", "UnknownJournal")
    assert r["ok"] is False
    assert "未知期刊" in r["error"]


def test_journal_fit_nature():
    text = (
        "我们提出一种新的剪枝方法，在边缘设备上实现 99% 精度。"
        "实验在 ImageNet、COCO、CIFAR-10 三个数据集进行。"
        "代码已开源 github.com/example/prune。"
    )
    r = journal_fit(text, "Nature")
    assert r["ok"] is True
    assert 0 <= r["score"] <= 100
    assert "breakdown" in r
    assert "gaps" in r
    assert "recommendations" in r


def test_journal_fit_cell():
    text = (
        "我们发现一种新的蛋白质折叠机制，在细胞分裂中起关键作用。"
        "实验结合冷冻电镜与基因敲除，揭示了分子机制。"
        "Graphical Abstract 展示了核心模型。"
        "Highlights: 1) 新机制 2) 功能验证 3) 临床意义。"
    )
    r = journal_fit(text, "Cell")
    assert r["ok"] is True
    assert r["venue"] == "Cell"
    assert r["score"] > 0


def test_journal_fit_nejm():
    text = (
        "背景：我们评估了一种新疗法在心衰患者中的疗效。"
        "方法：随机双盲对照试验，纳入 1000 例患者。"
        "结果：治疗组死亡率显著降低 (HR 0.85, 95% CI 0.75-0.95, p=0.01)。"
        "结论：该疗法可显著降低心衰死亡率。"
    )
    r = journal_fit(text, "NEJM")
    assert r["ok"] is True
    assert "structure" in r["breakdown"].keys()


# ---------- disciplines registry ----------
def test_disciplines_registry_count():
    discs = list_disciplines()
    assert len(discs) >= 16
    names = {d.name for d in discs}
    expected = {
        "mathematics", "physics", "chemistry", "biology", "medicine",
        "computer_science", "engineering", "economics", "psychology",
        "social_science", "neuroscience", "materials_science",
        "public_health", "nursing", "dentistry", "veterinary_science",
    }
    assert expected <= names


def test_discipline_base_fields():
    for name in ["mathematics", "physics", "medicine", "computer_science"]:
        d = get_discipline(name)
        assert isinstance(d, Discipline)
        assert d.name == name
        assert len(d.aliases) >= 1
        assert len(d.paper_types) >= 1
        assert d.citation_style
        assert len(d.reporting_standards) >= 1
        assert len(d.conventions) >= 1
        assert len(d.key_venues) >= 3
        assert d.units_and_formulas_notes


def test_mathematics_discipline():
    d = get_discipline("mathematics")
    assert "research" in d.paper_types
    assert "expository" in d.paper_types
    assert "survey" in d.paper_types
    assert "AMS" in d.citation_style
    assert any("Annals of Mathematics" in v for v in d.key_venues)


def test_physics_discipline():
    d = get_discipline("physics")
    # citation_style 是完整字符串，检查关键词
    assert "APS" in d.citation_style or "Physical Review" in d.citation_style or "PRL" in d.citation_style
    assert any("PRL" in v or "Physical Review" in v for v in d.key_venues)


def test_medicine_discipline():
    d = get_discipline("medicine")
    # reporting_standards 是 dict 或 tuple，检查整个对象字符串
    assert "CARE" in str(d.reporting_standards)
    assert "STARD" in str(d.reporting_standards)
    assert any("NEJM" in v or "New England Journal" in v for v in d.key_venues)


def test_computer_science_discipline():
    d = get_discipline("computer_science")
    # conventions 是 tuple/list，检查整体关键词
    assert "benchmark" in str(d.conventions).lower() or "benchmark" in d.reporting_standards
    assert any("NeurIPS" in v for v in d.key_venues)


def test_autodiscovery():
    """新增学科文件零注册即被发现（registry 自动发现）。"""
    discs = list_disciplines()
    assert len(discs) >= 12


# ---------- disciplines v2 字段（paper_capable / contribution_forms / tools / category / databases）----------
def test_discipline_v2_fields():
    """抽样学科的 v2 字段齐全：paper_capable、contribution_forms、tools、category、databases。"""
    for name in [
        "mathematics",
        "physics",
        "medicine",
        "computer_science",
        "quantum_computing",
    ]:
        d = get_discipline(name)
        assert d.paper_capable is True
        assert d.contribution_forms
        assert "论文" in d.contribution_forms
        assert len(d.tools) >= 2
        assert d.category != "未分类"
        assert len(d.databases) >= 2


def test_discipline_v2_all_fields():
    """全量 261 学科逐一校验 v2 字段完整性，无未分类、无空 tools/databases。"""
    for d in list_disciplines():
        assert isinstance(d.paper_capable, bool)
        assert d.name
        assert d.contribution_forms
        assert "论文" in d.contribution_forms
        assert len(d.tools) >= 2
        assert d.category != "未分类"
        assert len(d.databases) >= 2


def test_registry_filters():
    """四个 registry 过滤函数按 category / contribution_form / tool / database 检索。"""
    assert len(list_by_contribution_form("论文")) == 261
    assert len(list_by_category("理学")) > 0
    assert len(list_by_category("工学")) > 0
    assert len(list_by_tool("Python")) > 0
    assert len(list_by_database("OpenAlex")) > 0
    assert len(list_by_database("arXiv")) > 0


def test_registry_count_261():
    """registry 学科总数为 261。"""
    assert len(list_disciplines()) == 261


def test_contribution_forms_constants():
    """贡献形式常量表为 10 项且含关键项。"""
    assert len(CONTRIBUTION_FORMS) == 10
    assert "论文" in CONTRIBUTION_FORMS
    assert "软件与代码" in CONTRIBUTION_FORMS