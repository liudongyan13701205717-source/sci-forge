"""未来学学科论文支持：趋势预测、情景规划、技术演化与可持续发展研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="futurology",
    aliases=("futurology", "future studies", "未来学", "趋势预测", "情景规划", "技术演化", "可持续发展研究", "前瞻性研究"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "forecasting": "预测研究须报告预测方法、数据来源与置信度",
        "scenario": "情景规划须报告情景假设、驱动因素与时间尺度",
        "trends": "趋势分析须报告数据来源、时间跨度与分析方法"
    },
    conventions=(
        "预测方法须明确说明（如德尔菲法、情景分析）",
        "时间尺度须明确标注（短期/中期/长期）",
        "数据来源须注明出处与时间范围",
        "情景假设须区分驱动因素与不确定性因素",
        "结论须区分预测与推测"
    ),
    key_venues=(
        "Futures",
        "Journal of Futures Studies",
        "Technological Forecasting and Social Change",
        "Technological Forecasting and Social Change",
        "Global Environmental Change"
    ),
    units_and_formulas_notes=(
        "预测时间用年（yr）",
        "增长率用 %/yr",
        "置信区间用百分比",
        "模型预测精度用 MAPE 或 RMSE",
        "人口/能源等变量须注明单位和年份"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Delphi Technique Software", "Scenario Planning Tool", "Trend Analysis Software", "Future Studies Software", "Forecasting Model", "Simulation Software", "System Dynamics Software", "Agent-Based Model", "Data Visualization Tool", "Big Data Analysis Platform", "Predictive Analytics Tool", "Technology Roadmapping Tool", "Horizon Scanning Tool", "Strategy Mapping Tool", "Foresight Platform", "Future Vision Tool", "Trend Monitoring Software", "Future Studies Research Tool", "Forecasting Model Software", "Scenario Development Platform"),
    category="管理学",
    databases=("OpenAlex", "Crossref"),
)
