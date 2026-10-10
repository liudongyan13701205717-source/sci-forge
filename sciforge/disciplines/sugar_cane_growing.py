"""Sugar cane growing 学科论文支持：甘蔗种植/田间管理/品种改良/糖料生产。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sugar_cane_growing",
    aliases=(
        "sugar_cane_growing", "Sugar cane growing", "甘蔗种植",
        "甘蔗栽培", "甘蔗生产", "糖料甘蔗",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与种植问题）",
            "methods（田间试验设计与参数）",
            "results（产量与含糖量数据）",
            "discussion（机理与推广意义）",
            "references",
        ),
        "field_trial": (
            "abstract",
            "introduction",
            "methods（随机区组设计与小区面积）",
            "results（品种比较与农艺性状）",
            "discussion（品种评价与推广建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="农业科学样式（作者-年份；中国农学会期刊规范）",
    reporting_standards={
        "field_trial": "田间试验须报告设计（随机区组/拉丁方）、小区面积、重复数与田间位置",
        "variety_evaluation": "品种评价须报告生育期、农艺性状与含糖量测定方法",
        "yield_trial": "产量试验须报告采样时间、方法（鲜重/折干重）与误差",
        "pest_management": "病虫害管理须报告监测方法、防治指标与药剂剂量",
    },
    conventions=(
        "甘蔗品种名称须按国际命名规范书写",
        "产量用 t/ha；含糖量用 %（Brix）",
        "田间试验须报告小区编号与随机化方案",
        "气象数据须注明站点与时间范围",
        "土壤参数须注明采样深度与测定方法",
    ),
    key_venues=(
        "Crop Science",
        "Agricultural Water Management",
        "Sugar Tech",
        "Field Crops Research",
        "中国糖料作物学报",
    ),
    units_and_formulas_notes=(
        "产量用 t/ha；含糖量用 %（Brix）",
        "种植面积用 ha；株高用 cm",
        "灌溉水量用 m³/ha；肥料用量用 kg/ha",
        "气象数据：温度 °C；降水 mm；日照 h",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("甘蔗脱叶剂（草甘膦/敌草快）", "甘蔗收割机（约翰迪尔）", "糖厂制糖设备", "甘蔗糖分检测（阿贝折光仪）", "土壤养分速测仪", "无人机遥感监测", "甘蔗品种鉴定软件", "甘蔗田间管理 GIS 平台", "滴灌/喷灌系统", "甘蔗病虫害监测（性诱剂）", "甘蔗生长模拟模型（APSIM-Sugar）", "甘蔗基因组测序仪（Illumina）", "甘蔗组织培养设备", "甘蔗茎径/含糖量在线检测系统", "甘蔗田间物联网传感器", "甘蔗收割作业效率监测", "甘蔗糖厂糖度分析系统", "甘蔗水分测定仪", "甘蔗田间杂草识别系统（深度学习）", "甘蔗产量预测模型（随机森林）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
