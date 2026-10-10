"""建筑维护（Building maintenance）：设施管理、资产评估与预测性维护研究方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="building_maintenance",
    aliases=("building_maintenance", "建筑维护", "Building maintenance",
             "facilities management", "设施管理", "property maintenance",
             "asset management", "建筑资产管理", "predictive maintenance"),
    paper_types={
        "research": (
            "abstract",
            "introduction（设施背景与维护问题）",
            "methodology（CMMS 数据、传感器数据与预测模型说明）",
            "results（寿命预测、成本、可用率/MTBF 指标）",
            "discussion（维护策略对比：预防性 vs 预测性 vs 故障后）",
            "conclusion",
            "references",
        ),
    },
    citation_style="Elsevier 样式（FM/资产管理期刊主流）",
    reporting_standards={
        "data_source": "说明数据来源（CMMS、BMS、IoT 传感器）与时间跨度；缺失值处理写明",
        "model": "预测模型（PHM/机器学习）给特征工程、训练/验证划分与指标（RMSE、F1）",
        "cost_analysis": "维护成本按功能分区（IFM 标准）与资产类别拆分；通货膨胀调整至基准年",
        "asset_condition": "资产状态评级给评分体系（如 RICS 建筑状态评级 1-5）",
    },
    conventions=(
        "设备类型（电梯、空调机组、消防泵）与数量在首段交代；研究范围明确",
        "MTBF/MTTR 给定义与统计窗口；传感器给量程、采样频率与校准周期",
        "结论按「策略建议」与「方法贡献」分层；成本效益给基准对比",
    ),
    key_venues=(
        "Facilities and Construction Management",
        "Journal of Facility Management",
        "Building & Environment（建筑性能方向）",
        "Journal of Building Engineering",
        "International Journal of Production Research（预测维护）",
        "Building Simulation (Springer)",
    ),
    units_and_formulas_notes=(
        "MTBF/MTTR 给单位（h）；能耗 kWh/kWh·m²·yr；可用率 %（窗口内）",
        "传感器数据给采样频率与量程；模型给特征数量与缺失率",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Autodesk Revit", "Navisworks", "Facility Focus (FM)", "Diligent (FM software)", "IBM Maximo", "SAP EAM", "Custix", "UpKeep", "Hippo", "Fiix", "Python (pandas/scikit-learn)", "R (data.table)", "SPSS", "Stata", "PowerBI", "Tableau", "Grafana", "InfluxDB", "Azure IoT Hub", "MQTT (EMQ X)", "QGIS", "Blender", "Ladybug Tools", "EnergyPlus", "e3Viz"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Scopus"),
)
