"""太平洋人民健康与福祉学科论文支持：太平洋岛屿人群健康、传统医学、慢性病与文化适应性卫生。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pacific_peoples_health_and_wellbeing",
    aliases=("Pacific Peoples Health And Wellbeing", "太平洋人民健康与福祉", "Pacific Health", "Pacific Public Health", "Pacific Health Equity", "Pacific Chronic Disease", "Pacific Mental Health", "Pacific Traditional Healing"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 / Vancouver",
    reporting_standards={
        "k1": "原住民健康研究遵循IRPA太平洋研究伦理准则", "k2": "系统综述遵循PRISMA筛选流程", "k3": "临床试验遵循CONSORT报告规范"
    },
    conventions=("涉及原住民健康数据须遵循OCAP原则与社区同意", "传统医学描述须尊重当地习俗并说明知识归属", "流行病学数据须结合社会决定因素（SDOH）进行解释", "跨文化健康干预须采用文化适配框架（如Culturally Tailored）", "心理健康研究须尊重太平洋人民对健康/精神的整体理解"),
    key_venues=("Pacific Health Dialogue", "Pacific Health Research", "Journal Of Health Care For The Poor And Underserved", "International Journal For Equity In Health", "Health & Transformation", "The Lancet Public Health"),
    units_and_formulas_notes=("疾病编码遵循ICD-11与公共卫生分类标准", "流行病学率报告须区分发生率、患病率与病死率", "传统医学疗效评估须包含安慰剂对照与文化敏感指标", "跨文化健康量表须报告信效度跨组比较结果"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "SAS", "NVivo", "MAXQDA", "ATLAS.ti", "SurveyMonkey", "Qualtrics", "Google Forms", "RevMan", "JBI Systematic Review Software", "EpiTools", "OpenEpi", "Tableau", "Microsoft Power BI", "Zotero", "Endnote", "DHIS2", "KoboToolbox"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "Cochrane", "PubMed"),
)
