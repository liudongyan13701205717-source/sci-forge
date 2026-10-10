"""肉类加工学科论文支持：肉品工艺、品质控制与食品安全评价规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="meat_processing",
    aliases=("meat processing", "肉类加工", "肉品加工", "肉品工艺",
             "肉品安全", "肉品品质", "肉品保藏", "肉品化学",
             "肉类食品", "肉品生物技术", "meat science"),
    paper_types={
        "research": ("abstract", "introduction（肉品加工/品质/安全目标）", "methodology（原料、工艺参数、感官/理化/微生物检测）", "results（感官评分/理化指标/微生物计数）", "discussion（机理、优化与货架期评估）", "references"),
        "case_study": ("abstract", "introduction", "case description（肉品类型与加工工艺）", "analysis（工艺缺陷与品质分析）", "results（货架期与安全评估）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（肉品化学与工艺分类）", "evidence synthesis（跨工艺品质对比）", "future directions", "references"),
    },
    citation_style="编号（Journal of Food Science 风格）",
    reporting_standards={
        "raw_material": "原料来源、屠宰方式、成熟时间、初始品质须明确",
        "processing_parameters": "工艺参数（温度/时间/压力/湿度）须完整列出",
        "quality_testing": "感官/理化/微生物测试遵循 AOAC/ISO 标准并给条件",
    },
    conventions=(
        "肉品命名按品种+部位+加工方式（如猪里脊-水煮-冷却）",
        "货架期研究须设定明确终点（感官/微生物/理化/综合）",
        "微生物计数以 CFU/g 或 CFU/mL 表示，给培养条件",
        "感官评价给评价员人数、培训方案与统计方法",
        "色度值以 CIE L*a*b* 表示",
    ),
    key_venues=(
        "Journal of Food Science",
        "Meat Science",
        "Food Chemistry",
        "LWT - Food Science and Technology",
        "Journal of Muscle Foods",
    ),
    units_and_formulas_notes=(
        "温度 ℃；水分活度 aw（无量纲）；pH 无量纲",
        "微生物计数 CFU/g 或 CFU/mL；菌落总数、大肠菌群、沙门氏菌等",
        "硬度/嫩度以 N 或 kPa；剪切力按 Textron 标准",
        "保质期以天/周/月表示，给储存温度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("高温灭菌锅", "真空包装机", "低温冷却库", "滚筒式烟熏炉", "绞肉机/斩拌机", "注射机", "滚揉机", "色度计（Minolta CR-400）", "水分活度仪（Aqualab）", "便携式 pH 计", "肉嫩度仪（Textron）", "脂肪测定仪（索氏抽提）", "微生物培养箱", "ATP 荧光检测仪", "HACCP 管理系统", "SPSS", "R 统计软件", "Microsoft Excel", "LaTeX/BibTeX", "Origin Pro"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
