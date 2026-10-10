"""体操学科论文支持：动作技术、生物力学分析、评分规则与运动损伤研究的方法与报告注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="gymnastics",
    aliases=("gymnastics", "体操", "竞技体操", "artistic gymnastics", "动作评分", "event scoring", "生物力学分析", "biomechanics", "运动表现"),
    paper_types={
        "research": ("abstract", "introduction（技术或表现研究动机）", "methodology（运动员、动作与采集方法）", "results（角度、角速度、评分与损伤）", "discussion（技术要点与训练启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（运动员、队伍与训练阶段）", "analysis（动作阶段与生物力学链）", "results（难度分、完成分与成绩变化）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（体操运动学与评分规则）", "evidence synthesis（技术训练与损伤文献综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"rules": "评分按 FIG Code of Points 版本与适用年号标注", "ethics": "涉及未成年运动员研究须取得监护同意并匿名化处理", "motion_capture": "采样频率、标记点方案与滤波参数须报告"},
    conventions=("难度分与完成分按 FIG 版本分别报告（如 FIG Code of Points 2022–2024）", "角度用 °，角速度用 °/s，速度用 m/s", "动捕数据须给出采样频率（Hz）与低通滤波截止频率", "损伤按部位、类型与恢复时长（d）记录", "术语首次出现给出中英文对照"),
    key_venues=("Sports Biomechanics", "Journal of Applied Biomechanics", "International Journal of Sports Physiology and Performance", "Medicine & Science in Sports & Exercise", "体育科学"),
    units_and_formulas_notes=("角度用 °；角速度用 °/s；位移与速度用 m 与 m/s", "地面反作用力用 N（或按 N/kg 归一化）；压力用 kPa", "采样频率用 Hz；力板与动捕采样率须报告", "公式用 LaTeX（amsmath）；关节角度按矢量大小编号引用"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Gymnova GymMaster", "Duffner", "Vogtle", "Vicon Vantage", "OptiTrak", "Qualisys Track Manager", "Xsens MVN", "Delsys Trigno EMG", "Kistler Force Plates", "Tekscan Pressure Plates", "Kinovea", "SportsTracker", "Vantage Motion", "Catapult GPS", "Teammetrics 16", "BTS SprintTimer", "SiS Quest", "MySportPulse", "Momentum International", "Pak-T"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
