"""空乘培训学科论文支持：客舱安全服务培训、应急程序验证与培训效能研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="stewardesssteward_training",
    aliases=("stewardesssteward_training", "空乘培训", "空乘教育", "乘务员培训",
             "cabin crew training", "flight attendant training", "aviation cabin service",
             "客舱安全管理", "客舱服务培训"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与培训需求分析）",
            "methods（培训设计与评估方法）",
            "results（培训效能与技能获得）",
            "discussion（培训改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（航空公司培训实例）",
            "analysis（培训过程与效果分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（培训理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式",
    reporting_standards={
        "training_design": "培训课程设计须遵循 IATA 航空安全培训标准",
        "emergency_procedure": "应急程序训练须报告演练场景、参与人数与达标率",
        "skills_assessment": "技能评估须使用标准化量表并报告评分者信度",
        "feedback": "学员反馈须报告样本量与关键统计指标",
    },
    conventions=(
        "应急程序名称须使用 IATA / ICAO 标准术语",
        "培训时长以小时（h）报告",
        "考核结果以通过/未通过或百分制报告",
        "安全事件案例须隐去航空公司标识",
        "培训材料须标注版本与修订日期",
    ),
    key_venues=(
        "Journal of Air Transport Management",
        "Journal of Aviation Technology and Engineering",
        "Cabin Crew Safety Research",
        "International Journal of Aviation Engineering",
        "Human Factors: The Journal of the Human Factors and Ergonomics Society",
    ),
    units_and_formulas_notes=(
        "培训时长：h（小时）",
        "应急撤离时间：秒（s），标准 ≤90 s",
        "服务评分：5 级 Likert 量表（1–5）",
        "通过率：通过人数 / 总人数 × 100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Full-motion flight simulator", "Emergency evacuation simulator", "Fire-fighting simulator", "First-aid training manikin", "IATA Cabin Crew Training System", "CAE Aviation Training Software", "LMS (Learning Management System)", "VR Cabin Trainer", "Microsoft Teams (Virtual Classroom)", "Spinal immobilization training aid", "Life-vest training kit", "Halogen light fire trainer", "AED training device", "Smoke evacuation hood trainer", "Cabin door operation trainer", "Cruise simulation software", "Tableau (training analytics)", "Qualtrics (survey)", "Python (pandas)", "NVivo (qualitative analysis)"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
