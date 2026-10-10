"""科学传播学科论文支持：科学传播/科技传播/公众理解科学体裁与传播研究规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="science_communication",
    aliases=("science_communication", "科学传播", "科技传播", "科学普及", "science communication", "公众理解科学", "科普传播", "科学传播学"),
    paper_types={
        "research": ("abstract", "introduction（研究背景与传播问题）", "methodology（研究设计与样本）", "results（传播效果数据）", "discussion（传播机理讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（传播案例背景）", "analysis（传播策略分析）", "results（受众反馈）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（传播理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"survey": "问卷调查遵循 AAPOR 规范", "content_analysis": "内容分析遵循编码信度规范", "case_study": "案例研究遵循 COREQ 规范", "systematic_review": "系统综述遵循 PRISMA 声明"},
    conventions=("受众与样本特征须报告", "传播渠道与内容编码须明确", "效果指标（知晓度、态度、行为）须定义", "编码者间信度须报告", "统计显著性阈值与效应量须明确"),
    key_venues=("Science Communication", "Public Understanding of Science", "Journal of Science Communication", "Science & Education", "Frontiers in Communication", "Journal of Communication"),
    units_and_formulas_notes=("量表分无量纲；比例以 % 记", "公式用 amsmath；信度与效应量计算式须明确", "显示公式仅在被引用时编号", "数值结果给出均值 ± SD 与样本量", "信度给出 Cohen's κ 与 95% CI"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "MAXQDA", "ATLAS.ti", "SPSS", "R", "Stata", "Qualtrics", "SurveyMonkey", "Google Analytics (GA4)", "Twitter/X API", "Reddit API", "YouTube API", "Datawrapper", "Tableau", "Power BI", "Matplotlib", "Plotly", "Adobe Creative Cloud", "Figma", "Grammarly"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "DOAJ"),
)
