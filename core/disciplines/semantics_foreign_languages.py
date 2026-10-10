"""外语语义学学科论文支持：二语语义习得/对比语义/多语语义学体裁、Chicago 引用样式与语义记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="semantics_foreign_languages",
    aliases=("semantics_foreign_languages", "foreign language semantics", "外语语义学",
             "二语语义学", "L2 semantics", "second language semantics", "外语意义研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（外语语义习得问题与对比背景）",
            "methods（语料、判断与实验设计）",
            "results（对比语义与习得路径）",
            "discussion（习得机制与教学启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（对比语义/错误个案）",
            "analysis（迁移与中介语分析）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（对比语义理论谱系）",
            "evidence synthesis（跨研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago Notes and Bibliography 样式（17th，应用语言学主流）",
    reporting_standards={
        "contrastive": "对比语义须报告两语/多语语料库来源与标注一致性（κ）",
        "elicitation": "语义判断与翻译任务须报告被试语种背景与熟练度",
        "corpus": "学习语/平行语料研究须报告采样、抽样与标注规范",
    },
    conventions=(
        "标注 L1/L2/L3 母语背景与外语熟练度（CEFR 等级或等效指标）",
        "对比语义术语须用同一语义标签系统（如 UD、BabelNet）",
        "中介语错误按语义偏离类型（过度概括、隐喻偏离、搭配误用）编码",
        "跨语言例句须附原语言文本、转写与逐词/逐义对照",
        "统计检验采用 α = .05 并报告效应量与置信区间",
    ),
    key_venues=(
        "Applied Linguistics",
        "Studies in Second Language Acquisition",
        "Journal of Second Language Writing",
        "Language Learning",
        "Modern Language Journal",
    ),
    units_and_formulas_notes=(
        "CEFR 等级用 A1-A2/B1-B2/C1-C2；熟练度用 TOEFL、IELTS 分数区间报告",
        "对比语义数据用对数-似然（G²）与 t-score 报告搭配显著性",
        "中介语语料用自然对数（ln）与每千字词频",
        "样本量 n ≥ 30；效应量用 Cohen's d、η²、Cramér's V",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Sketch Engine", "AntConc", "WordSmith Tools", "ELAN", "FLEx", "Toolbox", "CorpusSearch", "CQP", "TreeTagger", "BabelNet", "Open Multilingual WordNet", "ProLexis", "Paroled", "Universal Dependencies", "spaCy", "Stanza", "SketchAntConc", "Sketch Engine Corpus Builder", "UAM CorpusTool", "LexUM"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
