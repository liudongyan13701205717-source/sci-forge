"""科学传播学科论文支持：科学传播/科技传播体裁、APA 引用样式与科学传播记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="science_communication",
    aliases=("science_communication", "科学传播", "科技传播", "科学普及", "science communication"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与科学传播问题）",
            "methods（研究设计与样本）",
            "results（传播效果数据）",
            "discussion（传播机理）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（传播案例背景）",
            "analysis（传播策略分析）",
            "conclusions（传播启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Sci Commun 遵循 APA 规范）",
    reporting_standards={
        "survey": "问卷调查遵循 AAPOR 报告规范",
        "content_analysis": "内容分析遵循编码信度报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "experimental": "实验研究遵循 APA 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "受众与样本特征须报告",
        "传播渠道与内容编码须明确",
        "效果指标（知晓度、态度等）须定义",
        "编码者间信度须报告",
        "统计显著性阈值与效应量须明确",
    ),
    key_venues=(
        "Science Communication",
        "Public Understanding of Science",
        "Journal of Science Communication",
        "Science & Education",
        "Frontiers in Communication",
        "Journal of Science Communication (JCOM)",
    ),
    units_and_formulas_notes=(
        "量表分无量纲；比例用 %",
        "公式用 amsmath；信度与效应量计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "信度给出 Cohen's κ 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告", "教案与教材"),
    tools=("数据可视化工具（Matplotlib/Plotly）", "多媒体叙事制作工具", "在线公众科普平台"),
    category="交叉学科",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "DOAJ"),
)