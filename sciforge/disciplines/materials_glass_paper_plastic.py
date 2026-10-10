"""材料（玻璃/纸/塑料）学科论文支持：日用材料加工、成型与性能表征。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="materials_glass_paper_plastic",
    aliases=("glass paper plastic", "玻璃纸塑料", "日用材料", "软包装",
             "软包装工程", "日用化工材料", "包装材料", "日用高分子"),
    paper_types={
        "research": ("abstract", "introduction（材料-性能-应用目标）", "methodology（配方与成型工艺）", "results（物理化学/热学/力学/阻隔性能）", "discussion（应用评价与优化方向）", "references"),
        "case_study": ("abstract", "introduction", "case description（材料与制品）", "analysis（工艺与质量分析）", "results（性能与失效评估）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（材料体系与分类）", "evidence synthesis（跨应用性能对比）", "future directions", "references"),
    },
    citation_style="编号（Journal of Applied Polymer Science 风格）",
    reporting_standards={
        "formulation": "配方给出各组分 wt%、牌号和供应商",
        "processing": "工艺给出温度、时间、压力、速度、模具规格",
        "characterization": "力学/热学/光学测试给 ASTM/ISO 标准编号与条件",
    },
    conventions=(
        "样品命名按配方+工艺组合给出（如 F50/220℃-3min）",
        "热性能以 Tg、Tm、Td 标注并给出加热速率",
        "阻隔性能给 OTR/WVTR 测试条件（%RH、温度、膜厚）",
        "光学/力学数据给重复次数与平均值±标准差",
        "缩写首次出现给出全称（如 PET、PP、HDPE）",
    ),
    key_venues=(
        "Journal of Applied Polymer Science",
        "Polymer Testing",
        "Packaging Technology and Science",
        "Glass Technology",
        "Applied Clay Science",
    ),
    units_and_formulas_notes=(
        "温度 ℃；压力 MPa；密度 g/cm³；熔融指数 g/10min",
        "热性能 Tg/Tm/Td 单位 ℃；DSC 给出 J/g 与加热速率",
        "阻隔性 OTR cm³/m²·24h·atm；WVTR g/m²·24h",
        "力学强度 MPa；弹性模量 GPa；伸长率 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("挤出机（ZSK/单螺杆）", "注塑机（Engel/Arburg）", "吹塑机", "滚涂机", "热压机", "熔融指数仪（ASTM D1238）", "差示扫描量热仪（DSC）", "热重分析仪（TGA）", "万能材料试验机", "耐折/撕裂强度仪", "雾度计（BYK）", "接触角测量仪", "O2 透过率仪（SY-G3）", "水蒸气透过率仪（SY-W3）", "透射电镜（TEM）", "红外光谱（FTIR）", "Origin Pro", "Python (NumPy/SciPy)", "Microsoft Excel", "LaTeX/BibTeX"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
