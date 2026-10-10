"""求职项目学科论文支持：求职/就业培训与劳动力市场体裁、APA 引用样式与就业指标记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="jobseeking_programmes",
    aliases=("jobseeking_programmes", "求职项目", "就业培训", "求职辅导", "job seeking", "job-seeking programmes", "employment training", "career transition"),
    paper_types={
        "research": ("abstract", "introduction（就业背景与问题）", "methodology（干预与评估方法）", "results（就业率与匹配）", "discussion（政策与建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（个案培训）", "analysis（过程分析）", "results（就业结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（人力资本理论）", "evidence synthesis（项目证据综述）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Journal of Vocational Behavior 遵循 APA 规范）",
    reporting_standards={"RCT": "随机对照试验遵循 CONSORT 声明", "quasi_experimental": "准实验遵循准实验报告规范", "systematic_review": "系统综述遵循 PRISMA 声明"},
    conventions=("干预组与对照组构成须说明", "就业结果定义与测量窗口须统一", "样本流失与失访须报告", "协变量与效应量须给出", "伦理审批与知情同意须交代"),
    key_venues=("Journal of Vocational Behavior", "Work, Employment and Society", "Journal of Employment Rehabilitation", "Education and Training", "International Journal for Educational Vocational Guidance"),
    units_and_formulas_notes=("就业率用百分比与置信区间", "处理效应用 Cohen's d 或平均边际效应", "追踪期用月数标注", "样本量与统计功效须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("招聘平台数据（LinkedIn API）", "简历解析工具", "SPSS（统计）", "R（处理效应）", "Stata（面板数据）", "NVivo（质性访谈）", "CareerTrack 跟踪平台", "就业匹配算法模型", "问卷平台（Qualtrics）", "Python（pandas）", "Microsoft Access（个案库）", "能力测评系统", "模拟面试软件", "职业规划软件（MyNextMove）", "学习管理系统（LMS）", "A/B 测试平台", "地理信息系统（ArcGIS）", "就业政策知识库", "Tableau（数据可视化）", "Excel（数据管理）"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "劳动力统计数据库（LFS）", "职业信息数据库（O*NET）"),
)
