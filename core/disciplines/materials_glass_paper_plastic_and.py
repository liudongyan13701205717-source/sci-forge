"""材料（玻璃/纸/塑料及其他）学科论文支持：日用材料加工与性能对比研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="materials_glass_paper_plastic_and",
    aliases=("glass paper plastic and", "玻璃纸塑料及", "玻璃纸塑料及其他",
             "日用材料加工", "日用高分子加工", "日用材料综合",
             "日用材料", "日用化工材料加工"),
    paper_types={
        "research": ("abstract", "introduction（材料—加工—应用关系）", "methodology（配方、工艺与表征）", "results（性能评估）", "discussion（工程化与优化）", "references"),
        "case_study": ("abstract", "introduction", "case description（材料/制品/工艺）", "analysis（工艺与性能分析）", "results", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（材料分类）", "evidence synthesis", "future directions", "references"),
    },
    citation_style="编号（Polymer Engineering & Science 风格）",
    reporting_standards={
        "formulation": "配方与工艺参数须给出，保证可复现",
        "characterization": "测试遵循 ASTM/ISO 并标注条件",
        "reproducibility": "重复测试次数与不确定度须报告",
    },
    conventions=(
        "样品命名清晰反映配方与工艺",
        "热/力学/光学/阻隔性能分组给出",
        "对比表包含本文与文献值并给出出处",
        "缩写首次出现给出全称",
        "图表标注单位与重复次数",
    ),
    key_venues=(
        "Polymer Engineering & Science",
        "Journal of Applied Polymer Science",
        "Applied Clay Science",
        "Express Polymer Letters",
        "Packaging Technology and Science",
    ),
    units_and_formulas_notes=(
        "温度 ℃；密度 g/cm³；熔融指数 g/10min",
        "强度 MPa；弹性模量 GPa；伸长率 %",
        "透光率 %；雾度 %；接触角 °",
        "透湿率 g/m²·24h；O2 透过率 cm³/m²·24h·atm",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("挤出机", "注塑机", "热压机", "吹塑机", "熔融指数仪", "DSC 差示扫描量热仪", "TGA 热重分析仪", "FTIR 红外光谱", "SEM 扫描电镜", "冷冻断口分析", "万能材料试验机", "耐折/撕裂强度仪", "雾度计（BYK）", "接触角仪", "O2 透过率仪", "水蒸气透过率仪", "Origin Pro", "Python (NumPy/SciPy)", "Microsoft Excel", "LaTeX/BibTeX"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
