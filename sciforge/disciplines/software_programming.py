"""软件编程学科论文支持：算法实现/软件工程/编程语言体裁、ACM 样式与编程记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="software_programming",
    aliases=(
        "software_programming",
        "软件编程",
        "编程",
        "编程开发",
        "软件工程",
        "coding",
        "software programming",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "method（方法）",
            "experiments（实验）",
            "conclusion（结论）",
            "references",
        ),
        "empirical_study": (
            "abstract",
            "introduction",
            "research questions（研究问题）",
            "study design（研究设计）",
            "results（结果）",
            "threats to validity（有效性威胁）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；ICSE/ISSTA 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "实验遵循软件工程实验报告规范",
        "empirical": "实证研究遵循软件工程实证报告规范",
        "benchmark": "基准测试遵循标准基准报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "可复现性遵循软件工程可复现性清单",
    },
    conventions=(
        "编程语言与版本须报告",
        "开发环境与工具链须说明",
        "算法复杂度与空间复杂度须报告",
        "实验数据集与参数须明确",
        "可复现性：提供可运行代码与配置",
    ),
    key_venues=(
        "ICSE",
        "ISSTA",
        "FSE",
        "IEEE Transactions on Software Engineering",
        "ACM Transactions on Software Engineering and Methodology",
    ),
    units_and_formulas_notes=(
        "时间用 s/min；空间用 MB/GB",
        "公式用 amsmath；算法与统计模型须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Visual Studio Code", "IntelliJ IDEA", "Eclipse", "PyCharm", "WebStorm", "Xcode", "Android Studio", "Visual Studio", "JetBrains Rider", "Sublime Text", "Notepad++", "Vim", "Neovim", "Emacs", "GitHub Copilot", "Git", "Docker", "Replit", "CodeSandbox", "VS Code Remote"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)
