"""商品学/商品营销学科论文支持：商品流通与零售营销研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="merchandising",
    aliases=("merchandising", "商品学", "merchandising", "零售", "商品营销", "陈列", "买手", "retail"),
    paper_types={
        "research": ("abstract", "introduction（行业背景）", "methodology（调研设计）", "results（销售数据）", "discussion（策略建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（商品策略分析）", "results（业绩）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论框架）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "销售数据须注明口径与时间范围", "k2": "消费者调研须报告样本量与回收率", "k3": "策略评估须量化投入产出比"},
    conventions=("指标首次出现标注定义", "销售数据注明币种与价格口径", "图表报告均值与标准差", "样本须说明抽样方法", "品牌名称保留原文"),
    key_venues=("Journal of Retailing", "Journal of Business Research", "International Journal of Retail & Distribution Management", "Journal of Marketing", "Harvard Business Review"),
    units_and_formulas_notes=("销售额以币种/时间区间报告", "毛利率 = 毛利/销售额 × 100%", "坪效 = 销售额/营业面积", "周转率 = 销售额/平均库存", "统计以均值±标准差报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (tidyverse)", "STATA", "Power BI", "Tableau", "Excel", "SAS", "Google Analytics", "Adobe Analytics", "POS Data Platform", "Nielsen", "Mintel", "Kantar", "Euromonitor", "SAP Retail", "Oracle Retail", "Shopify", "Salesforce", "Zotero", "LaTeX"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
