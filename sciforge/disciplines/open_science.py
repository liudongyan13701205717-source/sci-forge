"""开放科学学科论文支持：开放科学/开放研究体裁、APA 引用样式与开放科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="open_science",
    aliases=("open_science", "开放科学", "开放研究", "开放获取", "open research"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与开放科学问题）",
            "methods（研究设计与数据）",
            "results（开放实践数据）",
            "discussion（开放科学意义）",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "policy background（政策背景）",
            "analysis（政策选项评估）",
            "recommendations（政策建议）",
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
    citation_style="APA 样式（作者-年份；R Soc Open Sci 遵循 Royal Society 规范）",
    reporting_standards={
        "policy_analysis": "政策分析遵循政策评估报告规范",
        "survey": "问卷调查遵循 AAPOR 报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "preregistration": "预注册研究遵循预注册报告规范",
    },
    conventions=(
        "开放实践（预注册、数据共享等）须明确",
        "数据与代码可用性声明须完整",
        "许可与版权信息须注明",
        "开放获取状态须报告",
        "利益冲突与资助声明须完整",
    ),
    key_venues=(
        "Royal Society Open Science",
        "PLOS ONE",
        "Research Integrity and Peer Review",
        "Quantitative Science Studies",
        "Science and Public Policy",
        "F1000Research",
    ),
    units_and_formulas_notes=(
        "比例用 %；时间用年份",
        "公式用 amsmath；开放度指标计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "显著性给出 p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("数据管理规划工具（DMPTool）", "FAIR 合规检查器", "版本控制（Git）"),
    category="交叉学科",
    databases=("OpenAlex", "Crossref", "Zenodo", "DOAJ", "arXiv"),
)