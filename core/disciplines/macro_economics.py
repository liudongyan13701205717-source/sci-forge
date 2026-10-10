"""宏观经济学学科论文支持：经济周期、政策分析与宏观计量研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="macro_economics",
    aliases=(
        "macro_economics",
        "宏观经济学",
        "macroeconomics",
        "经济周期",
        "财政政策",
        "货币政策",
        "econometrics",
        "business cycle",
        "aggregate economics",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（政策分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "识别策略须报告工具变量或自然实验设计",
        "k2": "VAR 模型报告滞后阶数与脉冲响应区间",
        "k3": "宏观计量按 IMF 数据手册口径说明",
    },
    conventions=(
        "GDP 使用实际值与不变价报告",
        "通胀率使用 CPI 与 PCE 分别报告",
        "识别策略须在引言明确说明",
        "模型估计报告标准误与稳健性检验",
        "时点符号使用 t 与 t-1 表示滞后",
    ),
    key_venues=(
        "American Economic Review",
        "Journal of Political Economy",
        "Quarterly Journal of Economics",
        "Econometrica",
        "Journal of Monetary Economics",
    ),
    units_and_formulas_notes=(
        "增长率以百分比报告",
        "利率以百分点报告",
        "GDP 以不变价美元报告",
        "弹性符号遵循微观经济学术惯例",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R", "Stata", "Python", "EViews", "MATLAB", "GARCH (Ruggero)", "Dynare", "GK (Galo-Kawall)", "SVM (Sims)", "BVAR (Barnes)", "Bayesian VAR (Luttkiewicz)", "FRED", "Bloomberg", "IMF WEO", "OECD Stats", "World Bank WDI", "LaTeX", "TeXstudio", "Kaggle", "Tableau"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
