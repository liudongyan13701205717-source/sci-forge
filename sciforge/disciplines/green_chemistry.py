"""绿色化学学科论文支持：绿色合成与过程优化研究、绿色指标体系与 ACS 报告规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="green_chemistry",
    aliases=("green_chemistry", "绿色化学", "可持续化学", "sustainable chemistry", "绿色合成", "green synthesis", "原子经济性", "atom economy", "可再生原料"),
    paper_types={
        "research": ("abstract", "introduction（研究背景与可持续性动机）", "methodology（合成路线、反应条件与表征）", "results（产率、绿色指标与产物）", "discussion（与常规方法的对比）", "references"),
        "case_study": ("abstract", "introduction", "case description（实验室或工业放大场景）", "analysis（物料流、能耗与废物分析）", "results（E 因子、PMI、原子经济性）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（绿色化学 12 原则）", "evidence synthesis（策略与应用文献综合）", "future directions", "references"),
    },
    citation_style="ACS 样式",
    reporting_standards={"green_metrics": "E 因子、PMI、原子经济性须给出计算式与所用质量数据", "solvent": "溶剂名称与用量须报告，溶剂-free 或水、生物基溶剂须注明", "waste": "废物组成、催化剂回收次数与能量输入须说明"},
    conventions=("绿色化学 12 原则须在引言处引用（Anastas & Warner, 1998）", "E 因子与 PMI 无量纲，定义须在正文给出", "反应式排版统一，产物表征须标注仪器条件", "催化剂负载以 mmol/g 或 wt% 报告", "可再生原料须注明来源"),
    key_venues=("Green Chemistry", "ACS Sustainable Chemistry & Engineering", "ChemSusChem", "Green Synthesis and Catalysis", "Journal of Cleaner Production"),
    units_and_formulas_notes=("温度 °C；压力 bar；产率 %；浓度 mol/L", "E 因子 = 废物质量 / 产物质量（无量纲）；PMI = 全部输入 / 产物（无量纲）", "原子经济性 = 目标产物摩尔质量 / 反应物总摩尔质量 × 100%", "公式用 LaTeX（amsmath）；行内式避免复杂分式"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("CHEM21", "CHEMKIN Pro", "Cantera", "ChemDraw", "Gaussian 16", "ORCA", "ADF", "VMD", "GAMMA", "GreenLab Studio", "Aspen Plus", "ProEx", "ChemSep", "Agilent 1260 Infinity", "Bruker Avance", "Shimadzu GC-2030", "Thermo Fisher Q-Exactive", "Origin", "Python (NumPy/SciPy)", "LaTeX"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
