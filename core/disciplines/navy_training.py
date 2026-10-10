"""海军训练学科论文支持：军事训练/海上演习/指挥仿真体裁、军事学/Chicago 样式与训练记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="navy_training",
    aliases=("navy_training", "海军训练", "maritime training", "naval exercises",
             "海军演习", "海上训练", "naval exercise", "marine training", "海军指挥"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与海军训练问题）", "methodology（训练设计与评估）", "results（训练效果与数据）", "discussion（军事启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（演习/训练案例背景）", "analysis（组织与指挥分析）", "results（效果评估）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（训练体系与理论综述）", "evidence synthesis（训练实证综合）", "future directions", "references"),
    },
    citation_style="军事学/Chicago 样式（作者-年份）",
    reporting_standards={
        "training_design": "训练体系设计须遵循军事训练学规范与演习脚本说明",
        "simulation": "指挥仿真训练须报告模型参数与验证流程",
        "evaluation": "训练效果评估须遵循效标参照与信度分析规范",
    },
    conventions=(
        "演习与训练等级（一级/二级/三级/综合演习）须给出与出处",
        "指挥体系与军种缩写（AN/DE/AF/NATO 等）首次给出全称",
        "涉密内容须脱密并给出脱密声明",
        "训练脚本时间线与阶段划分须明确",
        "效果指标（战果、损耗、伤亡、达成率）须定义与来源",
    ),
    key_venues=(
        "Naval War College Review",
        "Joint Force Quarterly",
        "The RUSI Journal",
        "Journal of Strategic Studies",
        "Defense Studies",
    ),
    units_and_formulas_notes=(
        "伤亡与损耗用人数/数量、时间用 s/min/h、距离用 km/海里",
        "公式用 amsmath；战果与损耗计算式须完整",
        "仿真结果给出置信区间与运行次数并说明假设",
        "评估量表给出评分范围、维度与信度系数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Naval Combat Simulator", "Ship Simulator", "E-3 Simulator", "VR Training System", "ECDIS Trainer", "Weapon Training Simulator", "Gun Training System", "Missile Training Simulator", "E3C System", "MARISIM", "NATO STANAG", "Tactica", "Maritime Exercise Simulator", "Naval Command Training System", "Combat Management Trainer", "Underwater Sonar Trainer", "Drone Simulator", "UxO Trainer", "Live Fire Range", "Live Vessel Training System"),
    category="军事学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
