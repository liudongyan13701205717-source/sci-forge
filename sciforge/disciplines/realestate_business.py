"""房地产业务学科论文支持：开发/估价/资产管理体裁、APA 引用样式与财务指标记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="realestate_business",
    aliases=(
        "realestate_business",
        "房地产业务",
        "房地产",
        "房地产投资",
        "Real Estate Business",
        "Real Estate",
        "房地产开发",
        "物业估价",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（模型与数据）", "results（估价与投资结果）", "discussion（机理与市场意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（财务与市场分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；房地产研究常用 APA）",
    reporting_standards={
        "k1": "估价须遵循 IVSC 国际评估准则",
        "k2": "投资分析须遵循 CFA 估值报告规范",
        "k3": "系统综述须遵循 PRISMA 声明",
    },
    conventions=(
        "财务指标（Cap Rate、NOI、IRR）须给出计算口径",
        "物业类型与位置须说明",
        "数据来源与时间窗口须标注",
        "租赁条件须报告",
        "统计量给出 M/SD 与 95% CI",
    ),
    key_venues=(
        "Journal of Real Estate Finance",
        "Journal of Property Finance",
        "Real Estate Review",
        "Journal of Property Investment & Finance",
        "Journal of Real Estate Management",
    ),
    units_and_formulas_notes=(
        "金额用统一币种并注明年份",
        "Cap Rate 与 IRR 用 %",
        "统计量给出 M/SD 与 95% CI",
        "样本量与物业数量须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Yardi Voyager", "Yardi Matrix", "RealPage RealInsights", "MRI Real Estate", "Buildium", "AppFolio", "Rent Manager", "Zillow Zestimate", "Trulia", "Redfin", "JLL", "CBRE", "Savills", "Cushman", "WTW Valuations", "Knight Frank", "REBNY", "MLS", "Excel", "Tableau"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
