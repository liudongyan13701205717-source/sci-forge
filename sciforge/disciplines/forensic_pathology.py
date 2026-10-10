"""法医病理学科论文支持：死因分析、损伤机制、中毒鉴别与死后变化。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="forensic_pathology",
    aliases=("forensic_pathology", "forensic pathology", "法医病理", "死因诊断", "创伤学", "法医学", "尸检学", "损伤机制"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver（顺序编号式）",
    reporting_standards={
        "autopsy": "尸检须遵循法医学尸检操作指南",
        "histology": "组织切片须遵循标准化制片流程",
        "imaging": "影像学须遵循标准化报告规范",
        "toxicology": "毒物检测须遵循标准化分析流程"
    },
    conventions=(
        "解剖学名称须用标准化术语",
        "损伤描述须包含部位、形态、尺寸与深度",
        "死后变化须区分自体变化与外力作用",
        "标本须标注方向与比例尺",
        "图像须使用标准灰度级别"
    ),
    key_venues=(
        "Journal of Forensic Pathology",
        "International Journal of Legal Medicine",
        "Journal of Forensic and Investigative Pathology",
        "Forensic Science International",
        "Journal of Forensic Sciences"
    ),
    units_and_formulas_notes=(
        "长度用 cm 或 mm",
        "重量用 g",
        "温度用 °C",
        "时间用 min 或 h",
        "面积用 cm²"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Microscope", "HistoCore", "Leica", "Histology slide scanner", "Whole slide imaging system", "ImageJ", "CellProfiler", "Hematoxylin and eosin", "Masson staining", "Immunohistochemistry kit", "Autopsy suite", "CT scanner", "MRI scanner", "X-ray machine", "Digital forensic photography", "Postmortem sonography", "Virtual autopsy", "Forensic anthropology kit", "Toxicology lab", "DNA analysis system"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
