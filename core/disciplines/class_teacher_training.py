"""Class teacher training 学科论文支持：中小学/小学/班主任教育体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="class_teacher_training",
    aliases=(
        "Class teacher training", "class teacher training",
        "primary teacher training", "elementary teacher education",
        "teacher education", "class teacher professional development",
        "小学教师教育", "班主任培养", "小学教师培训", "基础教育师资培养",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（教师教育问题/理论框架）",
            "methodology（课堂观察、教师访谈、课堂实验）",
            "findings",
            "discussion",
            "conclusion",
            "references",
        ),
        "action_research": (
            "abstract",
            "introduction",
            "context_description",
            "planning",
            "action",
            "observation",
            "reflection",
            "references",
        ),
        "curriculum_analysis": (
            "abstract",
            "introduction",
            "curriculum_description",
            "analysis",
            "pedagogical_recommendations",
            "references",
        ),
    },
    citation_style="APA 7 样式（教育类中文论文亦常见 GB/T 7714）",
    reporting_standards={
        "classroom_observation": "观察法报告编码框架、观察者培训、观察者一致性 κ",
        "intervention": "准实验/实验报告前测-后测、班级数、学期数、评估工具与信度",
        "survey": "问卷遵循 IRB；报告 Cronbach's α、抽样方法、样本量",
        "qualitative": "访谈遵循饱和原则；报告参与者数、时长与编码树",
        "ethics": "涉及未成年人的研究须经 IRB 审查与监护人同意",
    },
    conventions=(
        "课程/教材引用官方版本（如「2022 版义务教育英语课程标准」）",
        "学生身份匿名化（化名、编号），报告班级数/年龄/性别等人口学变量",
        "评价工具报告项目数、Likert 等级、Cronbach's α 与因子载荷",
        "教学法术语（如 PBL、TBL、翻转课堂、大单元教学）首次出现给出中英文对照",
        "数据年份与统计口径明确；跨学期数据用统一口径",
    ),
    key_venues=(
        "Teachers College Record",
        "Journal of Teacher Education",
        "Journal of Educational Psychology",
        "American Educational Research Journal",
        "Educational Research",
        "Teaching and Teacher Education",
        "中小学教育研究",
        "全球教育展望",
    ),
    units_and_formulas_notes=(
        "样本量 n；班级数；学期数；教学时数 h",
        "评价量表报告 Cronbach's α、因子载荷、Likert 5/7 分",
        "统计报告 t 检验/F 检验、p 值、95% CI、效应量（d、η²）",
        "访谈报告参与者数、时长、编码节点数、主题树",
        "跨学期数据用统一口径并注明年级",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "Dedoose", "Atlas.ti", "MAXQDA", "SPSS Statistics", "Stata", "R 统计软件", "JASP", "AMOS", "Mplus", "HARMONY", "SPSSAU", "Adobe Premiere Pro", "DaVinci Resolve", "Camtasia（录屏）", "OBS Studio", "Adobe Captivate", "Articulate Storyline", "H5P", "Moodle", "Open edX", "雨课堂", "ClassIn", "智慧树", "超星尔雅", "中国大学 MOOC", "学银在线", "作业帮（教育数据）", "好未来教育平台", "PowerPoint", "WPS Office", "GeoGebra", "Desmos", "Excel", "Google Sheets", "LaTeX", "Microsoft Teams", "Zotero", "EndNote", "Qualtrics", "问卷星", "REDcap", "OSF", "Google Forms", "Microsoft Forms"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "ERIC", "CNKI", "SSCI"),
)
