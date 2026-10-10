"""医学检验技术学科论文支持：临床实验室检测、生物标志物与质量评估体裁注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_laboratory_technology",
    aliases=("medical_laboratory_technology", "医学检验技术", "clinical laboratory", "clinical chemistry", "clinical pathology", "临床检验", "laboratory medicine", "检验医学", "分子诊断技术", "免疫学检验"),
    paper_types={
        "research": ("abstract", "introduction（临床需求与检测背景）", "methods（样本采集与检测方法）", "results（分析性能与临床应用）", "discussion（方法学评价与转化意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例与检验背景）", "analysis（检验结果与鉴别诊断）", "results（诊断/随访结果）", "discussion（方法学改进）", "references"),
        "review": ("abstract", "introduction", "technology overview（检验技术综述）", "evidence synthesis（方法学证据整合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={
        "clinical_chemistry": "临床化学检验遵循 CLSI C28 分析质量评估",
        "hematology": "血液学检验遵循 ISLH 标准",
        "coagulation": "凝血检验遵循 ISTH/ICTH 指南",
        "immunoassay": "免疫分析遵循 IMDWF 指南",
        "molecular_diagnosis": "分子诊断遵循 CLSI M28 或 FDA 指南",
    },
    conventions=(
        "检测仪器型号、试剂批号、校准方法须注明",
        "参考区间须注明适用人群与检测方法",
        "质控结果须报告 CV% 与 Bias%",
        "分析性能须报告 LOD、LOQ、精密度与准确度",
        "危急值标准须注明",
    ),
    key_venues=(
        "Clinical Chemistry",
        "Clinical Chemistry and Laboratory Medicine",
        "Journal of Clinical Laboratory Analysis",
        "Laboratory Medicine",
        "Journal of Clinical Laboratory Analysis",
        "Analytical and Bioanalytical Chemistry",
        "Clinical Chemistry and Laboratory Medicine",
    ),
    units_and_formulas_notes=(
        "浓度用 mmol/L、μmol/L 或 g/L；酶活性用 U/L 或 IU/L",
        "血细胞计数用 ×10⁹/L（白细胞）或 ×10¹²/L（红细胞）",
        "血红蛋白用 g/L；红细胞压积用 %",
        "凝血时间用 s 或 min；国际标准化比值 INR 为无量纲",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Clinical Chemistry Analyzer", "Hematology Analyzer", "Coagulation Analyzer", "Blood Gas Analyzer", "Urinalysis System", "Immunoassay Analyzer (ELISA)", "Chemiluminescence Analyzer", "Microscope (Digital)", "Centrifuge (Blood Separator)", "Blood Glucose Analyzer", "Protein Electrophoresis System", "PCR Thermal Cycler", "Real-Time PCR System", "Automated Microbiology Workstation", "Staining Station", "Slide Scanner", "Laboratory Information System (LIS)", "Mass Spectrometer (Tandem MS)", "Spectrophotometer", "Calibrator System"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
