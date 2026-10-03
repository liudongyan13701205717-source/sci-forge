"""社会科学学科论文支持：定性/定量/混合设计与 COREQ/SRQR 规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_science",
    aliases=("social science", "社会科学", "社会学", "sociology", "政治学",
             "political science", "人类学", "anthropology", "教育学", "education"),
    paper_types={
        "qualitative": (
            "abstract",
            "introduction（问题与理论框架）",
            "methodology（田野点、抽样、资料收集、reflexivity）",
            "findings（按主题组织，对话材料佐证）",
            "discussion（理论对话与局限）",
            "references",
        ),
        "quantitative": (
            "abstract",
            "introduction（理论与假设）",
            "data and methods（数据、变量、模型）",
            "findings（结果与稳健性）",
            "conclusion（理论含义与政策含义）",
            "references",
        ),
        "mixed_methods": (
            "abstract",
            "introduction",
            "research design（混合设计类型与整合点）",
            "quantitative strand（定量线）",
            "qualitative strand（定性线）",
            "integration（两线整合与解释）",
            "discussion",
            "references",
        ),
    },
    citation_style="Chicago 作者-年份或 APA 7（视期刊）",
    reporting_standards={
        "qualitative": "定性研究透明度按 COREQ/SRQR 清单：研究者位置、抽样逻辑、饱和判断",
        "quantitative": "抽样设计、加权与缺失数据处理须说明；调查数据给出样本框与回应率",
        "ethics": "知情同意、匿名化与被试保护声明；敏感议题给出伦理审查信息",
        "positionality": "reflexivity 声明：研究者身份与立场对资料解释的影响",
        "data": "定性材料（访谈转写/田野笔记）去标识化存档并说明可获取性",
    },
    conventions=(
        "理论框架先行：明确对话的理论传统与概念定义",
        "定性引用对话材料给转写行号/时间戳，并标注受访者编号",
        "定量表格三线制；类别变量给频数与百分比（注明基数 N）",
        "概念操作化透明：概念 → 指标 → 测量的链条在方法中给出",
        "混合设计用联合展示表（joint display）呈现整合",
    ),
    key_venues=(
        "American Sociological Review",
        "American Journal of Sociology",
        "Social Forces",
        "World Politics",
        "Annual Review of Sociology",
    ),
    units_and_formulas_notes=(
        "百分比给出基数 N；加权数据注明权重变量",
        "指数/量表构造说明标准化方法与信度",
        "多层/面板数据说明层级结构与时点",
        "定性材料引用格式统一（受访者编号：行号）",
        "效应量与显著性并列报告，避免只报 p 值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("Stata", "R", "Python", "SPSS", "NVivo"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
