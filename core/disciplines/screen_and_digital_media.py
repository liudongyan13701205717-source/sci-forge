"""屏幕与数字媒体学科论文支持：屏幕媒体/数字传播/交互设计体裁与多媒体研究规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="screen_and_digital_media",
    aliases=("screen_and_digital_media", "屏幕与数字媒体", "数字媒体", "屏幕媒体", "screen media", "digital media", "交互设计", "多媒体"),
    paper_types={
        "research": ("abstract", "introduction（媒体问题与研究动机）", "methodology（研究设计与样本）", "results（用户行为数据）", "discussion（设计讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（数字媒体案例）", "analysis（界面与内容分析）", "results（用户反馈）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（媒体理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"usability": "可用性测试遵循 ISO 9241 规范", "user_study": "用户研究遵循 COREQ 规范", "survey": "问卷调查遵循 AAPOR 规范"},
    conventions=("术语须统一（用户/受众/交互等）", "样本量与招募方式须报告", "界面截图须注明版本", "效果指标须定义（完成率/错误率/满意度）", "伦理审查须声明"),
    key_venues=("New Media & Society", "Journal of Communication", "MIS Quarterly", "Journal of the American Society for Information Science and Technology", "International Journal of Human-Computer Studies", "CHI Conference Proceedings"),
    units_and_formulas_notes=("完成率与错误率以 % 记", "时间以秒记", "样本量与置信区间须报告", "统计显著性阈值 α=0.05 默认"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Figma", "Sketch", "Adobe XD", "Adobe Premiere Pro", "Adobe After Effects", "DaVinci Resolve", "Unity", "Unreal Engine", "Godot", "Blender", "Cinema 4D", "Maya", "Google Analytics (GA4)", "Mixpanel", "Amplitude", "Hotjar", "FullStory", "Qualtrics", "SPSS", "R"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
