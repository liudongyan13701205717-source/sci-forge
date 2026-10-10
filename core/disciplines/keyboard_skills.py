"""键盘技能学科论文支持：打字技能/计算机应用体裁、APA 引用样式与打字效率记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="keyboard_skills",
    aliases=("keyboard_skills", "键盘技能", "打字技能", "键盘操作", "键盘输入技能", "keyboard skills", "typing skills", "typing proficiency"),
    paper_types={
        "research": ("abstract", "introduction（技能背景与问题）", "methodology（训练与测试方法）", "results（速度准确率数据）", "discussion（训练建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（个案训练案例）", "analysis（技能掌握分析）", "results（技能提升效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（技能学习理论）", "evidence synthesis（训练证据综述）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Computers & Education 遵循 APA 规范）",
    reporting_standards={"RCT": "随机对照试验遵循 CONSORT 声明", "quasi_experimental": "准实验遵循准实验报告规范", "systematic_review": "系统综述遵循 PRISMA 声明"},
    conventions=("打字速度用 WPM（每分钟单词数）标注", "准确率须给出百分比", "测试文本与语言须说明", "训练时长与频次须记录", "样本人口统计须报告"),
    key_venues=("Computers & Education", "Educational Technology Research and Development", "Journal of Research on Technology in Education", "Computers in Human Behavior", "Interactive Learning Environments"),
    units_and_formulas_notes=("速度用 WPM（字/分钟）", "准确率用 %（错误率与修正后准确率均报告）", "时间用秒（测试时间标准化）", "样本量须报告", "练习次数须记录"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("TypeRacer（打字竞速平台）", "10FastFingers（打字测试）", "Keybr（打字训练）", "Typing.com（打字课程）", "Rapid Typing（打字练习）", "Microsoft Word（文档测试）", "Google Docs（在线打字）", "SPSS（统计）", "R（统计分析）", "Python（数据分析）", "Excel（成绩管理）", "Moodle（教学平台）", "Clickbait（注意力测试）", "Reaction Time（反应时间测试）", "Hand Tracking（手部追踪软件）", "Eye Tracking（眼动追踪系统）", "Keystroke Recording（按键记录工具）", "Qualtrics（问卷调查）", "NVivo（质性分析）", "Microsoft Office（办公技能测试）"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "Typing Metrics（打字指标数据库）"),
)
