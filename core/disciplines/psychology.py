"""心理学科论文支持：实证/元分析体裁、APA 7、预注册与效应量报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="psychology",
    aliases=(
        "psychology",
        "心理学",
        "Psychology",
        "Cognitive psychology",
        "Social psychology",
        "认知",
        "社会心理",
        "发展",
        "Developmental",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（理论与假设）",
            "methodology（参与者、材料、程序与统计）",
            "results（检验、效应量与补充分析）",
            "discussion（解释、局限与理论意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（个案描述）",
            "analysis（心理评估与分析）",
            "results（评估与干预结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合与元分析）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份，如 (Smith, 2020)；文末悬挂缩进）",
    reporting_standards={
        "preregistration": "预注册（OSF/AsPredicted）与分析计划披露：注册号须给出，偏离须说明",
        "statistics": "效应量+置信区间必报（不只报 p 值）；检验假设与软件包版本给出",
        "sample": "样本量确定方式（先验功效分析：效应量、α、power）与排除标准预先声明",
        "openness": "数据/材料共享声明（OSF/期刊开放科学徽章）",
        "ethics": "IRB 批准与知情同意；被试报酬说明",
    },
    conventions=(
        "被试招募与人口学信息须完整，量表给出信度（Cronbach's α/ω）",
        "p 值格式 APA：p = .03（去掉前导零），p < .001 单独表述",
        "统计符号斜体（M、SD、t、F、p、d、η²）",
        "预注册计划须公开，偏离须解释",
        "统计模型选择须说明依据，效应量须报置信区间",
    ),
    key_venues=(
        "Psychological Science",
        "Journal of Experimental Psychology: General",
        "Journal of Personality and Social Psychology",
        "Psychological Bulletin",
        "Cognitive Psychology",
    ),
    units_and_formulas_notes=(
        "效应量 Cohen's d / Hedges' g / η²p / OR 按设计选择并解释口径",
        "多层/重复测量数据用 ICC 与混合模型说明结构",
        "Bootstrap CI 注明重抽样次数（如 5000 次）",
        "测量给量表条目数、计分方向与信度",
        "功效分析给出软件（G*Power/pwr）与参数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "JASP", "PSPP", "NVivo", "ATLAS.ti", "MAXQDA", "E-Prime", "PsychoPy", "OpenSesame", "Inquisit", "Presentation", "E-SPS", "ECharts", "OSF", "Qualtrics", "SurveyMonkey", "G*Power", "Mplus", "Stata"),
    category="理学",
    databases=("OpenAlex", "Crossref", "Semantic Scholar", "CNKI"),
)
