"""兽医科学学科论文支持：动物科学生产性能与动物健康研究体裁、Vancouver 引用与生产度量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="veterinary_sciences",
    aliases=("veterinary sciences", "兽医科学", "动物科学", "animal sciences",
             "动物生产", "livestock science", "畜牧科学", "poultry science"),
    paper_types={
        "research": (
            "structured abstract",
            "introduction（生产问题与研究假设）",
            "methods（设计、动物群、处理、结局指标）",
            "results（基线表、生产性能与动物健康）",
            "discussion（生产外推性与经济效益）",
            "references",
        ),
        "trial": (
            "abstract",
            "introduction",
            "animal and treatments（动物与处理）",
            "feeding and management（饲养与管理）",
            "results（生产性能与体况）",
            "discussion（营养与生产意义）",
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
    citation_style="Vancouver（AJVR/Preventive Veterinary Medicine 体例）",
    reporting_standards={
        "trial": "ARRIVE 2.0 / CONSORT-animal",
        "cohort": "STROBE",
        "systematic_review": "PRISMA",
        "animal_research": "ARRIVE 2.0",
        "nutrition": "营养试验报告规范",
    },
    conventions=(
        "动物伦理：IACUC/伦理委员会批准号；遵循 3R 原则",
        "动物群描述完整：品种、年龄、性别、体重、饲养管理",
        "试验设计预先注册：随机化、盲法、分组",
        "生产性能指标定义明确：日均增重、料重比等",
        "动物福利与人道终点预先定义并报告",
    ),
    key_venues=(
        "Journal of Animal Science",
        "Poultry Science",
        "Animal Feed Science and Technology",
        "Animal Production Science",
        "Journal of Animal Physiology and Animal Nutrition",
    ),
    units_and_formulas_notes=(
        "体重给 kg；日均增重 ADG 给 g/d",
        "饲料转化率 FCR 给 kg/kg（料/重）",
        "产蛋率给 % 或枚/日；产蛋重给 g",
        "乳量给 kg/d；乳脂率给 %",
        "死亡率给 % 或 per 1000 animal-days",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "MATLAB", "动物遗传分析仪", "动物代谢分析仪", "动物营养分析仪", "动物繁殖分析仪", "动物行为分析仪", "动物生长分析仪", "动物健康分析仪", "动物生产分析仪", "动物环境分析仪", "动物免疫分析仪", "动物生化分析仪", "动物血气分析仪", "动物基因测序仪", "动物超声诊断仪", "动物X射线机", "动物内窥镜", "动物电子手术刀"),
    category="农学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
