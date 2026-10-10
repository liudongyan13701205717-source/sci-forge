"""药学学科论文支持：药代动力学、制剂开发、药物相互作用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pharmacy",
    aliases=("pharmacy", "pharmaceutics", "pharmaceutical sciences",
             "药学", "制剂", "临床药学", "药代动力学", "药物相互作用",
             "pharmaceutical technology", "药物分析"),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与目标）",
            "methodology（材料与方法）",
            "results（实验结果）",
            "discussion（讨论）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例/案例描述）",
            "analysis（分析与评估）",
            "results（结果与随访）",
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
    citation_style="ACS 或 Vancouver 样式",
    reporting_standards={
        "bioanalytical": "LC-MS/MS 方法验证须符合 FDA/EMA 指南（线性/精密度/回收率）",
        "pk": "非房室/房室模型选择须说明；Cmax、AUC0-t、AUC0-∞、t½、CL 给几何均值±CV",
        "ethics": "临床试验注册号与伦理批件须写明（ICH-GCP）",
        "stability": "稳定性条件（温度/湿度/光照）与取样时间点须列表",
        "interaction": "药物相互作用给机制（CYP450 酶）与临床意义分级",
        "formulation": "制剂遵循 ICH Q6/Q7 指南",
    },
    conventions=(
        "药物名首现用通用名（INN），后续可缩写；浓度单位统一（ng/mL、µM）",
        "给药方案表（剂量/途径/频次/疗程）必须出现",
        "溶出曲线给 f2 相似因子；处方组成用百分比或 mg/片",
        "剂量换算（人与动物）注明依据（体表面积法）",
    ),
    key_venues=(
        "British Journal of Pharmacology",
        "Journal of Pharmaceutical Sciences",
        "Molecular Pharmaceutics",
        "European Journal of Pharmaceutical Sciences",
        "Pharmaceutical Research",
    ),
    units_and_formulas_notes=(
        "AUC 单位 ng·h/mL；清除率 L/h；分布容积 L/kg",
        "溶出度 %；溶解度 mg/mL（注明温度与 pH）",
        "浓度单位统一（ng/mL、µM）",
        "公式用 amsmath",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ChemDraw 化学绘图画", "HPLC（Thermo Dionex）", "AutoDock 分子对接", "溶出仪（Hanson）", "GraphPad Prism", "SPSS 统计", "R 与 Bioconductor", "Phoenix WinNonlin 药代动力学", "NONMEM 群体药代", "MATLAB 建模", "OriginPro 作图", "LC-MS/MS（Waters Xevo TQ-S）", "GC-MS（Agilent 7890）", "DSC 差示扫描量热仪", "TGA 热重分析仪", "FTIR 红外光谱仪", "XRD 衍射仪", "高通量筛选平台", "ZINC 化合物库", "稳定性试验箱（恒温恒湿）"),
    category="医学",
    databases=("PubMed", "Crossref", "PubChem", "CNKI", "DrugBank", "DrugBank 药物数据库"),
)
