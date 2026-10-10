"""口腔医学学科论文支持：口腔临床/正畸/修复体裁、ADS 引用样式与口腔记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="odontology",
    aliases=("odontology", "口腔医学", "牙医学", "口腔", "dentistry", "dental"),
    paper_types={
        "research": ("abstract", "introduction（背景与口腔问题）", "methodology（设计与样本）", "results（临床结果）", "discussion（机理与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例）", "analysis（诊断与治疗计划）", "results（治疗过程）", "discussion（疗效与经验）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="ADS/American Dental Association 样式",
    reporting_standards={"randomized_trial": "遵循 CONSORT 声明", "systematic_review": "遵循 PRISMA 声明", "diagnostic_accuracy": "遵循 STARD 声明"},
    conventions=("牙齿编号须用 Universal 或 FDI 系统", "样本量须报告", "干预剂量与疗程须报告", "影像学与临床终点须报告", "知情同意须说明"),
    key_venues=("Journal of Dentistry", "Journal of Dental Research", "Journal of Prosthetic Dentistry", "American Journal of Dentistry", "Journal of Clinical Periodontology"),
    units_and_formulas_notes=("长度用 mm", "力用 N 或 kgf", "影像分辨率用 μm", "数值给出均值±SD", "公式用 amsmath"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("数字印模扫描仪", "CBCT 锥形束 CT", "口腔内窥镜", "CAD/CAM 设计软件", "3D 打印树脂", "CEREC 椅旁 CAD/CAM", "激光治疗仪", "牙周探针", "牙髓活力检测仪", "口腔显微镜", "正畸模拟器", "隐形矫治器设计软件", "咬合分析软件", "牙科影像 PACS", "SPSS", "R", "Stata", "GraphPad Prism", "Excel", "iTero 数字印模"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
