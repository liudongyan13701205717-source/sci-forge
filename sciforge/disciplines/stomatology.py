"""口腔学学科论文支持：口腔疾病与牙体牙髓治疗、临床研究报告与循证规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="stomatology",
    aliases=("stomatology", "口腔学", "口腔医学", "牙科学", "牙科",
             "oral medicine", "oral surgery", "dentistry", "口腔内科",
             "口腔外科", "正畸学", "牙周病"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与临床问题）",
            "methods（研究设计与患者样本）",
            "results（临床结果与影像学）",
            "discussion（临床意义与局限）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction",
            "case presentation（病例报告）",
            "treatment and outcome（治疗与结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "methods（系统综述方法，遵循 PRISMA）",
            "results（证据综合）",
            "discussion（临床建议）",
            "references",
        ),
    },
    citation_style="Vancouver 样式（数字编号）",
    reporting_standards={
        "clinical_trial": "临床试验须遵循 CONSORT 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "patient_consent": "患者知情同意与隐私保护须说明",
    },
    conventions=(
        "患者信息须匿名化，不得包含可识别信息",
        "诊断标准须注明（如 ICD-10、WHO 口腔健康调查）",
        "用药剂量须标注单位（mg、μg）与给药途径",
        "影像学报告须注明成像设备与参数",
        "随访时间以月为单位报告",
    ),
    key_venues=(
        "Journal of Dental Research",
        "Journal of Dentistry",
        "Community Dentistry and Oral Epidemiology",
        "Journal of Clinical Dentistry",
        "International Journal of Oral and Maxillofacial Implants",
    ),
    units_and_formulas_notes=(
        "剂量：mg 或 μg；浓度：μg/mL 或 mg/L",
        "影像学密度：Hounsfield unit (HU)",
        "疼痛评分：VAS（0–10）或 NRS",
        "随访：月（m），报告中位数（IQR）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Cone beam computed tomography (CBCT)", "Dental X-ray machine", "Intraoral scanner", "Dental CAD/CAM system", "Laser ablation unit", "Microscope (operating microscope)", "Periodontal probe", "Bitewing radiograph", "Bitewing X-ray", "Root canal length meter", "Endodontic motor", "Cariogram software", "Dentistry ERP software", "Photography software (Dolphin)", "Statistical software (SPSS)", "Endnote", "LaTeX", "Python (pandas)", "RevMan", "R"),
    category="医学",
    databases=("PubMed", "Cochrane", "OpenAlex", "Crossref", "CNKI"),
)
