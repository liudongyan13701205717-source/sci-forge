"""社会人类学学科论文支持：民族志/亲属/仪式体裁、Chicago 引用样式与田野资料编码规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_anthropology",
    aliases=("social_anthropology", "社会人类学", "文化人类学", "民族志", "kinship studies", "cultural anthropology", "social anthropology", "ethnography"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与理论框架）",
            "fieldwork and data collection（田野点、参与式观察、访谈）",
            "analysis（主题、话语与结构分析）",
            "discussion（理论对话与反思）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述与田野背景）",
            "analysis（个案深度分析）",
            "results（发现与讨论）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（跨文化证据综合）",
            "future directions",
            "references"
        )
    },
    citation_style="Chicago 作者-年份（American Anthropologist 遵循 ASA 规范；Current Anthropology 采用 Chicago）",
    reporting_standards={
        "ethnography": "民族志遵循 reflexivity 声明：研究者位置、进入田野过程、伦理审查、知情同意",
        "qualitative": "质性研究遵循 COREQ/SRQR 清单：抽样逻辑、饱和判断、编码方法透明",
        "consent": "涉及敏感议题（性别、宗教、少数族群）须报告二次告知与匿名化处理",
        "data_archiving": "田野资料（访谈录音、照片、笔记）按 AAAS/AnthroSource 规范去标识化存档并说明可获取性"
    },
    conventions=(
        "民族志以第三人称叙述为主，保留反思性第一人称段落说明研究者位置",
        "访谈引语给出转写行号或时间戳，并标注受访者编号与匿名化名",
        "亲属关系图使用 Draw.a.Kinship 或 ISO 标准符号，性别、婚姻、亲系标注清晰",
        "时间/空间参照系统声明：本土历法、地名发音、方位体系须在方法中说明",
        "跨文化比较须报告田野规模、田野持续时间、语言能力与访谈场次"
    ),
    key_venues=(
        "American Anthropologist",
        "Current Anthropology",
        "Journal of the Royal Anthropological Institute",
        "Cultural Anthropology",
        "Man and Society"
    ),
    units_and_formulas_notes=(
        "田野点信息给出经纬度、人口规模与民族构成",
        "访谈场次、录音时长、转写字数须在方法中报告",
        "亲属关系图使用 ISO 亲属图符号（□/○/─/∥），世代用横线分隔",
        "定量表格三线制；类别变量给频数与百分比（注明基数 N）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "MAXQDA", "ATLAS.ti", "Dedoose", "Transana", "ELAN", "Praat", "Audacity", "QGIS", "Garmin GPSMAP 66i", "Zoom H5", "Draw.a.Kinship", "Obsidian", "Zotero", "Adobe Lightroom", "DaVinci Resolve", "Google Earth Pro", "R", "EndNote", "iPad + Apple Pencil"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI")
)
