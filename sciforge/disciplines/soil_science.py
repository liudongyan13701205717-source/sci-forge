"""土壤科学学科论文支持：土壤发生/肥力/污染体裁、SSSA 引用样式与土壤度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="soil_science",
    aliases=("soil_science", "土壤学", "土壤科学", "土壤肥力"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "materials and methods（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "field_study": (
            "abstract",
            "introduction",
            "study area（研究区）",
            "sampling（采样设计）",
            "analyses（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "experimental_study": (
            "abstract",
            "introduction",
            "experimental design（实验设计）",
            "treatments（处理）",
            "measurements（测定）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="SSSA 样式（作者-年份；SSSAJ 遵循美国土壤学会规范）",
    reporting_standards={
        "experimental": "实验遵循土壤实验报告规范",
        "field_study": "野外研究遵循土壤调查报告规范",
        "observational": "观察研究遵循土壤观测报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循土壤数据规范",
    },
    conventions=(
        "土壤分类（USDA/FAO/WRB）须注明",
        "采样深度与层次须报告",
        "分析方法须附标准编号",
        "统计处理须说明",
        "单位须与国际单位一致",
    ),
    key_venues=(
        "Soil Science Society of America Journal",
        "Geoderma",
        "European Journal of Soil Science",
        "Soil Biology and Biochemistry",
        "Plant and Soil",
        "Catena",
    ),
    units_and_formulas_notes=(
        "pH 无量纲；有机碳用 g/kg；养分用 mg/kg",
        "容重用 g/cm³；含水量用 % 或 m³/m³",
        "公式用 amsmath；养分平衡公式须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "深度用 cm 并注明层次",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("R", "Python", "土壤养分分析仪", "离心机"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)