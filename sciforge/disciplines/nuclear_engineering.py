"""核工程学科论文支持：核反应堆/核安全/辐射防护体裁、ANS 引用样式与核工程记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nuclear_engineering",
    aliases=("nuclear_engineering", "核工程", "核能", "核反应堆", "核安全",
             "辐射防护"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与核工程问题）",
            "methods（建模、实验与参数）",
            "results（中子学/热工/安全数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "safety_analysis": (
            "abstract",
            "introduction",
            "plant model（电厂模型与假设）",
            "methodology（事故序列/概率安全分析）",
            "results（安全裕度与后果）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "state of the art（现状分类）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="ANS 样式（作者-年份；ANS 期刊遵循 ANS 规范）",
    reporting_standards={
        "safety_analysis": "安全分析遵循 IAEA SSR-2 安全标准",
        "experimental": "实验研究遵循 ANS 实验报告规范",
        "simulation": "中子学/热工仿真遵循 ANS 仿真报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "probabilistic_risk_assessment": "概率安全评价遵循 NUREG 报告规范",
    },
    conventions=(
        "反应堆类型与燃料循环须注明",
        "中子通量/截面单位与符号须规范",
        "安全裕度与限值（DNBR、LCO）须明确",
        "辐射剂量单位（Sv、Gy）须规范",
        "核数据来源与版本须引用",
    ),
    key_venues=(
        "Nuclear Science and Engineering",
        "Nuclear Technology",
        "Annals of Nuclear Energy",
        "Progress in Nuclear Energy",
        "Journal of Nuclear Materials",
        "Nuclear Engineering and Design",
    ),
    units_and_formulas_notes=(
        "功率用 MWth/MWe；通量用 n/cm²·s",
        "公式用 amsmath；中子扩散/输运方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "燃耗用 MWd/tU；剂量用 mSv/a",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("MCNP", "ANSYS", "Python", "Serpent"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)