"""织造学科论文支持：纺织工程、织物设计与织造工艺优化的体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="weaving",
    aliases=("weaving", "织造", "纺织工程", "机织", "针织",
             "weaving engineering", "textile manufacturing", "knitting",
             "textile engineering", "fabric engineering"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "materials and methods（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "fabric specification（织物规格描述）",
            "production process（生产工艺）",
            "quality control（质量控制）",
            "performance evaluation（性能评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "weaving technologies（织造技术综述）",
            "textile materials（纺织材料综述）",
            "smart textile trends（智能纺织趋势）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "fabric_specification": "织物规格须包含组织类型、经密/纬密、原料成分与规格",
        "mechanical_properties": "力学性能须标注测试标准（GB/T 或 ASTM）与测试条件",
        "production_process": "生产工艺须包含设备型号、参数设置与产出率",
    },
    conventions=(
        "织物组织用组织图（纹图）表示，经纱为竖线、纬纱为横线",
        "经密/纬密单位为根/cm 或根/in",
        "原料以成分百分比标注（如 棉65% 涤纶35%）",
        "强力测试以 N 或 cN 为单位，断裂伸长率以 % 表示",
        "设备转速以 r/min 标注",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of Industrial Textiles",
        "Polymers for Advanced Technologies",
        "Journal of Textile Science and Technology",
        "Color Research and Application",
    ),
    units_and_formulas_notes=(
        "经密/纬密：根/cm",
        "强力：N 或 cN",
        "断裂伸长率：%",
        "原料成分：%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python", "R", "SPSS", "Microsoft Excel", "Tableau", "AnyLogic", "AutoCAD", "SolidWorks", "COMSOL Multiphysics", "Optitex", "Style3D", "Marvelous Designer", "CLO3D", "Figma", "LaTeX", "OpenRefine", "Minitab", "WEKA", "Blender"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
