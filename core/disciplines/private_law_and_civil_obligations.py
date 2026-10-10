"""民法与民事义务学科论文支持：民事义务教义分析、判例评释与比较私法研究体裁、法学引注样式与裁判数据注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="private_law_and_civil_obligations",
    aliases=("private_law_and_civil_obligations", "民法与民事义务", "民法", "private law", "民事义务", "civil obligations", "合同与债法", "私法", "obligations"),
    paper_types={
        "research": ("abstract", "introduction（问题提出与规范梳理）", "methodology（教义分析、案例检索与比较方法）", "results（规则解释与实证发现）", "discussion（立法论与解释论建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（案情与裁判要旨描述）", "analysis（争点、裁判理由与规则适用分析）", "results（个案发现与规则展望）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（民事义务理论综述）", "evidence synthesis（域内与比较证据综合）", "future directions", "references"),
    },
    citation_style="《法学引注手册》（中文稿）/ OSCOLA（英文稿）",
    reporting_standards={"k1": "法条引用精确到条/款/项并注明版本日期", "k2": "案例引用注明案号、审级与裁判日期", "k3": "比较对象选择理由（功能等价）须说明"},
    conventions=("规范用语区分“应当”与“可以”", "学说引注给页码，案例评论区分裁判要旨与作者观点", "比较法须给功能性比较框架而非简单罗列", "立法建议须区分立法论与解释论", "注释体例全稿统一"),
    key_venues=("法学研究", "中国法学", "法学家", "比较法研究", "Civil Law News Review"),
    units_and_formulas_notes=("金额类以本币单位表示并注明年份", "裁判数据统计给样本量与统计期间", "比例用 % 表示并明确分母口径", "实证研究须声明伦理审查与匿名化处理"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("北大法宝", "威科先行", "元典智库", "iCourt Alpha", "中国裁判文书网", "全国法院案例库", "NVivo", "Atlas.ti", "MAXQDA", "R", "Stata", "SPSS", "Zotero", "EndNote", "LaTeX", "司法大数据平台", "Bluebook 引注插件", "Reflex（法律文本分析）", "Qualtrics", "Tableau（法律数据可视化）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "HeinOnline", "国家法律法规数据库"),
)
