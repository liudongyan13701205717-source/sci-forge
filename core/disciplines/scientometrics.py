"""科学计量学学科论文支持：科学计量学/科研评价体裁、APA 引用样式与科学计量学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="scientometrics",
    aliases=("scientometrics", "科学计量学", "科研评价", "科学指标", "scientometrics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与计量问题）",
            "methods（数据与指标）",
            "results（科研系统数据）",
            "discussion（科研政策意义）",
            "references",
        ),
        "indicator_study": (
            "abstract",
            "introduction",
            "methods（指标构建与数据）",
            "results（指标验证）",
            "discussion（与既有指标对比）",
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
    citation_style="APA 样式（作者-年份；Scientometrics 遵循 Springer 规范）",
    reporting_standards={
        "indicator": "指标研究遵循指标构建报告规范",
        "bibliometric": "文献计量研究遵循 PRISMA-S 检索报告规范",
        "network_analysis": "网络分析遵循网络研究报告规范",
        "data_quality": "数据质量遵循数据来源报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "指标定义与计算口径须明确",
        "数据源与覆盖范围须报告",
        "指标效度与稳健性检验须报告",
        "学科归一化方法须注明",
        "政策建议与指标局限须区分",
    ),
    key_venues=(
        "Scientometrics",
        "Journal of Informetrics",
        "Quantitative Science Studies",
        "Research Policy",
        "Science and Public Policy",
        "Journal of the Association for Information Science and Technology",
    ),
    units_and_formulas_notes=(
        "指标无量纲；比例用 %；时间用年份",
        "公式用 amsmath；归一化与百分位计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "稳健性给出敏感性分析结果",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "数据集"),
    tools=("R 界面 Biblioshiny", "CiteSpace", "Python 科学计量网络分析"),
    category="交叉学科",
    databases=("OpenAlex", "Crossref", "arXiv", "Semantic Scholar"),
)