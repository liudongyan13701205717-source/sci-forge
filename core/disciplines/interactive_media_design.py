"""互动媒体设计学科论文支持：设计/交互研究体裁、APA 引用样式与 HCI 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interactive_media_design",
    aliases=("interactive_media_design", "互动媒体设计", "交互设计", "交互媒体", "HCI", "交互工程", "互动叙事", "游戏设计", "UX 设计", "用户体验", "游戏工程"),
    paper_types={
        "research": ("abstract", "introduction（设计研究问题）", "methodology（原型/实验设计）", "results（可用性/情感反馈）", "discussion（设计启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（项目/产品背景）", "analysis（设计过程分析）", "results（设计效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（交互设计理论）", "evidence synthesis（实证证据综述）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"user_study": "用户研究须声明参与者、任务与统计口径", "design_artifact": "设计工件须提供可复现说明与迭代过程", "ethics": "涉及人体的研究须通过伦理审查"},
    conventions=("可用性指标（任务完成率、SUS、SOM）须报告", "原型版本与迭代须清晰说明", "参与式设计与共创过程须记录", "视觉素材署名与授权须合规", "情感/体验用可量化量表"),
    key_venues=("CHI Conference on Human Factors in Computing Systems", "IEEE Transactions on Visualization and Computer Graphics", "ACM Transactions on Computer-Human Interaction", "International Journal of Human-Computer Studies", "Proceedings of the Design Research Association"),
    units_and_formulas_notes=("响应时延用 ms 并声明设备/网络条件", "可用性量表须报告信度系数", "情感量表（SUS/SOM）报告均值与 95% CI", "公式用 amsmath；量表评分范围须声明"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Unity", "Unreal Engine", "Godot", "Figma", "Sketch", "Adobe Photoshop", "Adobe Illustrator", "Blender", "Maya", "ProBuilder", "Adobe XD", "InVision", "Maze", "Hotjar", "UsabilityHub", "UserTesting", "NVivo", "Qualtrics", "Unity Test Framework", "Python (Pandas/SciPy)"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
