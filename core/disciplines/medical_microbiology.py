"""医学微生物学学科论文支持：病原微生物学、抗菌药物与分子诊断体裁注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_microbiology",
    aliases=("medical_microbiology", "医学微生物学", "medical microbiology", "病原微生物学", "pathogenic microbiology", "临床微生物", "clinical microbiology", "抗菌药物", "antimicrobial resistance", "感染性疾病", "infectious disease microbiology"),
    paper_types={
        "research": ("abstract", "introduction（病原背景与感染问题）", "methods（分离鉴定与药敏方法）", "results（病原特征与耐药数据）", "discussion（流行病学与机制分析）", "references"),
        "case_study": ("abstract", "introduction", "case description（感染病例与流行病学）", "analysis（病原检测与药敏分析）", "results（治疗与转归）", "discussion（病原学启示）", "references"),
        "review": ("abstract", "introduction", "microbiology overview（微生物学综述）", "evidence synthesis（耐药证据整合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={
        "microbiology_lab": "微生物实验室遵循 CLSI M100/M100-A 标准",
        "antimicrobial_susceptibility": "药敏试验遵循 CLSI 或 EUCAST 指南",
        "clinical_microbiology_report": "报告遵循 ISO 15189 质量要求",
        "antimicrobial_resistance": "耐药报告遵循 GLASS/AR-I 报告",
        "infectious_disease": "传染病报告遵循 CDC 或国家卫健委指南",
    },
    conventions=(
        "病原菌须鉴定到种；分子分型须注明方法（MLST/MLVA/WGS）",
        "药敏结果须注明 MIC 值与 CLSI/EUCAST 折点",
        "培养基须注明成分、孵育条件与时间",
        "抗生素使用史须完整记录（种类、剂量、疗程）",
        "感染控制措施须报告",
    ),
    key_venues=(
        "Clinical Infectious Diseases",
        "Journal of Antimicrobial Chemotherapy",
        "Antimicrobial Agents and Chemotherapy",
        "Eclinical Medicine",
        "European Journal of Clinical Microbiology & Infectious Diseases",
        "Frontiers in Microbiology",
        "PLOS Neglected Tropical Diseases",
    ),
    units_and_formulas_notes=(
        "MIC 用 μg/mL 或 mg/L；药敏结果用 S/I/R 表示",
        "载量用 CFU/mL 或 copies/mL（PCR）",
        "生长曲线用 OD600 或 CFU/mL 表示",
        "耐药率用 % 表示，给出置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Microscope (Bright Field/Fluorescence)", "Incubator (CO2/Anaerobic)", "Autoclave", "Microbial Culture System", "Antimicrobial Susceptibility Testing System", "VITEK System", "MALDI-TOF MS System", "PCR System", "Real-Time PCR System", "Gel Electrophoresis Apparatus", "Centrifuge", "Microbial Colony Counter", "Flow Cytometer", "Microarray System", "Whole Genome Sequencing", "Antibiotic Susceptibility Testing", "Serology Testing Kit", "Blood Culture System", "Laboratory Information System", "SPSS"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
