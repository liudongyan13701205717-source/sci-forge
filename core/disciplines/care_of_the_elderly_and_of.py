"""Care of the elderly and of 学科论文支持：老年综合照护体裁（名称截断变体）、护理评估与 ADL 量表注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="care_of_the_elderly_and_of",
    aliases=("care of the elderly and of", "老年综合照护",
             "老年人照护服务", "elderly care service",
             "comprehensive elderly care", "老年照护", "养老服务"),
    paper_types={
        "research": (
            "abstract",
            "introduction（照护背景与问题）",
            "方法（研究设计与评估工具）",
            "结果（照护效果与数据）",
            "讨论（照护实践与改进）",
            "references",
        ),
        "report": (
            "abstract",
            "个案/项目概述",
            "照护计划与执行",
            "评估与调整",
            "经验总结",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；护理干预须可复核）",
    reporting_standards={
        "case_study": "个案须说明评估工具与照护干预全过程",
        "outcome_report": "结局报告须给出量表前后对比",
        "process_log": "照护日志须含时间与频次",
    },
    conventions=(
        "ADL/营养/跌倒风险量表须标注版本与适用对象",
        "照护形式（居家/机构/社区）须明确区分",
        "干预措施须具体可复现",
        "隐私保护（去标识化）须说明",
        "术语须与养老服务界一致",
    ),
    key_venues=(
        "The Gerontologist",
        "Journal of Applied Gerontology",
        "Journal of Aging and Social Policy",
        "Ageing and Society",
        "Journal of Gerontological Nursing",
        "Medical Care",
    ),
    units_and_formulas_notes=(
        "各量表分数须注明量表与满分",
        "服务频次/时长用 次/天、小时/周，须注明",
        "成本效益指标须注明口径",
        "统计量给出均值 ± SD 与样本量",
        "引用干预须注明剂量与疗程",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Barthel 指数", "Katz ADL 量表", "MMSE 简明精神状态量表", "MNA 营养风险筛查", "Braden 压力性损伤风险量表", "GDS 老年抑郁量表", "生活质量量表 QOL", "Caring 护理评估软件", "iClinicalDoc 护理记录", "Sage 21 护理管理平台", "Epic 电子病历", "养老服务监管系统", "SPSS", "R", "Excel", "GraphPad Prism", "NVivo", "QResearch", "Qualtrics 问卷平台", "Obsidian"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Semantic Scholar"),
)
