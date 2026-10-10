"""Caretaking, housekeeping, home 学科论文支持：家政/居家照护体裁、家庭管理注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="caretaking_housekeeping_home",
    aliases=("caretaking, housekeeping, home", "家政", "家庭管理",
             "居家照护", "housekeeping", "home care", "家政学",
             "home management", "家政管理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（家政/照护背景与问题）",
            "方法（研究设计与评估工具）",
            "结果（服务效果与数据）",
            "讨论（服务实践与改进）",
            "references",
        ),
        "report": (
            "abstract",
            "个案/项目概述",
            "服务方案与执行",
            "评估与调整",
            "经验总结",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；服务干预须可复核）",
    reporting_standards={
        "case_study": "个案须说明服务内容、频率与执行过程",
        "outcome_report": "结局报告须给出满意度/质量前后对比",
        "process_log": "服务日志须含时间与频次",
    },
    conventions=(
        "服务质量量表（满意度、护理质量）须标注版本与计分方式",
        "服务类型（家政、照护、家庭管理）须明确区分",
        "干预措施须具体可复现",
        "隐私保护（去标识化）须说明",
        "术语须与家政/居家照护界一致",
    ),
    key_venues=(
        "International Journal of Hospitality Management",
        "Journal of Housing and the Built Environment",
        "Housing Studies",
        "Family Relations",
        "Journal of Consumer Affairs",
        "Journal of Elder Abuse & Neglect",
    ),
    units_and_formulas_notes=(
        "满意度/质量分数须注明量表与满分",
        "服务频次/时长用 次/周、小时/周，须注明",
        "成本指标须注明口径",
        "统计量给出均值 ± SD 与样本量",
        "引用干预须注明剂量与疗程",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("家政服务质量量表", "满意度问卷", "护理质量评估工具", "Home-care 服务管理平台", "iClinicalDoc 居家照护记录", "Caring 护理评估软件", "Epic 电子病历", "Vocera 临床通信", "SPSS", "R", "Python", "Excel", "GraphPad Prism", "Qualtrics 问卷平台", "NotebookLM", "NVivo", "QResearch", "Tableau", "Figma", "Obsidian"),
    category="管理学",
    databases=("OpenAlex", "CNKI", "Semantic Scholar"),
)
