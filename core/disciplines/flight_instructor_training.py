"""飞行教官培训学科论文支持：飞行教学理论、训练评估与飞行安全。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="flight_instructor_training",
    aliases=("flight_instructor_training", "飞行教官培训", "flight instructor",
             "flight training education", "flight training assessment",
             "飞行教员培训", "aviation training", "飞行教学",
             "flight proficiency training"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="AIAA style（编号），如 [1] 或 (Author and Author Year)",
    reporting_standards={
        "training": "飞行训练评估须报告训练科目、评价标准与教员资质",
        "simulator": "模拟器训练须声明模拟器等级、设备型号与校准情况",
        "safety": "飞行安全分析须报告事件等级、调查方法与纠正措施",
    },
    conventions=(
        "飞行高度用 ft（英尺）或 m 表示",
        "飞行速度用 knots（节）或 km/h 表示",
        "训练学时用小时或分钟表示",
        "飞行日志须记录机型、日期与飞行时间",
        "检查评分用百分比(%)表示",
    ),
    key_venues=(
        "Human Factors",
        "The Aerospace Medical Journal",
        "Aviation Safety Journal",
        "Safety Science",
        "中国民航大学学报",
    ),
    units_and_formulas_notes=(
        "飞行高度用 ft 表示，1 ft = 0.3048 m",
        "速度用 knots 表示，1 knot = 0.5144 m/s",
        "飞行性能用 VREF、VMCA、VMO 等速域参数表示",
        "训练达标率 = 达标人数/总训练人数 × 100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("飞行模拟器 (Full Mission Simulator)", "飞行训练机 (Cessna 172/Skyhawk)", "飞行训练数据记录仪 (FDARS)", "飞行检查评估系统 (FIA)", "飞行安全分析系统", "飞行训练管理系统", "飞行气象雷达", "电子飞行包 (EFB)", "iPad Pro with ForeFlight", "飞行性能计算软件 (VREF/LAMPS)", "MATLAB/Simulink", "Python", "SPSS", "R (RStudio)", "Excel", "NVivo", "GIS (ArcGIS)", "飞行日志管理系统", "飞行训练评估系统", "机组资源管理培训系统 (CRM Training)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)