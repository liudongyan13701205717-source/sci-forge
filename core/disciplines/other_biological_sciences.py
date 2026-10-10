"""其他生物科学学科论文支持：跨方向生物学方法与报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_biological_sciences",
    aliases=(
        "other_biological_sciences",
        "其他生物科学",
        "Other Biological Sciences",
        "生物交叉学科",
        "Synthetic Biology",
        "Systems Biology",
        "进化生物学",
        "Bioinformatics 交叉",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methodology（材料与实验方法）",
            "results（结果与分析）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（国际生物学期刊）/ GB/T 7714（中文）",
    reporting_standards={
        "empirical": "生物实验 MIAME/MIBBI 报告规范",
        "gene_expression": "MIAME 规范",
        "systematic_review": "PRISMA 声明",
        "ecological_study": "Eco-Log 生态研究规范",
    },
    conventions=(
        "实验重复与随机化须说明",
        "物种/菌株拉丁学名与模式须报告",
        "测序数据须提交至 NCBI/ENA",
        "统计方法须给出检验类型与 α",
        "伦理与生物安全批准号须列出",
    ),
    key_venues=(
        "Nature Ecology & Evolution",
        "Current Biology",
        "Molecular Biology and Evolution",
        "Proceedings of the Royal Society B",
        "生物学报",
    ),
    units_and_formulas_notes=(
        "温度用 ℃，压力用 Pa 或 kPa",
        "浓度用 mol/L 或 mg/L 并注明",
        "长度精度到 μm 或 nm",
        "统计量给出 M/SD/95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Illumina NextSeq（测序）", "QIIME 2（微生物分析）", "Bioinformatics Galaxy", "R（统计与可视化）", "Python（Biopython）", "CLC Genomics Workbench", "ImageJ（图像分析）", "Flow Cytometer BD FACS", "qPCR ABI 7500", "Gel Doc（凝胶成像）", "Origin（绘图）", "EndNote", "LaTeX", "Photoshop", "Excel", "Molecular Biology Kit (QIAGEN)", "PCR Thermal Cycler", "Microscope OLYMPUS", "Mass Spectrometer (Q-TOF)", "Phylogenetic IQ-TREE"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
