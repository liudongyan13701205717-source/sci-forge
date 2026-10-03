"""人机工效学学科论文支持：人机工效学/人因工程体裁、APA 引用样式与人机工效学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ergonomics",
    aliases=("ergonomics", "人机工效学", "人因工程", "工效学", "human factors"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与工效学问题）",
            "methods（实验设计与任务）",
            "results（绩效与负荷数据）",
            "discussion（工效学意义）",
            "references",
        ),
        "usability_study": (
            "abstract",
            "introduction",
            "methods（用户与任务）",
            "results（可用性指标）",
            "discussion（设计建议）",
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
    citation_style="APA 样式（作者-年份；Ergonomics 遵循 Taylor & Francis 规范）",
    reporting_standards={
        "experimental": "实验研究遵循 APA 报告规范",
        "usability": "可用性研究遵循可用性报告规范",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "preregistration": "预注册研究遵循预注册报告规范",
    },
    conventions=(
        "参与者特征与任务设计须报告",
        "绩效指标（反应时、错误率等）须定义",
        "负荷测量（NASA-TLX 等）须注明",
        "环境条件（照明、噪声等）须报告",
        "统计显著性阈值与效应量须明确",
    ),
    key_venues=(
        "Ergonomics",
        "Human Factors",
        "Applied Ergonomics",
        "International Journal of Industrial Ergonomics",
        "Behaviour & Information Technology",
        "Human Factors and Ergonomics in Manufacturing",
    ),
    units_and_formulas_notes=(
        "反应时用 ms；负荷用量表分；姿势用角度",
        "公式用 amsmath；负荷指数与绩效计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "效应量给出 Cohen's d 或 η² 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("人体测量数据库", "工效学仿真软件", "姿势评估工具（RULA/REBA）"),
    category="交叉学科",
    databases=("OpenAlex", "Crossref", "PubMed", "arXiv"),
)