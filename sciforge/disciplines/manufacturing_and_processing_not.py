"""制造与加工未分类学科论文支持：加工制造技术、工艺优化与工业工程研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="manufacturing_and_processing_not",
    aliases=(
        "manufacturing_and_processing_not",
        "制造与加工",
        "加工制造",
        "制造工艺",
        "Manufacturing",
        "Processing Engineering",
        "Manufacturing Technology",
        "加工技术",
        "工业制造",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（机械工程与制造学通用）",
    reporting_standards={
        "fabrication": "制造工艺遵循 ISO 9001 与 ISO 14001 规范",
        "experimental": "实验研究遵循 ASTM 与 ISO 标准",
        "case_study": "案例研究遵循案例研究报告规范",
    },
    conventions=(
        "加工参数须标注单位（如 mm、mm/min、rpm）",
        "表面粗糙度以 Ra（μm）报告",
        "材料牌号须遵循 GB/T 或 ASTM 标准",
        "刀具/夹具须标注型号与几何参数",
        "测试仪器须标注精度与校准状态",
    ),
    key_venues=(
        "Journal of Materials Processing Technology",
        "International Journal of Machine Tools and Manufacture",
        "CIRP Annals",
        "Precision Engineering",
        "Journal of Manufacturing Science and Engineering",
        "机械工程学报",
    ),
    units_and_formulas_notes=(
        "长度以 mm 报告并遵循 GB/T 2971",
        "切削速度 v_c 以 m/min 报告",
        "进给量 f 以 mm/r 报告",
        "切削力 F 以 N 报告",
        "温度以 °C 报告并标注测量方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SolidWorks", "AutoCAD", "CATIA V5", "CATIA 3DEXPERIENCE", "Siemens NX", "Creo Parametric", "Fusion 360", "FreeCAD", "Inventor", "SolidEdge", "STEP", "IGES", "STL", "DXF", "DWG", "MATLAB", "ANSYS", "HyperWorks", "Abaqus", "SolidCAM"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
