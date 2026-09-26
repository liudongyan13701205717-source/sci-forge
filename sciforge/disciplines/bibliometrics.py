"""文献计量学学科论文支持：文献计量学/引文分析体裁、APA 引用样式与文献计量学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bibliometrics",
    aliases=("bibliometrics", "文献计量学", "引文分析", "文献计量", "bibliometric analysis"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与计量问题）",
            "methods（数据源与指标）",
            "results（计量数据）",
            "discussion（学科图景）",
            "references",
        ),
        "bibliometric_analysis": (
            "abstract",
            "introduction",
            "data（数据源与检索策略）",
            "analysis（计量指标分析）",
            "discussion（研究前沿与趋势）",
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
        "bibliometric": "文献计量研究遵循 PRISMA-S 检索报告规范",
        "network_analysis": "共现/共引网络遵循网络研究报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_quality": "数据质量遵循数据来源报告规范",
        "reproducibility": "可复现性遵循检索策略报告规范",
    },
    conventions=(
        "数据源（WoS、Scopus 等）与检索日期须报告",
        "检索策略与筛选标准须可复现",
        "计量指标（h 指数、影响因子等）须定义",
        "数据清洗与去重流程须说明",
        "分析工具与版本须注明",
    ),
    key_venues=(
        "Scientometrics",
        "Journal of Informetrics",
        "Journal of the Association for Information Science and Technology",
        "Quantitative Science Studies",
        "Research Evaluation",
        "Journal of Documentation",
    ),
    units_and_formulas_notes=(
        "指标无量纲；比例用 %；时间用年份",
        "公式用 amsmath；h 指数与标准化计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与文献量",
        "网络指标给出显著性检验结果",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "数据集"),
    tools=("文献计量软件（CiteSpace）", "R 包 Bibliometrix", "Python 数据分析（Pandas）"),
    category="交叉学科",
    databases=("OpenAlex", "Crossref", "Semantic Scholar", "arXiv"),
)