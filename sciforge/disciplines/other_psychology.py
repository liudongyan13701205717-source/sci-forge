"""其他心理学学科论文支持：非主流心理学分支：积极、健康、社会、发展与跨文化心理学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_psychology",
    aliases=("Other Psychology", "其他心理学", "Cognitive Psychology", "Clinical Psychology", "Health Psychology", "Positive Psychology", "Social Psychology", "Developmental Psychology"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "APA伦理准则（知情同意、保密、避免伤害）", "k2": "系统综述遵循PRISMA筛选流程", "k3": "观察/队列研究遵循STROBE报告规范"
    },
    conventions=("使用APA 7格式与心理学术语表（APA Dictionary）", "心理学量表引用须注明原作者、修订者与授权版本", "样本报告须给出人口学特征、样本量与流失率", "伦理审查(IRB)批准与同意书获取须于方法部分声明", "统计分析须报告效应量、置信区间与缺失数据处理"),
    key_venues=("Psychological Bulletin", "Journal Of Personality And Social Psychology", "Annual Review of Psychology", "Psychological Science", "Journal of Consulting and Clinical Psychology", "Emotion"),
    units_and_formulas_notes=("统计显著性：使用p值、效应量（Cohen's d）与95%置信区间", "量表分值须注明测量方式（原始分/标准化分/T分）与常模来源", "样本报告须包含N、年龄范围（M±SD）、性别构成与流失率", "缺失数据须说明处理方法（删除/多重插补/混合模型）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "SAS", "NVivo", "ATLAS.ti", "MAXQDA", "Osiris", "JASP", "Jamovi", "E-Prime", "PsychoPy", "Qualtrics", "SurveyMonkey", "Google Forms", "G*Power", "Zotero", "Endnote", "PsychINFO", "Mplus"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "PubMed"),
)
