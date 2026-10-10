"""其他农业、兽医与食品科学学科论文支持：交叉学科方法学与报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_agricultural_veterinary_and_food_sciences",
    aliases=(
        "other_agricultural_veterinary_and_food_sciences",
        "其他农业兽医食品科学",
        "Other Agricultural, Veterinary, and Food Sciences",
        "农业交叉学科",
        "兽医交叉学科",
        "食品交叉学科",
        "Rural Development",
        "农业系统",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methodology（方法与材料）",
            "results（结果与分析）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（社会科学向）/ Vancouver（兽医/食品科学向）/ GB/T 7714（中文）",
    reporting_standards={
        "empirical": "农业/食品科学研究规范",
        "systematic_review": "PRISMA 声明",
        "food_safety": "Codex Alimentarius 规范",
        "veterinary_trial": "AVMA 兽医试验规范",
    },
    conventions=(
        "数据来源与采集方法须说明",
        "样本量与抽样方法须报告",
        "统计方法与显著性须给出",
        "交叉学科术语须明确定义",
        "伦理审批与利益冲突须声明",
    ),
    key_venues=(
        "Agricultural Systems",
        "Food Policy",
        "Journal of Food Science",
        "Veterinary Quarterly",
        "中国农业大学学报",
    ),
    units_and_formulas_notes=(
        "面积单位统一 ha 或 km²",
        "产量报告以 t/ha 或 kg/mu",
        "食品污染物浓度用 mg/kg 或 μg/kg",
        "统计量给出 M/SD/95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R（统计与可视化）", "SPSS（统计）", "Stata（面板回归）", "Excel（数据整理）", "Python（Pandas/NumPy）", "Origin（绘图）", "QGIS（地理分析）", "ArcGIS", "EndNote（文献）", "LaTeX（排版）", "Photoshop", "JMP（试验设计）", "HACCP 食品安全管理", "GC-MS（食品残留）", "HPLC（食品分析）", "PCR 兽医诊断", "ELISA Reader", "土壤 EC/pH/Moisture 传感器", "Droplet Digital PCR", "Food Quality Vision Pro"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
