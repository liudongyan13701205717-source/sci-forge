"""制表学科论文支持：精密钟表工程、材料科学与钟表制造工艺的体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="watchmaking",
    aliases=("watchmaking", "制表", "钟表制造", "钟表工程", "精密制表",
             "watchmaking", "horology", "horology engineering",
             "clockmaking", "precision watch engineering"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "design description（设计描述）",
            "materials and methods（材料与工艺）",
            "results（性能测试结果）",
            "discussion（讨论）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "watch mechanism description（机芯描述）",
            "manufacturing process（制造流程）",
            "quality control（质量控制）",
            "performance evaluation（性能评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "history of horology（钟表史综述）",
            "movement types and mechanisms（机芯类型与机构综述）",
            "materials and manufacturing technologies（材料与制造技术综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "precision_specification": "精度参数须标注测试条件（温度、湿度、摆幅）与测量不确定度",
        "repeatability": "重复性测试须给出 ≥10 次测量的均值与标准差",
        "design_documentation": "设计图纸须包含公差标注、材料规格与装配顺序说明",
    },
    conventions=(
        "时间精度以 s/d 或 s/month 为单位",
        "尺寸公差以 μm 为单位，关键部件标注 GD&T（几何尺寸与公差）",
        "摆轮振动频率以 Hz 或 vph（次/小时）标注",
        "材料标注采用 ASTM 或 ISO 牌号",
        "力矩/扭矩以 mN·m 为单位",
    ),
    key_venues=(
        "Horological Journal",
        "Swiss Watch Magazine",
        "Precision Engineering",
        "Journal of Microengineering",
        "Microsystem Technologies",
    ),
    units_and_formulas_notes=(
        "摆幅正常范围为 270°-300°",
        "精度为 s/d 或 s/month",
        "扭矩单位为 mN·m",
        "频率单位为 Hz 或 vph（vibrations per hour）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SolidWorks", "CATIA", "Fusion 360", "Rhino", "Inventor", "MATLAB", "COMSOL Multiphysics", "ANSYS", "Microsoft Excel", "R", "Tableau", "LaTeX", "OpenRefine", "Figma", "Blender", "KeyShot", "Timegrapher", "Optical Comparator", "Python"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
