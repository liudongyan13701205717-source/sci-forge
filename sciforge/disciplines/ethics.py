"""伦理学科论文支持：伦理学、应用伦理与道德哲学研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ethics",
    aliases=(
        "ethics", "伦理学", "道德哲学",
        "ethics", "伦理学",
        "moral philosophy", "道德哲学",
        "applied ethics", "应用伦理",
        "bioethics", "生命伦理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（伦理问题与背景）",
            "methodology（伦理分析、哲学论证、案例研究）",
            "results（伦理分析与评估）",
            "discussion（伦理优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "ethical analysis（伦理分析）",
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
        "analysis": "伦理分析须注明理论框架",
        "case": "案例分析须注明来源与时间",
        "comparison": "比较研究须注明国家与时间",
    },
    conventions=(
        "伦理概念须定义清晰",
        "哲学论证须注明理论框架",
        "案例须注明来源与时间",
        "比较研究须注明国家与时间",
    ),
    key_venues=(
        "Ethics",
        "Journal of Philosophy",
        "Philosophy and Phenomenological Research",
        "Synthese",
        "Philosophical Studies",
        "Australasian Journal of Philosophy",
    ),
    units_and_formulas_notes=(
        "伦理概念须定义清晰",
        "哲学论证须注明理论框架",
        "案例须注明来源与时间",
        "比较研究须注明国家与时间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("EndNote", "Zotero", "Mendeley", "RefWorks", "Project MUSE", "PhilPapers", "Philosopher's Index", "NVivo", "Atlas.ti", "MAXQDA", "LaTeX", "Overleaf", "MS Word", "Qualtrics", "SurveyMonkey", "R (RStudio)", "SPSS", "Dedoose", "AntConc", "LogicGator"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
