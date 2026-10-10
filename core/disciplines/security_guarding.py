"""警卫学科论文支持：警卫培训/警卫行动/安保勤务/应急处置体裁、APA 7 管理学学术引用样式与警卫度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="security_guarding",
    aliases=("security_guarding", "警卫", "安保勤务", "保安警卫", "security guarding", "security patrol"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究意义）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据综合）",
            "future directions（展望）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "methodology": "研究须报告研究设计、样本来源、数据收集与分析方法",
        "data": "警卫勤务数据须报告勤务类型、时间、地点与处置结果",
        "risk": "风险评估须报告风险识别、量化方法与等级划分标准",
        "ethics": "涉及警卫人员数据研究须报告伦理审查与保密措施",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "警卫行动须注明行动类型、时间、地点与参与人员",
        "风险等级须注明划分标准与评估方法",
        "安防系统须注明系统类型、品牌与配置参数",
        "案例须说明时间、地点、事件性质与处置结果",
        "引用法规/标准须标注标准编号与版本年份",
    ),
    key_venues=(
        "Security Journal",
        "Journal of Safety Research",
        "Journal of Risk Research",
        "Journal of Loss Prevention",
        "Public Administration Review",
    ),
    units_and_formulas_notes=(
        "勤务时长用 h；响应时间用 min；风险等级用 1-5 级",
        "事件类型须分类统计：入侵/火警/人员冲突/设备故障等",
        "公式用 amsmath；风险计算公式须编号",
        "统计结果给出均值 ± 标准差与样本量；显著性用 p 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS 统计分析", "R 风险建模", "Python 数据分析", "LaTeX 排版", "Origin 绘图", "Excel 数据分析", "NVivo 质性分析", "CCTV 监控系统", "Access Control System 门禁系统", "Alarm System 报警系统", "Body Camera 执法记录仪", "Radio Communication 对讲通讯", "GPS Tracking 定位追踪", "Emergency Response System 应急响应系统", "Patrol Management System 巡逻管理系统", "QGIS 空间分析", "Tableau 数据可视化", "SurveyMonkey 问卷设计", "Google Forms 在线测评", "Moodle（培训管理平台）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "SQL 数据库管理"),
)