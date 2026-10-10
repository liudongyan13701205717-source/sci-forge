"""建筑与土木工程（Building and civil engineering）：结构、岩土与工程实践的研究方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="building_and_civil_engineering",
    aliases=("building_and_civil_engineering", "建筑与土木工程", "Building and civil engineering",
             "civil engineering", "土木工程", "structural engineering", "结构工程",
             "岩土工程", "geotechnical engineering"),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程背景与研究缺口）",
            "theoretical framework / governing equations（设计标准与力学模型）",
            "numerical model or experiment setup（有限元网格、材料本构、边界条件；试验制度与加载方案）",
            "results（位移/应力/变形曲线、破坏模式）",
            "verification and comparison（与规范条文、既有文献或实测数据对照）",
            "conclusion",
            "references",
        ),
    },
    citation_style="Elsevier 样式（建筑土木主流期刊）或 ASCE 样式",
    reporting_standards={
        "fem": "给单元类型、网格收敛性检验（至少 3 级网格）与材料模型参数（fck、Ec、本构曲线）",
        "experiment": "试件尺寸、养护条件、加载速率与传感器布置；破坏照片编号引用",
        "site_data": "岩土参数（标限、CPT）给测试标准（GB/ASTM/ISO）与深度分层",
        "design_check": "验算结果对照现行规范条文号（GB 50010、Eurocode 等），给富余率",
    },
    conventions=(
        "单位制统一（kN、kPa、MPa；SI）；符号全文一致，先定义后使用",
        "有限元结果区分节点/单元平均应力；局部应力集中须说明网格影响",
        "试验曲线给原始数据与拟合方程；不确定度按 GUM 或 A 类评定标注",
    ),
    key_venues=(
        "Engineering Structures",
        "Journal of Engineering Mechanics (ASCE)",
        "Journal of Geotechnical and Geoenvironmental Engineering (ASCE)",
        "Construction and Building Materials",
        "Soils and Foundations",
        "International Journal of Solids and Structures",
    ),
    units_and_formulas_notes=(
        "应力 MPa、强度等级 C30~C80 与 fc 值换算；应变 1e-6 标注量级",
        "弯矩 M=kN·m、荷载 q=kN/m²；抗震给设防烈度与反应谱周期",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS Mechanical", "ANSYS CivilFEM", "SAP2000", "MIDAS Civil", "ETABS", "STAAD.Pro", "Tekla Structures", "Autodesk Robot Structural Analysts", "OpenSees", "ABAQUS", "PLAXIS", "geoslope (PLAXIS 3D)", "LEAPCrust", "NASTRAN (MSC Nastran)", "RFEM", "SCIA Engineer", "RISA-3D", "Autodesk Civil 3D", "MicroStation", "QGIS", "AutoCAD Civil", "Revit", "Mathcad", "Oasys G1"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "ScienceDirect"),
)
