"""科学技术研究学科论文支持：科学技术研究（STS）/科学社会学/技术哲学体裁与跨学科规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="science_technology_studies",
    aliases=("science_technology_studies", "科学技术研究", "科学技术与社会", "科学社会学", "STS", "science and technology studies", "技术哲学", "创新研究"),
    paper_types={
        "research": ("abstract", "introduction（STS 问题与理论）", "methodology（经验或理论方法）", "results（研究结果）", "discussion（社会意义讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（技术案例背景）", "analysis（技术-社会分析）", "results（影响评估）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（STS 理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 风格（STS 领域常用芝加哥引用）",
    reporting_standards={"ethnography": "民族志研究遵循 COREQ 规范", "survey": "问卷调查遵循 AAPOR 规范", "systematic_review": "系统综述遵循 PRISMA 声明"},
    conventions=("理论框架须明确（社会建构主义/行动者网络等）", "经验材料来源须报告", "访谈须匿名化", "技术术语须定义", "跨学科视角须说明分析层级"),
    key_venues=("Science, Technology, & Human Values", "Social Studies of Science", "Studies in History and Philosophy of Modern Physics", "Research Policy", "Techné", "Technology Analysis & Strategic Management"),
    units_and_formulas_notes=("样本量与访谈人数须报告", "文献计量指标须定义", "公式用 LaTeX；行内公式避免复杂分式", "信度与有效性须讨论"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "专利", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "MAXQDA", "ATLAS.ti", "VOSviewer", "CiteSpace", "RefWorks", "Zotero", "EndNote", "Matplotlib", "NetworkX", "R", "SPSS", "Stata", "MATLAB", "Excel", "Grammarly", "Gephi", "OpenRefine", "Obsidian", "LaTeX"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "DOAJ", "Web of Science", "Scopus", "Google Scholar"),
)
