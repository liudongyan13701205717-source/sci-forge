"""形而上学学科论文支持：存在、实体、属性、因果、时间等问题的本体论论证与思辨体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="metaphysics",
    aliases=("metaphysics", "形而上学", "metaphysical_philosophy", "ontology", "metaphysics_theory", "being_ontology", "substance_theory", "property_theory", "causation_philosophy", "mind_body_problem", "time_theory_philosophy"),
    paper_types={
        "research": ("abstract", "introduction（问题动机与文献定位）", "methodology（论证方法与概念分析）", "results（论证结论）", "discussion（反驳与回应）", "references"),
        "case_study": ("abstract", "introduction", "case description（经典或当代案例）", "analysis（概念分析与论证）", "results（结论）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（主要理论谱系）", "evidence synthesis（论证力量与漏洞评析）", "future directions", "references"),
    },
    citation_style="Chicago 样式（哲学惯例；引文须标注版本与页码）",
    reporting_standards={"k1": "论证须明确前提与结论并标注推理类型", "k2": "反驳须区分强反驳与弱反驳并给出应对", "k3": "跨语言概念须注明版本与译者"},
    conventions=("概念界定须先于使用", "区分语义、语法与本体论层面", "形式化论证须标注推理规则", "引用经典文本须注明译本或版本", "结论须区分绝对与条件式"),
    key_venues=("Journal of Philosophy", "Noûs", "Mind", "Philosophical Review", "Australasian Journal of Philosophy"),
    units_and_formulas_notes=("概念分析须区分日常与学术用法", "形式化符号须先定义", "论证有效性与可靠性须分开评估", "模态逻辑式须标注量词作用域"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Prolog（形式化论证）", "Coq（形式化证明）", "Isabelle（形式化验证）", "Mizar（自动证明）", "Ontology editor（Protege）", "SPARQL（本体查询）", "DOLCE 本体框架", "SUMO 本体", "Cyc 知识库", "WordNet（概念关联）", "VOSviewer（知识图谱）", "CiteSpace（引文网络）", "Semantic Web tools", "Set theory toolbox", "Modal logic library", "First-order logic prover", "Ontology reasoning engine", "Metamath", "Lean（定理证明）", "HOL4（高阶逻辑证明）"),
    category="哲学",
    databases=("JSTOR", "PhilPapers", "OpenAlex", "Stanford Encyclopedia 数据库"),
)
