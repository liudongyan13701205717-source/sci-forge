"""细胞技术学科论文支持：细胞分离/自动化细胞处理/单细胞技术体裁与引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cell_technology",
    aliases=(
        "cell technology",
        "cell processing",
        "cell sorting",
        "single cell technology",
        "automated cell processing",
        "cell culture technology",
        "细胞技术",
        "细胞处理",
        "细胞分选",
        "单细胞技术",
        "自动化细胞处理",
        "细胞培养技术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（细胞技术需求与应用场景）",
            "materials and methods（细胞来源、分选与培养条件）",
            "results（回收率、活力与功能验证）",
            "discussion（平台通量、重复性与局限）",
            "conclusions",
            "references",
        ),
        "methods": (
            "abstract",
            "introduction",
            "protocol（分选策略与自动化流程）",
            "validation（回收率、纯度与功能验证）",
            "troubleshooting",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "taxonomy（按分选原理/平台分类）",
            "main developments",
            "future directions",
            "references",
        ),
    },
    citation_style="Cytometry Part A 样式；方法类引用 Current Protocols 与 JoVE",
    reporting_standards={
        "recovery": "细胞回收率与活力须报告，说明采样时点与染色方法",
        "sorting": "单细胞分选须给出排序器型号、阈值设置与双阳性去除策略",
        "automation": "自动化平台须报告通量、重复性 CV% 与批间差异",
        "culture": "细胞培养条件（CO₂/湿度/培养基）与传代代数须记录",
        "reagents": "试剂批号与细胞储存条件（液氮/超低温）须可追溯",
    },
    conventions=(
        "细胞回收率与活力须报告（台盼蓝/流式活死染色），并说明采样时点",
        "单细胞分选须给出排序器型号、阈值设置与双阳性去除策略",
        "自动化平台须报告通量、重复性 CV% 与批间差异",
        "细胞培养条件（CO₂/湿度/培养基）与传代代数须记录",
        "试剂批号与细胞储存条件（液氮/超低温）须可追溯",
    ),
    key_venues=(
        "Cytometry Part A",
        "Cytometry Part B (Clinical Cytometry)",
        "BioTechniques",
        "Journal of Laboratory Automation",
        "Lab Chip",
        "Current Protocols",
    ),
    units_and_formulas_notes=(
        "细胞浓度用 个/mL；通量用 个/秒 或 细胞/小时",
        "活力用 %；回收率用 %",
        "重复性用 CV%；温度用 ℃；时间用 min/h",
        "流式数据须说明补偿策略与活细胞门",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("BD FACSMelody 分选仪", "Sony MA900 流式细胞仪", "BD FACSDiva 软件", "10x Genomics Chromium X", "ImageStream Mark II", "BD CellenOne 单细胞分选", "BD BioLector 实时细胞分析", "Miltenyi MACS 磁珠分选", "Thermo CountStar 细胞计数仪", "Metamorph 成像软件", "FlowJo 软件", "CellProfiler", "Seurat 单细胞分析", "Thermo 二氧化碳培养箱", "Cytiva BIOSTAT 生物反应器", "Controlled Rate Freezer 细胞冻存仪", "BD Horizon 流式染色", "Simplic 单细胞捕获", "Thermo 流式细胞仪", "BD 磁珠分离系统"),
    category="理学",
    databases=("PubMed", "OpenAlex", "bioRxiv", "PubMed Central"),
)
