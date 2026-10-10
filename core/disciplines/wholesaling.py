"""批发学科论文支持：批发流通模式、批发市场运作与供应链优化研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wholesaling",
    aliases=(
        "wholesaling",
        "批发",
        "批发市场",
        "B2B 贸易",
        "wholesale market",
        "B2B trading",
        "wholesale distribution",
        "批发分销",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（行业背景与问题）",
            "theoretical framework（理论基础与假设）",
            "data collection and methodology（数据与方法）",
            "results（实证结果）",
            "discussion（讨论与理论贡献）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "market overview（市场概况描述）",
            "wholesaling model（批发模式描述）",
            "supply chain analysis（供应链分析）",
            "efficiency and impact（效率与影响评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "wholesale market evolution（批发市场演变）",
            "channel dynamics（渠道动态综述）",
            "digital wholesale trends（数字化批发趋势）",
            "research agenda",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "market definition": "批发市场研究须明确界定商品类别、地理范围与时间窗口",
        "transaction data": "交易数据须标注采集方式（电子/纸质/估算）与完整性说明",
        "channel relationships": "批发-零售关系研究须说明渠道权力（channel power）测量方法",
        "efficiency metrics": "市场效率评估须采用标准化指标（如交易量、价格波动、周转天数）",
    },
    conventions=(
        "批发类型区分制造商批发、代理商批发与经纪人批发",
        "价格单位统一使用元/吨（大宗品）或元/件（包装品）",
        "批发层级标注 W1→W2→R 传递路径与加价率",
        "市场份额数据须标注统计口径（按交易额或按交易量）",
        "大宗商品贸易须标注交割条件（CFR/CIF/FOB）",
    ),
    key_venues=(
        "Journal of Marketing Channels",
        "Journal of Distribution Science",
        "Industrial Marketing Management",
        "European Journal of Marketing",
        "Journal of Business & Industrial Marketing",
    ),
    units_and_formulas_notes=(
        "批发加价率 =（批发价-进货价）/进货价×100%",
        "渠道贡献利润 = 批发毛利 - 运营成本 - 渠道管理费",
        "库存周转天数 = 365 / 库存周转率（天）",
        "市场份额 = 企业批发额 / 市场总批发额×100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SAP ERP 企业资源计划", "Oracle SCM Cloud 供应链管理", "Microsoft Dynamics 365 商务管理", "SAP Ariba 供应链协同平台", "Coupa 采购与支出管理", "Tableau 数据可视化", "Power BI 商业智能分析", "Python 数据分析（pandas）", "R 语言统计分析", "Stata 计量软件", "SPSS 统计分析软件", "Vensim 系统动力学建模", "AnyLogic 多智能体仿真", "MATLAB 数值计算", "LaTeX 学术排版", "EndNote 文献管理", "VosViewer 文献计量可视化", "CiteSpace 知识图谱可视化", "Google Trends 市场趋势分析", "Wind 金融数据终端"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
