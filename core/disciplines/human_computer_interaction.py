"""人机交互学科论文支持：可用性/用户研究/界面实验体裁、ACM 引用样式与眼动/日志数据口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="human_computer_interaction",
    aliases=(
        "human_computer_interaction",
        "人机交互",
        "用户界面设计",
        "Human-Computer Interaction",
        "HCI",
        "User Experience",
        "可用性研究",
        "交互设计",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ACM 引用样式（作者-年份；CHI 等采用 ACM Reference Format）",
    reporting_standards={"k1": "实验研究须报告被试与设备信息", "k2": "用户研究须说明知情同意", "k3": "日志研究须报告采样与清洗口径"},
    conventions=(
        "被试数与分组须报告",
        "任务时长/错误率给出统计口径",
        "眼动数据报告注视点阈值",
        "预注册与伦理批准号须给出",
        "代码与数据须开放可复现",
    ),
    key_venues=(
        "ACM CHI Conference",
        "IEEE VIS",
        "Proc. of the ACM on HCI",
        "International Journal of Human-Computer Studies",
        "IEEE Transactions on Visualization and Computer Graphics",
    ),
    units_and_formulas_notes=(
        "任务时长以秒计",
        "SUS/SE 评分给出均值与标准差",
        "眼动坐标注明屏幕分辨率",
        "统计量给出 M/SD/CI 与显著性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("UserTesting", "OptiTrack", "Tobii 眼动仪", "Unity", "Unreal Engine", "Figma", "Adobe XD", "Sketch", "InVision", "Axure", "SPSS", "R", "Python", "MATLAB", "Excel", "Tableau", "Endnote", "GitLab", "OpenSim", "NVivo"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
