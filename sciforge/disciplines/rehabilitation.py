"""康复学科论文支持：康复服务、职业康复与功能评估研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="rehabilitation",
    aliases=(
        "rehabilitation",
        "康复",
        "康复治疗",
        "职业康复",
        "Rehabilitation Science",
        "Occupational Therapy",
        "Physical Therapy",
        "Vocational Rehabilitation"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与康复问题）",
            "methods（设计与人群）",
            "results（功能结局数据）",
            "discussion（机理与临床意义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（患者与干预）",
            "analysis（功能变化分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（ICF/康复理论）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references"
        ),
    },
    citation_style="Vancouver 样式（编号制；康复与护理主流）",
    reporting_standards={
        "randomized_trial": "RCT 遵循 CONSORT 康复扩展",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明"
    },
    conventions=(
        "ICF 分类术语（活动/参与/身体功能）使用须规范",
        "功能量表（FIM/BI/FMA/SPM）首现给出全称与范围",
        "干预方案（频率/强度/时长）须完整报告",
        "结局测量时间点须明确",
        "伦理审查与知情同意须报告"
    ),
    key_venues=(
        "Archives of Physical Medicine and Rehabilitation",
        "Disability and Rehabilitation",
        "American Journal of Occupational Therapy",
        "Journal of Rehabilitation Research and Development",
        "Physical Therapy"
    ),
    units_and_formulas_notes=(
        "功能量表分数无量纲；效应量给出 Cohen's d",
        "时间单位：周/月；治疗强度：次/周、分钟/次",
        "结果报告均值 ± SD 与 95% CI",
        "最小临床重要差异（MCID）须明确"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("FIM Scale", "Barthel Index", "Fugl-Meyer Scale", "SPM Scale", "Berg Balance Scale", "Timed Up and Go Test", "6-Minute Walk Test", "Vicon Motion Analysis", "Kinect Motion Capture", "MyoWare EMG Sensor", "Gait Trainer", "Robotic Exoskeleton", "FES System", "InBody Composition Analyzer", "MyoBot EMG System", "SPSS", "STATA", "R", "Qualtrics", "REDCap"),
    category="医学",
    databases=("OpenAlex", "PubMed", "Crossref", "CNKI"),
)
