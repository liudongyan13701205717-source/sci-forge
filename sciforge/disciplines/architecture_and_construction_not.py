"""建筑与建造学科论文支持：结构体系、构造节点、施工工艺与建造数字化。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="architecture_and_construction_not",
    aliases=(
        "architecture and construction",
        "建筑与建造",
        "建筑构造",
        "建造技术",
        "construction engineering",
        "建筑工程施工",
        "建筑结构与施工",
        "building construction",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "context and literature",
            "methodology",
            "case analysis",
            "findings",
            "engineering implications",
            "references",
        ),
        "experimental": (
            "abstract",
            "introduction",
            "specimen and test setup",
            "materials and methods",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "project_report": (
            "project overview",
            "structural system",
            "key construction nodes",
            "quality and safety control",
            "lessons learned",
            "references",
        ),
    },
    citation_style="作者-年份（GB/T 7714 或 Elsevier 系均可）",
    reporting_standards={
        "experiment": "试件尺寸、加载方案、量测点位与荷载-位移曲线须完整给出",
        "simulation": "有限元模型给网格划分、材料本构与单元类型（ABAQUS/ANSYS/STAAD.Pro）",
        "standard": "引用现行规范（GB 50011/GB 50010/GB 50009）条款号",
        "bim": "BIM 交付给模型精度（LOD/LOI）与数据标准（IFC/BSD）",
    },
    conventions=(
        "材料强度与弹性模量给标准试件与龄期",
        "结构图给比例尺、轴线编号与标高",
        "节点详图给出钢筋配筋表与焊缝符号",
        "试验数据给仪器型号与标定日期",
    ),
    key_venues=(
        "Automation in Construction",
        "Journal of Building Engineering",
        "Engineering Structures",
        "Construction Innovation",
        "Advanced Engineering Informatics",
        "Building Research & Information",
    ),
    units_and_formulas_notes=(
        "混凝土强度 MPa；钢筋等级 HRB/HRB 400；变形 mm",
        "荷载标准值 kN 或 kPa；应力 MPa",
        "抗震设防烈度与特征周期须注明",
        "钢筋屈服强度 MPa；弹性模量 GPa；泊松比无量纲",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "Revit", "Tekla Structures", "ArchiCAD", "Allplan", "Navisworks", "Solibri", "STAAD.Pro", "Robot Structural", "MIDAS", "RISA-3D", "SketchUp", "Rhino", "Grasshopper", "OpenSCAD", "FreeCAD", "AutoCAD Civil 3D", "Revit Structure", "IFC Web Viewer", "ANSYS"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "EI Compendex"),
)
