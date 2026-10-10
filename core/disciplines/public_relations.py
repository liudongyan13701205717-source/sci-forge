"""公共关系学科论文支持：传播策略/声誉管理/媒介关系体裁、APA 引用与传播指标注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="public_relations",
    aliases=("public_relations", "公共关系", "公关", "传播与声誉管理", "危机传播", "媒介关系", "corporate communication", "reputation management"),
    paper_types={
        "research": ("abstract", "introduction（传播问题与情境）", "methodology（方法与样本）", "results（传播效果）", "discussion（策略启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（公关事件）", "analysis（策略复盘）", "results（舆情结果）", "discussion（经验与教训）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions（传播趋势）", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"survey": "媒介与公众调查遵循 AAPOR 报告规范", "content_analysis": "内容分析须报告编码者间信度", "social_media": "社媒分析注明抓取范围与时间窗"},
    conventions=("公众/利益相关者界定须清晰", "传播指标（声量/情感/覆盖）须注明口径与平台", "危机传播区分预防期与回应期", "效果评估区分曝光与态度改变", "企业立场与研究者立场须声明"),
    key_venues=("Public Relations Research", "Journalism & Mass Communication", "Public Relations Quarterly", "New Media & Society", "现代传播"),
    units_and_formulas_notes=("传播量给出发帖/曝光/互动绝对数与时间窗", "情感极性注明算法与阈值", "样本代表性与加权方法须说明", "引用社媒数据注明抓取日期与许可证"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "SPSS", "R", "Python（Pandas/scikit-learn）", "ArcGIS", "Tableau", "Excel", "Minitab", "JMP", "Qualtrics", "SurveyMonkey", "Meltwater", "Gephi", "Stata", "Brandwatch", "MATLAB", "Word", "LaTeX", "Zotero", "PowerPoint"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
