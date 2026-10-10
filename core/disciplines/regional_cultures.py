"""区域文化学科论文支持：区域文化研究、地方性知识与文化地理研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="regional_cultures",
    aliases=(
        "regional_cultures",
        "区域文化",
        "地方文化",
        "地域文化",
        "Regional Cultures",
        "Regional Studies",
        "Area Studies",
        "Local Culture"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与研究区）",
            "literature review（文献综述）",
            "methodology（田野/分析方法）",
            "results（文化现象与地方性）",
            "discussion（意义与讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例区域）",
            "analysis（文化现象分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（区域文化理论）",
            "evidence synthesis（研究进展）",
            "future directions",
            "references"
        ),
    },
    citation_style="Chicago 样式（注-书目制；人文社科主流）",
    reporting_standards={
        "fieldwork": "田野工作须报告知情同意、样本与访谈时数",
        "cultural_analysis": "文化现象须给出文本/图像/口述的原文与出处",
        "historical": "历史研究须注明史料版本与馆藏编号"
    },
    conventions=(
        "术语首现英文原词加中文译名",
        "地方性知识表述须注明传承人与采集时间",
        "民族志描写须区分叙述与观察",
        "文化地理分析须配合空间坐标与图件",
        "尊重地方信仰与禁忌的伦理声明"
    ),
    key_venues=(
        "Journal of Folklore Research",
        "Cultural Geographies",
        "Ethnology",
        "Asian Ethnology",
        "China Folk Culture"
    ),
    units_and_formulas_notes=(
        "时间统一使用公元纪年并注明世纪（如 20 世纪 30 年代）",
        "度量衡须注明当地传统单位与国际单位的换算",
        "访谈与口述须给出原始语言与译文",
        "引用地方文献须标注馆藏、卷号与页码"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "Atlas.ti", "Dedoose", "QDA Miner", "MAXQDA", "Ethnologue", "ArcGIS", "QGIS", "Otter.ai", "Zoom H6 Field Recorder", "Sony α7 Camera", "DJI Mavic Drone", "Museum Archive Database", "Internet Archive", "Voyant Tools", "Transcription Software", "Dictaphone Recorder", "Adobe Lightroom", "Camtasia（视频剪辑）", "Transana（质性分析）"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "Google Scholar"),
)
