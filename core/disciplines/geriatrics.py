"""老年医学学科论文支持：老年临床/衰弱体裁、AGS/JAGS 引用样式与老年医学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geriatrics",
    aliases=("geriatrics", "老年医学", "老年科", "老年病学",
             "geriatric medicine", "老年健康"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与老年问题）",
            "methods（研究设计与人群）",
            "results（功能与结局数据）",
            "discussion（机理与临床意义）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法与统计）",
            "results（疗效与安全性终点）",
            "discussion（与既往试验对比）",
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
    citation_style="AGS/JAGS 样式（作者-年份；J Am Geriatr Soc 遵循 AGS 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "qualitative": "质性研究遵循 COREQ/SRQR 指南",
    },
    conventions=(
        "衰弱评估工具（Fried、FI 等）首次出现给出全称",
        "功能状态（ADL/IADL）评估须报告",
        "多重用药（polypharmacy）定义须明确",
        "认知评估（MMSE、MoCA）须注明版本",
        "老年综合征（跌倒、谵妄）定义须规范",
    ),
    key_venues=(
        "Journal of the American Geriatrics Society",
        "Age and Ageing",
        "The Journals of Gerontology Series A",
        "JAMA Internal Medicine",
        "The Lancet Healthy Longevity",
        "Journal of Gerontology: Medical Sciences",
    ),
    units_and_formulas_notes=(
        "量表分数无量纲；时间用月/年",
        "公式用 amsmath；衰弱指数与评分计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "生存/事件分析给出 HR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("老年人综合评估（CGA）软件", "SPSS", "R"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Europe PMC", "CNKI"),
)