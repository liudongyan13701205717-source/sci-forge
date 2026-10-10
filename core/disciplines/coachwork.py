"""车辆装配/车身加工学科论文支持：车辆设计与制造体裁、SAE 引用样式与车身工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="coachwork",
    aliases=("coachwork", "车辆装配", "车身加工", "整车制造",
             "底盘装配", "商用车车身", "客车车身",
             "coach building", "body-in-white", "vehicle assembly",
             "chassis construction", "motor vehicle manufacturing"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（车身结构、材料与制造工艺）",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "design_report": (
            "abstract",
            "requirements（设计规范与安全标准）",
            "design and process",
            "verification（NVH、碰撞、耐久）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "state of the art",
            "future directions",
            "references",
        ),
    },
    citation_style="SAE 样式（作者-字母编号，Journal of SAE International）",
    reporting_standards={
        "safety": "车辆安全遵循 GB 1589、GB 21670、ISO 15005 与 ECE R94",
        "crash_test": "碰撞试验遵循 C-NCAP / Euro-NCAP / J-NCAP 规范",
        "NVH": "NVH 试验遵循 ISO 7941、ISO 362、ISO 5130",
        "structural": "结构强度遵循 ISO 10360、GB/T 30790",
        "reproducibility": "制造工艺（焊接/涂装/冲压）须给出工艺参数与检测项目",
    },
    conventions=(
        "车型与车身形式须按 GB 1589 或 ISO 3833 分类标注",
        "质量与刚度指标须分别报告整车/白车身/组件三个层级",
        "试验温度、湿度、载荷工况须给出",
        "碰撞与 NVH 试验须给出标准编号与版本年份",
        "结论须明确车型与工况适用范围",
    ),
    key_venues=(
        "SAE International Journal of Commercial Vehicles",
        "SAE International Journal of Passenger Cars - Mechanical Systems",
        "Vehicular System Dynamics",
        "International Journal of Crashworthiness",
        "SAE Technical Papers Series",
        "Journal of Sound and Vibration",
        "Archives of Civil and Mechanical Engineering",
    ),
    units_and_formulas_notes=(
        "质量用 kg；刚度用 N/m 或 N·m/deg",
        "NVH 用 dB(A)；振动加速度用 m/s²",
        "碰撞试验报告 CRASH 与 VMO（Vehicle Matched Overlay）曲线",
        "结构分析给出位移 mm、应力 MPa、应变 mm/m",
        "公式用 amsmath；材料参数符号须定义（E、σ、ν 等）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CATIA V5/V6", "NXP (Delmia)", "NX (Siemens)", "ANSYS", "Abaqus", "HyperMesh", "Optistruct", "Radioss", "LS-DYNA", "Adams", "MSC Nastran", "SolidWorks", "CREO", "Teamcenter", "Windchill", "MATLAB/Simulink", "Star-CCM+", "Altair MotionWorks", "3D Systems Geomagic", "KUKA RobotWare"),
    category="工学",
    databases=("OpenAlex", "Crossref", "ScienceDirect", "SAE Mobility"),
)
