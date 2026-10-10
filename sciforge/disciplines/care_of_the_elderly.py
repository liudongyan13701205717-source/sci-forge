"""Care (non-medical) of the elderly 学科论文支持：老年非医疗照护体裁、护理评估与 ADL 量表注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="care_of_the_elderly",
    aliases=("care (non-medical) of the elderly", "老年非医疗照护",
             "老年人照护", "老年护理", "elderly care",
             "non-medical elderly care", "geriatric care", "养老护理"),
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
        "ADL 量表（Barthel、Katz 等）须标注版本与得分范围",
        "跌倒风险/营养风险须用标准筛查工具",
        "照护等级须用统一分级标准",
        "隐私保护（去标识化）须说明",
        "术语须与养老护理界一致",
    ),
    key_venues=(
        "The Gerontologist",
        "Journal of the American Geriatrics Society",
        "Age and Ageing",
        "British Journal of Nursing",
        "Journal of Gerontological Nursing",
        "Archives of Gerontology and Geriatrics",
    ),
    units_and_formulas_notes=(
        "ADL 分数须注明量表与满分",
        "照护频次用 次/天，须注明",
        "跌倒/营养风险须用统一分级",
        "统计量给出均值 ± SD 与样本量",
        "引用干预须注明剂量与疗程",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Barthel 指数", "Katz ADL 量表", "MMSE 简明精神状态量表", "MoCA 认知评估", "MNA 营养风险筛查", "Braden 压力性损伤风险量表", "FIMS 跌倒风险筛查", "GDS 老年抑郁量表", "Caring 护理评估软件", "iClinicalDoc 护理记录", "Sage 21 护理管理平台", "Vocera 临床通信", "Epic 电子病历", "Care Quality Compass 看板", "SPSS", "R", "Excel", "GraphPad Prism", "NVivo", "QResearch"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Semantic Scholar"),
)
