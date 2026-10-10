"""职业卫生与健康学科论文支持：职业流行病学/暴露评估体裁、Vancouver/AMA 引用样式与职业健康度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hygiene_and_occupational_health",
    aliases=("hygiene_and_occupational_health", "职业卫生与健康", "职业卫生", "职业病", "职业健康", "职业暴露", "工业卫生", "工作场所安全", "职业流行病学"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与研究问题）", "methodology（暴露评估与队列）", "results（暴露与健康结果）", "discussion（干预与控制意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（工作场所与病例）", "analysis（暴露分析）", "results（干预效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（剂量-反应框架）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver 样式（国际医学期刊常用）",
    reporting_standards={
        "cohort": "职业队列研究遵循 cohort 报告规范",
        "exposure": "职业暴露评估遵循 TLV/PC-TBA 限值对照",
        "case_report": "职业病报告遵循 ICDC 编码与报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "ethics": "人体研究须报告伦理批准与知情同意",
    },
    conventions=(
        "暴露限值须注明来源与年代",
        "样本量与失访须报告",
        "混杂因子与调整方法须给出",
        "ICDC 编码须使用",
        "单位（mg/m³、μg/m³）须规范",
    ),
    key_venues=(
        "American Journal of Industrial Medicine",
        "Occupational & Environmental Medicine",
        "Annals of Occupational Hygiene",
        "Preventive Medicine",
        "Journal of Occupational Health",
        "Environment International",
    ),
    units_and_formulas_notes=(
        "气溶胶与粉尘用 mg/m³ 或 μg/m³",
        "噪声用 dB(A)；辐射用 Sv 或 mSv",
        "公式用 amsmath；剂量-反应模型须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "风险指标（OR、RR、CI）须定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R", "Python", "SAS", "Stata", "SPSS", "MATLAB", "Python（pandas）", "Excel", "LaTeX", "EndNote", "Zotero", "JMP", "WinBUGS", "OpenBUGS", "RStudio", "NVivo", "Git", "QGIS", "ArcGIS", "REDCap"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
