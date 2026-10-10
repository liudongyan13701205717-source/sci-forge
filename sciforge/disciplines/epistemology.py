"""认识论学科论文支持：知识论、科学哲学与认识论研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="epistemology",
    aliases=(
        "epistemology", "认识论", "知识论",
        "epistemology", "认识论",
        "theory of knowledge", "知识论",
        "philosophy of science", "科学哲学",
        "knowledge theory", "知识理论",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（认识论问题与背景）",
            "methodology（哲学论证、概念分析、案例研究）",
            "results（认识论分析与评估）",
            "discussion（认识论优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "epistemological analysis（认识论分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "analysis": "哲学论证须注明理论框架",
        "case": "案例分析须注明来源与时间",
        "comparison": "比较研究须注明国家与时间",
    },
    conventions=(
        "哲学概念须定义清晰",
        "哲学论证须注明理论框架",
        "案例须注明来源与时间",
        "比较研究须注明国家与时间",
    ),
    key_venues=(
        "Episteme",
        "Journal of Philosophy",
        "Philosophy and Phenomenological Research",
        "Synthese",
        "Philosophical Studies",
        "Australasian Journal of Philosophy",
    ),
    units_and_formulas_notes=(
        "哲学概念须定义清晰",
        "哲学论证须注明理论框架",
        "案例须注明来源与时间",
        "比较研究须注明国家与时间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("EndNote", "Zotero", "Mendeley", "RefWorks", "Project MUSE", "PhilPapers", "Philosopher's Index", "NVivo", "Atlas.ti", "MAXQDA", "LaTeX", "Overleaf", "MS Word", "AntConc", "Tarski's World", "Prover9/Mace4", "Dedoose", "R (RStudio)", "SPSS", "LogiQA"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
