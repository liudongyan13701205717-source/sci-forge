"""建筑技术（Building technology）：材料、构造与设备系统的研究方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="building_technology",
    aliases=("building_technology", "建筑技术", "Building technology",
             "construction technology", "施工技术", "building materials",
             "建筑材料", "building services", "建筑设备"),
    paper_types={
        "research": (
            "abstract",
            "introduction（技术问题与既有方案）",
            "materials / systems description（材料组成、构造层次或设备参数）",
            "experiment or simulation methodology（试验制度、加载/测试标准；仿真边界条件）",
            "results（强度、热工、声学、耐久性能指标）",
            "comparison and discussion（与规范限值、既有产品对比）",
            "conclusion",
            "references",
        ),
    },
    citation_style="Elsevier 样式（Construction and Building Materials 系）",
    reporting_standards={
        "materials": "原材料来源、配比与养护条件；试件尺寸、数量与龄期写明",
        "testing": "测试标准号（GB/ISO/ASTM）与方法版本；重复试件数与离散度（标准差/变异系数）",
        "thermal": "热工参数（U 值、热惰性指标 D）按 ISO 6946 或 GB/T 8484 标注方法",
        "acoustic": "隔声量 Rw/计权隔声与背景噪声；混响时间按 ISO 3382 采样",
    },
    conventions=(
        "单位制统一 SI；强度 MPa、导热系数 W/(m·K)；比表面积 m²/kg",
        "试件编号与测试日期对应；曲线给原始数据与拟合方程",
        "多因素试验给正交设计/响应面参数范围；优化结果附验证试验",
    ),
    key_venues=(
        "Construction and Building Materials",
        "Building & Environment",
        "Cement and Concrete Research",
        "Applied Energy",
        "Materials (MDPI)",
        "Building Research & Information (RIBA BRANZ)",
    ),
    units_and_formulas_notes=(
        "混凝土强度 C 等级与 fc 换算；砖抗压强度 MPa；导热系数 W/(m·K)",
        "设备效率给工况点（部分负荷）；能效比 EER/COP 注明计算条件",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS Mechanical", "ABAQUS", "EnergyPlus", "DesignBuilder", "e3Viz", "IesLight", "DIALux", "Carrier HAP", "MagiCad", "Autodesk Revit MEP", "Mathematica", "MATLAB", "OpenFOAM", "COMSOL Multiphysics", "ANSYS Fluent", "SolidWorks", "Fusion 360", "AutoCAD", "Navisworks", "SPSS", "Minitab", "Origin", "JMP", "Python (NumPy/SciPy)"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "ScienceDirect"),
)
