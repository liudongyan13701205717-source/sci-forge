"""营养科学学科论文支持：营养基因组学/代谢组学/微生物组学体裁、Vancouver 引用样式与生物标志物注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nutrition_science",
    aliases=(
        "nutrition_science",
        "营养科学",
        "Nutrition Science",
        "Nutritional Biochemistry",
        "Nutrigenomics",
        "Nutritional Metabolomics",
        "Microbiome Nutrition",
        "Nutritional Genomics",
        "营养生化",
    ),
    paper_types={
        "research": ("abstract", "introduction（营养科学问题与假设）", "methods（对象、样品与生物标志物分析）", "results（组学与临床结局）", "discussion（分子机制）", "references"),
        "case_study": ("abstract", "introduction", "case description（研究对象概况）", "analysis（组学数据分析）", "results（分子发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（营养科学理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="AMA 或 Vancouver（营养科学期刊主流样式）",
    reporting_standards={
        "genomics": "组学研究遵循 GA4GH 数据规范",
        "metabolomics": "代谢组学研究遵循 MINASE 声明",
        "microbiome": "微生物组学研究遵循 MIxMiC 声明",
        "clinical": "临床研究遵循 CONSORT 与注册号",
    },
    conventions=(
        "营养素单位统一（g、mg、µg；维生素用 µg RE 或 IU 注明）",
        "组学数据处理流程说明（质控、标准化、批次效应校正）",
        "统计方法给出多重比较校正与效应量",
        "样本量给先验功效分析",
        "生物标志物给测定方法、灵敏度与特异性",
    ),
    key_venues=(
        "Nutrients",
        "American Journal of Clinical Nutrition",
        "The Journal of Nutrition",
        "British Journal of Nutrition",
        "Metabolomics",
    ),
    units_and_formulas_notes=(
        "能量 kcal 或 MJ；蛋白质 g/kg 体重",
        "代谢物浓度 µmol/L",
        "基因表达用 log2 FC 与 FDR",
        "微生物组用相对丰度 (%) 与 α/β 多样性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Python NumPy/Pandas", "R", "SAS", "Stata", "SPSS", "MATLAB", "Mathematica", "Bioconductor", "BLAST", "UniProt", "KEGG", "MetaboAnalyst", "MetaboLights", "HMDB", "NCBI", "ESHA", "NutritionData", "MetaPhlAn", "QIIME 2", "G*Power"),
    category="理学",
    databases=("PubMed", "OpenAlex", "Crossref", "PubChem"),
)
