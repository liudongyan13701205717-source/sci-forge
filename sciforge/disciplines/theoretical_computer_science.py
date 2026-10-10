"""理论计算机科学论文支持：算法、复杂度、证明与形式化方法。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="theoretical_computer_science",
    aliases=("tcs", "theoretical cs", "算法", "complexity", "proof theory",
             "逻辑", "formal methods", "模型检测", "计算理论"),
    paper_types={
        "research": ("abstract", "introduction", "preliminaries", "main results", "proofs", "conclusions", "references"),
        "survey": ("abstract", "introduction", "taxonomy", "open problems", "references"),
    },
    citation_style="ACM 或 Springer LNCS（会议）",
    reporting_standards={
        "correctness": "正确性证明须完整（不变式+终止性）",
        "complexity": "复杂度界须注明模型（RAM/Turing/Word RAM）",
        "reduction": "归约须证明保持性（LLL/Karp/Turing）",
        "probabilistic": "随机性来源与成功概率放大须处理（Chernoff）",
        "formal": "形式化证明须给出公理；自动验证须给工具（Coq/Isabelle/Lean）",
    },
    conventions=(
        "定义-定理-证明格式，编号一致（可用 amsthm）",
        "伪代码用算法环境（algorithm/algorithmic），行号引用",
        "图灵机变换给状态转移函数；规约构造给映射函数",
        "复杂度类记号统一（P/NP/#P/PSPACE），不可混用",
        "开放问题分开列为 Conjecture 或 Open Problem",
    ),
    key_venues=(
        "Journal of the ACM",
        "SIAM Journal on Computing",
        "IEEE Symposium on Foundations of Computer Science (FOCS)",
        "Symposium on Theory of Computing (STOC)",
        "Logical Methods in Computer Science",
    ),
    units_and_formulas_notes=(
        "大 O 记号给常数因子与定义域限制",
        "概率空间须明确；期望/方差记号关联随机变量",
        "下界证明须给路径（对手论证/信息论/转换图）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("LaTeX", "Coq", "Isabelle", "TLA+", "Lean 4", "Agda", "Alloy", "Prism（模型检测）", "Spot（LTL 检验）", "NuSMV（状态模型）", "UPPAAL（时序模型）", "CBMC（代码验证）", "KLEE（符号执行）", "Z3（定理证明器）", "Boolector（SMT 求解器）", "Yices（SMT 求解器）", "PACE（并行算法竞赛工具）", "DIMACS SAT 求解器", "Zotero", "EndNote"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)