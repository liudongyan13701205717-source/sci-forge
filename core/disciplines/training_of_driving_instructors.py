"""驾驶教练员培训学科论文支持：驾驶技能教学/科目考试/安全驾驶训练体裁、APA 与模拟训练注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="training_of_driving_instructors",
    aliases=("training_of_driving_instructors", "驾驶教练员培训", "驾驶员培训教练员",
             "驾驶培训教师", "教练培训",
             "driving instructor training", "driving school instructor",
             "driver education trainer", "driving coach training",
             "驾校教练员培训"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "methodology",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context and background",
            "case description",
            "analysis and implications",
            "references",
        ),
        "teaching_research": (
            "abstract",
            "introduction",
            "literature review",
            "teaching design",
            "implementation",
            "assessment and reflection",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_study": "案例研究遵循 COREQ 报告规范",
        "survey": "调查研究报告遵循 AAPOR 规范",
        "empirical": "实证研究遵循 APA 与职业教育研究惯例",
        "safety": "安全驾驶训练须报告风险暴露与事故指标",
    },
    conventions=(
        "驾驶技能术语须按科目分类（科目一至科目四）统一标注",
        "教学方法与教材须在方法部分列明",
        "样本量、显著性水平、置信区间须完整给出",
        "质性数据须给出编码规则与信度（Cronbach's α 或 Kappa）",
        "培训方案须说明安全规范与法律要求",
    ),
    key_venues=(
        "Traffic Injury Prevention",
        "Accident Analysis & Prevention",
        "Journal of Safety Research",
        "Safety Science",
        "交通安全与文明驾驶",
        "职业教育研究",
    ),
    units_and_formulas_notes=(
        "驾驶技能评分用百分制或科目通过/不通过报告",
        "培训效果须给出前测/后测差异与效应量（Cohen's d）",
        "事故率以起/万公里或起/万学时报告",
        "样本量、显著性水平与置信区间须完整给出",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("汽车驾驶模拟器", "摩托车驾驶模拟器", "公交车驾驶模拟器", "倒车入库模拟器", "科目二考试系统", "科目三路考系统", "驾驶技能评估系统", "交通标志识别训练系统", "夜间驾驶模拟器", "紧急避障训练系统", "学员学习管理系统", "教练员资格管理平台", "行车记录系统", "车载视频监控系统", "驾驶行为分析系统", "SPSS", "Excel", "NVivo", "R", "Canva"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "万方"),
)
