"""社区卫生学科论文支持：社区卫生/环境卫生/WASH 体裁、APA 引用样式与公共卫生注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="community_sanitation",
    aliases=(
        "community_sanitation", "社区卫生", "community sanitation and hygiene",
        "public health sanitation", "环境卫生", "community environmental health",
        "WASH", "water sanitation hygiene", "水卫生与卫生设施",
        "community water supply", "社区卫生服务", "public health engineering",
        "公共卫生工程", "community waste management",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与卫生问题）",
            "literature review（文献综述）",
            "methods（方法与采样）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction（案例背景）",
            "site description（场地概况）",
            "method（研究方法）",
            "findings（发现）",
            "analysis（分析）",
            "implications（启示）",
            "references",
        ),
        "evaluation": (
            "abstract",
            "introduction",
            "intervention description（干预描述）",
            "evaluation design（评估设计）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Bulletin of the WHO 遵循 APA 规范）",
    reporting_standards={
        "empirical": "实证研究遵循 STROBE 声明",
        "participatory": "参与式研究遵循 CARE 声明",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "quantitative": "定量研究遵循 CONSORT 或 PRISMA 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "环境卫生干预研究须遵循 STROBE 或 CARE 声明",
        "饮用水质检测须报告采样方法、检测标准与仪器型号",
        "健康行为干预须报告基线水平与对照设计",
        "涉及弱势群体的研究须声明伦理审查与知情同意",
        "病原体检测须报告检测方法（如 PCR、ELISA）与灵敏度",
    ),
    key_venues=(
        "Bulletin of the World Health Organization",
        "Health & Place",
        "Social Science & Medicine",
        "Environmental Health",
        "International Journal of Environmental Research and Public Health",
        "The Lancet Planetary Health",
    ),
    units_and_formulas_notes=(
        "水质指标单位用 mg/L 或 μg/L；pH 无量纲",
        "采样时间须注明采样日期与时间",
        "空间数据须注明地理投影与比例尺",
        "涉及统计检验时给出效应量与置信区间",
        "时间用统一纪年格式；货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "SPSS", "Stata", "R (RStudio)", "Python (Jupyter)", "NVivo", "KoboToolbox", "ODK (Open Data Kit)", "CommCare", "DHIS2", "Epi Info (CDC)", "OpenEpi", "BioStat", "Tableau", "Microsoft Power BI", "WaterStat (UN)", "Google Earth Pro", "MPOWER", "Qualtrics", "OpenClinica", "REDCap", "EndNote", "Zotero", "LaTeX", "Google Sheets", "Miro", "OpenStreetMap"),
    category="工学",
    databases=("PubMed", "OpenAlex", "CNKI", "万方", "Crossref", "ScienceDirect", "Scopus"),
)
