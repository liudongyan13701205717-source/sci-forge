"""葡萄园建造学科论文支持：葡萄园工程设计与基础设施体裁、IEEE 引用与工程度量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vineyard_construction",
    aliases=("vineyard construction", "葡萄园建造", "葡萄园工程", "vineyard engineering",
             "葡萄园基础设施", "vineyard infrastructure", "葡萄园规划", "vineyard design"),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程问题与研究假设）",
            "methods（设计、选址、施工、监测）",
            "results（性能评估与经济性分析）",
            "discussion（工程外推性与可持续性）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "site description（场地描述）",
            "design and construction（设计与施工）",
            "results（运行评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE（工程类常用）",
    reporting_standards={
        "case_study": "工程案例报告规范",
        "research": "工程研究报告规范",
        "systematic_review": "PRISMA",
    },
    conventions=(
        "坐标与高程须注明基准（如 WGS84 / EGM96）",
        "材料规格须明确：钢管/木桩/不锈钢线等",
        "灌溉设计须给用水量与灌溉制度",
        "电气系统须给负载计算与接地规范",
        "施工方案须给安全与环保措施",
    ),
    key_venues=(
        "Journal of Irrigation and Drainage Engineering",
        "Computers and Electronics in Agriculture",
        "Precision Agriculture",
        "Agricultural Engineering International: CIGR Journal",
        "Journal of Terramechanics",
    ),
    units_and_formulas_notes=(
        "长度给 m；面积给 ha 或 km²",
        "灌溉量给 mm/d 或 m³/ha",
        "坡度给 % 或 °",
        "材料强度给 MPa 或 kN/m²",
        "投资给 元/ha 或 USD/ha",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SketchUp", "Revit", "GIS", "MATLAB", "葡萄园地形测量仪", "葡萄园土壤分析仪", "葡萄园气象站", "葡萄园无人机", "葡萄园灌溉控制器", "葡萄园传感器网络", "葡萄园自动化设备", "葡萄园机器人", "葡萄园喷灌系统", "葡萄园滴灌系统", "葡萄园通风系统", "葡萄园排水系统", "葡萄园照明系统", "葡萄园温室系统", "葡萄园仓库系统"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
