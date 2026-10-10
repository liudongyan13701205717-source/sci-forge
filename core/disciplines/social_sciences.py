"""社会科学总学科论文支持：跨分支方法与理论体裁、Chicago/APA 引用样式与社科统计规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_sciences",
    aliases=("social_sciences", "社会科学", "社会科学总论", "social science", "cross-disciplinary social science", "socioeconomic research", "social science research", "empirical social science"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与理论框架）",
            "methods（数据、变量、模型、抽样）",
            "results（结果与稳健性）",
            "discussion（讨论与含义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例与情境）",
            "analysis（过程与机制）",
            "results",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "literature search（文献检索）",
            "evidence synthesis（跨案例证据综合）",
            "future directions",
            "references"
        )
    },
    citation_style="Chicago 作者-年份或 APA 7（视期刊与分支传统）",
    reporting_standards={
        "quantitative": "抽样设计、加权与缺失数据处理须说明；调查数据给出样本框与回应率",
        "qualitative": "定性研究遵循 COREQ/SRQR 清单：研究者位置、抽样逻辑、饱和判断",
        "mixed_methods": "混合设计用联合展示表（joint display）呈现整合点",
        "ethics": "知情同意、匿名化与被试保护声明；敏感议题给出伦理审查信息"
    },
    conventions=(
        "理论框架先行：明确对话的理论传统与概念定义",
        "概念操作化透明：概念 → 指标 → 测量的链条在方法中给出",
        "定量表格三线制；类别变量给频数与百分比（注明基数 N）",
        "定性引用给转写行号或时间戳，并标注受访者编号与匿名化名",
        "混合设计用联合展示表（joint display）呈现整合"
    ),
    key_venues=(
        "American Sociological Review",
        "Annual Review of Sociology",
        "Social Forces",
        "World Politics",
        "British Journal of Sociology"
    ),
    units_and_formulas_notes=(
        "百分比给出基数 N；加权数据注明权重变量",
        "效应量与显著性并列报告，避免只报 p 值",
        "多层/面板数据说明层级结构与时点数",
        "定性材料引用格式统一（受访者编号：行号）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "RStudio", "Python", "SPSS", "NVivo", "MAXQDA", "ATLAS.ti", "Dedoose", "Transana", "Mplus", "AMOS", "JASP", "jamovi", "Qualtrics", "SurveyMonkey", "Zotero", "Mendeley", "Tableau", "Gephi"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI")
)
