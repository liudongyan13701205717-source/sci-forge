"""Te Hauora Me Te Oranga O Te Māori 学科论文支持：毛利健康与福祉研究论文体裁、APA 引用样式与毛利健康研究方法论记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="te_hauora_me_te_oranga_o_te_mori",
    aliases=(
        "te_hauora_me_te_oranga_o_te_mori",
        "Te Hauora Me Te Oranga O Te Māori",
        "毛利健康与福祉",
        "Māori Health And Wellbeing",
        "te hauora",
        "te oranga",
        "Māori health",
        "whānau health",
        "hauora research",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与毛利健康/福祉问题）",
            "methodology（毛利研究方法论与参与原则）",
            "findings（发现与证据）",
            "discussion（对毛利健康实践与政策的意义）",
            "whakaaetanga（毛利参与与伦理声明）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（毛利健康/福祉案例）",
            "analysis",
            "conclusion（结论与政策启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview（毛利健康史与现代研究）",
            "current state",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（Te Reo、NZ Medical Journal 遵循 APA/NZMJ 规范）",
    reporting_standards={
        "maori_methods": "研究须遵循 Te Ara Pūāwai 与 Kaupapa Māori，报告毛利治理、Kaumātua 咨询与毛利社区参与",
        "ethics": "伦理审查须报告：毛利社区知情同意、Kaumātua 咨询、毛利研究机构参与、保密与访问权限",
        "population": "人群定义须报告：毛利族裔自我认同、样本量 n、抽样的 iwi/区域",
        "measures": "毛利健康指标须报告：Te Whare Tapa Whā（身心/家族/精神/身体）与 Te Puna Koko（精神/家族/社会/环境/身体）模型应用",
        "systematic_review": "系统综述遵循 PRISMA 2020 声明",
    },
    conventions=(
        "毛利语健康概念须报告毛利语原文与英文翻译：te hauora（健康）、te oranga（福祉）、mātauranga Māori（毛利知识）、te whānau（家族/家庭）",
        "毛利健康框架遵循 Te Whare Tapa Whā（四支柱：taha wairua 精神、taha hinengaro 心理、taha whānau 家族、taha tinana 身体）",
        "毛利健康指标须报告 Te Puna Koko 五维（spiritual、relational、community、environmental、physical）评估",
        "研究遵循 Te Ara Pūāwai、Kaupapa Māori、Te Aho Aratangiwhā 与 Te Ara Mahi；伦理审查报告毛利治理参与",
        "毛利语地名与 iwi 名遵循毛利语正字法；首次出现附英文名与位置",
        "毛利健康研究数据须报告毛利社区参与与访问权限管理；毛利族谱/谱系数据遵循 Ngā Taonga Sound & Vision 访问等级",
    ),
    key_venues=(
        "Te Ao Māori",
        "NZ Medical Journal",
        "New Zealand Journal of Public Health",
        "Australian and New Zealand Journal of Public Health",
        "Journal of Pacific Family Therapy",
        "Te Reo",
    ),
    units_and_formulas_notes=(
        "健康指标遵循 Te Whare Tapa Whā 与 Te Puna Koko 五维模型；毛利健康研究须报告维度适用性",
        "毛利研究方法论遵循 Te Ara Pūāwai、Kaupapa Māori、Te Aho Aratangiwhā 与 Te Ara Mahi",
        "毛利研究伦理审查遵循毛利社区知情同意、Kaumātua 咨询与毛利研究机构参与协议",
        "毛利健康数据（谱系、口述史、健康记录）须报告毛利社区参与与访问权限管理",
        "毛利语地名、iwi 名、毛利语术语须保留原文与 macron；公式（如流行病学指标）用 amsmath",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Te Whare Tapa Whā Framework", "Te Puna Koko", "R", "Stata", "SPSS", "NVivo", "Atlas.ti", "Excel", "QGIS", "Google Forms", "SurveyMonkey", "REDCap", "Zoom H1n Recorders", "Audacity", "Adobe Audition", "ELAN", "Transana", "Python (pandas)", "Google Docs", "Zotero"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "Te Kete O Te Māori"),
)
