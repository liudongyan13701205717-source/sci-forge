"""公法学科论文支持：宪政/行政法/规制比较体裁、蓝引与脚注引用样式及法源层级注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="public_law",
    aliases=("public_law", "公法", "宪法与行政法", "宪法学", "行政法学", "规制法", "constitutional law", "administrative law"),
    paper_types={
        "research": ("abstract", "introduction（问题与法源定位）", "methodology（法律方法）", "results（规范分析结果）", "discussion（教义与制度反思）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例与裁判）", "analysis（裁判要旨分析）", "results（法律效果）", "discussion（制度影响）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（判例与立法综合）", "future directions（立法与修法方向）", "references"),
    },
    citation_style="Bluebook（法律引注规范；中文期刊可用脚注式）",
    reporting_standards={"legal_research": "法律研究遵循 IRAC/CRAC 论证结构", "comparative_law": "比较法研究遵循法域说明与效力层级注记", "legislative_analysis": "立法分析须区分建议稿与生效文本"},
    conventions=("法源层级（宪法/法律/行政法规/规章）须标明", "判例引用给出案号与裁判要旨", "规范性（应当）与描述性（是）表述须区分", "比较法研究须说明法域与制度背景", "术语保持全篇统一（如「公权力」「基本权利」）"),
    key_venues=("China Political and Legal Science", "Comparative Law Review", "Harvard Law Review", "Administrative Law Review", "法学家/中国法学"),
    units_and_formulas_notes=("规范效力按位阶（上位法优于下位法）说明", "比例原则分析给出处置手段与目的相称性判断", "引用法条注明版本与修订日期", "涉外法注明冲突规范与准据法选择"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("北大法宝", "威科先行法律研究", "裁判文书网", "SPSS", "Stata", "R", "Python", "Excel", "Word", "LaTeX", "Bluebook 引注插件", "Zotero", "EndNote", "Tableau", "Practical Law", "元典法律咨询", "Qualtrics", "Reflex（法律文本分析）", "Power BI", "NVivo"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "CNKI 法律库", "Google Scholar"),
)
