"""化学工程（与过程控制/绿色化学）学科论文支持：过程控制/生命周期评价/过程安全体裁与引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chemical_engineering_and",
    aliases=(
        "chemical engineering and",
        "process control",
        "process optimization",
        "bioprocess",
        "green chemistry",
        "process safety",
        "过程控制",
        "过程优化",
        "生物过程工程",
        "绿色化学",
        "过程安全",
        "过程工程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（过程问题与优化目标）",
            "materials and methods（过程模型、实验与控制策略）",
            "results（性能、控制与经济性数据）",
            "discussion（机理与适用性）",
            "conclusions",
            "references",
        ),
        "process": (
            "abstract",
            "introduction",
            "process model and simulation（过程建模与模拟）",
            "control and optimization（控制策略与优化）",
            "environmental and safety assessment（环境与安全性评价）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "taxonomy（按过程类型/控制方法分类）",
            "state of the art",
            "challenges and outlook",
            "references",
        ),
    },
    citation_style="Industrial & Engineering Chemistry Research 样式（ACS）",
    reporting_standards={
        "control": "过程控制须报告被控变量、操纵变量与 PID 参数",
        "economics": "经济性评价须说明贴现率、基准年与情景假设",
        "lca": "环境影响须按 LCA 边界报告（GB/T 24040 / ISO 14040）",
        "safety": "过程安全须给出 HAZOP/LOPA 摘要与 SIL 等级",
        "kinetics": "反应器动力学须注明标准状态与置信区间",
    },
    conventions=(
        "过程控制须报告被控变量、操纵变量与 PID 参数",
        "经济性评价须说明贴现率、基准年与情景假设",
        "环境影响须按 LCA 边界报告（GB/T 24040 / ISO 14040）",
        "过程安全须给出 HAZOP/LOPA 摘要与 SIL 等级",
        "反应器动力学须注明标准状态与置信区间",
    ),
    key_venues=(
        "Industrial & Engineering Chemistry Research",
        "AIChE Journal",
        "Chemical Engineering Science",
        "Computers & Chemical Engineering",
        "Control Engineering Practice",
        "Journal of Process Control",
    ),
    units_and_formulas_notes=(
        "温度用 K 或 ℃；压力用 kPa 或 MPa",
        "反应速率用 mol/(L·s)；转化率用 %",
        "经济性用 NPV/IRR；LCA 指标用 kg CO₂e 等功能单位",
        "引用控制参数须注明采样周期与控制器类型",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Aspen Plus", "Aspen HYSYS", "ChemCAD", "Aspen Custom Modeler", "Aspen Dynamics 动态模拟", "MATLAB Simulink", "Siemens PCS 7 过程控制系统", "SimaPro 生命周期评估", "OpenLCA 生命周期评估", "反应器动力学测试仪", "催化剂评价装置", "过程数字孪生平台", "换热网络优化软件", "HAZOP/LOPA 安全分析工具", "过程强化技术平台", "反应工程软件", "过程控制仿真软件", "生物反应器（Eppendorf Biostat）", "绿色化学指标计算软件", "过程安全风险评估平台"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
