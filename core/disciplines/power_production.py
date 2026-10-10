"""电力生产学科论文支持：发电燃料优化、机组性能与并网运行研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="power_production",
    aliases=(
        "power production", "电力生产", "发电生产",
        "power generation", "电力生产运营",
        "thermal power plant", "火电厂",
        "generation scheduling", "发电调度",
        "fuel optimization", "燃料管理",
        "power plant efficiency", "机组效率",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（运行问题与生产目标）",
            "methodology（数据采集、建模与优化方法）",
            "results（效率、燃料成本与排放）",
            "discussion（机组适配性与实施建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（机组与生产工况）",
            "analysis（运行参数与偏差诊断）",
            "results（调优前后性能对比）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（热力过程与热力循环理论）",
            "evidence synthesis（节能降碳证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "k1": "机组性能试验按 GB/T 14531 与 IEC 60059 规程报告",
        "k2": "排放数据须注明采样工况、折算氧含量与折算系数",
        "k3": "优化研究须报告约束条件、初值敏感性与时限指标",
    },
    conventions=(
        "供电煤耗以 g/kWh 表示并注明是否含辅助电量",
        "负荷率、等效满负荷小时数须标注统计区间",
        "蒸汽参数注明额定/实际值（MPa、℃）",
        "NOx/SO₂ 以 mg/m³ 折算至 3% 或 6% O₂ 后报告",
        "试验须注明额定负荷比例与连续运行时长",
    ),
    key_venues=(
        "Applied Energy",
        "Energy Conversion and Management",
        "IEEE Transactions on Power Systems",
        "Fuel",
        "International Journal of Thermal Sciences",
    ),
    units_and_formulas_notes=(
        "热效率 η = 发电量 / (标准煤耗量 × 29.27 MJ/kg) × 100%",
        "供电煤耗 = 标准煤耗量 kg / 上网电量 kWh，单位 g/kWh",
        "可用系数/负荷因子须注明容量因子与强迫停运次数",
        "排放强度以 tCO₂/MWh 表示并注明电网排放因子来源",
        "单位成本以元/MWh 表示并注明燃料价与折损口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MatSim 机组仿真平台", "Digsilent DIgSILENT PowerFactory", "MATLAB Simulink", "Python (pandas, scipy)", "SAS", "R (RStudio)", "EXCEL 高级数据建模", "ANSYS Fluent", "COMSOL Multiphysics", "Gatecycle 热力循环分析", "Hemo 热力过程模拟", "OPC 现场总线采集系统", "Siemens PCS-7 DCS", "Emerson DeltaV", "ABB ACS880 变频调速", "Omega 热工量热仪", "Mettler Toledo TOC 分析仪", "Dräger 烟气分析系统", "Hillphoenix 在线监测", "Power BI"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
