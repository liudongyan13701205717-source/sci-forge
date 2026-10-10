"""语言学的普遍/总体学科论文支持：语言类型学、结构与功能总体研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="linguistics_general",
    aliases=("linguistics_general", "语言学总体", "一般语言学",
             "linguistics, general", "language typology",
             "语言类型学", "通用语言学", "理论语言学", "比较语言学"),
    paper_types={
        "research": ("abstract", "introduction", "background/theory",
                     "methodology（语料/实验设计）",
                     "analysis", "discussion", "conclusion", "references"),
        "case_study": ("abstract", "introduction",
                       "case description（语言/方言背景）",
                       "analysis（分析）", "results（结果）",
                       "discussion", "references"),
        "review": ("abstract", "introduction",
                   "theoretical overview（理论综述）",
                   "evidence synthesis（证据整合）",
                   "future directions", "references"),
    },
    citation_style="Unified Stylesheet for Linguistics（作者-年份）或 APA 7",
    reporting_standards={
        "corpus": "语料来源、规模、时间跨度、标注方案须声明",
        "experiment": "被试数、语言背景、刺激材料与统计模型须写明",
        "examples": "例句须带 gloss（Leipzig Glossing Rules）",
        "stats": "混合效应模型报告固定/随机效应与置信区间",
        "typology": "语言系属与类型学特征须给出（WALS 引用）",
        "fieldwork": "田野调查遵循 SIL 伦理与知情同意",
    },
    conventions=(
        "国际音标 IPA 标注；斜体标语言形式，引号标语义",
        "例句编号与 gloss 对齐；语法判断用 */?/#/? 标记",
        "语料图给坐标轴单位与语料规模",
        "术语首现给英文原词与定义",
        "语言名称首现给 ISO 639 代码",
        "参考文献遵循期刊风格",
    ),
    key_venues=(
        "Language",
        "Journal of Linguistics",
        "Lingua",
        "Studies in Language",
        "Folia Linguistica",
        "Language Typology",
    ),
    units_and_formulas_notes=(
        "频率给每百万词（pmw）；效应量给 Cohen's d 或 odds ratio",
        "互信息/困惑度注明计算公式",
        "显著性标注于图上",
        "音长/时长以毫秒（ms）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Praat", "Python", "R", "RStudio", "Jupyter Notebook", "LaTeX", "Overleaf", "Zotero", "EndNote", "Mendeley", "AntConc", "Noosa Explorer", "Concordance", "ELAN（语料标注）", "FLEx（Field Linguistics Explorer）", "SIL FieldWorks", "WordFreq", "TaalApp", "Sphinx 语音识别", "Audacity"),
    category="文学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
