"""Māori 环境知识学科论文支持：Ngā Mātauranga Taiao O Te Māori 环境观/生态知识体裁、Te Aotearoa 报告规范与毛利生态记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ng_mtauranga_taiao_o_te_mori",
    aliases=("ng_mtauranga_taiao_o_te_mori", "毛利环境知识", "Māori Environmental Knowledges",
             "Ngā Mātauranga Taiao O Te Māori", "environmental knowledges",
             "Māori ecology", "毛利生态学", "te taiao",
             "传统生态知识", "TEK"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与毛利世界观）",
            "methodology（whakapapa 谱系与观察方法）",
            "results（生态知识发现）",
            "discussion（与 whakapapa 关联）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例地物与 iwi 归属）",
            "analysis（生态与 whakapapa 分析）",
            "results（发现与实践）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（传统生态知识理论）",
            "evidence synthesis（iwi 与部落知识综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份，毛利语术语须标音）",
    reporting_standards={
        "te_tiriti": "论文须尊重 Te Tiriti o Waitangi 精神",
        "iwi_consultation": "涉及 iwi 的知识须取得 iwi 认可",
        "maori_language": "毛利语术语遵循 Te Aka 词典规范",
        "karakia": "研究开始前须行 karakia 仪式",
        "ethics": "HREC 与 iwi 双批准",
    },
    conventions=(
        "毛利语术语遵循 Te Aka 规范",
        "地名遵循 iwi 官方命名",
        "whakapapa 谱系须标注层数",
        "毛利语首字母大写",
        "引用遵循 kaitiakitanga 守护者原则",
    ),
    key_venues=(
        "Te Reo 140206",
        "Te Aroha",
        "Te Ao Māori Journal",
        "Journal of Polynesian Research",
        "Te Whare Wānanga Press",
        "Te Aotearoa Journal",
    ),
    units_and_formulas_notes=(
        "距离用 km；海拔用 m",
        "温度用摄氏度",
        "面积用 km²",
        "毛利语术语首字母大写",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("QGIS", "ArcGIS", "Google Earth Pro", "NVivo", "R", "Python", "Microsoft Excel", "SPSS", "StoryMapJS", "FieldNotes", "DJI Mavic 3", "Garmin GPSmap", "Te Aka Dictionary", "Whakapapa Tree", "iwi Registry", "Māori Dictionary", "Cambridge Dictionary", "Endnote", "Zotero", "LaTeX"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
