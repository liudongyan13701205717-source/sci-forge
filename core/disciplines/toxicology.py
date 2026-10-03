"""毒理学学科论文支持：毒理基础/风险评估体裁、SOT/Toxicological Sciences 引用样式与毒理学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="toxicology",
    aliases=("toxicology", "毒理学", "毒理", "毒物学", "风险评估",
             "risk assessment", "毒理研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与毒理问题）",
            "methods（暴露方案与模型）",
            "results（毒性终点与剂量反应）",
            "discussion（机理与风险评估）",
            "references",
        ),
        "risk_assessment": (
            "abstract",
            "introduction",
            "methods（暴露评估与剂量外推）",
            "results（风险表征）",
            "discussion（不确定性与建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="SOT/Toxicological Sciences 样式（作者-年份；Toxicol Sci 遵循 SOT 规范）",
    reporting_standards={
        "preclinical": "毒理研究遵循 ARRIVE 指南",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "dose_response": "剂量-反应研究须报告 NOAEL/LOAEL",
        "in_vitro": "体外研究遵循 OECD 测试指南",
    },
    conventions=(
        "毒性终点（LD₅₀、NOAEL、LOAEL）定义须明确",
        "暴露途径（经口/吸入/经皮）须报告",
        "剂量单位（mg/kg/day）须规范",
        "物种与品系（大鼠 SD 等）须注明",
        "风险评估术语（TDI、RfD）首次出现给出全称",
    ),
    key_venues=(
        "Toxicological Sciences",
        "Toxicology and Applied Pharmacology",
        "Chemical Research in Toxicology",
        "Archives of Toxicology",
        "Environmental Health Perspectives",
        "Journal of Applied Toxicology",
    ),
    units_and_formulas_notes=(
        "剂量用 mg/kg/day；浓度用 mg/m³ 或 ppm",
        "公式用 amsmath；LD₅₀ 与剂量外推计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "剂量-反应曲线给出拟合参数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("高效液相色谱仪（HPLC）", "质谱仪", "SPSS", "R"),
    category="医学",
    databases=("PubMed", "OpenAlex", "PubChem", "Europe PMC", "CNKI"),
)