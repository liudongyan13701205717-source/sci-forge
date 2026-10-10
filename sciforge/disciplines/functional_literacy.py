"""功能文盲学科论文支持：读写能力、功能识字、成人教育与基础素养。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="functional_literacy",
    aliases=("functional_literacy", "literacy", "功能文盲", "文盲", "读写能力", "识字教育", "成人教育", "基础素养"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methods（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA（作者-年份）",
    reporting_standards={
        "survey": "调查须遵循标准化调查工具",
        "test": "测试须遵循标准化测试规范",
        "intervention": "干预须遵循标准化干预方案",
        "evaluation": "评估须遵循标准化评估规范"
    },
    conventions=(
        "术语须用标准化术语（读写能力、功能识字）",
        "研究对象须用标准化描述",
        "教育阶段须用标准化阶段",
        "年龄须用标准化年龄",
        "数据来源须用标准化来源"
    ),
    key_venues=(
        "Literacy Research",
        "Journal of Adult and Continuing Education",
        "Review of Research in Education",
        "Journal of Education and Work",
        "International Journal of Literacy Research"
    ),
    units_and_formulas_notes=(
        "年龄用年（years）",
        "样本量用人数（persons）",
        "得分用分数（points）",
        "完成率用 %（百分比）",
        "时间用小时（hours）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Literacy assessment software", "Literacy learning platform", "Adult education software", "Literacy training program", "Literacy testing system", "Literacy curriculum design", "Literacy materials development", "Literacy evaluation tool", "Literacy research database", "Literacy statistics", "Literacy case study analysis", "Literacy policy analysis", "Literacy program management", "Literacy resource center", "Literacy workshop facilitation", "Literacy volunteer training", "Literacy mentorship", "Literacy advocacy", "Literacy data collection", "Literacy reporting tools"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
