"""灌溉技术学科论文支持：田间水分管理、喷灌、滴灌与水分利用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="irrigation_techniques",
    aliases=("irrigation techniques", "灌溉技术", "田间水分管理", "喷灌", "滴灌", "微灌", "水分利用效率", "灌溉调度"),
    paper_types={
        "research": ("abstract", "introduction（问题与作物、土壤背景）", "methodology（田间试验与传感器网络）", "results（水分、产量与 ET 结果）", "discussion（推广与调度）", "references"),
        "case_study": ("abstract", "introduction", "case description（地块、作物与灌溉系统）", "analysis（水分平衡与产量评估）", "results（发现与对比）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（作物水分需求理论）", "evidence synthesis（多区域灌溉证据）", "future directions", "references"),
    },
    citation_style="ASCE 与 ASABE 样式（编号引用）或 GB/T 7714",
    reporting_standards={
        "k1": "试验设计（作物、灌溉制度、复数）给完整",
        "k2": "传感器位置、频率与校准说明",
        "k3": "产量、水分、ET 指标定义清晰",
    },
    conventions=(
        "水量平衡公式（ET 等于 P 加 I 减 ΔS 减 D 减 R）给符号定义",
        "灌溉频次与水量分别给",
        "土壤水势（kPa 或 bar）与体积含水量（%）区分",
        "作物水分生产函数给参数",
        "传感器精度与误差给出"
    ),
    key_venues=(
        "Agricultural Water Management",
        "Irrigation Science",
        "Journal of Irrigation and Drainage Engineering",
        "Agronomy",
        "Agricultural Systems"
    ),
    units_and_formulas_notes=(
        "水量以 mm 或 m³/ha，ET0 以 mm/日",
        "土壤含水率以 % 体积或 % 质量",
        "水势以 kPa，渗漏水势区分",
        "产量 t/ha 或 kg/ha"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AquaCrop", "CROPWAT", "ETMapper", "SOILWAT", "HYDRUS-1D", "SWAP", "RZW2D", "MODFLOW", "OpenET", "FAO-56 Penman-Monteith Calculator", "Neutron moisture probe", "Capacitive soil moisture sensor", "Pressure transducer", "Weighing lysimeter", "Bowen ratio system", "Eddy covariance", "MODIS-16A2", "ArcGIS", "MATLAB", "Python"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
