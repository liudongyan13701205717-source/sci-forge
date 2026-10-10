"""太平洋族群社会与社区学科论文支持：波利尼西亚/密克罗尼西亚/美拉尼西亚族群田野体裁与社区参与报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pacific_peoples_society_and_community",
    aliases=(
        "pacific_peoples_society_and_community",
        "太平洋族群社会与社区",
        "Pacific Peoples Society And Community",
        "Pacific Studies",
        "Oceania Studies",
        "岛民社会研究",
        "Melanesia Polynesia Micronesia",
        "Pacific Islander Community Studies",
        "太平洋岛民社群研究"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（田野方法）",
            "results（发现）",
            "discussion（讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references"
        ),
    },
    citation_style="APA 第7版",
    reporting_standards={
        "k1": "田野民族志遵循 COREQ 报告规范",
        "k2": "社区参与研究遵循社区知情同意与数据主权规范",
        "k3": "实证调查遵循 APA 报告规范"
    },
    conventions=(
        "民族志研究须获得社区伦理批准与社区知情同意",
        "原住民数据主权须尊重，数据返还与公开须经社区授权",
        "田野工作须报告在场时长、使用语言与口译安排",
        "口述史材料须标注受访者代号与文化审查流程",
        "涉及传统知识与领地信息时须避免精确地理坐标的公开披露"
    ),
    key_venues=(
        "Pacific Affairs",
        "Journal of the Pacific Society",
        "Pacific Studies",
        "Oceanic Studies",
        "Asia Pacific Journal of Anthropology"
    ),
    units_and_formulas_notes=(
        "人口与家计单位以村落或家系为统计单位，须注明分类依据",
        "田野时长以在场周数或月份计量并注明季节影响",
        "受访者规模给出 N 并说明饱和判断依据",
        "涉及传统历法时须换算公历并说明对应关系"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "MAXQDA", "ATLAS.ti", "SPSS", "R", "JASP", "Tableau", "QGIS", "Microsoft Excel", "EndNote", "Zotero", "Dedoose", "SurveyMonkey", "Qualtrics", "Zoom", "OBS Studio", "Sony ZV-1", "Adobe Premiere Pro", "Google Maps", "Transkriptor"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
