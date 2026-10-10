"""计算机程序设计学科论文支持：编程语言/软件工程/算法体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_programming",
    aliases=("computer programming", "计算机程序设计", "编程",
             "programming languages", "编程语言", "software development",
             "软件开发", "软件工程", "software engineering",
             "程序设计语言", "program design"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "related work",
            "method",
            "evaluation",
            "results",
            "discussion",
            "references",
        ),
        "systems_paper": (
            "abstract",
            "introduction",
            "background and motivation",
            "design",
            "implementation",
            "evaluation",
            "related work",
            "conclusion",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method",
            "taxonomy",
            "open problems",
            "references",
        ),
    },
    citation_style="ACM/IEEE 编号样式",
    reporting_standards={
        "benchmark": "算法/工具基准须公开数据集、划分与协议",
        "reproducibility": "代码仓库与依赖版本须记录",
        "complexity": "复杂度以 O()/Θ() 标注，说明输入规模",
        "correctness": "算法给出正确性论证或形式化验证",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "算法用 algorithm 环境写伪代码，输入/输出显式给出",
        "复杂度以 O()/Θ()/Ω() 标注，输入规模 n 度量须说明",
        "贡献以编号列表在引言末尾显式陈述",
        "图表矢量导出；对比表加粗最优并标注显著性",
        "脚注或正文给出代码仓库链接（匿名期用匿名仓库）",
        "缩写首次出现给出全称",
    ),
    key_venues=(
        "Journal of Functional Programming",
        "ACM POPL",
        "PLDI",
        "OOPSLA",
        "ECOOP",
        "IEEE Transactions on Software Engineering",
        "Software: Practice and Experience",
        "Empirical Software Engineering",
        "IEEE Transactions on Computers",
        "Computers & Education",
    ),
    units_and_formulas_notes=(
        "复杂度用 O()/Θ()/Ω() 记法，注明输入规模度量",
        "性能对比给硬件环境与百分位",
        "数值结果给出均值 ± 标准差与样本量",
        "公式用 amsmath；编号仅在被引用时",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("Python", "Java", "C", "C++", "C#", "JavaScript", "TypeScript", "Go", "Rust", "Swift", "Kotlin", "Scala", "Haskell", "Ruby", "PHP", "Perl", "VS Code", "JetBrains IntelliJ IDEA", "Eclipse", "PyCharm", "GitHub Copilot", "Git", "GitHub", "GitLab", "Docker", "Postman", "LeetCode", "HackerRank", "Codewars", "LeetHub", "Jupyter Notebook", "Pydantic", "NumPy", "PyTorch", "TensorFlow", "pandas", "Flask", "FastAPI", "Django", "React", "Vue", "Node.js", "Webpack", "Vite", "ESLint", "Prettier", "pytest", "JUnit", "Mocha", "Cypress", "Selenium", "Valgrind", "gdb", "LLDB", "GDB", "Perf", "Clang-Tidy", "SonarQube", "GitHub Actions", "Jenkins", "CircleCI", "Babel", "Terser", "Rollup"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)
