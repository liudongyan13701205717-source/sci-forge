"""社会学论文支持：社会分层、网络分析、定性定量混合方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sociology",
    aliases=("sociology", "social science", "社会学", "社会分层", "社会网络"),
    paper_types={
        "research": ("abstract", "introduction", "theory and hypotheses", "data and methods",
                     "results", "discussion", "conclusion", "references"),
        "qualitative": ("abstract", "introduction", "theoretical framing", "methodology（访谈/参与观察）",
                        "findings", "discussion", "references"),
        "review": ("abstract", "introduction", "scope", "synthesis", "gaps", "references"),
    },
    citation_style="ASA style（作者-年份）",
    reporting_standards={
        "sampling": "抽样框与代表性讨论须给出；加权方案说明",
        "models": "回归模型给系数与稳健标准误；多层模型给 ICC",
        "qualitative": "访谈人数、时长、编码方案（开放编码/轴编码）与信度须报告",
        "mixed": "混合设计的整合点（说明如何互证）须明确",
        "ethics": "被访者匿名化与伦理审查说明",
    },
    conventions=(
        "理论贡献与实证发现分开陈述",
        "表格三线制；变量定义表必须出现",
        "机制解释给反事实推理；避免生态谬误",
        "社会网络图给节点/边定义与布局算法",
    ),
    key_venues=(
        "American Sociological Review",
        "American Journal of Sociology",
        "Social Forces",
        "Annual Review of Sociology",
        "Sociological Methods & Research",
    ),
    units_and_formulas_notes=(
        "效应量与解释力（R²）并列报告；对数几率给 odds ratio 解释",
        "网络指标（中心性/密度）注明计算定义",
    ),
)
