"""Agricultural Biotechnology 学科论文支持：农业生物技术/作物遗传/分子育种体裁、APA/Vancouver 引用样式与农艺注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agricultural_biotechnology",
    aliases=("agricultural biotechnology", "农业生物技术", "农业生物",
             "农业生物技术工程", "plant biotechnology", "农业生物科技",
             "作物生物", "农业生物技术", "作物遗传改良"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "methods": (
            "abstract",
            "introduction",
            "principle",
            "protocol",
            "validation",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context and background",
            "case description",
            "analysis",
            "findings",
            "implications",
            "references",
        ),
    },
    citation_style="APA 7 或 Vancouver",
    reporting_standards={
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "animal": "动物实验遵循 ARRIVE 2.0",
        "protocol": "分子生物学实验遵循 ISA 惯例",
        "data": "实验数据遵循 FAIR/AAAAM 惯例",
    },
    conventions=(
        "物种/基因/等位基因命名遵循官方分类（如作物物种拉丁名、基因缩写）",
        "实验材料（品系、突变体、转基因）须给出来源与世代",
        "分子实验条件（PCR 程序、电泳条件、酶切位点）须完整报告",
        "统计显著性用 p 值与效应量并列报告；置信区间给出",
        "田间试验须说明设计（随机区组/裂区）、重复数与取样策略",
        "转基因与基因编辑须给出编辑工具与插入位点信息",
    ),
    key_venues=(
        "Plant Cell",
        "Plant Physiology",
        "Plant Biotechnology Journal",
        "Journal of Experimental Botany",
        "Molecular Plant",
        "Crop Science",
        "Plant Methods",
    ),
    units_and_formulas_notes=(
        "基因/蛋白表达量用相对量（2^-ΔΔCt）或绝对量（copies/μL）",
        "田间数据以均值 ± 标准差/SEM 报告；显著性水平 α=0.05",
        "DNA/蛋白浓度用 ng/μL 或 μg/mL；纯度用 A260/A280 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Applied Biosystems Real-Time PCR", "Illumina HiSeq", "Illumina NovaSeq", "Sanger Sequencer", "Oxford Nanopore MinION", "Bio-Rad NanoDrop", "Thermo Fisher", "Eppendorf Centrifuge", "Bio-Rad Electrophoresis", "BD FACS", "QIAGEN Kit", "CHOPCHOP", "CRISPR design", "BLAST", "Geneious", "MEGA", "ClustalW", "QIIME", "ImageJ", "R", "SPSS", "MATLAB", "Microsoft Office", "Zotero"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "PubMed"),
)
