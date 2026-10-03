"""公共管理学科论文支持：治理/政策执行/组织体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="public_administration",
    aliases=("public_administration", "公共管理", "行政管理", "公共政策"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "theory（理论框架）",
            "hypotheses（假设）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case selection（案例选择）",
            "analysis（分析）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "policy_evaluation": (
            "abstract",
            "introduction",
            "policy design（政策设计）",
            "evaluation method（评估方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Public Administration Review 遵循 APA 规范）",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "evaluation": "政策评估遵循评估报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "理论框架与假设须明确",
        "数据来源与样本须说明",
        "政策背景须交代",
        "因果识别策略须报告",
        "局限与推广性须讨论",
    ),
    key_venues=(
        "Public Administration Review",
        "Journal of Public Administration Research and Theory",
        "Public Management Review",
        "Governance",
        "American Review of Public Administration",
        "Public Administration",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "效应量用 Cohen's d 或 η²",
        "回归系数给出标准误与显著性",
        "样本量须报告",
        "货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("SPSS", "Stata（面板与因果推断）", "NVivo（政策文本质性编码）", "R（统计与可视化）",
           "Python（Pandas/Statsmodels）"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)