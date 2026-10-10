"""反射疗法学科论文支持：足部反射/替代医学/整体健康体裁、APA 引用样式与疗程评估口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="reflexology",
    aliases=(
        "reflexology",
        "反射疗法",
        "足部反射",
        "足疗",
        "Reflexology",
        "Foot Reflexology",
        "足部反射疗法",
        "替代医学",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（疗程设计与评估）", "results（疗效与安全性）", "discussion（机理与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（疗程分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；替代医学研究常用 APA）",
    reporting_standards={
        "k1": "替代医学研究须遵循 CONSORT 扩展规范",
        "k2": "系统综述须遵循 PRISMA 声明",
        "k3": "病例报告须遵循 CARE 指南",
    },
    conventions=(
        "疗程参数（频率、时长、手法）须完整报告",
        "评估量表与评分标准须说明",
        "对照设计与随机化须报告",
        "安全性与不良反应须报告",
        "统计量给出 M/SD 与 95% CI",
    ),
    key_venues=(
        "Journal of Alternative and Complementary Medicine",
        "Journal of Bodywork and Movement Therapies",
        "Manual Therapy",
        "Evidence-Based Complementary and Alternative Medicine",
        "Complementary Therapies in Medicine",
    ),
    units_and_formulas_notes=(
        "疗程时长用 min",
        "频率用 次/周",
        "疼痛评分用 VAS（mm）",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Excel", "R", "Stata", "SAS", "JMP", "NVivo", "Qualtrics", "Tableau", "Power BI", "MATLAB", "Python", "Reflexology Chart Software", "Foot Mapping Software", "Reflexology Diagram Tool", "Reflexology Chart Generator", "Reflexology Assessment Tool", "Reflexology Training Software", "Reflexology Practice Manager", "Endnote"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
