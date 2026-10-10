"""Numeracy 学科论文支持：数理素养教育/统计素养体裁、APA 7 引用样式与教育测量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="numeracy",
    aliases=(
        "numeracy",
        "数理素养",
        "Numeracy Education",
        "Mathematics Literacy",
        "Statistical Literacy",
        "Quantitative Literacy",
        "Mathematics Education",
        "Quantitative Reasoning",
        "数感",
    ),
    paper_types={
        "research": ("abstract", "introduction（研究问题与理论基础）", "methodology（研究对象、工具与统计分析）", "results（结果与效应量）", "discussion（教学含义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例背景与情境）", "analysis（教学行为与数据分析）", "results（成效与变化）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（素养理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份；教育期刊主流样式）",
    reporting_standards={
        "survey": "调查报告遵循 AAPOR 规范",
        "intervention": "干预研究遵循 CONSORT/EQUATOR",
        "measurement": "量表信效度遵循 COSMIN 声明",
    },
    conventions=(
        "素养框架引用（OECD PISA、TAT 框架、NCTM 标准）",
        "任务分析说明认知层级（回忆/应用/推理）",
        "统计量给出 M/SD/SE/CI 与显著性",
        "效应量报告 Cohen's d 与 95% CI",
        "样本量给先验功效分析",
    ),
    key_venues=(
        "Journal for Research in Mathematics Education",
        "Educational Studies in Mathematics",
        "Teaching and Teacher Education",
        "Cognition and Instruction",
        "Journal for the Education of the Gifted",
    ),
    units_and_formulas_notes=(
        "PISA 分数以 200 分为间隔、均值 500、SD 100 标准化",
        "信度报 Cronbach's α 与重测 ICC",
        "量表分值给出范围与计分方向",
        "效应量与 p 值须给出",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("GeoGebra", "Desmos", "Wolfram Alpha", "Python", "R", "SPSS", "Microsoft Excel", "Google Sheets", "Tableau", "Mathletics", "IXL Math", "Khan Academy", "MATHia", "NWEA MAP Growth", "WeXL", "CASIO fx-991ES Plus", "CASIO ClassPad 330", "TI-Nspire CAS", "Casio fx-CG50", "Numicon 教具"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "ERIC"),
)
