"""动物训练学科论文支持：动物行为学、强化学习训练、工作动物应用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="animal_training",
    aliases=(
        "animal training",
        "Animal training",
        "动物训练",
        "动物驯化",
        "operant conditioning",
        "正强化训练",
        "clicker training",
        "工作犬训练",
        "警犬训练",
        "导盲犬训练",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（动物、任务、强化方案、训练员）",
            "results（学习曲线、成功率、反应时）",
            "discussion（行为机制与生产/警务意义）",
            "conclusions",
            "references",
        ),
        "technical_report": (
            "abstract",
            "task description",
            "training protocol",
            "success rate and reliability",
            "recommendations",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "learning theory overview",
            "current evidence",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（行为学/心理学主流样式）",
    reporting_standards={
        "animals": "物种、品种、年龄、性别、既往训练经验须说明；福利与伦理审查（AAALAC/3R）须披露",
        "protocol": "训练任务定义、强化物（食物/玩具/社会强化）、时程、次数须明确",
        "training": "训练员资质、每日训练时长、休息间隔须记录",
        "statistics": "样本量、独立性与重复测量须说明；效应量与置信区间报告",
        "generalization": "任务在陌生情境下的泛化表现须报告",
    },
    conventions=(
        "动物用拉丁学名首次出现标注；工作犬品种用中文常用名",
        "学习曲线以「累计正确率 vs 训练次数」呈现，横轴为训练次数",
        "统计量报告 M±SD；组间比较用 ANOVA 或混合效应模型",
        "训练阶段（acquisition/maintenance/extinction/generalization）标注",
        "所有缩写首次出现给全名；关键行为术语中英对照",
    ),
    key_venues=(
        "Journal of the Experimental Analysis of Behavior",
        "Animal Learning & Behavior",
        "Applied Animal Behaviour Science",
        "Journal of Veterinary Behavior",
        "Animal Cognition",
    ),
    units_and_formulas_notes=(
        "反应时 ms；强化延迟 s；训练次数（trials）",
        "正确率 %；泛化率 %",
        "统计量 M±SD 或中位数（四分位距）",
        "样本量 n；重复测量用混合效应模型（lme4/nlme）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("训练箱（Shuttle/Box/Chamber）", "目标棒（Target Stick）", "哨子（Whistle，可变频）", "点击器（Clicker）", "计时器（Stopwatch/ChronoGraph）", "训练日志软件（Fidelity Training）", "GPS 追踪器（Tractive/Whistle/Garmin）", "运动记录仪（Fitbit）", "行为分析软件（Noldus EthoVision XT）", "视频分析软件（Kinovea/Dartfish）", "相机/GoPro 运动相机", "红外行为追踪（DeepLabCut）", "统计软件 SPSS", "R", "RStudio", "Python", "Excel", "LaTeX", "Zotero", "MATLAB"),
    category="农学",
    databases=("PubMed", "Web of Science", "PsycINFO", "OpenAlex", "Crossref", "CNKI"),
)
