"""演讲技能学科论文支持：口头表达训练、修辞效果与演示表现研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="presentation_skills",
    aliases=(
        "presentation skills", "演讲技能", "演示技能",
        "public speaking", "公开演讲",
        "speech communication", "演说沟通",
        "presentation delivery", "演讲表现",
        "communication skills", "沟通技能",
        "audience engagement", "受众互动",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（表达问题与训练目标）",
            "methodology（培训设计与效果测量）",
            "results（表现评分与自信度变化）",
            "discussion（教学法讨论与迁移效果）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（受众场景与演讲任务）",
            "analysis（内容结构、非言语与临场表现）",
            "results（受众反应与能力提升）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（修辞与传播理论谱系）",
            "evidence synthesis（演讲训练研究证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "评分量表须报告评分者构成、评分标准与一致性",
        "k2": "培训效果须报告前测后测设计与对照组设置",
        "k3": "受众反馈须报告样本量、抽样方式与匿名处理",
    },
    conventions=(
        "演讲表现须区分内容、结构、言语与非言语维度",
        "自信度量表须注明版本与常模来源",
        "培训须报告课时、练习频次与反馈机制",
        "受众反应须注明测量时点与干扰控制",
        "录音录像材料须说明知情同意与匿名化",
    ),
    key_venues=(
        "Communication Education",
        "Journal of Communication Education",
        "International Communication Gazette",
        "Language and Communication",
        "Communication Quarterly",
    ),
    units_and_formulas_notes=(
        "表现评分以百分制或 Likert 级数表示并附均值与标准差",
        "语速以每分钟词数（wpm）表示，中文按每分钟字数",
        "停顿与填充词须注明计数口径与取样时段",
        "观众注意力以注视时长或反应量表分数表示",
        "培训效果以前后测差值与效应量共同报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "NVivo", "ATLAS.ti", "Camtasia 录课工具", "iSpring Suite 微课制作", "Obs 课堂录制", "PowerPoint", "Canva 演示设计", "Keynote", "Prezi 演示平台", "Qualtrics", "SurveyMonkey", "Python (pandas, scipy)", "MATLAB", "Excel", "Adobe Premiere", "Adobe Audition 语音处理", "iSpeech 语音评估"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
