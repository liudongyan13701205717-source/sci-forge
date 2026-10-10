"""Agriculture machinery mechanics 学科论文支持：农业机械与农机工程体裁、ASA S251.1/Elsevier 与农机测试注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agriculture_machinery_mechanics",
    aliases=(
        "agriculture machinery mechanics",
        "农业机械",
        "农机工程",
        "agricultural engineering",
        "农业机械化",
        "agricultural mechanization",
        "农田机械",
        "农机设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（机型/试验条件）",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "design": (
            "abstract",
            "introduction",
            "requirements",
            "design and modeling",
            "simulation",
            "validation",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope",
            "findings",
            "research gaps",
            "references",
        ),
    },
    citation_style="ASA S251.1 (Society for Agricultural and Biosystems Engineering) 或 Elsevier numbered",
    reporting_standards={
        "design": "结构强度试验遵循 ISO 5006 与 GB/T 国标",
        "field_test": "田间作业试验须遵循 ISO 11540 系列作业效率标准",
        "power_test": "动力测定遵循 ISO 3262 与 ASABE S251.1",
        "emissions": "排放测试遵循 ISO 14396 与欧 V 标准",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "机型名称、型号、厂家与出厂日期须完整给出",
        "作业速率（km/h）、作业幅宽（m）、单位面积能耗（kJ/kg 或 MJ/ha）须明确",
        "动力测定按 ISO 3262；油耗单位 L/h 或 g/kWh",
        "田间数据须按 ISO 11540 报告作业质量与效率",
    ),
    key_venues=(
        "Biosystems Engineering",
        "Journal of Agricultural Mechanization Research",
        "Agricultural Engineering International: CIGR Journal",
        "ASABE Journal",
        "Transactions of the ASABE",
        "Journal of Terramechanics",
        "Computers and Electronics in Agriculture",
    ),
    units_and_formulas_notes=(
        "作业效率 kg/h 或 t/h；作业质量合格率 %",
        "油耗 L/h 或 g/kWh；比油耗单位 g/kWh",
        "单位面积能耗 MJ/ha；油耗-速度关系须报告",
        "公式用 amsmath；显示公式仅在被引用时编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SolidWorks", "CATIA", "UG NX", "ANSYS", "Adams", "MATLAB Simulink", "GT-Suite", "Agricultural Simulator Game GTA", "Tractor John Deere", "Tractor Kubota", "Tractor MF", "Combine John Deere", "Combine Claas", "Field Camera Canon EOS", "Load Cell", "Speed Sensor", "GPS", "Data Acquisition System", "COMSOL Multiphysics"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "ASABE Digital Library", "CIGR Journal", "AGC"),
)
