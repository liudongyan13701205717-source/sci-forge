"""表演艺术学科论文支持：戏剧/演出/实践体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="performing_arts",
    aliases=("performing_arts", "表演艺术", "戏剧学", "舞台艺术"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "analysis（分析）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "performance_analysis": (
            "abstract",
            "introduction",
            "performance（演出）",
            "analytical framework（分析框架）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
        "practice_based": (
            "abstract",
            "introduction",
            "creative process（创作过程）",
            "performance（演出）",
            "reflection（反思）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；Theatre Journal 遵循 Chicago 规范）",
    reporting_standards={
        "performance": "演出分析遵循演出分析报告规范",
        "practice": "实践研究遵循创作实践报告规范",
        "historical": "历史研究遵循史料来源报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "演出信息（剧名/剧团/日期/场地）须完整",
        "剧作版本须注明",
        "舞台语境须交代",
        "引文给出页码",
        "分析框架须明确",
    ),
    key_venues=(
        "Theatre Journal",
        "Theatre Research International",
        "TDR: The Drama Review",
        "Performance Research",
        "New Theatre Quarterly",
        "Asian Theatre Journal",
    ),
    units_and_formulas_notes=(
        "时长用 分:秒",
        "引文给出页码",
        "版本与版次须注明",
        "时间用统一纪年格式",
        "货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "艺术作品"),
    tools=(
        "演出数字档案系统",
        "演出录像分析软件",
    ),
    category="艺术学",
    databases=("DOAJ", "OpenAlex", "Crossref", "CNKI"),
)