"""应用经济学学科论文支持：实证经济、政策评估、产业与市场分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="applied_economics",
    aliases=(
        "applied economics",
        "Applied Economics",
        "应用经济学",
        "实证经济学",
        "empirical economics",
        "policy evaluation",
        "产业经济学",
        "政策评估",
        "劳动经济学",
        "health economics",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（政策/问题背景与贡献）",
            "theoretical framework",
            "data and methodology（数据来源、变量定义）",
            "empirical strategy（识别假设、因果推断）",
            "results",
            "robustness and heterogeneity",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "literature review",
            "open questions",
            "future research",
            "references",
        ),
        "working_paper": (
            "abstract",
            "introduction",
            "body",
            "conclusion",
            "references",
        ),
    },
    citation_style="芝加哥（Chicago Notes-Bibliography）或哈佛（Harvard Author-Date）",
    reporting_standards={
        "identification": "识别策略（DID/RD/IV/PSM/合成控制）与识别假设须明确声明",
        "data": "数据来源、时间范围、样本筛选与缺失值处理须说明",
        "estimation": "估计量、聚类层级（cluster）、稳健性检验（SE/t）须报告",
        "robustness": "安慰剂检验、工具变量有效性（first stage F）、样本子集须报告",
        "ethics": "涉及微观数据时须声明隐私合规与伦理审查",
    },
    conventions=(
        "变量定义表放附录或首段；关键变量用符号（Y/D/X/Z）说明",
        "表格按 OLS→2SLS→FE→DiD 递进；每列给 n、R²、聚类 SE",
        "统计显著性标记 *p<0.1 **p<0.05 ***p<0.01",
        "计量软件 Stata/R 版本须注明；Do-file/R 脚本公开",
        "图表中英对照；横纵轴单位与样本量必须标注",
    ),
    key_venues=(
        "The Review of Economics and Statistics",
        "American Economic Journal: Applied Economics",
        "Journal of Applied Economics",
        "Journal of Econometrics",
        "The Economic Journal",
        "Journal of Labor Economics",
    ),
    units_and_formulas_notes=(
        "货币单位统一：元、美元、人民币千元；增长率 %",
        "面板数据：T=时间、N=单位；固定效应 FE / 随机效应 RE",
        "识别：DID = (Post×Treat) 系数；IV 一阶段 F 值 >10",
        "软件：Stata/R/EViews/Matlab/Gauss",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "RStudio", "EViews", "Gauss", "Matlab", "SAS", "Python (Statsmodels/Linearmodels)", "Excel", "Tableau", "Power BI", "Wind 金融终端", "Bloomberg Terminal", "World Bank WDI", "IMF WEO", "OECD Stat", "LaTeX", "Zotero", "CausalImpact（因果推断工具）", "MatchIt（匹配分析工具）"),
    category="经济学",
    databases=("EconLit", "Web of Science", "NBER Working Papers", "SSRN", "CNKI", "万方", "OpenAlex", "CEIC 数据库", "CSMAR 数据库"),
)
