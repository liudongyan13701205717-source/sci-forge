"""建筑施工（Building construction）：施工组织、进度管理与现场方法的研究路径。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="building_construction",
    aliases=("building_construction", "建筑施工", "Building construction",
             "construction management", "施工管理", "construction engineering",
             "建筑工程", "building technology and construction"),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程背景与问题）",
            "case/project description（工程概况、合同形式）",
            "methodology（施工方法、进度模型、BIM 流程说明）",
            "results（工期、成本、质量指标对比）",
            "lessons learned and discussion",
            "conclusion",
            "references",
        ),
    },
    citation_style="Elsevier 样式（建造管理期刊主流）",
    reporting_standards={
        "case_data": "给出工期基准（合同 vs 实际）、成本代码（CAS/SOBS）与变更单统计",
        "progress_model": "进度计划（CPM/PERT）给关键路径、资源约束与缓冲参数",
        "bim_workflow": "BIM 模型 LOD 等级、协同平台（CDE）与交付标准（ISO 19650）写明",
        "hse": "安全记录（TRIR/LTIR）与事故类型分类法（事故树/事件链）说明",
    },
    conventions=(
        "工程信息（业主、结构体系、合同额）在首段完整交代；敏感性数据可用区间值",
        "图表统一编号；甘特图/网络图标注关键路径与非关键路径",
        "结论按「管理启示」与「方法论贡献」分层；避免只罗列事实无分析",
    ),
    key_venues=(
        "Construction Management and Economics",
        "International Journal of Project Management",
        "Building and Environment（施工环境方向）",
        "Journal of Construction Engineering and Management (ASCE)",
        "Automation in Construction",
        "Engineering Project Organization Journal",
    ),
    units_and_formulas_notes=(
        "工期以天/月表示，给日历日与工作日换算；成本按通胀调整至基准年",
        "生产率指标给工日/产量（m³ 混凝土/工日）；机械台班换算为小时",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Project", "Primavera P6", "MS Visio", "AutoCAD", "Revit", "Tekla Structures", "Navisworks", "BIM 360", "Syncro", "PlanSwift", "Cubis", "Dianame", "PowerBI", "SPSS", "Stata", "Python (pandas/scikit-learn)", "R (dplyr)", "Tableau", "QGIS", "DroneDeploy", "Autodesk Forma", "Unicad", "OpenRoads Designer", "Bentley"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Sciencedirect"),
)
