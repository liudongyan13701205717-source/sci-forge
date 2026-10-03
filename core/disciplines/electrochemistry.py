"""电化学学科论文支持：电分析/电池与电催化体裁、ACS 引用样式与电化学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electrochemistry",
    aliases=("electrochemistry", "电化学", "电分析", "electroanalysis", "电催化",
             "electrocatalysis", "电池", "batteries", "电化学储能", "electrochemical energy storage"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与电化学体系）",
            "experimental（电极、电解液与仪器）",
            "results（伏安、阻抗或充放电数据）",
            "discussion（机理与性能分析）",
            "conclusion",
            "references",
        ),
        "battery": (
            "abstract",
            "introduction",
            "experimental（电池组装与测试条件）",
            "results（容量、倍率与循环）",
            "discussion（衰减机理）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "fundamentals（电化学原理）",
            "main developments（按材料/应用综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份；J. Electrochem. Soc. 亦可遵循 IOP/ECS 样式）",
    reporting_standards={
        "reference_electrode": "参比电极类型与电位换算（vs. RHE/SHE）须报告",
        "electrolyte": "电解液组成、浓度与溶剂须完整",
        "potential_scale": "电位标度（vs. 参比电极）与换算须明确",
        "cycling_conditions": "充放电测试须报告电流密度、电压窗口与温度",
        "capacity_normalization": "容量归一化基准（质量/面积）须声明",
    },
    conventions=(
        "电位 E 与电流密度 j 符号约定（阳极/阴极）须声明",
        "参比电极缩写（SHE、RHE、Ag/AgCl、SCE）首次出现处给出定义",
        "循环伏安图标注扫描方向与峰电位",
        "阻抗谱用 Nyquist 图，标注等效电路拟合",
        "库仑效率 CE 与能量效率定义须给出",
    ),
    key_venues=(
        "Journal of the Electrochemical Society",
        "Electrochimica Acta",
        "Journal of Power Sources",
        "ACS Energy Letters",
        "Advanced Energy Materials",
        "Analytical Chemistry",
    ),
    units_and_formulas_notes=(
        "电位用 V（vs. 参比电极）；电流密度用 mA/cm^2；容量用 mAh/g",
        "RHE 换算：E_RHE = E_ref + 0.059 × pH（25°C）",
        "公式用 amsmath；Nernst 方程与 Butler-Volmer 方程形式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值与误差（如容量 1200 mAh/g ± 30）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集", "专利"),
    tools=("Python (NumPy/SciPy)", "MATLAB", "Origin", "EC-Lab", "LaTeX"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "Semantic Scholar", "CNKI"),
)