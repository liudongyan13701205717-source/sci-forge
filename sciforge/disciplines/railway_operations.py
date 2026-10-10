"""铁道运营学科论文支持：调度/信号/运营优化体裁、GB/T 引用样式与运营参数记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="railway_operations",
    aliases=(
        "railway_operations",
        "铁道运营",
        "铁路运营",
        "铁路调度",
        "Railway Operations",
        "Rail Operations",
        "列车调度",
        "铁路信号",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与运营问题）", "methodology（模型与算法）", "results（调度结果与性能）", "discussion（机理与运营意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（调度分析与运营评估）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714 样式（中国文献规范）与英文文献采用数字编号",
    reporting_standards={
        "k1": "调度模型须遵循 ETCS 与 CBTC 信号规范",
        "k2": "运营仿真须遵循 RailCom 数据格式",
        "k3": "系统综述须遵循 PRISMA 声明",
    },
    conventions=(
        "列车运行图须标注时间窗与运行区间",
        "闭塞区间与信号系统须说明",
        "仿真参数与假设须报告",
        "运营指标（周转时间、通过能力、准点率）须给出",
        "安全边界须明确",
    ),
    key_venues=(
        "Transportation Research Part B",
        "IET Railways",
        "Journal of Rail and Rapid Transit",
        "European Journal of Operational Research",
        "Transportation Research Part E",
    ),
    units_and_formulas_notes=(
        "运行时间用 s 与 min",
        "通过能力用 列/h",
        "速度用 km/h",
        "统计量给出 M/SD 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Thales Rail Vision", "Siemens RailCom", "Bombardier Movim", "Alstom Rail Operations", "Hitachi Rail Operations", "RailWorks (Autosim)", "Train Simulator (Dovetail)", "EuroSignal", "ETCS Level 2", "CBTC", "RailCom SCADA", "RailSim", "Rivet", "RailPlan", "Athena Dispatch", "RailTraffic", "OptiTwin", "SimRail", "MATLAB", "Python (SimPy)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
