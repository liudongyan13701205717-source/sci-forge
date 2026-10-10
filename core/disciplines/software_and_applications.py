"""软件与应用学科论文支持：系统实现/工具类论文体裁、IEEE 引用样式与可复现构建注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="software_and_applications",
    aliases=("software_and_applications", "软件与应用", "应用软件", "软件应用", "工具软件", "信息系统应用"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="IEEE 样式（数字编号制，如 [1]；按目标会议/期刊规范）",
    reporting_standards={
        "tool_paper": "工具类论文须遵循工具论文报告规范（设计、实现、场景、评估、可用性）",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "工具/方法须给出可复现链接与依赖版本清单",
    },
    conventions=(
        "研究问题（RQ）须显式列出并可验证",
        "数据集/代码仓库须给出可复现链接",
        "统计检验与效应量须报告",
        "有效性威胁（内部/外部/构造/结论）须讨论",
        "工具/方法命名须与既有文献一致",
    ),
    key_venues=(
        "Communications of the ACM",
        "IEEE Software",
        "Journal of Open Source Software",
        "IEEE Access",
        "Journal of Systems and Software",
    ),
    units_and_formulas_notes=(
        "性能指标用 ms/s；吞吐用 ops/s",
        "公式用 amsmath；算法伪代码用 algorithm 环境",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Office", "Google Workspace", "Foxit Reader", "Tinkercad", "GIMP", "Adobe Premiere Pro", "LabVIEW", "Tableau Desktop", "Qlik Sense", "Slack", "Notion", "Zoom", "Sketch", "Postman", "Swagger", "Apache JMeter", "Fiddler", "7-Zip", "TeamViewer", "VMware Workstation"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)
