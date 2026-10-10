"""出版学/出版传播学科论文支持：出版流程/发行传播/数字出版体裁、APA 引用与出版指标注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="publishing",
    aliases=("publishing", "出版学", "出版", "编辑学", "出版传播", "图书发行", "digital publishing", "scholarly publishing"),
    paper_types={
        "research": ("abstract", "introduction（出版问题与背景）", "methodology（方法与数据）", "results（出版/传播数据）", "discussion（行业启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（出版案例）", "analysis（流程与模式分析）", "results（销售与传播结果）", "discussion（经验总结）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions（出版趋势）", "references"),
    },
    citation_style="APA 7（图书/期刊条目按版次与出版年排布）",
    reporting_standards={"bibliometrics": "文献计量遵循数据源与年份说明", "sales_survey": "发行调查注明采样框与口径", "citation_analysis": "引证分析注明数据库与去重方法"},
    conventions=("出版物须标注版次、印刷次与 ISBN", "引文/引证分析注明数据库与统计年份", "发行量与销售口径须区分（印数/印次/册次）", "数字化指标（下载/引用/被引）注明平台", "术语（编辑/审读/出版）须界定"),
    key_venues=("Journal of Publishing", "Publishing Research Quarterly", "Journal of Scholarly Publishing", "中国出版", "编辑之友"),
    units_and_formulas_notes=("发行/销售数给出绝对值与时间窗（万册/册次）", "引证指标给出年份口径（Web of Science/Scopus/Google Scholar）", "下载量与访问量须区分", "定价与折扣给出币种与年份"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "软件与代码", "教案与教材", "译文", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "Python（Pandas）", "Excel", "Tableau", "NVivo", "Gephi", "MATLAB", "Minitab", "JMP", "Qualtrics", "SurveyMonkey", "EndNote", "Zotero", "Mendeley", "LaTeX", "Word", "BibTeX", "VosViewer"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
