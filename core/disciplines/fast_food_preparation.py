"""快餐制作学科论文支持：食品加工、标准化操作与卫生安全体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fast_food_preparation",
    aliases=(
        "fast_food_preparation", "快餐制作", "快餐业",
        "fast food", "快餐烹饪",
        "quick service", "即时服务餐饮", "食品标准化", "餐饮操作",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（食品安全与工业化背景）",
            "methodology（实验设计、工艺参数、卫生检测）",
            "results（品质与安全性数据）",
            "discussion（标准化与产业意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（连锁餐饮品牌案例）",
            "analysis（工艺流程与管理体系）",
            "results（案例发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（快餐食品安全研究综述）",
            "evidence synthesis（现有研究与缺口）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式",
    reporting_standards={
        "haccp": "食品安全遵循 HACCP 体系报告规范",
        "food_safety": "食品检测遵循 ISO 22000 食品安全管理体系",
        "sensory": "感官评价遵循 ISO 4120 食品感官检验规范",
        "sop": "标准操作程序须完整描述",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "温度单位统一用 °C；时间用秒或分钟注明",
        "食品添加剂标注 INS 编号与使用量",
        "微生物检测报告 CFU/g 并注明检测方法",
        "工艺流程图须注明关键控制点（CCP）",
        "营养成分标注遵循 GB 28050 标准",
    ),
    key_venues=(
        "Food Control",
        "Journal of Food Science",
        "Intervention in Food Science",
        "Food Control",
        "Journal of the Science of Food and Agriculture",
    ),
    units_and_formulas_notes=(
        "温度用 °C；水分活度 Aw；pH 值",
        "微生物用 CFU/g 或 CFU/mL",
        "营养成分 g/100g 或 kJ/100g",
        "食品添加剂用量 g/kg 或 ppm",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("HACCP 食品安全管理系统", "温度记录仪（数据记录探针）", "ATP 荧光检测仪", "金属探测器", "电子秤（高精度）", "油炸温度控制器", "商用冰箱温度监测", "水分活度仪", "菌落计数仪", "食品安全快速检测箱", "厨房操作系统（POS）", "食品安全管理软件", "Excel", "SPSS", "Python（pandas）", "R", "Minitab", "Power BI", "Tableau", "Endnote"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
