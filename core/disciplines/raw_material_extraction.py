"""原材料开采学科论文支持：采矿/钻探/爆破体裁、GB/T 引用样式与采矿参数记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="raw_material_extraction",
    aliases=(
        "raw_material_extraction",
        "原材料开采",
        "采矿",
        "露天开采",
        "Raw Material Extraction",
        "Mining",
        "钻探",
        "爆破",
    ),
    paper_types={
        "research": ("abstract", "introduction（地质条件与开采问题）", "methodology（开采方案与工艺）", "results（监测数据与数值分析）", "discussion（机理与工程意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（矿井简介与开采条件）", "analysis（工艺与监测）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714 样式（中国文献规范）与英文文献采用数字编号",
    reporting_standards={
        "k1": "开采方法须遵循 GB 50215《煤矿井下安全规程》与采矿安全规范",
        "k2": "爆破须遵循 GB 6722《爆破安全规程》",
        "k3": "系统综述须遵循 PRISMA 声明",
    },
    conventions=(
        "矿体参数（品位、厚度、埋深、倾角）须给出具体数值",
        "开采方法须按分类体系标注（长壁/房柱/露天/地下）",
        "钻探参数（孔径、进尺、钻速）须报告",
        "爆破参数（孔距、装药量、雷管类型）须给出",
        "回收率与贫化率须标注",
    ),
    key_venues=(
        "International Journal of Mining Science and Technology",
        "Mining Science and Technology",
        "International Journal of Rock Mechanics and Mining Sciences",
        "煤炭学报",
        "采矿与安全工程学报",
    ),
    units_and_formulas_notes=(
        "矿体厚度与埋深用 m",
        "品位用 % 或 g/t",
        "开采强度用 万t/年",
        "回收率与贫化率用 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Caterpillar CAT 797", "Komatsu HD8050", "Liebherr T264", "Sandvik", "Epiroc", "Atlas Copco", "Blastmate", "Surpac", "Datamine", "Maptek VDR", "Maptek VMi", "Maptek GEM", "Micromine", "Vulcan", "Whisker", "GEMS", "MATLAB", "QGIS", "AutoCAD", "ANSYS"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
