"""语言学论文支持：语料库方法、实验音系/句法、计算语言学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="linguistics",
    aliases=("linguistics", "语言学", "语料", "corpus", "phonology", "syntax",
             "semantics", "pragmatics", "计算语言学", "computational linguistics"),
    paper_types={
        "research": ("abstract", "introduction", "background/theory", "methodology（语料/实验设计）",
                     "analysis", "discussion", "conclusion", "references"),
        "corpus_study": ("abstract", "introduction", "corpus description（语料来源与规模）",
                         "annotation scheme", "results", "discussion", "references"),
        "fieldwork": ("abstract", "introduction", "language background", "methodology",
                      "data（例句带语感标注）", "analysis", "references"),
    },
    citation_style="Unified Stylesheet for Linguistics（作者-年份）或 APA 7",
    reporting_standards={
        "corpus": "语料来源、规模、时间跨度、标注方案（POS/依存）须声明；标注一致性（kappa）须报告",
        "experiment": "被试数、语言背景、刺激材料与统计模型须写明；随机效应结构报告",
        "examples": "例句须带 gloss（ Leipzig Glossing Rules）；原始语料存档链接",
        "stats": "混合效应模型报告固定/随机效应与置信区间；多重比较校正",
        "typology": "语言系属与类型学特征（SVO/语态等）须给出（WALS 引用）",
    },
    conventions=(
        "国际音标 IPA 标注；斜体标语言形式，引号标语义",
        "例句编号与 gloss 对齐；语法判断用 */?/#/? 标记",
        "语料图（频率、分布）给坐标轴单位与语料规模",
        "术语首现给英文原词与定义；避免未经定义的生成语法记号",
    ),
    key_venues=(
        "Language",
        "Journal of Linguistics",
        "Lingua",
        "Computational Linguistics",
        "Journal of Phonetics",
    ),
    units_and_formulas_notes=(
        "频率给每百万词（pmw）；效应量给 Cohen's d 或 odds ratio",
        "互信息/困惑度注明计算公式；显著性标注于图上",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "译文"),
    tools=("Praat", "Python", "R", "LaTeX", "Zotero"),
    category="文学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
