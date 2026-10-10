"""软件开发学科论文支持：实现/工具链/实证体裁、IEEE 引用样式与构建可复现注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="software_development",
    aliases=("software_development", "软件开发", "应用软件开发", "Web 开发", "移动开发", "前端开发"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="IEEE 样式（数字编号制，如 [1]；按目标会议/期刊规范）",
    reporting_standards={
        "tool_paper": "工具类论文须遵循工具论文报告规范（设计、实现、场景、评估、可用性）",
        "reproducibility": "代码仓库须给出构建脚本、依赖版本清单与运行说明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "研究问题（RQ）须显式列出并可验证",
        "数据集/代码仓库须给出可复现链接",
        "统计检验与效应量须报告",
        "有效性威胁（内部/外部/构造/结论）须讨论",
        "工具/方法命名须与既有文献一致",
    ),
    key_venues=(
        "Software Quality Journal",
        "Software: Practice and Experience",
        "ACM SIGSOFT Software Engineering Notes",
        "Software Testing, Verification and Reliability",
        "Empirical Software Engineering",
    ),
    units_and_formulas_notes=(
        "性能指标用 ms/s；吞吐用 ops/s",
        "构建与 CI 时长给中位数与 p95",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Visual Studio", "WebStorm", "PhpStorm", "Android Studio", "Xcode", "Flutter", "React Native", "GitKraken", "TeamCity", "Azure DevOps", "CircleCI", "Travis CI", "npm", "Yarn", "pnpm", "Vite", "Webpack", "Cypress", "WebdriverIO", "Charles Proxy"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)
