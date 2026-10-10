"""环境伦理学科论文支持：环境哲学、生态伦理与可持续发展伦理研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environmental_ethics",
    aliases=(
        "environmental_ethics", "环境伦理", "生态伦理",
        "environmental ethics", "环境伦理",
        "ecological ethics", "生态伦理",
        "sustainability ethics", "可持续伦理",
        "environmental philosophy", "环境哲学",
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
        "Environmental Ethics",
        "Journal of Agricultural and Environmental Ethics",
        "Ethics, Policy & Environment",
        "Environmental Values",
        "Journal of Environmental Philosophy",
        "Philosophy & Public Affairs",
    ),
    units_and_formulas_notes=(
        "伦理概念须定义清晰",
        "哲学论证须注明理论框架",
        "案例须注明来源与时间",
        "比较研究须注明国家与时间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("EndNote", "Zotero", "Mendeley", "RefWorks", "Legal Citation Software", "Case Analysis Software", "NVivo", "Atlas.ti", "MAXQDA", "Qualtrics", "SurveyMonkey", "Otter.ai", "LaTeX", "XMind", "Miro", "VOSviewer", "R (RStudio)", "SPSS", "Tableau", "Word"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
