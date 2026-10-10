"""人机交互计算学科论文支持：HCI 研究/设计/系统报告、ACM 引用样式与人因度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="humancentred_computing",
    aliases=("humancentred_computing", "人机交互计算", "人机交互", "HCI", "人因计算", "用户体验", "交互设计", "计算机支持合作", "可及性"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与研究问题）", "methodology（被试、任务与度量）", "results（量化与质性发现）", "discussion（启示与局限）", "references"),
        "case_study": ("abstract", "introduction", "case description（情境与用例）", "analysis（设计分析）", "results（评估结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论与设计空间）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ACM 样式（作者-年份；Proc. of CHI 遵循 ACM 规范）",
    reporting_standards={
        "empirical_study": "实证研究遵循被试/任务/度量报告规范",
        "design_research": "设计研究遵循设计空间/制品报告规范",
        "usability": "可用性评估遵循任务成功度量规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "ethics": "人因实验须报告伦理审查编号",
    },
    conventions=(
        "被试样本量与人口学须报告",
        "任务与成功指标须定义",
        "统计检验与效应量须给出",
        "设备与版本须注明",
        "伦理批准与知情同意须说明",
    ),
    key_venues=(
        "ACM CHI Conference",
        "ACM TOCHI",
        "International Journal of Human-Computer Studies",
        "ACM CSCW",
        "Proceedings of ASSETS",
        "Human Factors",
    ),
    units_and_formulas_notes=(
        "时间用 s；错误率用 %；满意度量表标注量程",
        "公式用 amsmath；统计量报告 p 值与 95% CI",
        "数值结果给出均值 ± 标准差与样本量",
        "反应时注明测量方法与剔除准则",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Figma", "Adobe XD", "MATLAB", "SPSS", "NVivo", "UsabilityLab", "OpenSUSE Lab", "Python", "R", "Unity", "Processing", "LabVIEW", "Qualtrics", "OptiTrack", "Tobii 眼动仪", "OpenCV", "KeePass", "Jupyter", "Git", "Blender"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
