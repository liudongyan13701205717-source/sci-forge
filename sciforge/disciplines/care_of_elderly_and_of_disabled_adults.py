"""Care of elderly and of disabled adults 学科论文支持：老年及残障成人综合照护体裁、综合评估与量表注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="care_of_elderly_and_of_disabled_adults",
    aliases=("care of elderly and of disabled adults", "老年与残障成人照护",
             "老年残障照护", "elderly and disability care",
             "geriatric and disability care", "comprehensive care"),
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
            "个案概述",
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
        "综合评估量表（CGA、Barthel、MNA、GDS 等）须标注版本与适用对象",
        "照护等级须用统一分级标准",
        "干预措施须具体可复现",
        "隐私保护（去标识化）须说明",
        "术语（残疾类型、照护形式）须与行业一致",
    ),
    key_venues=(
        "The Gerontologist",
        "Journal of the American Geriatrics Society",
        "Age and Ageing",
        "Disability and Rehabilitation",
        "British Journal of Nursing",
        "Journal of Multidisciplinary Care in Aging",
    ),
    units_and_formulas_notes=(
        "活动能力/营养分数须注明量表与满分",
        "照护频次用 次/天，须注明",
        "风险等级须用统一分级标准",
        "统计量给出均值 ± SD 与样本量",
        "引用干预须注明剂量与疗程",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Barthel 指数", "CGA 综合老年评估", "MNA 营养风险筛查", "GDS 老年抑郁量表", "Braden 压力性损伤风险量表", "RICE 疼痛量表", "MoCA 认知评估", "Caring 护理评估软件", "iClinicalDoc 护理记录", "Sage 21 护理管理平台", "Vocera 临床通信", "Epic 电子病历", "Care Quality Compass 看板", "SPSS", "R", "Excel", "GraphPad Prism", "NotebookLM", "NVivo", "QResearch"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Semantic Scholar"),
)
