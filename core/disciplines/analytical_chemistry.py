"""分析化学学科论文支持：分离科学/光谱分析体裁、ACS 引用样式与分析化学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="analytical_chemistry",
    aliases=("analytical chemistry", "分析化学", "分离科学", "separation science",
             "色谱", "chromatography", "质谱", "mass spectrometry", "光谱分析", "spectroscopy"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与分析目标）",
            "experimental（仪器、试剂与样品制备）",
            "method development（方法优化与验证）",
            "results（校准、检出限与样品分析）",
            "discussion（方法性能与对比）",
            "conclusion",
            "references",
        ),
        "method_validation": (
            "abstract",
            "introduction",
            "experimental",
            "validation（线性、精密度、准确度、回收率）",
            "application（实际样品应用）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "techniques overview（技术原理与进展）",
            "applications（按样品类型综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份；Anal. Chem. 遵循 ACS 规范）",
    reporting_standards={
        "validation_metrics": "方法验证须报告线性范围、LOD/LOQ、精密度（RSD）与回收率",
        "calibration": "校准曲线须给出方程、R^2 与浓度范围",
        "sample_preparation": "样品制备步骤与试剂纯度须完整",
        "instrument_conditions": "仪器参数（色谱柱、流动相、电离模式）须报告",
        "matrix_effects": "基质效应与干扰须评估",
    },
    conventions=(
        "检出限 LOD 与定量限 LOQ 定义（3σ/10σ 或 S/N）须给出",
        "色谱术语（保留时间、分离度、塔板数）定义统一",
        "质谱 m/z 与电离模式（ESI、APCI、MALDI）标注",
        "浓度单位（ppm、ppb、μg/L、mg/L）须统一并注明换算",
        "不确定度按 GUM 或 EURACHEM 指南报告",
    ),
    key_venues=(
        "Analytical Chemistry",
        "Journal of Chromatography A",
        "Analytica Chimica Acta",
        "Talanta",
        "Analytical and Bioanalytical Chemistry",
        "Mass Spectrometry Reviews",
    ),
    units_and_formulas_notes=(
        "浓度常用 mol/L、μg/L、mg/L；ppm/ppb 使用时注明质量比或体积比",
        "色谱流速用 mL/min；柱温用 °C",
        "公式用 amsmath；校准方程与统计量排版统一",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出有效数字与不确定度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("Python (NumPy/SciPy)", "Origin", "SPSS", "R", "Chromeleon"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "Semantic Scholar", "CNKI"),
)