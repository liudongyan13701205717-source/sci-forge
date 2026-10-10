"""发育生物学科论文支持：胚胎发育、形态发生与进化发育生物学体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="developmental_biology",
    aliases=(
        "developmental_biology", "发育生物学", "发育生物学",
        "embryology", "胚胎学",
        "morphogenesis", "形态发生",
        "evo-devo", "进化发育生物学",
        "stem cell biology", "干细胞生物学",
        "organogenesis", "器官发生",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（发育问题与理论背景）",
            "materials and methods（模型系统、遗传操作、形态学分析）",
            "results（发育表型与分子机制）",
            "discussion（发育机理与进化意义）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview（发育生物学发展脉络）",
            "main themes（主要主题）",
            "future directions",
            "references",
        ),
        "protocols": (
            "title",
            "introduction",
            "materials and methods",
            "results",
            "discussion",
            "acknowledgements",
        ),
    },
    citation_style="Nature/Science 格式（按引用顺序编号）",
    reporting_standards={
        "genetics": "转基因/基因编辑动物须注明品系、基因型与饲养条件",
        "imaging": "活体成像须标注设备、分辨率与标记方法",
        "statistics": "统计检验须注明方法、样本量与显著性水平",
        "ethics": "动物实验须声明伦理审批编号",
    },
    conventions=(
        "物种名称首次出现给出拉丁名与英文俗名",
        "发育阶段须用标准化术语（如 Carnegie stages、HH stages）",
        "基因符号遵循各物种命名规范",
        "图像须标注比例尺与染色方法",
        "统计检验注明方法（t-test、ANOVA等）与显著性阈值",
    ),
    key_venues=(
        "Development",
        "Developmental Cell",
        "Nature",
        "Cell",
        "Nature Genetics",
        "Developmental Biology",
        "Mechanisms of Development",
    ),
    units_and_formulas_notes=(
        "长度用 μm 表示",
        "时间用 h (小时) 表示",
        "基因表达用 fold change 表示",
        "蛋白定量用 Western blot 相对条带强度表示",
        "p 值注明具体数值（*p<0.05, **p<0.01）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ImageJ", "Fiji", "CellProfiler", "Imaris", "Amira", "MetaMorph", "Volocity", "Zeiss ZEN", "Leica LAS", "OlympusCellS", "MATLAB", "Python (scipy, numpy)", "R (RStudio)", "SPSS", "Prism", "CRISPR-Cas9", "PCR", "Gel Electrophoresis", "Western Blot", "Flow Cytometry"),
    category="理学",
    databases=("PubMed", "OpenAlex", "Crossref", "EMBL-EBI"),
)
