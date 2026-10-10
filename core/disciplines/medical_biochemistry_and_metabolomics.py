"""医学生物化学与代谢组学学科论文支持：代谢分析、生物化学实验体裁与报告规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_biochemistry_and_metabolomics",
    aliases=("medical_biochemistry_and_metabolomics", "医学生物化学与代谢组学", "medical biochemistry", "metabolomics", "代谢组学", "临床生化", "clinical biochemistry", "生物化学", "代谢物分析"),
    paper_types={
        "research": ("abstract", "introduction（疾病背景与生化机制）", "methodology（样本采集与代谢分析）", "results（代谢物谱与差异分析）", "discussion（通路富集与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例与生化背景）", "analysis（代谢谱与异常代谢物分析）", "results（诊断/治疗结果）", "discussion（机制探讨）", "references"),
        "review": ("abstract", "introduction", "biochemistry overview（生化原理综述）", "evidence synthesis（代谢证据整合）", "future directions", "references"),
    },
    citation_style="Vancouver（Nature 系列采用作者-年份）",
    reporting_standards={
        "metabolomics": "代谢组学研究遵循 MIAPE 指南（Metabolomics International Association of Proteomics and Glycomics）",
        "mass_spec": "质谱报告遵循 MRM/IonQuant 规范",
        "clinical_assays": "临床检验遵循 CLSI 指南",
        "protein_analysis": "蛋白质组学遵循 MIAPE 与 FAANG 报告",
        "sample_preparation": "样本处理遵循 SOP 规范",
    },
    conventions=(
        "样本类型（血清/尿液/组织）与采集条件须注明",
        "内标/外标标准须注明；质控样本须报告",
        "代谢物注释须给出 CAS 号与置信度等级",
        "统计方法须说明多重检验校正（FDR/BH）",
        "酶反应须注明 pH、温度、底物浓度与条件",
    ),
    key_venues=(
        "Clinical Chemistry",
        "Journal of Clinical Investigation",
        "Metabolomics",
        "BMC Genomics",
        "Metabolites",
        "Analytical Biochemistry",
        "Biochimie",
    ),
    units_and_formulas_notes=(
        "浓度用 μM/mM 或 nmol/L；分子量用 Da/kDa",
        "代谢物丰度用相对丰度或内标校正值",
        "统计结果给出 p 值与 FDR 校正后 q 值",
        "酶动力学参数 Km、Vmax 须注明测定条件",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("LC-MS/MS (Liquid Chromatography-Tandem Mass Spectrometry)", "GC-MS (Gas Chromatography-Mass Spectrometry)", "NMR Spectrometer", "Capillary Electrophoresis", "Protein Assay Kit", "Enzyme Activity Assay", "HPLC System", "Mass Spectrometer (MALDI-TOF)", "ELISA Kit", "Western Blot System", "Centrifuge (Ultracentrifuge)", "Spectrophotometer", "PCR Machine", "Thermal Cycler", "Bioinformatic Pipeline (R/MetaboAnalyst)", "Metabolomics Database (HMDB)", "Metabolomics Workbench", "Sample Pre-processing Station", "Automated Liquid Handler", "Spectrometer (UV-Vis)"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
