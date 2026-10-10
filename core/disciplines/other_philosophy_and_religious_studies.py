"""其他哲学与宗教研究学科论文支持：跨文化的哲学理论、宗教研究、数字人文与解释学方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_philosophy_and_religious_studies",
    aliases=("Other Philosophy And Religious Studies", "其他哲学与宗教研究", "Philosophy", "Philosophy Of Mind", "Ethics", "Religious Studies", "Comparative Religion", "Theology"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 17 (notes & bibliography)",
    reporting_standards={
        "k1": "数字人文研究遵循DHRA数据报告规范", "k2": "文本校勘遵循TEI编码与Lemaître校勘方法", "k3": "比较宗教研究遵循IREL分类术语表"
    },
    conventions=("术语使用须依学术传统（分析哲学/大陆哲学/东方哲学）准确", "文本引用须给出文献全出处，含章节段落与页码", "涉及宗教文本须使用权威译本并注明译者版本", "论证逻辑须区分前提—推理—结论三层结构", "跨文化概念比较须说明语义边界与文化语境"),
    key_venues=("Philosophy", "Journal of Religious Ethics", "Journal Of The American Academy Of Religion", "Phenomenology and the Continental Philosophy", "The Journal of Philosophy", "Religion"),
    units_and_formulas_notes=("引用古籍须注明版本、卷册、页码与译者", "涉及宗教/伦理讨论须区分规范性描述与事实性描述", "数字人文文本须遵循TEI XML编码与统一字符集（UTF-8）", "引证文献年代跨越多世纪须给出纪年换算与历史背景"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "Mendeley", "Microsoft Word", "LaTeX", "Overleaf", "CollateX", "TEIViewer", "OCRmyPDF", "ABBYY FineReader", "Tableau", "R", "Python", "Jupyter Notebook", "Google Books", "Internet Archive", "Internet Sacred Texts", "Internet Religion Sourcebook", "Internet Theology Sourcebook", "Project Gutenberg", "Internet Archive Scholar"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
