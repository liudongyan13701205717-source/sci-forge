"""文献史学科论文支持：史料学、文献学与学术史研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="literature_history",
    aliases=(
        "literature_history",
        "文献史",
        "history of scholarship",
        "book history",
        "历史文献",
        "学术史",
        "古籍整理",
        "manuscript studies",
        "bibliography",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究缘起）",
            "methodology（史料与方法）",
            "results（考证与结论）",
            "discussion（意义讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（文献与史实）",
            "analysis（考证分析）",
            "results（结论）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（史学理论综述）",
            "evidence synthesis（史料综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago",
    reporting_standards={
        "k1": "考证研究须列出所据版本与卷次",
        "k2": "史料引用注明档案馆藏号或图版编号",
        "k3": "学术史梳理覆盖主要流派与代表人物",
    },
    conventions=(
        "引用古籍标注版本、卷数与页码",
        "首次出现史家著作注明作者、出版年",
        "档案引用给出馆藏、档号、页码",
        "译注文献须说明底本与校勘依据",
        "图像材料注明拍摄者与编号",
    ),
    key_venues=(
        "Journal of the History of Ideas",
        "Renaissance Quarterly",
        "Journal of Book History",
        "Archiv für Geschichte der Sozialwissenschaften",
        "历史研究",
    ),
    units_and_formulas_notes=(
        "古籍引用遵循中华书局点校本规范",
        "档案日期标注纪年并括注公元",
        "图版引用注明尺寸与来源",
        "译文中外文并列时以原意为准",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("中国基本古籍库", "敦煌写本文献研究平台", "Europeana", "Internet Archive", "DAMS (Digital Archives)", "Abydos (Papyri Tool)", "Vesuvius Challenge", "Papyri.info", "Trismegistos", "TEI (Text Encoding Initiative)", "EAD", "ArchivesSpace", "Ora et Labora Digital (OraMedia)", "Digital Scriptorium", "HathiTrust", "Collate (Digital Philology)", "TEI Publisher（TEI 出版）", "IIIF / Universal Viewer", "Papyri.info Editor", "OpenEdition 学术出版平台"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "ProQuest Historical", "国家图书馆古籍数据库"),
)
