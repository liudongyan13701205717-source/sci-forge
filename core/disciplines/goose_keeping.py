"""养鹅学科论文支持：鹅群饲养/繁殖/管理体裁、农学引用样式与鹅养殖记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="goose_keeping",
    aliases=("goose keeping", "养鹅", "鹅群饲养", "鹅类管理", "鹅繁殖", "鹅群健康", "鹅类生产"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（设计与种群）", "results（生产与健康）", "discussion（机理与意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（鹅场描述）", "analysis（管理分析）", "results（生产结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（鹅类生物学）", "evidence synthesis（饲养综述）", "future directions", "references"),
    },
    citation_style="JAS/农学作者-年份样式（养鹅与家禽学通用）",
    reporting_standards={"k1": "饲养实验须记录饲料/密度/管理", "k2": "健康评估遵循 ARRIVE", "k3": "生产记录须交代周期与群体"},
    conventions=("鹅品种/品系须明确", "饲养密度与光照须报告", "饲料配方须列明", "健康指标须说明方法", "生产参数须可复现"),
    key_venues=("Poultry Science", "World's Poultry Science Journal", "Archives of Animal Nutrition", "Journal of Applied Poultry Research", "Animal Production Science"),
    units_and_formulas_notes=("生产指标以 g/d 与只/天表示", "公式用 amsmath，FCR 计算须明确", "数值结果给均值 ± SD 与样本量", "周期以周/月计"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("鹅群体重电子秤（feed system）", "鹅群产蛋率记录（egg counter）", "鹅群健康监测（veterinary）", "鹅群饲料配方软件（feed formulation）", "鹅群密度监测（IR sensor）", "鹅群产蛋质量（egg quality）", "鹅群羽毛质量（feather quality）", "鹅群繁殖记录（breeding log）", "鹅群遗传评估（BLUP）", "鹅群饲养记录（management log）", "鹅群生产记录（production log）", "鹅群营养评估（nutrient analysis）", "鹅群环境控制（HVAC system）", "鹅群照明控制（lighting system）", "鹅群饮水系统（water system）", "鹅群饲料分析（proximate analysis）", "鹅群性能记录（performance log）", "鹅群疫苗接种记录系统", "鹅群胴体评估设备", "鹅群水质分析仪"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "家禽饲养数据库（PoultryBase）", "鹅群健康数据库（health DB）", "鹅群遗传数据库（genetic DB）"),
)
