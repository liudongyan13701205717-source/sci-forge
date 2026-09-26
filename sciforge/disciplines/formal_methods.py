"""形式化方法学科论文支持：验证/证明/模型检测体裁、ACM 引用样式与逻辑记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="formal_methods",
    aliases=("formal_methods", "形式化方法", "形式验证", "模型检测"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "formalization（形式化）",
            "method（方法）",
            "evaluation（评估）",
            "references",
        ),
        "verification_paper": (
            "abstract",
            "introduction",
            "background（背景：验证技术）",
            "formalization（形式化）",
            "method（验证方法）",
            "case studies（案例研究）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；CAV/POPL 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "实验遵循形式化工具评估规范",
        "proof": "证明遵循机器可检查证明报告规范",
        "case_study": "案例研究遵循工业案例报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "benchmark": "基准测试遵循标准验证基准报告规范",
    },
    conventions=(
        "逻辑系统（一阶/高阶/时序等）须明确",
        "证明工具与版本须报告",
        "完备性与可靠性声明须给出",
        "案例研究须说明规模与来源",
        "与既有工具对比须公平（同输入）",
    ),
    key_venues=(
        "International Conference on Computer Aided Verification (CAV)",
        "ACM SIGPLAN Symposium on Principles of Programming Languages (POPL)",
        "ACM/IEEE Symposium on Logic in Computer Science (LICS)",
        "International Conference on Formal Methods in Computer-Aided Design (FMCAD)",
        "Formal Methods in System Design",
        "Journal of Automated Reasoning",
    ),
    units_and_formulas_notes=(
        "证明规模用行数或步数；状态空间用状态数",
        "时间用 s 或 min；内存用 MB/GB",
        "公式用 amsmath；逻辑规则与定理须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "量词与模态算子记法须与工具一致",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Coq", "Isabelle", "TLA+"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)