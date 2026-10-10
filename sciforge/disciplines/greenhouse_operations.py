"""温室作业学科论文支持：设施栽培的环境调控、水肥一体化与作物生长监测的方法与数据规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="greenhouse_operations",
    aliases=("greenhouse_operations", "温室作业", "设施栽培", "protected cultivation", "水肥一体化", "fertigation", "环境调控", "climate control", "温室自动化"),
    paper_types={
        "research": ("abstract", "introduction（设施栽培问题与研究动机）", "methodology（温室结构、环境设定与处理设计）", "results（产量、品质与能耗）", "discussion（环境因子与栽培管理的影响）", "references"),
        "case_study": ("abstract", "introduction", "case description（温室规模、作物与茬口）", "analysis（气候、水肥与遮阳策略分析）", "results（产量与资源消耗）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（设施环境物理与作物生理）", "evidence synthesis（控制策略与传感器文献综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"climate_setpoints": "温度、湿度、CO₂ 与 DLI 的设定值与实测波动须报告", "fertigation": "EC、pH、施肥频次与总养分输入须报告", "energy": "能耗按季节与单位面积（kWh/m²）报告"},
    conventions=("温室内气候变量按高度（冠层、叶面）分别记录", "EC 单位用 mS/cm；pH 报告为无单位数值", "辐照用 DLI（mol/m²·d）与瞬时辐照度（μmol/m²·s）区分", "作物生长指标按叶面积指数（LAI）与干重报告", "传感器位置、型号与采样频率须标明"),
    key_venues=("Acta Horticulturae", "Scientia Horticulturae", "Computers and Electronics in Agriculture", "HortScience", "Frontiers in Plant Science"),
    units_and_formulas_notes=("温度 °C；相对湿度 %；CO₂ ppm；辐照 μmol/(m²·s)", "DLI 用 mol/(m²·d)", "灌溉量 mm 或 L/m²；EC 用 mS/cm", "公式用 LaTeX（amsmath）；产量 kg/m²；能耗 kWh/m²"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Priva EcoControl", "Hortisense", "Andritz ClimateControl", "Van Meuwen", "Netafim HydroNet", "Rain Bird", "Decagon ECH2O", "Decagon PR-2", "Onset HOBO SSM3", "CropX NetStation", "GrowFlow Control", "Green Office", "Spectrum Crop", "AgriSense", "Sensirion SHT4x", "Delta-T Deltamax 2", "AquaCount EC-50", "Nelson & Sons", "Fluke Ti120", "Flir E8 Pro"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
