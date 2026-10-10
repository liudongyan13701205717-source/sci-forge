"""航空地勤训练学科论文支持：机坪作业与地面保障的训练设计、模拟器评估与安全文化研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ground_crew_training",
    aliases=("ground_crew_training", "地勤训练", "地面保障", "ground handling", "机组资源管理", "crew resource management", "机坪作业", "apron operations", "地面服务"),
    paper_types={
        "research": ("abstract", "introduction（地勤安全与训练问题）", "methodology（任务分析、课程设计与评估方案）", "results（技能评分、差错率与学习曲线）", "discussion（训练对作业安全的影响）", "references"),
        "case_study": ("abstract", "introduction", "case description（机场、航司与地勤作业场景）", "analysis（作业流程与人因风险）", "results（差错率与纠正效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（人因与机组资源管理理论）", "evidence synthesis（地勤训练研究文献综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"safety_stats": "差错与事故须按事件类型统计，并给出统计区间与数据来源", "simulation": "模拟器机型、场景脚本与评分量表须说明", "ethics": "涉及在岗人员评估须说明知情同意与数据匿名化"},
    conventions=("作业规范按 ICAO 附件 14 与机场手册条款标注", "事件分类按 IATA 或 IATA AHTM 定义统一", "时间数据以 min 或 s 报告，并说明起止定义", "评分量表须报告分制、权重与评分者一致性", "术语首次出现给出中英文对照"),
    key_venues=("Journal of Air Transport Management", "Transportation Research Part A: Policy and Practice", "Safety Science", "Journal of Human Factors, Ergonomics and the Environment", "航空运输研究"),
    units_and_formulas_notes=("时间以 min 或 s 报告；航班周转以 min 报告", "安全指标以每百班次差错数（per 100 ops）报告", "训练效果以技能评分（0–100）与达标率（%）报告", "公式用 LaTeX（amsmath）；达标率 = 达标人数 / 总人数 × 100%"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Thales VANTAGE", "Pinnacle Aeronautics", "CAE", "Amadeus Altea Ground Handling", "Travelport Sabre", "AGL Flightline", "Grotech Airport", "SITA", "Lufthansa Technik", "Menzies Aviation", "Swissport", "Airports International", "Delta Ground Solutions", "ATA AGS", "IATA AHTM", "IOSA Ground Safety Audit", "Microsoft Flight Simulator", "X-Plane", "Blackboard Learn", "Moodle"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
