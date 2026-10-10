"""垃圾污水处理学科论文支持：焚烧、填埋、生化处理与资源化技术建模注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="refusesewage_disposal",
    aliases=(
        "refusesewage_disposal",
        "垃圾污水处理",
        "废弃物处理",
        "污水处理",
        "Refuse Sewage Disposal",
        "Wastewater Treatment",
        "Waste Disposal",
        "Waste Management"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与处理问题）",
            "methodology（工艺设计/建模方法）",
            "results（污染物去除与性能数据）",
            "discussion（工程与环保意义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（厂区与工艺）",
            "analysis（去除效率与稳定性）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（工艺与污染控制基础）",
            "evidence synthesis（技术比较与趋势）",
            "future directions",
            "references"
        ),
    },
    citation_style="Elsevier 样式（Water Research 遵循编号制）",
    reporting_standards={
        "wastewater_treatment": "污水试验须报告进水/出水 COD、BOD、SS、NH3-N 与去除率",
        "landfill_monitoring": "填埋气与渗滤液须报告监测频次与点位分布",
        "sludge_treatment": "污泥处置须报告含水率、热稳定性与资源化产品指标"
    },
    conventions=(
        "SI 单位：COD/BOD mg/L；SS mg/L；氨氮 mg/L",
        "BOD 负荷 kg/(m³·d)；HRT、SRT、SVI 首次出现须给出定义",
        "出水达标等级须注明标准（GB 18918、GB 8978 等）",
        "能量与成本核算须报告单位体积/单位垃圾",
        "对比研究须在同一进水水质或同一处理规模比较"
    ),
    key_venues=(
        "Water Research",
        "Water Science and Technology",
        "Environmental Science & Technology",
        "Waste Management",
        "Water Environment Research"
    ),
    units_and_formulas_notes=(
        "COD、BOD、SS、氨氮单位 mg/L；pH 无量纲",
        "去除率 = (C_in - C_out)/C_in × 100%",
        "BOD 负荷 kg/(m³·d)；HRT = V/Q（h）",
        "生化需氧量 BOD5 = 5 日生物需氧量"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("BioWin", "GPS-X", "EPANET", "SWMM", "MODFLOW", "PHREEQC", "MIKE SHE", "InfoWorks ICM", "Autodesk Civil 3D", "MATLAB", "PyMuSiC", "BioWin Activated Sludge Model", "COD Tester", "BOD Incubator", "Nessler Reagent (氨氮)", "XRF Analyzer", "GC-MS", "DCS (分布式控制系统)", "Water Quality Instrument", "Gas Analyzer (CH4/CO2)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
