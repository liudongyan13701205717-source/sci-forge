"""Data analysis 学科论文支持：统计/量化/建模分析体裁、APA 样式与数据记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="data_analysis",
    aliases=(
        "data_analysis", "数据分析", "统计数据分析", "quantitative analysis",
        "统计建模", "statistical analysis", "统计推断", "statistics",
        "数据建模", "数学分析",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究动机）",
            "methodology（数据、方法与假设）",
            "results（分析结果）",
            "discussion（讨论与意义）",
            "conclusions（结论与建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（案例背景）",
            "analysis（分析过程）",
            "conclusions（结论与启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（综述主体）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份）",
    reporting_standards={
        "quantitative": "定量分析遵循 CONSORT/STROBE 相关报告规范",
        "survey": "问卷调查遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "modeling": "统计建模须报告拟合优度、残差与诊断",
    },
    conventions=(
        "样本量、抽样方法、缺失值处理与异常值检测须报告",
        "统计检验与显著性水平（如 p<0.05）须明确；模型系数须报告 CI",
        "图与表须用三线表；数值报告均值±标准差",
        "公式用 amsmath 排版；符号首次出现处定义",
        "所有分析在方法部分给出软件版本与代码链接",
    ),
    key_venues=(
        "Journal of Data Science",
        "Statistical Science",
        "Journal of the Royal Statistical Society",
        "Journal of Business and Economic Statistics",
        "Journal of Applied Statistics",
        "Annals of Statistics",
        "Journal of Computational and Graphical Statistics",
    ),
    units_and_formulas_notes=(
        "比例用 %；指标无量纲；样本量用 n",
        "公式用 amsmath；显示公式仅在被引用时编号",
        "数值结果给出均值 ± SD 与样本量",
        "所有变量首次出现时给出符号与单位",
        "时间用统一纪年格式；货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R", "RStudio", "Python (NumPy/pandas)", "Jupyter Notebook", "SPSS", "SAS Enterprise", "Stata", "Minitab", "JMP", "Excel (Power Query)", "Tableau", "Power BI", "KNIME", "RapidMiner", "Weka", "Orange", "Qlik Sense", "D3.js", "Plotly", "Matplotlib", "Seaborn", "scikit-learn", "statsmodels", "JASP", "Jamovi", "R PyMC3", "Stan", "OpenRefine", "Google Sheets", "SQLite"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)
