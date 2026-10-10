"""整体医学学科论文支持：整体医学、身心医学与整合医疗临床研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="holistic_medicine",
    aliases=("holistic_medicine", "整体医学", "整合医学", "身心医学", "自然医学", "Holistic Medicine", "Integrative Medicine", "Mind-Body Medicine", "Complementary Medicine"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"k1": "CONSORT 随机对照试验报告规范", "k2": "STROBE 观察性研究报告规范", "k3": "CAM-PRIS 补充与替代医学研究方案规范"},
    conventions=("干预方案须完整描述（时间、剂量、疗程、操作者资质）", "疼痛评分须注明 NRS/VAS 与时间点", "主观量表须注明信效度来源", "对照组须注明替代干预内容", "伦理与知情同意须单独列出"),
    key_venues=("Journal of Integrative Medicine", "Evidence-Based Complementary and Alternative Medicine", "Journal of Alternative and Complementary Medicine", "PLOS ONE", "BMC Complementary and Alternative Medicine"),
    units_and_formulas_notes=("疼痛/疲劳：NRS 0–10 或 VAS 0–100 mm", "心率：bpm", "血压：mmHg", "量表得分须注明计分方向与总分上限"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("IBM SPSS Statistics", "R（统计建模）", "JASP（贝叶斯分析）", "Stata", "Epi Info", "REDCap（电子病例报告）", "Qualtrics（量表平台）", "OpenClinica（临床试验管理）", "Pavilion（电子健康档案）", "Biohealth 生物反馈仪", "HeartMath HRV 心电仪", "GSR 皮肤电导仪", "Sphygmocor 动脉硬化检测", "红外热成像仪（FLIR）", "EndNote", "Zotero", "PRISMA Flow Diagram 工具", "RevMan（Meta 分析）", "Cochrane Risk of Bias Tool", "CONSORT Checklist 工具"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
