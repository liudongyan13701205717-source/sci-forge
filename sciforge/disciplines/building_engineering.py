"""建筑工程（Building engineering）：结构、机电与建筑性能的研究方法与写作约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="building_engineering",
    aliases=("building_engineering", "建筑工程", "Building engineering",
             "civil engineering", "土木工程", "structural engineering", "结构工程",
             "construction engineering", "建筑工程技术"),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程背景与问题）",
            "theoretical / numerical model（力学模型、有限元设置、试验制度）",
            "results（应力、变形、承载力、机电性能指标）",
            "verification（与规范条文、既有数据或实测对照）",
            "conclusion",
            "references",
        ),
    },
    citation_style="Elsevier 样式或 ASCE 样式",
    reporting_standards={
        "fem": "单元类型、网格收敛性检验（≥3 级）、材料参数（fck、Ec、本构曲线）与边界条件完整",
        "experiment": "试件尺寸、养护条件、加载速率、传感器布置；破坏照片编号引用",
        "mep": "暖通/给排水/电气性能指标给设计参数（负荷指标 W/m²、供回水温度、流量）",
        "code_check": "验算对照规范条文号（GB 50010/Eurocode），给安全系数与富余率",
    },
    conventions=(
        "单位制统一 SI（kN、kPa、MPa）；符号先定义后使用，全文一致",
        "FEM 结果区分节点/单元值；局部应力集中须说明网格敏感性",
        "试验曲线附原始数据表与拟合方程；不确定度按 GUM A 类评定标注",
    ),
    key_venues=(
        "Engineering Structures",
        "Construction and Building Materials",
        "Journal of Building Engineering",
        "International Journal of Mechanical Sciences",
        "Engineering Failure Analysis",
        "Journal of Building Performance (Building Simulation)",
    ),
    units_and_formulas_notes=(
        "应力 MPa；混凝土强度等级 C30~C80 与 fc 换算；应变 1e-6 标注",
        "暖通负荷 W/m²、空气流量 m³/h；水头 m；电气功率 kW/UA·K",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS Mechanical", "ANSYS CivilFEM", "SAP2000", "MIDAS Civil", "ETABS", "STAAD.Pro", "ABAQUS", "PLAXIS", "OpenSees", "NASTRAN (MSC)", "RFEM", "SCIA Engineer", "Revit", "Tekla Structures", "Carrier HAP", "HAP-Systems", "DIALux", "e3Viz", "IesLight", "HAP", "Autodesk Revit MEP", "MagiCad", "Aquilon", "QGIS"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "ScienceDirect"),
)
