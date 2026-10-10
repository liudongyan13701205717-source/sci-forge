"""药理学与药学学科论文支持：药物发现/制剂/临床体裁、ACS/AJPC 引用样式与药学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pharmacology_and_pharmaceutical_sciences",
    aliases=("pharmacology and pharmaceutical sciences", "药理学与药学",
             "drug discovery", "pharmaceutics", "medicinal chemistry",
             "药物研发", "新药研发", "药学", "药物化学", "制剂学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与目标）",
            "methodology（实验设计与方法）",
            "results（合成/表征/活性数据）",
            "discussion（机制与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例或药物案例）",
            "analysis（分析与评价）",
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
    citation_style="ACS 样式（ACS 期刊规范；作者-年份或数字）",
    reporting_standards={
        "synthesis": "合成路线遵循 IUPAC 命名与条件报告",
        "bioanalytical": "LC-MS/MS 方法验证遵循 FDA/EMA 指南",
        "pk": "药代数据遵循 CONSORT 扩展",
        "formulation": "制剂遵循 ICH Q6/Q7 指南",
        "clinical": "临床试验遵循 ICH-GCP 与 CONSORT",
        "adme": "ADME 研究须报告清除率、半衰期与代谢物",
    },
    conventions=(
        "药物名称用 INN 通用名；化学名遵循 IUPAC",
        "单位规范（ng/mL、μM、mg/kg、AUC ng·h/mL）",
        "化合物结构式给出 SMILES/分子式",
        "给药方案与剂量须表列",
        "结构-活性关系（SAR）用表格与图示",
    ),
    key_venues=(
        "Journal of Medicinal Chemistry",
        "Journal of Pharmaceutical Sciences",
        "Molecular Pharmaceutics",
        "European Journal of Pharmaceutical Sciences",
        "Pharmaceutical Research",
        "Drug Design, Development and Therapy",
    ),
    units_and_formulas_notes=(
        "浓度 mol/L（μM/nM）；剂量 mg/kg",
        "药代：Cmax、AUC、t½、CL、Vd 给几何均值",
        "合成产率用 %；溶解度 mg/mL",
        "结构式与分子式须给出；SAR 用表格",
        "公式用 amsmath",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ChemDraw 化学绘图画", "MarvinSketch（ChemAxon）", "AutoDock 分子对接", "Schrödinger Glide 分子对接", "MOE（Chemical Computing）", "ADMET Predictor", "SimCyp Simulator", "HPLC（Thermo Dionex）", "LC-MS/MS（Waters Xevo TQ-S）", "GC-MS（Agilent 7890）", "溶出仪（Hanson）", "DSC 差示扫描量热仪", "TGA 热重分析仪", "FTIR 红外光谱仪", "XRD 衍射仪", "高通量筛选平台（HTS, Hitachi）", "GraphPad Prism", "SPSS 统计", "ZINC 化合物库", "冷冻干燥机（冻干制剂）"),
    category="医学",
    databases=("PubMed", "Crossref", "PubChem", "ChEMBL", "DrugBank", "CNKI", "DrugBank 药物数据库"),
)
