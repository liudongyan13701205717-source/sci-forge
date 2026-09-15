"""心理学科论文支持：APA 7、预注册与效应量报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="psychology",
    aliases=("psychology", "心理学", "认知", "cognitive", "行为", "behavior",
             "社会心理", "social psychology", "发展", "developmental"),
    paper_types={
        "empirical": (
            "abstract",
            "introduction（理论与假设）",
            "method（participants / materials / procedure / data analysis 分小节）",
            "results（检验、效应量与补充分析）",
            "discussion（解释、局限与理论意义）",
            "references",
        ),
        "meta_analysis": (
            "abstract",
            "introduction",
            "method（检索、纳排、编码、效应量模型）",
            "results（森林图、异质性、发表偏倚）",
            "discussion",
            "references",
        ),
        "registered_report": (
            "abstract",
            "introduction（理论与假设）",
            "methods（阶段 1 预注册的分析计划）",
            "results（阶段 2 按计划执行）",
            "discussion",
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
        "方法内分 participants/materials/procedure 小节；量表给出信度（Cronbach's α/ω）",
        "p 值格式 APA：p = .03（去掉前导零），p < .001 单独表述",
        "统计符号斜体（M、SD、t、F、p、d、η²）",
        "结果按假设顺序报告，每个假设对应明确检验",
        "讨论先回应假设再谈局限，避免过度因果表述",
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
)
