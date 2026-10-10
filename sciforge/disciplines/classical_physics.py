"""Classical Physics 学科论文支持：力学/电磁学/热力学经典理论。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="classical_physics",
    aliases=(
        "Classical Physics", "经典物理学", "Classical Mechanics", "经典力学",
        "Classical Electrodynamics", "经典电动力学", "Classical Thermodynamics",
        "经典热力学", "经典物理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="Springer LNCS / IOP Journal Style",
    reporting_standards={
        "units": "所有量须标注 SI 单位；非 SI 单位须给换算系数",
        "uncertainty": "实验结果须附不确定度（A 类/B 类合成标准不确定度）",
        "references": "文献引用须含 DOI；经典教材须注明版次与章节",
        "reproducibility": "实验参数（温度、磁场、激光功率）须完整可复现",
        "notation": "矢量/张量标记全文统一；微分符号（d/dt）须一致",
    },
    conventions=(
        "使用国际单位制（SI），所有量纲一致；非 SI 单位须声明换算关系",
        "矢量用粗体或箭头标记；张量用多指标（下标/上标）",
        "力学/电磁学/热力学方程独立编号，全文引用一致",
        "单位随数值给出，单位符号斜体或正体须统一",
        "图形使用 SI 单位、图例与坐标轴标签完整，误差棒须显式标注",
    ),
    key_venues=(
        "American Journal of Physics",
        "European Journal of Physics",
        "Reports on Progress in Physics",
        "Annual Review of Fluid Mechanics",
        "Journal of Applied Mechanics",
        "Physical Review Letters",
    ),
    units_and_formulas_notes=(
        "力学：力用 N；能量用 J；角速度用 rad/s；转动惯量用 kg·m²",
        "电磁学：电荷用 C；电场强度用 V/m；磁感应强度用 T；电阻用 Ω",
        "热力学：熵用 J/K；比热容用 J/(kg·K)；热导率用 W/(m·K)",
        "公式用 amsmath 排版；矢量标记（粗体或箭头）全文统一",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "译文", "报告", "数据集"),
    tools=("COMSOL Multiphysics", "MATLAB", "Mathematica", "Maple", "GNU Octave", "OpenFOAM", "VPython", "Manim", "PhET Simulations", "GeoGebra", "gnuplot", "ROOT", "SciPy", "Matplotlib", "Jupyter Notebook", "LaTeX", "TikZ", "Plotly", "Desmos", "Wolfram Alpha"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv"),
)
