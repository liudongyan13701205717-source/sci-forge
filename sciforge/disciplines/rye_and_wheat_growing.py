"""黑麦与小麦种植学科论文支持：品种、栽培与作物管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="rye_and_wheat_growing",
    aliases=(
        "rye_and_wheat_growing",
        "黑麦小麦种植",
        "麦类作物",
        "cereal crop",
        "wheat",
        "rye",
        "麦类栽培",
        "grain cultivation",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景）",
            "materials and methods（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "field_trial": (
            "abstract",
            "introduction",
            "trial design（试验设计）",
            "materials and methods（材料与试验）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（作物理论综述）",
            "evidence synthesis（试验证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "field_trial": "随机区组或裂区设计须完整；重复数与地块须说明",
        "genetics": "群体、标记与遗传模型须报告",
        "metabolomics": "样本、处理与检测方法须给出",
    },
    conventions=(
        "产量以 t/ha 或 kg/ha 报告；水分 %",
        "生育期按出苗、拔节、抽穗、成熟标记",
        "试验点气候数据（气温、降水）须附于原表",
        "品种名给出品种代码或品种审定编号",
        "化学处理剂量 kg/ha 与处理时间须报告",
    ),
    key_venues=(
        "Field Crops Research",
        "European Journal of Agronomy",
        "Crop Science",
        "Journal of Cereal Science",
        "植物遗传资源学报",
    ),
    units_and_formulas_notes=(
        "土壤养分 N、P、K 以 mg/kg 报告；pH 无量纲",
        "光合速率 μmol·m⁻²·s⁻¹；干物质 g/plant",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Soil Analyzer", "pH Meter", "Soil Moisture Sensor", "Weather Station", "Greenhouse Climatic Controller", "Seed Germination Chamber", "Plant Height Scanner", "Chlorophyll Fluorometer", "Handheld NIR Spectrometer", "Grain Moisture Meter", "Kernel Analyser", "Plant Phenotyping Platform", "Drone with RGB/Spectral Camera", "GIS Software ArcGIS", "R with agronomics packages", "Stata", "SPSS", "DNA Sequencer", "PCR Thermocycler", "Flow Cytometer"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CABI"),
)
