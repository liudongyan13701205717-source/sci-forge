"""技术（Technology）学科论文支持：技术评估/创新与工具链开发的体裁、IEEE 与 ACM 引用样式与注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="technology",
    aliases=(
        "technology",
        "技术",
        "技术研究",
        "技术评估",
        "技术创新",
        "technology assessment",
        "technology transfer",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与贡献声明）",
            "methods（方案设计与实现）",
            "results（实验/评测结果）",
            "discussion（讨论与局限）",
            "references",
        ),
        "technical_report": (
            "abstract",
            "introduction",
            "system description（系统与工具链描述）",
            "evaluation（评测设计与结果）",
            "reproducibility notes（复现说明）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与筛选方法）",
            "evidence synthesis（技术路线比较）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号制，工程技术论文主流规范）",
    reporting_standards={
        "experimental": "实验研究须报告硬件/软件环境、随机种子与重复次数",
        "reproducibility": "可复现要求须给出代码链接、依赖清单与环境版本",
        "evaluation": "评测须含基线对照与消融实验",
        "statistical": "显著性检验须报告检验类型、假设与 p 值",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "算法复杂度须给出时间与空间复杂度符号（Big-O）",
        "图表自明（self-explanatory），坐标轴标注量纲与单位",
        "实现细节（版本、配置、参数）须在附录或复现说明中完整列出",
        "评测指标须定义计算方式并给出单位",
        "术语首次出现时给出全称与缩写（如 CNN, convolutional neural network）"
    ),
    key_venues=(
        "IEEE Transactions on Technology and Society",
        "Research Policy",
        "Technological Forecasting and Social Change",
        "IEEE Technology and Society Magazine",
        "Journal of Engineering and Technology Management",
    ),
    units_and_formulas_notes=(
        "SI 单位优先；速率用 bps/Mbps，能量用 J/kWh",
        "公式用 amsmath；核心指标（吞吐、时延、准确率）公式须编号并被引用",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "数值结果报告均值 ± 标准差与样本量/重复次数"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python", "R", "SPSS", "Minitab", "JMP", "Tableau", "Power BI", "Miro", "FigJam", "Lucidchart", "draw.io", "XMind", "Anaconda", "Jupyter Notebook", "Git", "Docker", "VS Code", "LaTeX", "Zotero"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)
