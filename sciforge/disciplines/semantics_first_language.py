"""第一语言语义学学科论文支持：母语意义理论/构式语义/语料库语义体裁、Chicago 引用样式与语义记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="semantics_first_language",
    aliases=("semantics_first_language", "first language semantics", "第一语言语义学",
             "母语语义学", "L1 semantics", "native semantics", "母语意义理论"),
    paper_types={
        "research": (
            "abstract",
            "introduction（语义问题与构式背景）",
            "methods（语料、判断与实验）",
            "results（语义表征与分布）",
            "discussion（理论贡献与后续问题）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（语言/语义现象个案）",
            "analysis（描写与解释）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（语义理论谱系）",
            "evidence synthesis（跨研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago Notes and Bibliography 样式（17th，语言学主流）",
    reporting_standards={
        "elicitations": "语义判断实验须报告刺激、被试与判定标准",
        "corpus": "语料库研究须报告语种、样本量、采样与标注规范",
        "experimental": "语义知觉实验遵循心理语言学实验报告规范（P3）",
    },
    conventions=(
        "区分外延（denotation）与内涵（sense/connotation）并标注所用定义理论",
        "命题逻辑与蒙太克语法记法全文一致（λ、∨、⟦·⟧）",
        "构式义、词汇义与习语义须显式标注并给出例句",
        "跨语言比较须用同一语义标签系统（如 Universal Dependencies）",
        "例句使用斜体/引号/编号并按语义维度组织",
    ),
    key_venues=(
        "Journal of Semantics",
        "Linguistics and Philosophy",
        "Journal of Linguistics",
        "Lingua",
        "Semantics and Pragmatics",
    ),
    units_and_formulas_notes=(
        "语义模型论用 \\⟦\\cdot⟧ 与 λ-演算；量词用 FOL/FO+R",
        "蒙太克类型用 a（个体）、t（真值）、s（情境）；类型组合标注 (s,t)、(a,t) 等",
        "语料库检索词频与 t-score、log-likelihood 用于搭配显著性",
        "分布数据用自然对数（ln）与相对频率；样本量 n ≥ 30",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ELAN", "FLEx", "Toolbox", "Sketch Engine", "AntConc", "WordSmith Tools", "CLAN", "CHILDES", "CorpusSearch", "CQP", "TreeTagger", "WordNet", "FrameNet", "SemBank", "ConceptNet", "ProLexis", "LingSys", "SketchAntConc", "UAM CorpusTool", "LexUM"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
