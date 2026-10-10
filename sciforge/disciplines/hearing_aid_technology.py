"""助听器技术学科论文支持：听觉辅助与听力临床体裁、APA 7 引用样式与声学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hearing_aid_technology",
    aliases=("hearing_aid_technology", "助听器技术", "助听器", "听力技术", "听力学", "听觉辅助设备", "耳蜗植入", "助听设备", "听觉康复"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "clinical_trial": "CONSORT 声明",
        "device_trial": "器械临床试验规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "频率/分贝用 dB HL/dB SPL",
        "助听器参数须报告",
        "听力图须标注频率轴",
        "测试结果给出均值±SD",
        "伦理审批号须报告",
    ),
    key_venues=(
        "Hearing Research",
        "Trends in Hearing",
        "Hear Res",
        "J Acoust Soc Am",
        "Int J Audiology",
    ),
    units_and_formulas_notes=(
        "频率用 Hz/kHz；响度用 dB",
        "公式用 amsmath；声学公式须编号",
        "行内公式避免复杂分式",
        "数值结果给出均值±SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (SciPy)", "LabVIEW", "PureTone Audiometer", "Impedance Audiometer", "OtoPlug Analyzer", "Sound Field Audiometer", "RealEar Analyzer", "FreeBES", "Audition", "myPhonak", "Widex Entourage", "Oticon More", "Signia AudioConnect", "PRA", "PureTone 5020", "Sound Field 351", "Audioscan", "OAE Analyzer", "Headphone HDA-200"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
