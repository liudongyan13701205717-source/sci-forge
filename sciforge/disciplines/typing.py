"""打字学科论文支持：键盘输入技能与培训体裁、APA 引用样式与人因记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="typing",
    aliases=("typing", "打字", "键盘输入", "文字录入", "打字技能",
             "keyboarding", "touch typing", "typing skill"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与打字问题）",
            "methods（被试、任务与测量）",
            "results（速度、准确率与学习曲线）",
            "discussion（人因与培训意义）",
            "references",
        ),
        "training_study": (
            "abstract",
            "introduction",
            "methods（训练方案、周期与评估）",
            "results（前后测差异与统计）",
            "discussion（教学启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；人因与教育期刊多用 APA）",
    reporting_standards={
        "human_factors": "人因研究须报告被试特征、键盘布局与任务条件",
        "training_study": "训练研究须报告训练时长、频次与评估方法",
        "performance_metrics": "须报告 WPM/CPM 与准确率并说明测量协议",
        "statistical": "须报告样本量、统计检验与效应量",
    },
    conventions=(
        "打字速度用 WPM 或 CPM，并说明词/字符定义",
        "准确率用百分比，并说明错误计数规则",
        "键盘布局（QWERTY/Dvorak）与设备须注明",
        "测试文本语料来源与长度须交代",
        "被试样本特征（年龄、经验）须报告",
    ),
    key_venues=(
        "Computers in Human Behavior",
        "Applied Ergonomics",
        "Ergonomics",
        "Human Factors",
        "Journal of Educational Computing Research",
        "Behaviour & Information Technology",
    ),
    units_and_formulas_notes=(
        "速度用 WPM（words per minute）或 CPM（characters per minute）",
        "准确率用 %，错误率用 错误数/千字符",
        "反应时用 ms；学习曲线用对数或幂函数拟合",
        "统计量给出均值 ± SD；显著性用 P 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("TypingMaster", "Mavis Beacon Teaches Typing", "TypeRacer", "10FastFingers", "Keybr.com", "Monkeytype", "Klavaro", "TIPP10", "Typing.com", "RapidTyping", "KTouch", "GNU Typist (gtypist)", "Microsoft Word", "Notepad++", "Kinesis 人体工学键盘", "Typing Pal", "Typing Trainer", "TypingTest 软件", "Dvorak 键盘布局", "Colemak 键盘布局"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
