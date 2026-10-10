"""军事工业学科论文支持：军事装备、防务系统与作战技术的研究、案例与综述体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="military_and_defence",
    aliases=("military_and_defence", "军事工业", "防务", "国防", "military_industry", "defence_industry", "armament", "munitions", "military_equipment", "weapons_systems", "combat_operations"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（装备/系统与技术方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（装备或作战案例）", "analysis（性能与效能分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（军事装备与防务技术综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"k1": "装备性能测试遵循 GJB / MIL 系列标准", "k2": "作战效能评估遵循效能建模与不确定度报告规范", "k3": "保密内容须按安全审查要求处理"},
    conventions=("装备型号须按保密要求使用代号或脱敏名称", "试验条件与场地须注明", "效能指标须给出计算方法与不确定度", "作战想定须说明边界条件与假设", "结果须附样本量与重复性验证"),
    key_venues=("Journal of Defence Management and Policy", "Defence Technology", "Military Technology", "中国军事科学", "国防科技大学学报"),
    units_and_formulas_notes=("速度用 m/s 或 km/h；用度（°）标注方位", "质量用 t；功率用 kW 或 MW", "概率性指标用置信区间表示", "公式用 amsmath；效能评估须标注模型假设与适用域"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "SIMULINK", "Python (NumPy, SciPy)", "GAMBIT", "SLEP", "MOSADEF", "MIL-STD models", "OPENSIM", "ARTEMIS", "MILSIM", "PHOENIX", "JNETSIM", "GROM", "MIL-STD TEST equipment", "EQUIPMENT TEST bench", "SENSOR calibration system", "BALLISTIC range", "RANGE instrumentation", "LIDAR", "Radar simulator"),
    category="军事学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
