"""军事学学科论文支持：军事理论、作战指挥与战略研究、案例与综述体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="military_science",
    aliases=("military_science", "军事学", "military_theory", "war_studies", "defence_studies", "strategic_studies", "operational_art", "tactics", "military_history", "military_policy", "military_strategy"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（理论/案例与建模方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（战役/作战案例）", "analysis（作战过程与决策分析）", "results（结论）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（军事理论谱系综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（历史与战略研究常用）",
    reporting_standards={"k1": "战役案例须注明时间、地点与交战方", "k2": "效能评估须遵循效能建模与不确定度报告规范", "k3": "涉密内容须按安全审查要求脱敏处理"},
    conventions=("术语须区分中英与语种差异", "战役/战斗/作战须明确层级", "时间线须以统一时区标注", "引文须标注来源与页码", "结论须区分绝对式与条件式"),
    key_venues=("Journal of Strategic Studies", "Defense Studies", "Military Review", "中国军事科学", "国防经济研究"),
    units_and_formulas_notes=("伤亡率用百分比；时间线以小时/日标注", "装备效能用命中率/摧毁率等指标表示", "概率性指标须附置信区间", "公式用 amsmath；模拟须标注假设与适用域"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (NumPy, SciPy)", "Agent-based modeling", "System Dynamics", "NETLogo", "GAMS", "R", "SPSS", "Stata", "QGIS", "ArcGIS", "Google Earth", "Historical database", "Text analysis", "NLP tools", "Network analysis", "Agent-Based Modeling Platform", "Wargame simulation", "Military simulator", "JNETSIM"),
    category="军事学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
