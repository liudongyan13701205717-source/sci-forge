"""光化学学科论文支持：光物理/光催化体裁、ACS 引用样式与光化学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="photochemistry",
    aliases=("photochemistry", "光化学", "光物理", "photophysics", "光催化",
             "photocatalysis", "光敏化", "photosensitization", "光化学合成", "photochemical synthesis"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与光化学过程）",
            "results（光谱、量子产率或产物）",
            "discussion（机理与激发态过程）",
            "experimental section（光源、条件与表征）",
            "references",
        ),
        "mechanistic": (
            "abstract",
            "introduction",
            "photophysical characterization（吸收/发射/瞬态光谱）",
            "mechanistic studies（淬灭、时间分辨与同位素效应）",
            "proposed mechanism（机理图）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "fundamentals（光化学原理）",
            "main developments（按反应类型/应用综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份；J. Am. Chem. Soc. 遵循 ACS 规范）",
    reporting_standards={
        "light_source": "光源类型、波长与功率密度须报告",
        "quantum_yield": "量子产率须报告测定方法与标准物",
        "irradiation_conditions": "辐照时间、波长范围与反应器须完整",
        "transient_spectroscopy": "瞬态光谱须报告激发波长、时间窗口与拟合",
        "actionmetry": "化学/物理光量计校准须说明",
    },
    conventions=(
        "激发态记号（S_0、S_1、T_1）与跃迁类型（π→π*、n→π*）统一",
        "量子产率符号 Φ 与下标（Φ_f、Φ_ISC）规范",
        "吸收/发射光谱标注波长（nm）与摩尔消光系数 ε",
        "Jablonski 图用于说明激发态过程",
        "光催化条件（催化剂负载、光源、溶剂）完整",
    ),
    key_venues=(
        "Journal of the American Chemical Society",
        "Journal of Photochemistry and Photobiology A: Chemistry",
        "Photochemical & Photobiological Sciences",
        "Chemical Reviews",
        "Angewandte Chemie International Edition",
        "Journal of Physical Chemistry A",
    ),
    units_and_formulas_notes=(
        "波长用 nm；能量用 eV（E = 1240/λ[nm] eV）",
        "摩尔消光系数 ε 用 L/(mol·cm)",
        "公式用 amsmath；速率常数与 Stern-Volmer 方程形式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值与误差（如 Φ = 0.85 ± 0.03）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集", "专利"),
    tools=("Python (NumPy/SciPy)", "MATLAB", "Origin", "紫外-可见分光光度计", "纳秒瞬态光谱仪"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "Semantic Scholar", "CNKI"),
)