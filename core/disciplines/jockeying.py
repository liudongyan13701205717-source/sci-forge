"""骑师训练学科论文支持：骑师/马术运动生物力学与训练体裁、APA 引用样式与马匹运动记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="jockeying",
    aliases=("jockeying", "骑师训练", "赛马骑术", "马术运动", "jockeying", "horse riding", "equestrian sport", "racing jockey"),
    paper_types={
        "research": ("abstract", "introduction（运动背景与问题）", "methodology（生物力学与训练方法）", "results（运动学与成绩）", "discussion（训练建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（训练个案）", "analysis（技术动作分析）", "results（成绩变化）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（训练理论）", "evidence synthesis（证据综述）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Equine Veterinary Journal 遵循 APA 规范）",
    reporting_standards={"biomechanical": "生物力学研究遵循 ISB 报告规范", "intervention": "干预研究遵循 CONSORT 声明", "systematic_review": "系统综述遵循 PRISMA 声明"},
    conventions=("运动参数（步幅、步频、心率）须量化", "动作捕捉标记点与坐标系须注明", "马匹与骑师体型须报告", "训练负荷与恢复须记录", "赛事环境（赛道、天气）须说明"),
    key_venues=("Equine Veterinary Journal", "Equine Veterinary Education", "Veterinary Journal", "Journal of Equine Veterinary Science", "International Journal of Sport and Exercise Psychology"),
    units_and_formulas_notes=("步频用 steps/min；速度用 km/h", "心率用 bpm（标注采样间隔）", "地面反作用力用 N", "运动负荷用 HR×秒 或 TRIMP"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Vicon 光学运动捕捉系统", "Dymon 地面测力台", "Polar 心率带（心率监测）", "GPS 运动记录仪", "EMG 肌电系统", "运动生物力学软件（C3D）", "视频慢动作分析（Dartfish）", "运动生理学实验室", "血气分析仪", "乳酸分析仪", "运动营养实验室", "马匹肌肉超声仪", "X 射线摄影", "蹄铁测量工具", "马术模拟器", "平衡测试仪（力板）", "训练记录软件", "运动数据分析（R）", "马术比赛数据平台（ATPC）", "马匹健康管理系统"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
