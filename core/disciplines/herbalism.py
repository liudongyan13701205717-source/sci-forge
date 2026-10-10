"""草药学科论文支持：草药治疗与民族植物学体裁、Vancouver 引用样式与草药记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="herbalism",
    aliases=("herbalism", "草药", "草药学", "草药治疗", "中草药", "中草药治疗", "草药疗法", "传统草药", "草药研究"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver（作者-序号）",
    reporting_standards={
        "ethnobotanical": "民族植物学规范",
        "pharmacological": "药理研究规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "草药名称须给出学名",
        "剂量须报告",
        "采集/处理须报告",
        "成分分析须报告",
        "安全性评价须报告",
    ),
    key_venues=(
        "Journal of Ethnopharmacology",
        "Molecules",
        "Evidence-Based Complementary and Alternative Medicine",
        "Phytomedicine",
        "Journal of Natural Products",
    ),
    units_and_formulas_notes=(
        "剂量用 mg/kg",
        "公式用 amsmath；化学公式须编号",
        "行内公式避免复杂分式",
        "数值结果给出均值±SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Python (SciPy)", "HPLC", "GC-MS", "LC-MS", "NMR", "UV-Vis", "FTIR", "TLC", "Phytochemistry Software", "Ethnobotanical Database", "TCM Database", "Scimago", "EndNote", "VOSviewer", "Meta-Analyst", "ImageJ", "Origin Lab", "Antioxidant Assay Kit"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "PubMed", "Web of Science"),
)
