"""动物学学科论文支持：动物分类/动物行为体裁、Wiley 引用样式与动物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="zoology",
    aliases=("zoology", "动物学", "动物分类学", "animal taxonomy", "动物行为学",
             "animal behavior", "动物生理学", "animal physiology", "无脊椎动物学", "invertebrate zoology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与动物类群）",
            "materials and methods（采集、饲养与观测）",
            "results（形态/行为/生理数据）",
            "discussion（进化与生态意义）",
            "references",
        ),
        "taxonomic": (
            "abstract",
            "introduction",
            "materials and methods（标本与测量）",
            "taxonomic treatment（新种描述与检索表）",
            "discussion（系统关系）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按类群/主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Wiley 样式（作者-年份；J. Zool. 遵循 Wiley 规范）",
    reporting_standards={
        "specimen_info": "标本数量、采集地点与保藏机构须报告",
        "animal_husbandry": "饲养条件（温度、光照、食物）须完整",
        "measurement_methods": "形态测量与行为观测方法须报告",
        "ethics": "动物伦理审批与福利声明须给出",
        "statistics": "统计检验与样本量须给出",
    },
    conventions=(
        "学名用斜体（Danio rerio），首次出现给出命名人",
        "形态测量术语与缩写（TL、SL、BW）统一",
        "行为观测定义（ethogram）须给出",
        "地理坐标与采集日期规范记录",
        "新种描述遵循 ICZN 命名法规",
    ),
    key_venues=(
        "Journal of Zoology",
        "Zoological Journal of the Linnean Society",
        "Journal of Experimental Biology",
        "Animal Behaviour",
        "Biological Journal of the Linnean Society",
        "Zoomorphology",
    ),
    units_and_formulas_notes=(
        "体长用 mm/cm；体重用 g",
        "温度用 °C；时间用 h/min",
        "公式用 amsmath；异速生长与行为指标公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SE 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "R (lme4)",
        "Python (NumPy/SciPy)",
        "野外 GPS 定位追踪器",
        "体视显微镜",
        "行为观测摄像系统",
    ),
    category="理学",
    databases=(
        "PubMed",
        "OpenAlex",
        "bioRxiv",
        "Zenodo",
    ),
)