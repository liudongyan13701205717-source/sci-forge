"""社区护理学科论文支持：社区护理/公共卫生护理体裁、CARE 声明与护理研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="community_nursing",
    aliases=(
        "community_nursing", "社区护理", "community health nursing",
        "公共卫生护理", "community health services", "family nursing",
        "family nursing practice", "community case management",
        "社区护理实践", "community midwifery", "社区卫生服务",
        "community health worker", "public health nursing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与社区健康问题）",
            "literature review（文献综述）",
            "methods（方法与样本）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction（案例背景）",
            "participant profile（参与者概况）",
            "method（研究方法）",
            "findings（发现）",
            "analysis（分析）",
            "implications（启示）",
            "references",
        ),
        "quality_improvement": (
            "abstract",
            "introduction",
            "program description（项目描述）",
            "intervention（干预措施）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Community Health Nursing Research 遵循 APA 规范）",
    reporting_standards={
        "participatory": "参与式研究遵循 CARE 声明",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "quantitative": "定量研究遵循 CONSORT 或 PRISMA 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "社区护理实践报告须遵循 CARE 声明或 SRQR 规范",
        "患者隐私须遵循当地法规，报告前须去标识化",
        "慢性病管理干预须报告依从率与不良事件",
        "健康筛查研究须报告受试者知情同意过程与伦理审批编号",
        "护理术语首次出现处须给出全称与缩写",
    ),
    key_venues=(
        "Community Health Nursing Research",
        "Journal of Advanced Nursing",
        "Nurse Education Today",
        "Journal of Nursing and Health Sciences",
        "Public Health Nursing",
        "Journal of Clinical Nursing",
    ),
    units_and_formulas_notes=(
        "时间用统一纪年格式；剂量单位用国际标准（mg、mL、g）",
        "血压、血糖等生理指标须注明测量方法与正常参考值",
        "量表得分须说明计分方式与信度系数",
        "涉及统计检验时给出效应量（Cohen's d、η²）",
        "涉及成本效益分析时给出货币单位与折现率",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Epi Info (CDC)", "REDCap", "SPSS", "Stata", "R (RStudio)", "Python (Jupyter)", "NVivo", "ATLAS.ti", "DHIS2", "Tableau", "KoboToolbox", "SurveyMonkey", "Qualtrics", "OpenClinica", "CommCare", "EpiStat", "BioStat", "OpenEpi", "MPOWER", "Microsoft Power BI", "EndNote", "Zotero", "Mendeley", "LaTeX", "Google Sheets", "Miro", "Microsoft Teams", "Google Forms"),
    category="医学",
    databases=("PubMed", "Cochrane Library", "CINAHL", "OpenAlex", "CNKI", "万方", "Crossref"),
)
