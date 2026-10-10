"""民族学学科论文支持：民族研究、文化人类学与民族志研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ethnology",
    aliases=(
        "ethnology", "民族学", "民族研究",
        "ethnology", "民族学",
        "cultural anthropology", "文化人类学",
        "ethnography", "民族志",
        "social anthropology", "社会人类学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（民族问题与背景）",
            "methodology（田野调查、民族志、文化分析）",
            "results（民族分析与文化评估）",
            "discussion（民族研究启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "ethnographic analysis（民族志分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "fieldwork": "田野调查须注明地点、时间与方法",
        "analysis": "文化分析须注明理论框架",
        "ethics": "涉及民族数据须声明隐私保护",
    },
    conventions=(
        "民族名称须使用标准名称",
        "田野调查须注明地点、时间与方法",
        "文化概念须定义清晰",
        "民族志须注明来源与时间",
    ),
    key_venues=(
        "American Ethnologist",
        "Journal of the Royal Anthropological Institute",
        "Ethnology",
        "Cultural Anthropology",
        "Journal of Material Culture",
        "Anthropological Quarterly",
    ),
    units_and_formulas_notes=(
        "民族名称须使用标准名称",
        "田野调查须注明地点、时间与方法",
        "文化概念须定义清晰",
        "民族志须注明来源与时间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "NVivo", "Atlas.ti", "MAXQDA", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "ArcGIS", "QGIS", "Google Earth", "Camera", "Audio Recorder", "Video Camera", "Transcription Software", "Translation Software", "Dedoose", "Zotero", "Tableau"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
