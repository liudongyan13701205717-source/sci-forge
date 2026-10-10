"""法学学科论文支持：法理学/法律研究/法律实证研究体裁、APA 引用样式与法律文献记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="jurisprudence",
    aliases=("jurisprudence", "法学", "法理学", "法律学", "法学研究", "法律实证研究", "Jurisprudence", "law and legal studies"),
    paper_types={
        "research": ("abstract", "introduction（问题背景与研究意义）", "methodology（研究方法：文献/实证/比较）", "results（法律分析或实证发现）", "discussion（法律论证与建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（案件或立法案例）", "analysis（法律分析）", "results（裁判要旨或立法效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（法律理论综述）", "evidence synthesis（实证证据综述）", "future directions", "references"),
    },
    citation_style="Bluebook 样式（法学标准；国际期刊可附 APA 格式）",
    reporting_standards={"legal_research": "法律实证研究遵循法律研究规范", "case_study": "案例研究遵循法律案例报告规范", "systematic_review": "法律政策综述遵循系统综述规范"},
    conventions=("案例引注须完整（法院、年份、卷号、页码）", "法规引用须注明效力与修订日期", "法律论证须区分应然与实然", "实证数据来源须说明（裁判文书、立法文本）", "作者立场与利益冲突须披露"),
    key_venues=("Journal of Legal Studies", "Harvard Law Review", "Yale Law Journal", "Stanford Law Review", "Chinese Journal of Law"),
    units_and_formulas_notes=("统计数据须标注样本与置信区间", "裁判文书数量须给出检索条件", "时间线须注明法律效力状态", "比较法研究须标注法域", "引用格式须统一（Bluebook 或 APA）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Vlex（法律研究平台）", "中国裁判文书网", "RefWorks（文献管理）", "Zotero（参考管理）", "EndNote（文献管理）", "NVivo（质性分析）", "SPSS（法律实证统计）", "R（统计与文本挖掘）", "Python（NLP 法律文本分析）", "Gephi（法律网络可视化）", "ArcGIS（法律地理分析）", "Moodle（教学平台）", "Lexis+ AI（法律 AI 助手）", "北大法宝 AI 法律分析", "LaTeX", "Bluebook 引注插件", "Reflex（法律文本分析）", "Qualtrics", "Casetext（AI 法律检索）", "Tableau（法律数据可视化）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw（西文法律数据库）", "LexisNexis（法律文献）", "ProQuest Law（国际法律库）", "HeinOnline（法学历史文献）", "北大法宝（中国法律数据库）", "国家法律法规数据库"),
)
