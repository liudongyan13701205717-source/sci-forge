"""蔬菜种植学科论文支持：蔬菜栽培与设施园艺体裁、ASA 引用样式与园艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vegetable_plantation",
    aliases=("vegetable plantation", "蔬菜种植", "蔬菜栽培", "蔬菜园艺", "设施蔬菜",
             "vegetable production", "vegetable cultivation", "olericulture"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与栽培问题）",
            "materials and methods（品种、设计与测定）",
            "results（产量、品质与生理数据）",
            "discussion（栽培机理与应用）",
            "references",
        ),
        "field_trial": (
            "abstract",
            "introduction",
            "materials and methods（田间设计、重复与小区）",
            "results（处理间差异与统计）",
            "discussion（适用条件与推广）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="ASA/CSSA 样式（作者-年份；HortScience 遵循 ASHS 规范）",
    reporting_standards={
        "field_trial": "田间试验遵循 ASA/CSSA 农艺试验报告规范",
        "cultivar_evaluation": "品种评价须报告试验点、年份与对照品种",
        "quality_analysis": "品质分析须报告测定方法、仪器与重复数",
        "statistical": "须报告试验设计、重复数与统计检验方法",
    },
    conventions=(
        "蔬菜种类/品种须给出拉丁学名与品种名",
        "产量用 t/ha 或 kg/m² 报告",
        "施肥量用 kg N-P₂O₅-K₂O/ha 报告",
        "栽培方式（露地/设施/水培）须明确",
        "采收期与成熟度判定标准须交代",
    ),
    key_venues=(
        "HortScience",
        "Scientia Horticulturae",
        "Journal of the American Society for Horticultural Science",
        "HortTechnology",
        "Postharvest Biology and Technology",
        "Agronomy Journal",
    ),
    units_and_formulas_notes=(
        "产量用 t/ha 或 kg/m²；单果重用 g",
        "施肥量用 kg/ha；灌溉量用 mm 或 m³/ha",
        "可溶性固形物用 °Brix；酸度用 %",
        "统计量给出均值与标准误；显著性用 P 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("精准播种机 (precision seeder)", "移栽机 (transplanter)", "滴灌系统 (drip irrigation)", "温室气候控制计算机", "土壤 EC/pH 计", "SPAD-502 叶绿素仪", "叶面积指数仪 (LAI-2200)", "便携式光合仪 (LI-6800)", "无人机多光谱相机", "Pix4Dmapper", "GreenSeeker 光谱仪", "土壤养分速测仪", "气象站", "诱虫灯 (insect trap)", "自动灌溉控制器", "收获机械 (harvester)", "冷链设备 (cold chain)", "折光仪 (refractometer)", "R (agricolae)", "SAS"),
    category="农学",
    databases=("AGRIS", "OpenAlex", "Crossref", "CNKI"),
)
