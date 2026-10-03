"""人工智能伦理学科论文支持：AI 伦理/负责任 AI 体裁、APA 引用样式与 AI 伦理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ai_ethics",
    aliases=("ai_ethics", "人工智能伦理", "AI 伦理", "负责任 AI", "AI ethics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与 AI 伦理问题）",
            "methods（研究设计与分析）",
            "results（伦理评估数据）",
            "discussion（伦理意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（AI 系统案例）",
            "analysis（伦理风险分析）",
            "conclusions（治理启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；AI and Ethics 遵循 Springer 规范）",
    reporting_standards={
        "case_study": "案例研究遵循案例研究报告规范",
        "algorithmic_audit": "算法审计遵循审计报告规范",
        "policy_analysis": "政策分析遵循政策评估报告规范",
        "survey": "问卷调查遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "AI 系统范围与能力边界须明确",
        "伦理框架（公平、问责、透明等）须定义",
        "风险评估方法与指标须报告",
        "治理与合规机制须说明",
        "利益相关者与受影响群体须识别",
    ),
    key_venues=(
        "AI and Ethics",
        "AI & Society",
        "Ethics and Information Technology",
        "Nature Machine Intelligence",
        "ACM FAccT (conference)",
        "Philosophy & Technology",
    ),
    units_and_formulas_notes=(
        "公平性指标无量纲；比例用 %",
        "公式用 amsmath；公平性与偏差指标计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "审计结果给出置信区间与敏感性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=("公平性测试工具（AIF360/Fairlearn）", "模型审计框架", "偏差检测评测套件"),
    category="交叉学科",
    databases=("OpenAlex", "arXiv", "Crossref", "Semantic Scholar", "CNKI"),
)