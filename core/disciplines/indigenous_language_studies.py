"""原住民语言研究论文支持：语言记录、濒危语言保护、社会语言学、田野调查与语法描写。"""
from __future__ import annotations
from sciforge.disciplines.base import Discipline
DISCIPLINE = Discipline(
    name="indigenous_language_studies",
    aliases=("indigenous_language_studies", "原住民语言研究", "aboriginal_linguistics", "endangered_languages", "documentary_linguistics", "descriptive_linguistics", "first_nations_languages", "field_linguistics", "language_revitalization"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法论）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 17（语言学常用）或 Linguistic Society of America Style",
    reporting_standards={"field_recording": "录音须遵循 ELDP 元数据标准（录音者、语言、日期、GPS、知情同意）", "interlinear_glossing": "互译须遵循 Leipzig Glossing Rules 或 Leiden Interlinear Glossing Conventions", "lexical_db": "词汇库须使用 Lexvo/Ontolex 对齐词性并标注重音/格"},
    conventions=("语言名用民族语言学正字法（WALS/Glottolog 代码）", "术语遵循 IPA 与 Leipzig 缩写表", "例句编号按语料库顺序，音系描写用 IPA", "语料归属遵循 FAIR/OCAP 原则", "引用原住民母语者贡献须署名"),
    key_venues=("Journal of the Linguistic Society of America", "Language", "Oceanic Linguistics", "Linguistic Typology", "Language Documentation & Conservation"),
    units_and_formulas_notes=("音长用毫秒 ms", "音高用 Hz（基频 F0）", "语料规模以 tokens/words/hours 表达", "词汇库用 lemma/gloss/POS 结构化"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ELAN", "Anviz", "SIL FieldWorks", "FLEx", "Paratext", "Interlinear Glosses Editor (IGE)", "Lexique+", "Sketch Engine", "CQPweb", "Antibody", "Audacity", "FieldRecorder", "ZoomText", "Transana", "NVivo", "LaTeX", "XeLaTeX", "PolyGlot", "SIL Toolbox", "Chatterbox"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
