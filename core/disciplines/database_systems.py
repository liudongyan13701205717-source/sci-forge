"""数据库系统学科论文支持：数据管理/查询处理体裁、ACM 引用样式与数据库记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="database_systems",
    aliases=("database_systems", "数据库系统", "数据库", "数据管理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "design（系统设计）",
            "implementation（实现）",
            "evaluation（评估）",
            "references",
        ),
        "system_paper": (
            "abstract",
            "introduction",
            "architecture（架构）",
            "query processing（查询处理）",
            "storage（存储）",
            "evaluation（评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；SIGMOD/VLDB 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "实验遵循数据库论文评估规范",
        "benchmark": "基准测试遵循 TPC 报告规范",
        "reproducibility": "可复现性遵循系统论文可复现性清单",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_study": "案例研究遵循系统案例报告规范",
    },
    conventions=(
        "数据集与工作负载须报告",
        "查询集与参数须明确",
        "索引/存储配置须说明",
        "对比基线须公平（同硬件）",
        "扩展性实验须报告",
    ),
    key_venues=(
        "SIGMOD",
        "VLDB",
        "ICDE",
        "ACM Transactions on Database Systems",
        "The VLDB Journal",
        "IEEE Transactions on Knowledge and Data Engineering",
    ),
    units_and_formulas_notes=(
        "吞吐量用 tps；延迟用 ms；数据量用 GB/TB",
        "公式用 amsmath；查询计划与算法须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("PostgreSQL", "MySQL", "DuckDB", "Python"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)