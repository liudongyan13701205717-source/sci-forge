"""Mātauranga Māori 学科论文支持：毛利知识与毛利教育研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mtauranga_mori",
    aliases=(
        "mtauranga_mori", "Mātauranga Māori", "毛利知识", "毛利教育",
        "Māori Education", "te reo Māori", "Māori learning",
        "Māori knowledge systems", "毛利知识体系",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（研究设计与 iwi 关系）",
            "results（发现）",
            "discussion（意义与影响）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（社区背景）",
            "analysis（分析与讨论）",
            "results（结果）",
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
    citation_style="APA 7（配合 iwi 数据主权规范）",
    reporting_standards={
        "k1": "毛利研究须遵循 Kātiritanga 与 iwi 数据主权规范",
        "k2": "参与式研究须报告 iwi 授权与参与者知情同意",
        "k3": "语言与口述史研究须报告录音许可与文化审查",
    },
    conventions=(
        "毛利语术语首次出现须给出音译与释义",
        "人名地名拼写遵循 te reo Māori 正字法",
        "涉及 iwi 数据须说明授权来源",
        "口述史引用须遵循毛利口述传统礼节",
        "图表标注需中英毛利三语对齐",
    ),
    key_venues=(
        "Journal of Pacific Studies",
        "Maui: International Review of Indigenous Education",
        "Educational Research for Social Change",
        "Te Reo",
        "《毛利教育研究》",
    ),
    units_and_formulas_notes=(
        "毛利日期给出 te wa puapua 与格里日期对应",
        "iwi/hapū 数据分组须遵循部落分类",
        "样本量与社区人数按 iwi 归属分组",
        "引用口述史须给出口述者与日期",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "Transana", "MAXQDA", "Collected Works", "Droplet", "Māori Dictionary", "Te Aka Māori Dictionary", "Wikitoki", "EndNote", "RefWorks", " Zotero", "Microsoft Excel", "RStudio", "QGIS", "Panopto", "Audacity", "Adobe Premiere Pro", "Google Docs", "Microsoft Word"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
