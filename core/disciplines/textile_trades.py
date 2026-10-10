"""纺织贸易学科论文支持：纺织贸易政策、供应链管理与关税合规研究体裁、Chicago 引用样式与贸易数据口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="textile_trades",
    aliases=(
        "textile_trades",
        "Textile trades",
        "纺织贸易",
        "纺织品国际贸易",
        "纺织供应链",
        "Textile trade policy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（贸易背景与研究问题）",
            "data and methods（贸易数据来源与计量方法）",
            "results（贸易流量与政策效应）",
            "discussion",
            "conclusions",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction（政策背景与目标）",
            "policy review（现行政策梳理）",
            "impact assessment（影响评估）",
            "recommendations",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份）",
    reporting_standards={
        "data_source": "贸易数据须注明来源（WITS、UN Comtrade、OECD）与 HS 编码版本",
        "hs_classification": "商品 HS 编码须明确（纺织类通常为 50-63 章）",
        "time_coverage": "数据时间范围与频率（年/月）须注明",
        "regional_scope": "国别与区域定义须与统计口径一致",
    },
    conventions=(
        "金额用统一币种（USD）与年份基准（现价/不变价）须声明",
        "HS 编码精确到 6 位，跨年度版本变更须说明",
        "贸易额区分 FOB 与 CIF 口径",
        "增长率以百分比表示并标注基期",
        "图表须标注数据来源与年份范围",
    ),
    key_venues=(
        "Journal of International Economics",
        "World Economy",
        "China Economic Review",
        "Textile Research Journal",
        "国际贸易问题",
    ),
    units_and_formulas_notes=(
        "贸易额用 USD（百万），汇率按 IMF 年均汇率换算",
        "关税税率用百分比（%），最惠国税与协定税分别列出",
        "增速用同比（%）与环比（%）区分",
        "市场份额用百分比，基期份额须注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("WITS", "UN Comtrade", "OECD iTrade", "World Integrated Trade Solution", "EViews", "Stata", "R", "Python (pandas, statsmodels)", "MATLAB", "Excel", "PowerBI", "Tableau", "Qlik Sense", "SAP Ariba", "Coupa", "SAP S/4HANA", "Oracle SCM Cloud", "Hyperledger Fabric", "Zotero", "VOSviewer"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
