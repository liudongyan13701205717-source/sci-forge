"""犬类繁殖学科论文支持：犬类育种、遗传学与行为学研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dog_breeding",
    aliases=(
        "dog_breeding", "犬类繁殖", "犬类育种",
        "canine breeding", "犬类繁殖",
        "dog genetics", "犬遗传学",
        "canine health", "犬健康",
        "dog behavior", "犬行为学",
        "dog training", "犬训练",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（育种问题与背景）",
            "methodology（遗传分析、表型评估、数据收集）",
            "results（遗传模式与健康结果）",
            "discussion（育种优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "genetic analysis（遗传分析）",
            "outcome（健康效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "genetic overview（遗传综述）",
            "health issues（健康问题分析）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "genetics": "基因型/表型须注明检测方法与时机",
        "breeding": "繁殖计划须注明配对方案与遗传评估",
        "health": "健康评估须注明评估方法与时间",
        "ethics": "动物实验须声明伦理审批",
    },
    conventions=(
        "犬品种名称须使用标准品种名",
        "基因型须使用标准遗传标记命名",
        "健康指标须注明检测方法（如 OFA、GAO）",
        "繁殖记录须注明配对、时间与后代",
        "统计检验注明方法、p 值与置信区间",
    ),
    key_venues=(
        "Journal of Hereditary Medicine",
        "Canine Genetics and Epidemiology",
        "Veterinary Genetics",
        "Journal of Veterinary Science",
        "Journal of Animal Science",
    ),
    units_and_formulas_notes=(
        "遗传频率用 % 表示",
        "健康评分用 等级 表示",
        "繁殖间隔用 月 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "Python (pandas, numpy)", "Excel", "Google Sheets", "Pedigree Database Software", "Genetic Analysis Software", "Animal Genetics Software", "DNA Testing Kit", "PCR", "Gel Electrophoresis", "Sequencing Software", "Genetic Mapping Software", "Animal Health Records", "Vet Software", "DNA Database", "Pedigree Chart Software", "Genetic Risk Calculator", "Health Testing Database", "Genetic Screening Software"),
    category="农学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
