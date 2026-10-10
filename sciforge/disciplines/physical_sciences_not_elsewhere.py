"""其他自然科学学科论文支持：非主流自然科学体裁、IEEE 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="physical_sciences_not_elsewhere",
    aliases=("physical_sciences_not_elsewhere", "其他自然科学", "physical sciences n.e.c.",
             "未分类自然科学", "unclassified physical science", "其他理科", "其他自然科学门类"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与科学问题）",
            "methodology（实验/观测/计算方法）",
            "results（数据与量化结论）",
            "discussion（机理与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（体系/事件描述）",
            "analysis（过程与机理）",
            "results（结果与不确定性）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（学科理论综述）",
            "evidence synthesis（关键实验/观测综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号制；期刊规范优先）",
    reporting_standards={
        "units": "一律使用 SI 单位制",
        "constants": "基本物理常数引用 CODATA 2022 推荐值",
        "uncertainty": "测量结果按 GUM 表示（±、置信水平、分量）",
        "data_availability": "数据可用性声明须给出 DOI",
        "statistics": "拟合优度、系统误差与自由度须显式给出"
    },
    conventions=(
        "量符号斜体、单位符号正体；矢量/张量用粗斜体",
        "缩写首次出现给出全称；装置/探测器名用首字母大写",
        "图表自含：caption 可独立阅读，须给出工况",
        "理论曲线与数据点同图对比时注明误差棒含义",
        "首次出现的效应/定律给出引用"
    ),
    key_venues=(
        "Nature",
        "Science",
        "Physical Review Letters",
        "PRL X",
        "Nature Physics",
        "Reviews of Modern Physics"
    ),
    units_and_formulas_notes=(
        "能量/质量常用自然单位制（ℏ=c=1）时必须在首次出现处声明换算因子",
        "大/小数值用科学计数法或 SI 词头（µ、n、G），全文一致",
        "公式编号仅对被引用者编号；方程变量在随后一句中定义",
        "光谱/能级以 cm⁻¹ 或 eV 表示并注明零点约定",
        "派生单位按 SI 导出单位书写（rad、T）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Python (NumPy/SciPy)", "MATLAB", "COMSOL Multiphysics", "R", "SPSS", "Origin", "LaTeX", "Python (Pandas)", "Google Sheets", "QGIS", "Zemax OpticStudio", "Gaussian", "NWChem", "Wolfram Mathematica", "OriginPro", "NIST WebBook", "CODATA Constants Database", "Semantic Scholar", "Zotero", "ANSYS Fluent"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Zenodo"),
)
