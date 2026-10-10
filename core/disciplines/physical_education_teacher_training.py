"""体育教师教育学科论文支持：体育教师培养/职前职后体裁、APA 引用样式与教师教育记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="physical_education_teacher_training",
    aliases=("physical_education_teacher_training", "体育教师教育", "体育教师培养",
             "PE teacher education", "体育教师职前培养", "physical education teacher preparation",
             "体育教师职后发展", "PE teacher professional development", "体育教学技能"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与教师教育问题）",
            "methodology（研究设计与样本）",
            "results（培训与教学数据）",
            "discussion（教师发展意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（教师/项目描述）",
            "analysis（培训过程与效果）",
            "results（教学改善）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（教师教育理论）",
            "evidence synthesis（课程、项目与政策综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；Research Quarterly for Exercise and Sport 遵循 APA 规范）",
    reporting_standards={
        "teacher_training_programme": "教师培养项目须报告时长、学分与实习安排",
        "reflective_practice": "反思性实践遵循 SRQR 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "qualitative_interview": "访谈研究遵循 COREQ 声明",
        "curriculum_design": "课程设计遵循 TACCP 教师教育认证标准"
    },
    conventions=(
        "教师培养课程/项目描述须完整（学时、实习周、认证标准）",
        "教师样本（职前/在职/职后）须报告年龄、教龄、专业背景",
        "教学观察工具（TEACH、TABC）须注明信效度",
        "反思日志、教案、课堂录像等教学档案作为数据附",
        "统计显著性阈值与效应量须明确"
    ),
    key_venues=(
        "Research Quarterly for Exercise and Sport",
        "Journal of Teaching in Physical Education",
        "Physical Education and Sport Pedagogy",
        "European Physical Education Review",
        "Sport, Education and Society",
        "Journal of Teacher Education"
    ),
    units_and_formulas_notes=(
        "培养学时/课时以国家教育标准为准（学时或学时数）",
        "公式用 amsmath；量表得分、效应量与 Cronbach's α 计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "质性分析给出编码数、主题数与信度指标"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("PPT/Word 教案与教学设计软件", "SPSS", "R", "NVivo 质性分析", "MAXQDA", "Thematic Appraiser", "TEACH 课堂观察量表", "TABC 教师行为编码", "教师效能感量表 (TSES)", "Dartfish 教学视频分析", "Kinovea 动作分析", "SMART 运动分析系统", "Qualtrics 调查平台", "Google Docs 反思日志", "Prezi 课件", "Canva 教学材料", "Miro 白板协作", "Adobe Premiere Pro", "Edmodo / 智慧教室", "Coursera MOOC 平台"),
    category="教育学",
    databases=("CNKI", "万方", "OpenAlex", "ERIC"),
)
