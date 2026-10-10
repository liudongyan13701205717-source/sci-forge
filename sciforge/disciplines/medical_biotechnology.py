"""医学生物技术学科论文支持：基因工程、细胞治疗与生物制药体裁与报告规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_biotechnology",
    aliases=("medical_biotechnology", "医学生物技术", "medical biotech", "clinical biotechnology", "基因治疗", "gene therapy", "cell therapy", "biopharmaceutical", "生物制药", "tissue engineering"),
    paper_types={
        "research": ("abstract", "introduction（疾病背景与技术动机）", "methodology（基因操作与细胞培养）", "results（表达验证与功能数据）", "discussion（疗效机制与转化前景）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例/技术案例）", "analysis（治疗过程与分子机制）", "results（临床结果）", "discussion（安全性评估）", "references"),
        "review": ("abstract", "introduction", "technology overview（技术综述）", "evidence synthesis（转化证据整合）", "future directions", "references"),
    },
    citation_style="Vancouver（Nature 系列采用作者-年份）",
    reporting_standards={
        "gene_editing": "基因编辑报告遵循 EGAP 指南",
        "cell_therapy": "细胞治疗遵循 GMP 规范与 ICH Q11",
        "biopharmaceutical": "生物制药开发遵循 ICH Q5A/Q5B",
        "clinical_trials": "临床试验遵循 ICH E6 GCP",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "细胞系须经 STR 鉴定确认；病毒载体须注明滴度与包装效率",
        "基因编辑效率须以 NGS 数据报告",
        "动物模型须注明品系、性别、年龄与处理组",
        "蛋白表达须报告分子量、纯度与表达条件",
        "生物安全等级（BSL-1/2）须标注",
    ),
    key_venues=(
        "Nature Biotechnology",
        "Molecular Therapy",
        "Cell Stem Cell",
        "Gene Therapy",
        "Biotechnology and Bioengineering",
        "Human Gene Therapy",
        "Therapeutic Advances in Pharmacology",
    ),
    units_and_formulas_notes=(
        "病毒滴度用 vg/mL；细胞计数用 cells/mL",
        "浓度用 μg/mL 或 ng/μL；分子量用 Da/kDa",
        "统计结果给出 p 值与效应量；组间比较须注明检验方法",
        "转基因表达须报告 mRNA 水平（CT 值或 RPKM）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PCR System", "Thermal Cycler", "Gel Electrophoresis Apparatus", "Flow Cytometer", "Centrifuge", "CO2 Incubator", "Bioreactor", "Laminar Flow Hood", "Gene Sequencing (Next-Gen)", "qPCR System", "Western Blot Apparatus", "ELISA Reader", "CRISPR-Cas9 Editing Kit", "Viral Packaging System", "Cell Imager", "Microarray Scanner", "Cell Sorter", "Protein Extraction Kit", "Cell Viability Assay Kit", "Protein Quantification Kit"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
