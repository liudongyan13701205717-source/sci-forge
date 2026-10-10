"""谷物种植学科论文支持：谷物栽培/品种/管理体裁、作物学引用样式与谷物种植记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="grain_growing",
    aliases=("grain growing", "谷物种植", "谷类作物", "谷物栽培", "水稻种植", "小麦种植", "玉米种植"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（设计与田块）", "results（产量与品质）", "discussion（机理与意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（田块描述）", "analysis（栽培分析）", "results（产量结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（作物学理论）", "evidence synthesis（栽培综述）", "future directions", "references"),
    },
    citation_style="Crop Science/作物学作者-年份样式（谷物种植与作物学通用）",
    reporting_standards={"k1": "栽培实验须记录品种/密度/管理", "k2": "田间试验遵循 DARR", "k3": "产量记录须交代面积与周期"},
    conventions=("谷物品系/品种须明确", "种植密度与灌溉须报告", "施肥制度须列明", "产量指标须说明方法", "栽培参数须可复现"),
    key_venues=("Crop Science", "Field Crops Research", "Agronomy Journal", "Journal of Experimental Agriculture", "Plant and Soil"),
    units_and_formulas_notes=("产量以 t/ha 表示，密度以株/m²", "公式用 amsmath，WRUE 计算须明确", "数值结果给均值 ± SD 与样本量", "周期以天/季计"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("谷物产量测量（combine harvester）", "谷物品质分析（nitrogen test）", "谷物土壤传感器（soil probe）", "谷物灌溉系统（irrigation system）", "谷物施肥记录（fertilizer log）", "谷物田间密度（plot density）", "谷物转基因检测（PCR）", "谷物遗传评估（BLUP）", "谷物田间试验（DARR protocol）", "谷物遥感监测（Sentinel-2 NDVI）", "谷物田间记录（field log）", "谷物土壤分析（proximate analysis）", "谷物田间管理（management log）", "谷物灌溉控制（HVAC system）", "谷物施肥分析（nutrient analysis）", "谷物田间性能（performance log）", "谷物产量模拟（APSIM）", "谷物收割机产量监测系统", "谷物病虫害监测陷阱", "谷物水分测定仪"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "谷物产量数据库（CropBase）", "谷物品种数据库（VarmBase）", "谷物遗传数据库（genetic DB）"),
)
