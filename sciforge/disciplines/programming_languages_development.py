"""编程语言开发学科论文支持：工程实践/工具链体裁、ICSE 报告规范与工程度量注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="programming_languages_development",
    aliases=(
        "programming_languages_development",
        "编程语言开发",
        "软件开发",
        "Programming languages development",
        "Software development",
        "软件工程",
        "编译开发",
        "工具链开发",
        "SE",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（工程方法）",
            "results（实验与度量）",
            "discussion（工程启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（项目案例描述）",
            "analysis（流程与工具链分析）",
            "results（质量与效率结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（方法综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；ICSE/ASE 遵循 ACM 规范）",
    reporting_standards={
        "engineering": "工程研究遵循软件工程案例报告规范",
        "empirical": "实证研究遵循 DSR/DSM 声明",
        "case_study": "案例研究遵循 DSR-CASE 报告规范",
        "systematic_review": "系统综述遵循 SWiM 指南",
        "replication": "可重复性遵循代码与数据发布规范",
    },
    conventions=(
        "开发环境与工具链版本须完整披露",
        "实验须在受控基准上执行并报告失败率",
        "度量指标定义须形式化，口径一致",
        "构建系统、依赖与 CI 配置须公开",
        "对比实验须报告效应量与显著性检验",
    ),
    key_venues=(
        "ICSE",
        "ASE",
        "FSE/ESEC",
        "MSR",
        "Empirical Software Engineering",
        "IEEE Transactions on Software Engineering",
        "Empirical Software Engineering",
    ),
    units_and_formulas_notes=(
        "度量单位须明确（行/分钟/缺陷密度）",
        "缺陷密度 = 缺陷数 / KLOC，KLOC 口径须声明",
        "构建时间与覆盖率以百分比报告并标注工具版本",
        "公式用 amsmath；指标定义式须编号",
        "时间戳与时区须在数据集说明中给出",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("Bazel", "CMake", "Gradle", "Maven", "NPM", "Docker", "GitHub Actions", "GitLab CI", "Git", "Valgrind", "LLVM", "GCC", "Rustc", "Clang", "LLDB", "GDB", "CockroachDB", "Bazel Remote Execution", "Bazelisk", "Sourcegraph"),
    category="工学",
    databases=("OpenAlex", "Crossref", "GitHub", "Zenodo"),
)
