"""人机交互学科论文支持：交互设计/可用性体裁、ACM 引用样式与 HCI 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="human_computer_interaction",
    aliases=("human_computer_interaction", "人机交互", "HCI", "交互设计",
             "可用性"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "study design（研究设计）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "user_study": (
            "abstract",
            "introduction",
            "participants（参与者）",
            "procedure（流程）",
            "measures（测量）",
            "results（结果与分析）",
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
    citation_style="ACM 样式（作者-年份；CHI/UIST 遵循 ACM 规范）",
    reporting_standards={
        "user_study": "用户研究遵循 CHI 论文检查清单",
        "qualitative": "质性研究遵循 COREQ/SRQR 规范",
        "experimental": "实验遵循 APA 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "accessibility": "无障碍研究遵循 WCAG 指南",
    },
    conventions=(
        "参与者数量与招募方式须报告",
        "研究伦理（IRB、知情同意）须说明",
        "测量工具与量表须注明",
        "统计方法与效应量须报告",
        "定性分析（编码、主题）须透明",
    ),
    key_venues=(
        "CHI",
        "UIST",
        "CSCW",
        "International Journal of Human-Computer Studies",
        "Human-Computer Interaction",
        "ACM Transactions on Computer-Human Interaction",
    ),
    units_and_formulas_notes=(
        "时间用 s/min；效应量用 Cohen's d；显著性用 p",
        "公式用 amsmath；统计模型须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "量表分数注明范围与信度（Cronbach's α）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Figma", "Maze", "Python", "R"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Semantic Scholar", "arXiv"),
)