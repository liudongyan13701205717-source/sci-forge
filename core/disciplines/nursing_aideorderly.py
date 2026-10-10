"""护理辅助与护士助理学科论文支持：基础护理技能/岗位胜任力体裁、APA 7 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nursing_aideorderly",
    aliases=(
        "nursing_aideorderly",
        "护理辅助",
        "Nursing Aide",
        "Nursing Assistant",
        "Orderly",
        "Patient Care Technician",
        "Personal Care Aide",
        "Care Assistant",
        "护士助理",
    ),
    paper_types={
        "research": ("abstract", "introduction（岗位与研究问题）", "methodology（技能评估工具与样本）", "results（技能掌握与安全性指标）", "discussion（岗位实践含义）", "references"),
        "case_study": ("abstract", "introduction", "case description（岗位情境）", "analysis（护理行为分析）", "results（工作成效）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（岗位标准综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "skills_assessment": "技能评估遵循 Objective Structured Clinical Examination 规范",
        "safety": "护理安全事件报告遵循 RC/NCQA 框架",
        "survey": "岗位胜任力调查遵循 AAPOR 规范",
    },
    conventions=(
        "岗位职责说明按国家/地区护理规范引用",
        "技能评估给 OSCE 评分标准与信度",
        "患者安全指标给定义与统计口径",
        "伦理委员会批准与知情同意须说明",
        "岗位培训与继续教育学时记录",
    ),
    key_venues=(
        "Journal of Nursing Education",
        "Nursing Standard",
        "Journal of Advanced Nursing",
        "Nurse Education Today",
        "Journal of Nursing Regulation",
    ),
    units_and_formulas_notes=(
        "OSCE 评分给标准分与信度",
        "患者安全指标给定义口径（每 1000 患者-日）",
        "培训学时与技能通过率给出",
        "样本量与显著性检验须说明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Epic EHR", "Cerner Millennium", "Microsoft Excel", "Google Sheets", "SPSS", "R", "NVivo", "ATLAS.ti", "Tableau", "EndNote", "Mendeley", "Zotero", "CINAHL", "SIMMAN 3G", "CAVE MAN Simulator", "Nursing Skills Simulator", "Lippincott CQ", "病人转运带", "护理评估软件", "Qualtrics"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
