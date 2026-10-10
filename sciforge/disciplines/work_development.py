"""职业发展学科论文支持：职业生涯与人力开发体裁、APA 引用样式与人因统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="work_development",
    aliases=("work development", "职业发展", "职业生涯发展", "人力开发", "职业成长",
             "career development", "workforce development", "career progression"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与研究问题）",
            "literature review（文献综述与理论框架）",
            "methods（样本、测量与分析）",
            "results（假设检验与发现）",
            "discussion（理论与实践意义）",
            "references",
        ),
        "qualitative": (
            "abstract",
            "introduction",
            "theoretical framework（理论框架）",
            "methods（抽样、访谈与编码）",
            "findings（主题与引语）",
            "discussion（反思与局限）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Journal of Vocational Behavior 遵循 APA 规范）",
    reporting_standards={
        "quantitative": "定量研究须报告样本、测量信效度与统计方法",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "psychometric": "量表使用须报告信度（α/ω）与效度证据",
        "ethics": "涉及人类被试须报告伦理审查与知情同意",
    },
    conventions=(
        "职业阶段/模型术语须界定并引用理论来源",
        "量表须给出信度系数与来源",
        "样本特征（行业、职级）须报告",
        "效应量（Cohen's d/η²）须报告",
        "缺失数据处理方式须交代",
    ),
    key_venues=(
        "Journal of Vocational Behavior",
        "Career Development International",
        "Journal of Career Development",
        "Human Resource Development Quarterly",
        "Journal of Organizational Behavior",
        "Personnel Psychology",
    ),
    units_and_formulas_notes=(
        "量表分数须报告均值、SD 与信度",
        "效应量用 Cohen's d、η² 或 r",
        "路径系数用 β 并给出标准误",
        "缺失率用 %；样本量须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Holland 职业兴趣量表 (SDS)", "MBTI 职业性格测评", "Strong Interest Inventory", "LinkedIn", "Qualtrics", "SPSS", "R (lavaan/psych)", "Mplus", "AMOS (SEM)", "Python (pandas)", "NVivo", "ATLAS.ti", "Workday 人才管理系统", "HRIS", "Moodle 学习管理系统", "Kirkpatrick 评估工具", "360 度反馈系统", "Tableau", "Power BI", "Zotero"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "PsycINFO", "CNKI"),
)
