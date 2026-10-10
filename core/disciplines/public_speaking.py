"""公共演讲/演讲学学科论文支持：修辞分析/演讲评价/口头传播体裁、APA 引用与评量量表注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="public_speaking",
    aliases=("public_speaking", "公共演讲", "演讲学", "口才学", "修辞学", "口头传播", "rhetoric", "speech communication"),
    paper_types={
        "research": ("abstract", "introduction（传播情境与研究问题）", "methodology（评价量表与样本）", "results（演讲效果数据）", "discussion（教学启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（演讲事件）", "analysis（修辞策略分析）", "results（受众反应）", "discussion（改进建议）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions（研究趋势）", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"rhetorical_analysis": "修辞分析遵循批评框架说明（如修辞三角）", "speech_assessment": "演讲评量报告量表信度与评分者一致性", "audience_survey": "受众调查遵循 AAPOR 报告规范"},
    conventions=("演讲情境（听众/场合/媒介）须交代", "评测量表须报信度系数", "修辞术语（ethos/pathos/logos）须界定后使用", "音频/视频转写文本须附编码说明", "教学效果区分即时表现与长期能力"),
    key_venues=("Communication Studies", "Western Journal of Communication", "International Journal of Speech Communication", "修辞研究", "传播学术辑"),
    units_and_formulas_notes=("评量分数给出 M/SD 与量表区间", "评分者间信度报告 ICC 或 κ 系数", "样本量与应答率须报告", "录音视频时长与截取方式须注明"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "NVivo", "Excel", "Word", "PowerPoint", "Audacity", "Camtasia", "OBS Studio", "Premiere Pro", "Gephi", "Stata", "MATLAB", "EndNote", "Zotero", "LaTeX", "Minitab", "JMP", "Adobe Audition", "Python（Pandas）"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
