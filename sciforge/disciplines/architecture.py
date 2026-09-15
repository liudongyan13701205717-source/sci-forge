"""建筑学论文支持：建筑设计研究、建成环境性能、建成后评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="architecture",
    aliases=("architecture", "building", "built environment", "建筑学",
             "建筑", "城市设计", "urban design"),
    paper_types={
        "research": ("abstract", "introduction", "context and literature", "methodology",
                     "case analysis", "findings", "design implications", "references"),
        "performance": ("abstract", "introduction", "building description", "measurement campaign",
                        "simulation setup", "results", "recommendations", "references"),
        "design_study": ("design brief", "site analysis", "design strategy", "drawings/renders",
                         "technical resolution", "reflection", "references"),
    },
    citation_style="作者-年份（IEEE/Elsevier 系均可）",
    reporting_standards={
        "performance": "实测给仪器（热舒适仪/声级计/照度计）型号与标准（ASHRAE 55/ISO 7730）",
        "simulation": "能耗模拟给软件（EnergyPlus/IDA-ICE）版本、气象文件（TMY/EPW）与校准（NMBE/CV(RMSE)）",
        "survey": "建成后评估（POE）给问卷量表与样本量；统计检验报告",
        "drawings": "图纸给比例尺与指北针；渲染区分真实照片与效果表现",
    },
    conventions=(
        "平面/剖面/立面图组完整；技术详图节点标注",
        "热舒适指标（PMV/PPD/UTCI）定义与计算输入说明",
        "声学给混响时间 RT60 与噪声级 dB(A)；采光给照度 lux 与 DGP",
        "可持续指标（LEED/绿建三星）引用具体得分项",
    ),
    key_venues=(
        "Building and Environment",
        "Energy and Buildings",
        "Automation in Construction",
        "Journal of Architectural Education",
        "Frontiers of Architectural Research",
    ),
    units_and_formulas_notes=(
        "能耗 kWh/m²·yr；照度 lux；声压级 dB(A)；温度 °C",
        "窗墙比 WWR %；体形系数；热阻 R 值或 U 值 W/m²·K",
    ),
)
