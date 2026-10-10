"""安保服务（未另分类）学科论文支持：安保服务研究/行业分析/服务质量评估/安全管理体裁、APA 7 管理学学术引用样式与服务度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="security_services_not_elsewhere",
    aliases=("security_services_not_elsewhere", "安保服务", "安保行业", "security services", "security industry"),
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
        "data": "服务数据须报告服务类型、客户类型、服务质量指标与统计口径",
        "risk": "风险评估须报告风险识别、量化方法与等级划分标准",
        "ethics": "涉及内部数据研究须报告伦理审查与保密措施",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "服务类型须分类统计：人防/技防/物防/消防/应急等",
        "服务质量指标须注明定义、测量方法与基准值",
        "案例须说明时间、地点、服务类型与处置结果",
        "引用法规/标准须标注标准编号与版本年份",
        "涉及敏感信息须脱敏处理并注明脱敏规则",
    ),
    key_venues=(
        "Security Journal",
        "Journal of Loss Prevention",
        "Journal of Safety Research",
        "Journal of Risk Research",
        "Public Administration Review",
    ),
    units_and_formulas_notes=(
        "服务时长用 h；响应时间用 min；满意度用 Likert 5 级量表",
        "服务质量指标用百分比或等级制；成本节约用货币单位",
        "公式用 amsmath；服务质量计算公式须编号",
        "统计结果给出均值 ± 标准差与样本量；显著性用 p 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS 统计分析", "R 统计分析", "Python 数据分析", "LaTeX 排版", "Origin 绘图", "Excel 数据分析", "NVivo 质性分析", "MATLAB 数据分析", "AMOS 结构方程", "Mplus 潜变量分析", "CCTV 监控系统", "Access Control System 门禁系统", "Alarm System 报警系统", "Security Incident Reporting System", "Tableau 数据可视化", "Power BI 商业智能", "QGIS 空间分析", "SurveyMonkey 问卷设计", "Google Forms 在线测评", "Body Camera 执法记录仪"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "SQL 数据库管理"),
)