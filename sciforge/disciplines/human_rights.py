"""人权学科论文支持：国际人权法/基本权利/人权保障研究体裁、OSCOLA/APA 引用样式与法理文献口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="human_rights",
    aliases=(
        "human_rights",
        "人权",
        "国际人权法",
        "Human Rights",
        "International Human Rights Law",
        "Fundamental Rights",
        "人权保障",
        "Civil Liberties",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="OSCOLA 引用样式（法学期刊通用）；APA 亦可作辅样",
    reporting_standards={"k1": "法律实证研究须说明案例检索口径", "k2": "规范分析须引用成文法条", "k3": "实证研究须报告伦理与隐私处理"},
    conventions=(
        "法条须给出条款编号与生效时间",
        "案例名称给出全名与年份",
        "人权公约须给出条款号",
        "实证数据须匿名化处理",
        "论证须区分规范与实证",
    ),
    key_venues=(
        "Harvard Human Rights Journal",
        "European Human Rights Law Review",
        "American Journal of International Law",
        "Michigan Journal of International Law",
        "Human Rights Quarterly",
    ),
    units_and_formulas_notes=(
        "司法辖区须注明",
        "案例年份给出判决/裁决日期",
        "统计性数据须报告样本量",
        "文献区分一级/二级来源",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Jusline", "OpenJur", "vLex", "Blei Law Lib", "SPSS", "Stata", "NVivo", "Atlas.ti", "Excel", "Tableau", "Power BI", "Endnote", "RefWorks", "Mendeley", "R", "LaTeX", "Zotero", "Qualtrics", "Reflex（法律文本分析）", "iCourt Alpha 法律分析平台"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "HeinOnline", "Google Scholar", "JSTOR", "UN OHCHR 数据库"),
)
