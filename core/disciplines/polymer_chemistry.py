"""高分子化学学科论文支持：聚合物合成/高分子物理体裁、ACS 引用样式与高分子记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="polymer_chemistry",
    aliases=("polymer chemistry", "高分子化学", "聚合物科学", "polymer science",
             "高分子物理", "polymer physics", "高分子合成", "polymer synthesis",
             "材料化学", "materials chemistry"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与聚合物体系）",
            "results and discussion（合成、表征与性能）",
            "conclusion",
            "experimental section（单体、聚合与表征）",
            "references",
        ),
        "synthesis": (
            "abstract",
            "introduction",
            "polymerization（聚合方法与条件）",
            "characterization（分子量、结构与组成）",
            "properties（热学、力学或光学性质）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按聚合方法/材料类型综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份；Macromolecules 遵循 ACS 规范）",
    reporting_standards={
        "molecular_weight": "分子量（M_n、M_w、PDI）须报告测定方法（GPC/SEC）与标准",
        "polymerization_details": "聚合条件（引发剂、温度、时间、转化率）须完整",
        "structural_characterization": "结构表征（NMR、IR、元素分析）须给出",
        "thermal_properties": "热学性质（T_g、T_m、T_d）须报告测量方法（DSC/TGA）",
        "reproducibility": "关键聚合与表征须足以复现",
    },
    conventions=(
        "分子量符号 M_n（数均）、M_w（重均）、PDI = M_w/M_n 统一",
        "聚合物命名与重复单元结构式须给出",
        "GPC 数据注明溶剂、柱与标样（如 PS 标样）",
        "热学转变温度（T_g、T_m）标注升温速率",
        "共聚物组成用摩尔分数或质量分数注明",
    ),
    key_venues=(
        "Macromolecules",
        "Journal of the American Chemical Society",
        "Angewandte Chemie International Edition",
        "ACS Macro Letters",
        "Polymer Chemistry",
        "Progress in Polymer Science",
    ),
    units_and_formulas_notes=(
        "分子量用 g/mol 或 kDa；浓度用 mol/L 或 wt%",
        "温度用 °C 或 K（T_g 常用 °C）",
        "公式用 amsmath；聚合度与分子量关系式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值与误差（如 M_n = 45.2 kDa, PDI = 1.12）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("Python (NumPy/SciPy)", "MATLAB", "Origin", "ChemDraw", "LaTeX"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "Semantic Scholar", "CNKI"),
)