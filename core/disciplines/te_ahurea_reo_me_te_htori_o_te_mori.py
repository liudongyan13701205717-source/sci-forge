"""Te Ahurea, Reo Me Te Hītori O Te Māori 学科论文支持：毛利文化、语言与历史研究论文体裁、APA 引用样式与毛利研究方法论记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="te_ahurea_reo_me_te_htori_o_te_mori",
    aliases=(
        "te_ahurea_reo_me_te_htori_o_te_mori",
        "Te Ahurea, Reo Me Te Hītori O Te Māori",
        "毛利文化、语言与历史",
        "Māori Culture, Language And History",
        "te reo Māori",
        "maoritanga",
        "oral history",
        "ethnography",
        "whakapapa",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与毛利文化/语言/历史问题）",
            "methodology（毛利研究方法论与参与原则）",
            "findings（发现与证据）",
            "discussion（对毛利文化与实践的意义）",
            "whakaaetanga（毛利参与与伦理声明）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（文化/语言/历史案例）",
            "analysis",
            "conclusion（结论与意义）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview（历史脉络与关键节点）",
            "current state（当代研究与实践）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（Te Ao Māori、The Journal of Pacific History 遵循 APA 规范）",
    reporting_standards={
        "maori_methods": "研究须遵循 Te Ara Pūāwai（毛利研究方法论）或 Kaiwhakahaere（毛利治理原则），报告毛利治理与参与",
        "ethics": "伦理审查须报告：毛利社区参与、知情同意、Kaumātua（毛利长者）咨询、Kaupapa Māori 参与",
        "oral_history": "口述史研究须报告：口述者身份与关系、录音条件、转录与转译方法、保密约定",
        "linguistic": "语言研究须报告：语料来源、标注工具（ELAN/Transana）、正字法与转写规则",
        "whakapapa": "涉及毛利族谱/谱系须报告：Kaumātua 参与、族谱来源与验证方法",
        "systematic_review": "系统综述遵循 PRISMA 2020 声明",
    },
    conventions=(
        "毛利语拼写遵循 Te Aka 正字法；macron（tāraro）保留：ā ē ī ō ū；hākerekorehe 无空格书写词根",
        "毛利称谓遵循文化尊重原则：iwi（部落）、hapū（亚部落）、marae（会堂）、kaumātua（长者）、tohunga（专家）首次出现须给出毛利语原文与英文翻译",
        "毛利历法与时间：毛利新年 Matariki、季节 koanga/tāmano（夏）、tōi/kohanga（秋）、hōtoke（冬）、puranga/māwharau（春）须用毛利语原文",
        "地名遵循毛利语原名（如 Aotearoa、Waikato、Te Tai Tokerau），首次出现附英文名",
        "研究遵循 Kaupapa Māori（毛利本位研究法）与 Te Aho Aratangiwhā（毛利研究指南）；伦理审查报告毛利治理参与",
        "毛利语引用须保留原文与翻译；毛利语引用遵循毛利语标点惯例（无引号或单引号）",
    ),
    key_venues=(
        "Te Ao Māori",
        "Te Reo",
        "Journal of the Polynesian Society",
        "The Journal of Pacific History",
        "Te Puna Wānanga",
        "Maui Journal of Māori Studies",
    ),
    units_and_formulas_notes=(
        "研究涉及毛利语词汇与短语须报告毛利语原文与英文翻译（毛利语-英语对照表）",
        "研究涉及毛利家族谱系/毛利语地名须报告毛利语原文（含 macron）与英文/拉丁转写",
        "毛利研究方法论遵循 Te Ara Pūāwai、Kaupapa Māori、Te Aho Aratangiwhā 与 Te Ara Mahi（毛利研究实践指南）",
        "毛利研究伦理审查遵循 Te Kete O Te Rāngatira、Kaumātua 参与协议与毛利社区知情同意书",
        "毛利研究数据（口述史、族谱、文化资料）须报告毛利社区参与与访问权限管理（如 Ngā Taonga Sound & Vision 访问等级）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Te Kete O Te Māori", "Te Arawhiti (Te Ao Māori Dictionary)", "Te Awa Tupua Toolkit", "Te Reo Awhi (Māori Language Learning)", "ELAN", "Transana", "NVivo", "Atlas.ti", "Zotero", "EndNote", "Adobe Audition", "Audacity", "Zoom H1n Recorders", "Sony PCM-D100", "Google Earth", "GIS (QGIS)", "Python (pandas)", "R", "Google Docs", "Overleaf"),
    category="文学",
    databases=("OpenAlex", "Crossref", "Te Kete O Te Māori", "Te Arawhiti"),
)
