"""药理学学科论文支持：药理基础/临床体裁、ASPET/JPET 引用样式与药理学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pharmacology",
    aliases=("pharmacology", "药理学", "基础药理学", "临床药理学",
             "clinical pharmacology", "药代动力学", "药效学", "临床药学",
             "drug discovery", "pharmacology research"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与药理问题）",
            "methodology（实验设计与模型）",
            "results（药效与药代数据）",
            "discussion（机理与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例描述）",
            "analysis（药物分析与干预）",
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
    citation_style="ASPET/JPET 样式（作者-年份；JPET 遵循 ASPET 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "preclinical": "临床前研究遵循 ARRIVE 指南",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "pharmacokinetics": "药代研究遵循 CONSORT 药代扩展",
        "dose_response": "剂量-反应研究须报告 EC₅₀/IC₅₀",
        "clinical_report": "临床报告遵循 CARE 声明",
    },
    conventions=(
        "药物名称用国际非专利名（INN）",
        "剂量单位（mg/kg、μmol/L）须规范",
        "药代参数（AUC、Cmax、t½）缩写首次出现给出全称",
        "受体/靶点命名（IUPHAR）须规范",
        "动物实验伦理与 ARRIVE 合规须声明",
    ),
    key_venues=(
        "Journal of Pharmacology and Experimental Therapeutics",
        "British Journal of Pharmacology",
        "Molecular Pharmacology",
        "Pharmacological Reviews",
        "Clinical Pharmacology & Therapeutics",
        "Nature Reviews Drug Discovery",
    ),
    units_and_formulas_notes=(
        "浓度用 mol/L（μM/nM）；剂量用 mg/kg",
        "公式用 amsmath；EC₅₀/IC₅₀ 与药代计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "药代参数给出中位数与范围",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("GraphPad Prism 剂量-反应分析", "SPSS 统计", "R 与 Bioconductor", "Phoenix WinNonlin 药代动力学", "NONMEM 群体药代", "MATLAB 药代建模", "OriginPro 作图", "AutoDock 分子对接", "Schrödinger Glide 分子对接", "ChemDraw 化学绘图画", "ZINC 化合物库", "PatchClamp 电生理仪（Axon AxoPatch）", "LC-MS/MS（Waters Xevo TQ-S）", "荧光定量 PCR（QuantStudio）", "微流控器官芯片（Emulate）", "高通量筛选平台（Hitachi HTS）", "Bio-Rad 细胞读数仪", "MetaboAnalyst 代谢组学平台", "细胞培养箱（CO2 恒温）", "酶标仪（ELISA 定量）"),
    category="医学",
    databases=("PubMed", "OpenAlex", "PubChem", "ChEMBL", "CNKI", "DrugBank", "ChEMBL 化合物数据库", "DrugBank 药物数据库"),
)
