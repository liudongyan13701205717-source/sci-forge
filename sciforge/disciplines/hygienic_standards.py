"""卫生标准学科论文支持：卫生标准制定/评价体裁、Vancouver 样式与卫生限值度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hygienic_standards",
    aliases=("hygienic_standards", "卫生标准", "标准制定", "卫生监测", "卫生学", "卫生检验", "食品安全标准", "饮用水标准", "公共场所卫生", "卫生法规"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与标准缺口）", "methodology（监测、评价与限值推导）", "results（监测与限值结果）", "discussion（标准与政策意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（标准/领域）", "analysis（符合性分析）", "results（评价结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（标准体系框架）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver 样式（卫生/标准类期刊常用）",
    reporting_standards={
        "standard_dev": "标准制定遵循卫生标准编制与评审规范",
        "monitoring": "监测研究遵循采样与限量报告规范",
        "compliance": "符合性评价须报告对照限值与年份",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "risk": "风险评估遵循 WHO/JECFA 风险表征规范",
    },
    conventions=(
        "限值须注明来源标准与发布年份",
        "采样点与采样量须报告",
        "检测方法须给出标准号",
        "统计检验与效应量须给出",
        "单位（mg/L、mg/kg、μg/m³）须规范",
    ),
    key_venues=(
        "Food Control",
        "Journal of Food Protection",
        "Water Research",
        "Environmental Research",
        "The Lancet Global Health",
        "Food and Chemical Toxicology",
    ),
    units_and_formulas_notes=(
        "食品限值用 mg/kg 或 μg/kg",
        "饮用水用 mg/L；空气用 μg/m³",
        "公式用 amsmath；风险模型与限值须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "检出限（LOD）与未检出须显式说明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R", "Python", "SAS", "SPSS", "Stata", "MATLAB", "Excel", "LaTeX", "EndNote", "Zotero", "GC-MS", "LC-MS/MS", "原子吸收光谱仪", "IC 离子色谱仪", "HPLC", "WinBUGS", "JMP", "Git", "RStudio", "Minitab"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
