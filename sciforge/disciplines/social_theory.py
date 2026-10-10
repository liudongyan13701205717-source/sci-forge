"""社会理论学科论文支持：理论重构/批判/概念操作化体裁、ASA 引用样式与文本分析注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_theory",
    aliases=("social_theory", "社会理论", "批判理论", "结构主义", "符号互动论", "解释社会学"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="ASA 样式（作者-年份，如 Smith, 2020；文末悬挂缩进）",
    reporting_standards={
        "conceptualization": "核心概念须给出操作性定义，并说明与相邻概念的边界",
        "stance": "理论立场（实证主义/解释主义/批判）须显式声明，不混用",
        "attribution": "引证与解释须区分：引号内为原文引述，其余为作者解释",
    },
    conventions=(
        "理论命题与经验证据分层陈述，不混写",
        "关键概念首次出现给出中英对照与操作性定义",
        "经典文本引用标注原出版年份与再版年份（如 Durkheim, 1897/1951）",
        "文献谱系按学派归置（功能主义/冲突论/符号互动/女性主义/后现代）",
        "同一概念全文同一译名，避免一词多译",
    ),
    key_venues=(
        "Society",
        "Theory and Society",
        "Critical Review of Sociology",
        "Sociological Theory",
        "Theory, Culture & Society",
    ),
    units_and_formulas_notes=(
        "文本分析给出语料总量、编码类别数与编码一致性（Cohen's κ）",
        "共现/共引网络指标（次数、中心性）注明计算窗口与阈值",
        "量表条目数与信度（Cronbach's α）并列给出",
        "统计符号斜体（M、SD、p、d），效应量给置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "MAXQDA", "DiscourseWorkbench", "AntConc", "Wmat", "uWc", "LancsBox", "STYLO", "R", "Python", "Gephi", "CiteSpace", "VOSviewer", "Connected Papers", "OSF", "RefManageX", "EndNote", "LaTeX", "Microsoft Word"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
