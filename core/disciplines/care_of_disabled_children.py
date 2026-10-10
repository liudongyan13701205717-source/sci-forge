"""Care (non-medical) of disabled children 学科论文支持：儿童/青少年残障非医疗照护体裁、发育评估与量表注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="care_of_disabled_children",
    aliases=("care (non-medical) of disabled children", "儿童残障非医疗照护",
             "残障儿童照护", "disability child care",
             "pediatric disability care", "supported childhood care"),
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
        "发育/认知评估量表（Bayley、Vineland、C-SPC 等）须标注版本与适用年龄",
        "照护形式须区分医疗/非医疗",
        "干预措施须具体可复现",
        "未成年人隐私保护（监护人知情同意）须说明",
        "术语须与儿童残障照护界一致",
    ),
    key_venues=(
        "Journal of Intellectual Disability Research",
        "Disability and Rehabilitation",
        "Child: Care, Health and Development",
        "Pediatrics",
        "Journal of Pediatric Psychology",
        "Children's Health Care",
    ),
    units_and_formulas_notes=(
        "发育年龄须注明评估工具",
        "评分/等级须注明量表与满分",
        "照护频次用 次/天，须注明",
        "统计量给出均值 ± SD 与样本量",
        "引用干预须注明剂量与疗程",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Bayley 婴幼儿发育量表", "Vineland 适应行为量表", "C-SPC 儿童支持需求评定", "Pediatric RICE 疼痛量表", "PedsQL 生活质量量表", "MoCA-K 儿童认知评估", "Caring 护理评估软件", "iClinicalDoc 护理记录", "Sage 21 护理管理平台", "Vocera 临床通信", "Epic 电子病历", "Simplicity 儿童照护记录", "SPSS", "R", "Excel", "GraphPad Prism", "NVivo", "QResearch", "PEMS 发育行为量表", "PDI 个人日常独立性量表"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Semantic Scholar"),
)
