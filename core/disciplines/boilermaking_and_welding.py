"""锅炉制造与焊接学科论文支持：焊接冶金/压力容器体裁、AWS/ASME 引用样式与焊接记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="boilermaking_and_welding",
    aliases=(
        "boilermaking_and_welding",
        "boilermaking",
        "welding",
        "Boilermaking and welding",
        "锅炉制造",
        "焊接工程",
        "压力容器制造",
        "锅炉锻造",
        "welding and fabrication",
        "boiler fabrication",
        "金属焊接",
        "锅炉工",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（试件制备、焊接参数与检测）",
            "results（金相、力学、无损检测结果）",
            "discussion",
            "conclusion",
            "references",
        ),
        "design": (
            "abstract",
            "design basis",
            "weld procedure specification (WPS)",
            "non-destructive testing plan",
            "pressure boundary analysis",
            "references",
        ),
    },
    citation_style="AWS/ASME 样式（作者-年份，AWS D1.1 与 ASME BPVC Section V 规范引用）",
    reporting_standards={
        "procedure": "焊接工艺规程（WPS）须完整给出参数（电流、电压、速度、热输入）",
        "materials": "母材与填充材料牌号须报告",
        "qualification": "焊工资格（WPS/PQR）须符合 AWS D1.1 或 ASME BPVC",
        "ndt": "无损检测结果须符合 ASME BPVC Section V",
        "code_section": "引用压力容器规范须明确版本（ASME BPVC Section I/V/VIII 等）",
    },
    conventions=(
        "焊接位置符号用 1G/2G/3G/4G/5G/6G 或 F/H/V 标记",
        "焊接工艺符号用 SMAW/GMAW/GTAW/FCAW/SAW/EBW/LBW/FSW 标准缩写",
        "热输入 H = P·I·U·η / v（kJ/mm）",
        "金相照片须标注放大倍数与显影方法",
        "无损检测符号 UT/RT/MT/PT 全文一致",
    ),
    key_venues=(
        "International Journal of Pressure Vessels and Piping",
        "Materials Science and Engineering A",
        "Welding Journal",
        "Welding in the World",
        "Journal of Materials Processing Technology",
        "Engineering Fracture Mechanics",
        "Metallurgical and Materials Transactions A",
    ),
    units_and_formulas_notes=(
        "热输入单位 kJ/mm；温度用 ℃；压力用 MPa",
        "力学性能用 MPa 与 mm 报告",
        "无损检测灵敏度以 dB 与 %A 标注",
        "金相照片报告放大倍数与显影试剂",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Ansys", "Abaqus", "Simufact Additive", "MSC Marc", "COMSOL Multiphysics", "MATLAB", "Pro-Tech WeldPro", "HypoTherm", "Zeiss SEM", "Thermo Fisher SEM", "JEOL SEM", "Bruker XRD", "Rigaku XRD", "Gleeble", "Evident FlawMaster", "Sonatest TOFD", "GE RayTech", "Miller Welders", "Lincoln Electric Welders", "ESAB Welders"),
    category="工学",
    databases=("OpenAlex", "Google Scholar", "ScienceDirect", "AWS Webstore", "ASME Digital Collection"),
)
