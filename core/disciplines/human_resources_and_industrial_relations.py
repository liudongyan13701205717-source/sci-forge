"""人力资源与劳动关系学科论文支持：劳动关系/工会/集体谈判研究体裁、APA 引用样式与劳动经济学口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="human_resources_and_industrial_relations",
    aliases=(
        "human_resources_and_industrial_relations",
        "人力资源与劳动关系",
        "劳动关系学",
        "Human Resources and Industrial Relations",
        "Industrial Relations",
        "Labor Relations",
        "工会研究",
        "Employment Law",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；劳动关系研究亦常引文献法规范）",
    reporting_standards={"k1": "劳动经济学研究须说明工资口径", "k2": "工会案例须注明谈判周期", "k3": "综述须说明证据分级"},
    conventions=(
        "工资/工时/失业率注明统计口径",
        "雇佣形式须区分类型",
        "工会覆盖率给出口径",
        "案例须说明司法管辖区",
        "法律条款须给出法条编号",
    ),
    key_venues=(
        "Industrial and Labor Relations Review",
        "Industrial Relations",
        "British Journal of Industrial Relations",
        "Human Relations",
        "Journal of Labor Economics",
    ),
    units_and_formulas_notes=(
        "工资数据以时薪/年薪单位统一",
        "失业率/覆盖率给出百分比口径",
        "工时以小时/周计",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "R", "Python", "MATLAB", "Excel", "NVivo", "Tableau", "Power BI", "SAP SuccessFactors", "Oracle HCM", "Workday", "Qualtrics", "Endnote", "Jusline", "BLS 美国劳工统计局", "ILOSTAT", "Wind 万得", "BambooHR", "ADP Workforce Now"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis"),
)
