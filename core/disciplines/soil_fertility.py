"""土壤肥力学科论文支持：养分循环/供肥方案/肥力评价体裁、SSSA 样式与养分记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="soil_fertility",
    aliases=(
        "soil_fertility",
        "土壤肥力",
        "土壤养分",
        "供肥方案",
        "土壤质量",
        "soil fertility",
    ),
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
        "experimental": "实验遵循土壤肥力实验报告规范",
        "field_study": "野外研究遵循土壤肥力调查报告规范",
        "observational": "观察研究遵循土壤肥力观测报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循土壤肥力数据规范",
    },
    conventions=(
        "土壤分类（USDA/FAO/WRB）须注明",
        "采样深度与层次须报告",
        "养分分析方法须附标准编号",
        "统计处理须说明",
        "单位须与国际单位一致",
    ),
    key_venues=(
        "Soil Science Society of America Journal",
        "European Journal of Soil Science",
        "Nutrient Cycling in Agroecosystems",
        "Plant and Soil",
        "Agronomy for Sustainable Development",
    ),
    units_and_formulas_notes=(
        "pH 无量纲；有机碳用 g/kg",
        "养分含量用 mg/kg 或 g/kg",
        "公式用 amsmath；养分平衡公式须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R", "Python", "Soil Nutrient Analyzer", "Centrifuge", "ICP-MS", "XRD", "FTIR Spectrometer", "Field Portable XRF", "Munsell Colorimeter", "pH Meter", "EC Meter", "Olsen Phosphorus Extractor", "KCl Extractor", "N-P-K Analyzer", "CEC Analyzer", "Soil Moisture Sensor", "TDR", "NIR Spectrometer", "Laser Diffraction", "SEM"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
