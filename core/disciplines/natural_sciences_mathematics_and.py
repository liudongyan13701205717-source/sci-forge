"""自然科学、数学与统计学学科论文支持：综合理科数学统计研究体裁、学术引用规范与理科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="natural_sciences_mathematics_and",
    aliases=("natural_sciences_mathematics_and", "自然科学、数学与统计学",
             "理科与统计学", "自然科学数学统计", "理综数学统计"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methodology（理论/实验/统计方法）",
            "results（推导/实验/统计结果）",
            "discussion（结论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（研究系统或数据场景）",
            "analysis（建模与统计分析）",
            "results（求解/验证结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论基础综述）",
            "evidence synthesis（现有方法证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式（理科常用）",
    reporting_standards={
        "experimental": "实验遵循科学报告规范",
        "statistical": "统计遵循 ASA 统计声明",
        "mathematical": "数学遵循数学论文规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "可复现性遵循科学可复现性指南",
    },
    conventions=(
        "实验条件与参数须完整报告",
        "统计方法与检验须定义",
        "显著性水平 α 须注明",
        "数据/代码可用性须说明",
        "样本量与效应量须报告",
    ),
    key_venues=(
        "Nature",
        "Science",
        "PNAS",
        "Journal of Statistical Planning and Inference",
        "Statistical Science",
    ),
    units_and_formulas_notes=(
        "SI 单位",
        "公式用 amsmath；统计方程须编号",
        "显著性水平 α 须注明",
        "p 值/置信区间须报告",
        "变量定义须完整",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python（NumPy/SciPy）", "R", "RStudio", "Mathematica", "Maple", "Julia", "Stata", "SAS", "Jupyter Notebook", "LaTeX", "SPSS", "JMP", "Pandas", "scikit-learn", "Matplotlib", "OriginLab", "Excel", "Git/GitHub", "Wolfram Alpha"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "万方"),
)
