"""学前教师培养学科论文支持：幼儿课程设计、教学实践与早期发展支持研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="preprimary_teacher_training",
    aliases=(
        "preprimary teacher training", "学前教师培养", "学前教育师资",
        "preschool teacher education", "幼儿教师教育",
        "early childhood education", "学前教育",
        "early childhood teacher training", "早期教师培训",
        "nursery teacher training", "托幼教师培养",
        "kindergarten education",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（教学问题与发展目标）",
            "methodology（教学实验设计与测量工具）",
            "results（幼儿发展与教学成效）",
            "discussion（教学法讨论与实施条件）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（班级与幼儿学情）",
            "analysis（活动设计与观察记录）",
            "results（行为变化与发展评价）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（儿童发展理论谱系）",
            "evidence synthesis（教学法证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "幼儿发展测量须报告工具信效度与施测条件",
        "k2": "观察研究须报告观察方法、编码系统与观察时长",
        "k3": "伦理须说明监护人知情同意与幼儿隐私保护",
    },
    conventions=(
        "学情须交代年龄段、班级人数与园所类型",
        "活动设计须说明目标、材料、教师语言与互动策略",
        "发展评价须区分领域（认知、语言、社会性、动作）",
        "教师反思须与观察证据对应，避免主观化表述",
        "质性分析须注明编码过程与示例片段",
    ),
    key_venues=(
        "Early Childhood Research Quarterly",
        "Early Childhood Education Journal",
        "Journal of Research in Early Childhood Education",
        "Early Childhood Education Journal",
        "Early Years (Taylor & Francis)",
    ),
    units_and_formulas_notes=(
        "活动时长以分钟计量并注明是否为连续互动",
        "师幼比须报告班级人数与在场教师数",
        "观察编码须报告样本文本量与编码一致性",
        "发展工具得分须报告常模来源与年龄分段",
        "学习成效报告前后测差值并附显著性检验",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "NVivo", "ATLAS.ti", "MAXQDA", "ClassIn 智慧课堂", "iSpring Suite 微课制作", "Camtasia 录课工具", "MindMap 教学概念图工具", "GeoGebra", "Python (pandas, scipy)", "Jamovi", "Qualtrics", "SurveyMonkey", "Moodle LMS", "H5P 互动学习", "Obs 课堂录制", "MATLAB", "Excel", "PowerPoint"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
