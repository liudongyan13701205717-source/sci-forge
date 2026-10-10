"""烟草加工学科论文支持：烟叶调制/配方优化体裁、Tobacco Science 样式与烟草加工记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="tobacco_processing",
    aliases=("tobacco_processing", "烟草加工", "烟叶调制", "卷烟工艺", "烟草化学",
             "tobacco processing", "tobacco chemistry", "leaf curing", "blend formulation"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与烟草加工问题）",
            "materials and methods（烟叶与加工参数）",
            "results（化学成分与感官评价）",
            "discussion（工艺优化与机理）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（品种/工艺案例）",
            "analysis（配方优化与品控）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="ACS 样式（数字编号，期刊缩写遵循 CASSI）",
    reporting_standards={
        "sample_specification": "烟叶品种、部位、产地与调制方式须明确",
        "chemical_analysis": "化学成分检测遵循国标方法（GB/T）",
        "sensory_evaluation": "感官评价遵循卷烟评吸规范",
        "repeatability": "检测重复数≥3，数据报告均值±标准差",
    },
    conventions=(
        "烟叶品种用栽培品种名标注（如 K326）",
        "化学成分单位：总糖用 g/100g，氮用 %",
        "焦油量单位 mg/支，烟气烟碱用 μg/支",
        "调制方式（烤烟/晒烟/晾烟）须注明",
        "感官评分标准（如国标的 9 分制）须声明",
    ),
    key_venues=(
        "Tobacco Science",
        "Journal of Agricultural and Food Chemistry",
        "Tobacco Research International",
        "Nicotine & Tobacco Research",
        "Food Chemistry",
    ),
    units_and_formulas_notes=(
        "化学成分：总糖 g/100g，总氮 %，总糖碱比无量纲",
        "焦油量 mg/支，烟气烟碱 μg/支",
        "水分含量单位 %",
        "公式用 amsmath 排版；感官评分须报告评分员数量与平均得分",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("总糖测定仪", "总氮测定仪", "水分测定仪", "气相色谱仪（GC）", "液相色谱-质谱联用仪（LC-MS）", "近红外光谱仪（NIR）", "烟气分析仪（ISO 方法）", "卷烟评吸杯", "恒温恒湿箱", "精密电子天平", "匀浆机", "索氏抽提器", "旋转蒸发仪", "烘箱", "振荡器", "pH 计", "电导率仪", "分光光度计", "SPSS", "Origin Pro"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
