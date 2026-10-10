"""Classical languages 学科论文支持：古典语言/文献学/译学/古典学体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="classical_languages",
    aliases=(
        "Classical languages", "classical languages", "classics",
        "Latin", "Greek", "Sanskrit", "classical philology",
        "古典语言", "古典学", "拉丁语", "古希腊语", "梵语", "古典文献学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（文本/作者/历史语境）",
            "methodology（语文学/比较语言学/语料库方法）",
            "analysis（原文引证、注释、比较）",
            "discussion",
            "conclusion",
            "references",
        ),
        "textual_criticism": (
            "abstract",
            "introduction",
            "apparatus_criticus",
            "reading_analysis",
            "textual_decision",
            "references",
        ),
        "translation_studies": (
            "abstract",
            "introduction",
            "source_analysis",
            "translation_strategy",
            "discussion",
            "references",
        ),
    },
    citation_style="Chicago Manual of Style 17（古典学论著主流）；APA 7 亦可",
    reporting_standards={
        "text_citation": "引用原文采用 Loeb/Teubner/Oxford 等权威版本文本；引用页/行号/列号",
        "apparatus": "校勘录（apparatus criticus）遵循 EDSA（Editio Principis Digitalis）与 LEU 规范",
        "transliteration": "拉丁语遵循 Lewis & Short 转写；希腊语遵循 LSJ 与 ISO 843；梵语遵循 Monier-Williams",
        "manuscript": "抄本引用采用 siglum（如 B = Bodmer MS 82）并给出收藏地/编号",
        "philology": "形变/异读/省略/补遗标注遵循国际语文学规范",
    },
    conventions=(
        "原文引用使用斜体（希腊/梵）；专有名词保留原文大小写",
        "术语引用经典文献（如 Plato, Phaedrus 229a, 5）；给出页-行-列或 Book.XX",
        "引文附转写（若为原文照录，附原文+转写+译文）",
        "缩略语遵循 LSJ/L&S/M-W 等词典首字母缩写；避免自造缩写",
        "参考文献遵循芝加哥样式（作者-出版年份-页码）；版本、页码、抄本编号完整",
    ),
    key_venues=(
        "Classical Quarterly",
        "Hermes: Zeitschrift für klassische Philologie",
        "Philologus",
        "Greek, Roman, and Byzantine Studies",
        "Mnemosyne",
        "Classical Philology",
        "Transactions of the American Philological Association",
        "Journal of Hellenic Studies",
        "Sanskrit-Philologie",
    ),
    units_and_formulas_notes=(
        "原文/转写/译文三者并列；斜体与直排区分",
        "页-行-列格式（如 Plat. Rep. 514e, 12–15）",
        "抄本引用给出 siglum 与日期（如 B (v. 14c)）",
        "音译遵循 ISO 843（希腊）与 ISO 15919（梵语）",
        "缩略符遵循 LSJ/L&S 惯例",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "软件与代码", "教案与教材", "译文", "报告", "数据集"),
    tools=("Perseus Digital Library", "Thesaurus Linguae Graecae (TLG)", "Bretton Woods Latin Library", "Trismegistos", "Pleiades", "ToposText", "PhiloLogos", "Logos Bible Software", "LSJ (Liddell-Scott-Jones Lexicon)", "Lewis & Short (Latin Dictionary)", "Monier-Williams Sanskrit-English Dictionary", "Brents' Concordance (Greek Testament)", "Thesaurus Graecus Electronic", "Smith's Dictionary of Greek and Roman Antiquities", "Smith's Dictionary of Greek and Roman Biography and Mythology", "RE (Real-Encyclopädie der classischen Altertumswissenschaft)", "Packard Humanities Institute (PHI)", "Bibliothèque interuniversitaire d'études anciennes (BnF)", "Wikisource", "GRETIL (Göttingen Register of Electronic Texts)", "Sanskrit Heritage Project", "Sanskrit Projects (Sanskrit.org)", "Sanskrit Automatic Parser", "Sankha Sanskrit Analyzer", "Sankha Sanskrit Corpus", "SAP (Sanskrit Automatic Philology)", "Amarakosha Sanskrit Dictionary", "Dhruva Sanskrit Dictionary", "Dhruva Sanskrit Analyzer", "Dhruva Sanskrit Parser", "Dhruva Sanskrit Tagger", "Dhruva Sanskrit Stemmer", "Sanskrit Word Processor", "LaTeX (polyglossia / babel)", "BibLaTeX", "Zotero", "Mendeley", "EndNote", "Adobe Acrobat Pro", "Vim", "Emacs", "EpiDoc XML", "TEI P5", "XMLstarlet", "oXyGen XML Editor", "XML Spy", "Pleiades Atlas", "Google Books Ngram Viewer", "Project Gutenberg", "Internet Archive", "Digital Classics", "Open Library", "Bibliothèque de l'INHA"),
    category="文学",
    databases=("OpenAlex", "Crossref", "JSTOR", "PhilPapers", "Bibliothèque interuniversitaire d'études anciennes"),
)
