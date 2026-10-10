"""其他人文学科与社会学学科论文支持：未被细类归入的社会学与社会科学交叉研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_human_society",
    aliases=(
        "other_human_society", "其他人文学科与社会学",
        "other human society", "其他人文学科与社会学",
        "human society and culture", "人类社会与文化",
        "sociology not elsewhere classified", "社会学未另分类",
        "social research", "社会研究",
        "political sociology", "政治社会学",
        "social theory", "社会理论",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（社会问题与理论定位）",
            "methodology（研究与抽样方法）",
            "results（发现与统计检验）",
            "discussion（机制解释与理论贡献）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（田野点/个案与历史情境）",
            "analysis（编码、主题与过程追踪）",
            "results（模式与比较发现）",
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
    citation_style="ASA",
    reporting_standards={
        "k1": "量化研究须报告样本量、抽样框、加权方案与响应率",
        "k2": "质性研究须按 COREQ 报告研究者立场、编码与信度",
        "k3": "因果推断须说明识别策略与反事实构造",
    },
    conventions=(
        "变量须报告操作化定义与测量工具来源",
        "问卷与量表须报告信度系数与效度检验",
        "访谈须报告时长、场域、语言与翻译方式",
        "伦理审查与知情同意须明确说明",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "American Sociological Review",
        "American Journal of Sociology",
        "Sociology",
        "Social Forces",
        "British Journal of Social Work",
        "《社会学研究》",
    ),
    units_and_formulas_notes=(
        "比率与概率用 % 或小数表示并注明分母",
        "人口数据注明统计口径与调查年份",
        "量表题项报告总分范围与理论极值",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "MAXQDA", "SPSS", "R (RStudio)", "Stata", "Python (pandas)", "Mplus", "AMOS", "HLM", "ModelTree", "Microsoft Excel", "Qualtrics", "SurveyMonkey", "World Values Survey", "Eurostat", "Pew Research Center", "EndNote", "Zotero", "LaTeX"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
