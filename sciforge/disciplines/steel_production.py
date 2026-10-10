"""钢铁生产学科论文支持：钢铁冶炼与轧制工艺、冶金参数与质量验证研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="steel_production",
    aliases=("steel_production", "钢铁生产", "钢铁冶炼", "炼钢", "轧钢",
             "steel making", "iron and steel", "steel manufacturing", "炼铁", "铸钢"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "materials and methods（原料、工艺与试验）",
            "results（成分、性能与工艺结果）",
            "discussion（机理与优化讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（产线工艺实例）",
            "analysis（工艺质量与效能分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（工艺路线综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式",
    reporting_standards={
        "process": "工艺参数（温度、压力、速度、时间）须完整报告并标注单位",
        "composition": "钢的成分须以质量分数（%）报告并注明检测依据",
        "mechanical": "力学性能（抗拉、屈服、硬度、冲击）须报告试验条件与样本量",
        "environmental": "环保与能效须符合 ISO 14001 / ISO 50001 要求",
    },
    conventions=(
        "钢种牌号须按标准注明（如 GB/T、ASTM、ISO）",
        "温度以 °C 报告；压力以 MPa 报告；速度以 m/s 或 m/min 报告",
        "成分以质量分数 % 报告并标注元素符号（C、Si、Mn、Cr、Ni 等）",
        "硬度须注明试验方法（HV / HB / HRc / HRC）",
        "试验结果以均值 ± 标准差与样本量表示",
    ),
    key_venues=(
        "ISIJ International",
        "Steel Research International",
        "Iron and Steel",
        "Journal of Materials Processing Technology",
        "Metallurgical Transactions B",
    ),
    units_and_formulas_notes=(
        "应力/强度用 MPa；硬度须注明试验方法",
        "温度用 °C；冶炼温度常用范围 1400–1650 °C",
        "成分用质量分数（wt%）并说明检测依据",
        "试验结果用均值 ± 标准差与样本量表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("High-frequency induction furnace", "Basic oxygen furnace (BOF)", "Electric arc furnace (EAF)", "Continuous caster", "Hot rolling mill", "Cold rolling mill", "Spectroanalyzer (OES)", "Scanning electron microscope (SEM)", "X-ray diffraction (XRD)", "Universal testing machine", "Hardness tester", "Thermal analyzer (DSC)", "Coordinate measuring machine (CMM)", "Laser thickness gauge", "Gamma-ray thickness meter", "Steel quality spectrometer", "Analogical computation software (ProCAST)", "ANSYS Fluent", "DEFORM-3D", "SolidWorks"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
