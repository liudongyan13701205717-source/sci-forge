"""正畸学学科论文支持：错颌畸形病因、矫治机理与临床试验规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="orthodontics",
    aliases=(
        "orthodontics",
        "正畸学",
        "Orthodontics",
        "口腔正畸",
        "咬合矫治",
        "错颌畸形",
        "Orthodontics and Dentofacial Orthopedics",
        "隐形矫治",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与假设）",
            "methodology（样本与矫治方案）",
            "results（矫治效果结果）",
            "discussion（机理与讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例与检查描述）",
            "analysis（方案设计分析）",
            "results（矫治结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与系统综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver（国际口腔期刊）/ GB/T 7714（中文）",
    reporting_standards={
        "clinical_trial": "CONSORT 声明",
        "diagnostic_test": "STARD 声明",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "样本纳入排除标准须列出",
        "头影测量参数须给出误差与可靠性",
        "正畸力值以 N 或 N/cm 报告",
        "疼痛/舒适度量表（VAS/NRS）标注",
        "试验须在 ClinicalTrials.gov 注册",
    ),
    key_venues=(
        "American Journal of Orthodontics and Dentofacial Orthopedics",
        "European Journal of Orthodontics",
        "Angle Orthod",
        "Progress in Orthodontics",
        "China Journal of Orthodontics",
    ),
    units_and_formulas_notes=(
        "矫治力以 N 报告（0.5–3.0 N 常用）",
        "头影测量误差须给出 ICC 与 Dahlberg 公式",
        "疼痛评分 VAS 0–10",
        "统计学用 t 检验/Mann-Whitney/卡方，α=0.05",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CEPH-Nometrics（头影测量）", "CephMatis（头影分析）", "Dolphin 3D（口腔数字化）", "iTero Element 5D（口扫）", "Insignia（Invisalign 计划）", "CBCT Scanner (iCat)（锥形束 CT）", "Photoshop（图像调整）", "SPSS 26（统计分析）", "R（统计与可视化）", "Excel（数据整理）", "Origin（绘图）", "EndNote（文献）", "LaTeX（排版）", "T-Scan（咬合压力）", "Myo-monitor 2（肌电）", "Naled（数字化种植设计）", "Formlabs SLA Printer（矫治器打印）", "SofSprint（口扫软件）", "Vocal Video Analysis (Ludwig)", "CBM / CephNavi 正畸软件"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
