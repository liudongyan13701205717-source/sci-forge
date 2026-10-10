"""社会福利未另分类学科论文支持：社会福利政策的比较分析与制度评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="welfare_not_elsewhere_classified",
    aliases=(
        "welfare not elsewhere classified",
        "社会福利",
        "社会救助",
        "社会服务",
        "welfare policy",
        "social assistance",
        "social services",
        "社会福利制度",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "literature review（理论视角与文献综述）",
            "research design（研究设计与数据来源）",
            "findings（研究发现）",
            "discussion（讨论与政策含义）",
            "conclusion",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "policy background（政策背景与演变）",
            "policy content analysis（政策文本分析）",
            "implementation and impact（执行与影响评估）",
            "comparison and recommendations（比较与政策建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical foundations（福利国家理论综述）",
            "regional welfare models（区域福利模式比较）",
            "critical perspectives（批判性视角）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "data transparency": "数据来源、样本量、时间范围与抽样方法须完整披露",
        "ethics approval": "涉及人的研究须说明伦理审查编号与知情同意程序",
        "policy context": "政策分析须注明分析时点、政策文本版本与法律渊源",
        "measurement validity": "福利效果评估须说明指标定义与效度验证方法",
    },
    conventions=(
        "福利制度类型按 Esping-Andersen 三分法标注：自由主义/保守主义/社会民主主义",
        "政策分析须区分政策输入、政策过程与政策产出三个层次",
        "社会指标须注明来源（如 OECD、ILO、国家统计局）与统计口径",
        "比较研究须说明可比性前提与差异处理（如汇率、购买力平价）",
        "弱势群体描述避免污名化语言，使用尊重性表述",
    ),
    key_venues=(
        "Journal of Social Policy",
        "European Journal of Social Security",
        "British Journal of Social Work",
        "Social Policy & Administration",
        "International Journal of Social Welfare",
    ),
    units_and_formulas_notes=(
        "收入不平等指标：基尼系数（Gini Coefficient）、洛伦兹曲线",
        "福利支出占 GDP 比重（%）：公共社会支出/GDP×100",
        "贫困线：以中位数收入 50% 为相对贫困线；以基本生活需求法测算绝对贫困",
        "社会政策指数（SIP）：综合覆盖范围、充分性与去商品化维度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R 语言统计分析", "Stata 计量软件", "NVivo 质性分析软件", "MAXQDA 质性编码工具", "ATLAS.ti 文本分析平台", "SPSS 统计分析软件", "OECD i-Library 政策数据检索平台", "World Bank Open Data 世界经济数据", "国家统计局数据检索系统", "Python 数据处理（pandas）", " Gephi 社会网络分析", "VosViewer 文献计量可视化", "CiteSpace 知识图谱可视化", "Tableau 数据可视化", "LaTeX 学术排版", "EndNote 文献管理", "SurveyMonkey 在线问卷平台", "Qualtrics（在线调查平台）", "Excel（数据管理）", "Power BI（商业智能）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "PolicyBench 政策比较数据库工具", "ILOSTAT 国际劳工统计数据库", "Eurostat 欧盟统计数据库"),
)
