"""核医学技术学科论文支持：PET/SPECT/放射性药物体裁、Vancouver 引用样式与核医学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nuclear_medicine_technologies",
    aliases=("nuclear_medicine_technologies", "核医学技术",
             "Nuclear Medicine Technologies", "核医学",
             "PET/CT", "SPECT", "放射性药物",
             "radionuclide imaging", "医学影像", "medical imaging"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与临床问题）",
            "methodology（被试、药物与采集）",
            "results（影像与定量结果）",
            "discussion（临床意义与局限）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例与病史）",
            "analysis（影像与核素分析）",
            "results（诊断与治疗）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（核医学理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver 样式（数字编号，医学期刊规范）",
    reporting_standards={
        "clinical": "临床研究遵循 CONSORT/STARD 声明",
        "imaging": "影像报告遵循 REID/RECOMMEND 规范",
        "dose": "剂量学遵循 ICRP 规范",
        "ethics": "伦理遵循 Helsinki 声明与 GCP",
        "data": "数据集遵循 FAIR 共享规范",
    },
    conventions=(
        "核素用标准记号 ^A X 表示",
        "剂量用 Bq 或 MBq",
        "衰减与半衰期须标注",
        "SUV 值须注明计算方式",
        "公式用 amsmath；显示公式编号",
    ),
    key_venues=(
        "Journal of Nuclear Medicine",
        "European Journal of Nuclear Medicine and Molecular Imaging",
        "European Journal of Hybrid Imaging",
        "Clinical Nuclear Medicine",
        "Annals of Nuclear Medicine",
        "Journal of Nuclear Cardiology",
    ),
    units_and_formulas_notes=(
        "剂量用 Bq 或 MBq；半衰期用 min/h",
        "SUV 无量纲；能量用 keV 或 MeV",
        "公式用 amsmath；显示公式编号",
        "样本量 N 与 p 值须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("GE Neuber Genesis 2", "GE Discovery MI", "Siemens Biograph Vision", "Siemens ACi.SPECTR", "GE Onyx", "NM Lab", "EXPLORER", "EXPLORER PLUS", "EXPLORER 2", "EXPLORER 3", "EXPLORER 4", "EXPLORER 5", "EXPLORER 6", "EXPLORER 7", "EXPLORER 8", "EXPLORER 9", "EXPLORER 10", "EXPLORER 11", "EXPLORER 12", "EXPLORER 13"),
    category="医学",
    databases=("OpenAlex", "Crossref", "PubMed", "CNKI"),
)
