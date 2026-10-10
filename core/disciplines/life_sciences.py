"""生命科学学科论文支持：生物/生态/分子/遗传体裁、Nature 与期刊引用样式及实验记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="life_sciences",
    aliases=("life_sciences", "生命科学", "生物学", "分子生物学",
             "生态生物学", "生物化学", "细胞生物学", "遗传学",
             "biochemistry", "molecular biology", "genetics",
             "细胞生物学", "生物科学", "生命科学与工程"),
    paper_types={
        "research": ("abstract", "introduction（背景与假设）",
                     "materials and methods（材料与方法）",
                     "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction",
                       "case description（个案描述）",
                       "analysis（分析）", "results（结果）",
                       "discussion", "references"),
        "review": ("abstract", "introduction",
                   "theoretical overview（理论综述）",
                   "evidence synthesis（证据整合）",
                   "future directions", "references"),
    },
    citation_style="Nature/Science 样式（作者-年份，编号引用可选）",
    reporting_standards={
        "animal": "ARRIVE 2.0 动物研究报告规范",
        "clinical": "CONSORT 临床试验报告规范",
        "meta": "PRISMA 系统综述/元分析声明",
        "cell": "MIQE 实时 qPCR 报告规范",
        "genomics": "MIAME/MiGen 基因组报告规范",
        "proteomics": "MIAPE 质谱蛋白质组报告规范",
    },
    conventions=(
        "物种学名斜体；首现给拉丁学名与属名缩写",
        "实验组/对照组样本量、随机化与盲法须报告",
        "统计检验须说明；效应量与置信区间须给出",
        "p 值精确到四位（p<0.001 单独标注）",
        "参考文献遵循期刊风格（Vancouver 或 Nature 样式）",
    ),
    key_venues=(
        "Nature",
        "Science",
        "Cell",
        "Nature Reviews Genetics",
        "Molecular Cell",
        "PNAS",
    ),
    units_and_formulas_notes=(
        "SI 单位（g、mol、L、m、s）",
        "浓度以 mol/L（M）或 mg/mL；pH 用 7.4 或生理标准",
        "温度以 °C 或 K",
        "公式用 amsmath；行内用 $...$；编号仅在被引用时",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R", "Python（pandas）", "RStudio", "Jupyter Notebook", "EndNote", "Zotero", "Mendeley", "LaTeX", "Overleaf", "GraphPad Prism", "SPSS", "SAS", "R (ggplot2)", "Python (matplotlib)", "ImageJ / Fiji", "FlowJo", "Flow cytometry 分析平台", "Geneious Prime", "Chromas Pro", "BioRender"),
    category="理学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI"),
)
