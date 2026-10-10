"""中学教学学科论文支持：中学课堂教学/课程实施/学业评价/教师专业发展体裁、APA 7 教育学术引用样式与教育度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="secondary_teaching",
    aliases=("secondary_teaching", "中学教学", "中学教育", "secondary education", "middle school teaching"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究意义）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据综合）",
            "future directions（展望）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "methodology": "研究须报告研究设计、样本来源、数据收集与分析方法",
        "data": "教学数据须报告数据来源、样本量、缺失值处理与质量控制",
        "measurement": "学业测评须报告信度、效度、标准化信息与评分标准",
        "ethics": "涉及未成年被试研究须报告伦理审查、家长同意与学生知情同意",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "学生数据须匿名化处理，仅报告脱敏后的班级/学校信息",
        "教学实验须报告对照组与实验组、教学周期与干预内容",
        "学业成绩须注明测评工具、满分分值与得分范围",
        "课堂观察须注明观察量表、观察时长与观察者信度",
        "引用课标/教学大纲须标注版本与年份",
    ),
    key_venues=(
        "American Educational Research Journal",
        "Journal of Educational Psychology",
        "Review of Educational Research",
        "Educational Researcher",
        "Teaching and Teacher Education",
    ),
    units_and_formulas_notes=(
        "学业成绩用百分制或五级制；标准差用 SD；t 检验须报告效应量",
        "信度用 Cronbach's α；效度用 CFA/SEM 指标",
        "公式用 amsmath；统计公式须编号",
        "统计结果给出均值 ± 标准差与样本量；显著性用 p 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS 统计分析", "R 统计建模", "NVivo 质性分析", "LaTeX 排版", "Origin 绘图", "Python 数据分析", "MATLAB 数据分析", "AMOS 结构方程", "Mplus 潜变量分析", "Classroom Observation System", "Student Achievement Database", "Curriculum Mapping Software", "Learning Management System (LMS)", "PISA 测评工具", "NAEP 学业测评", "GPA Calculator", "Excel 数据分析", "QGIS 教育地理分析", "SurveyMonkey 问卷设计", "Google Forms 在线测评"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)