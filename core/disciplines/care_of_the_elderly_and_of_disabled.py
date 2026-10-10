"""Care of the elderly and of disabled 学科论文支持：老年与残障综合照护体裁、多领域评估与量表注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="care_of_the_elderly_and_of_disabled",
    aliases=("care of the elderly and of disabled", "老年与残障综合照护",
             "残障老年照护", "elderly and disability care",
             "multidisciplinary care", "综合照护", "跨领域照护"),
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
        "outcome_report": "结局报告须给出多领域量表前后对比",
        "process_log": "照护日志须含时间与频次",
    },
    conventions=(
        "多领域量表（ADL、认知、营养、疼痛、抑郁）须标注版本与适用对象",
        "照护形式（居家/机构/社区/混合）须明确区分",
        "跨专业团队角色须说明",
        "隐私保护（去标识化）须说明",
        "术语须与综合照护界一致",
    ),
    key_venues=(
        "The Gerontologist",
        "Disability and Rehabilitation",
        "Journal of Advanced Nursing",
        "Age and Ageing",
        "International Journal of Older People Nursing",
        "Journal of Multidisciplinary Care in Aging",
    ),
    units_and_formulas_notes=(
        "各量表分数须注明量表与满分",
        "照护频次/时长用 次/天、小时/周，须注明",
        "多领域结局须逐项对照",
        "统计量给出均值 ± SD 与样本量",
        "引用干预须注明剂量与疗程",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Barthel 指数", "MMSE 简明精神状态量表", "MoCA 认知评估", "MNA 营养风险筛查", "RICE 疼痛量表", "GDS 抑郁量表", "Braden 压力性损伤风险量表", "CGA 综合评估", "Caring 护理评估软件", "iClinicalDoc 护理记录", "Sage 21 护理管理平台", "Vocera 临床通信", "Epic 电子病历", "Care Quality Compass 看板", "SPSS", "R", "Excel", "GraphPad Prism", "NVivo", "QResearch"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Semantic Scholar"),
)
