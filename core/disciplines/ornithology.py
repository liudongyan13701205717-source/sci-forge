"""鸟类学学科论文支持：鸟类生态/鸟类行为体裁、Wiley 引用样式与鸟类学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ornithology",
    aliases=("ornithology", "鸟类学", "鸟类生态学", "avian ecology", "鸟类行为学",
             "avian behavior", "鸟类保护", "bird conservation", "鸟类迁徙", "bird migration"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与鸟类类群）",
            "materials and methods（野外调查与数据分析）",
            "results（生态/行为数据）",
            "discussion（进化与保护意义）",
            "references",
        ),
        "field": (
            "abstract",
            "introduction",
            "methods（样线/样点、环志、遥测）",
            "results（种群与分布数据）",
            "discussion（管理建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题/类群综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Wiley 样式（作者-年份；Ibis 遵循 Wiley 规范）",
    reporting_standards={
        "survey_methods": "调查方法（样线、样点、计数）与努力量须报告",
        "site_info": "研究地点、坐标与生境类型须完整",
        "marking_methods": "环志/标记（彩环、GPS）方法须报告",
        "ethics": "动物伦理与许可（环志许可）须给出",
        "statistics": "统计检验与样本量须给出",
    },
    conventions=(
        "学名用斜体（Parus major），首次出现给出命名人",
        "行为观测定义（ethogram）须给出",
        "种群密度用 只/km^2 或 只/km",
        "迁徙术语（breeding、wintering、stopover）统一",
        "IUCN 保护等级（LC、VU、EN）规范引用",
    ),
    key_venues=(
        "Ibis",
        "Journal of Avian Biology",
        "The Auk (Ornithology)",
        "The Condor (Ornithological Applications)",
        "Animal Behaviour",
        "Bird Conservation International",
    ),
    units_and_formulas_notes=(
        "密度用 只/km^2；距离用 km/m",
        "时间用 min/h；日期用标准格式",
        "公式用 amsmath；存活率与种群模型公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SE 与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "R (unmarked)",
        "鸟声录音仪（声学记录仪）",
        "GPS 卫星定位器",
        "双筒望远镜",
        "环志工具与 Mist-NET",
    ),
    category="理学",
    databases=(
        "OpenAlex",
        "PubMed",
        "Zenodo",
        "Crossref",
    ),
)