"""技术教学学科论文支持：职教/技术技能教学与实训设计的体裁、APA 7 引用样式与教学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="technical_teaching",
    aliases=(
        "technical_teaching",
        "技术教学",
        "职业技术教育",
        "实训教学",
        "职业教育教学法",
        "technical education pedagogy",
        "vocational training",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、教学问题与研究问题）",
            "methods（研究设计与技能测评）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "design_based_research": (
            "abstract",
            "introduction",
            "design rationale（教学原理与能力目标）",
            "development and implementation（资源开发与实训实施）",
            "findings（发现与能力证据）",
            "design principles",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与筛选方法）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份制，职业教育研究主流规范）",
    reporting_standards={
        "empirical": "实证研究须报告实训项目数、学员构成与前后测设计",
        "skill_assessment": "技能评价遵循国家职业技能标准或 DCN（可观察职业行为）",
        "ethics": "实训操作数据与视频须取得伦理批准与知情同意",
        "mixed_methods": "混合方法研究遵循 MMRM 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "能力目标须分解为可观察行为与合格判定标准",
        "实训学时、工位配比与安全防护须在方法节说明",
        "技术软件/设备版本须标注（如 PLC 型号、仿真软件版本）",
        "技能测评须报告评分者间信度与评分量表",
        "学员一律匿名化，企业名称与项目编号可保留"
    ),
    key_venues=(
        "Journal of Vocational Education and Training",
        "Vocational Education and Training",
        "Journal of Engineering Education",
        "International Journal of Training and Development",
        "Teaching in Higher Education",
    ),
    units_and_formulas_notes=(
        "实训投入用学时（含指导/自主比）；工位配比用 1:n 表示",
        "技能熟练度用达成率（%）或等级（DCN 编号）报告",
        "公式用 amsmath；技能掌握曲线与达标判定公式须编号并被引用",
        "设备参数按设备手册单位书写（V、A、rpm、Hz）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Canvas LMS", "Blackboard", "Articulate 360", "iSpring Suite", "Adobe Captivate", "H5P", "Genially", "Camtasia", "OBS Studio", "Sway", "Nearpad", "Socrative", "Canva", "Microsoft Teams", "Scratch", "Arduino IDE", "SoftPLC", "LabVIEW", "MATLAB/Simulink"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
