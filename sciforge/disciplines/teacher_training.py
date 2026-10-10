"""Teacher Training 学科论文支持：教师培训/师资教育研究论文体裁、APA 引用样式与师资教育研究方法论记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training",
    aliases=(
        "teacher_training",
        "Teacher training",
        "教师培训",
        "师资教育",
        "teacher education",
        "teacher preparation",
        "initial teacher education",
        "professional development",
        "教师培养",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与教师培训问题）",
            "literature review",
            "methodology（研究设计与参与）",
            "findings",
            "discussion（对教师教育与政策的意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（教师培训项目案例）",
            "analysis",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "literature review（教师培训研究综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（Teachers College Record、Journal of Teacher Education 遵循 APA 规范）",
    reporting_standards={
        "sample": "样本须报告：参与者类型（初职/在职/研究生）、人数 n、机构类型（师范/综合）、地区",
        "design": "研究设计须报告：混合/质性/量化、数据收集方法（问卷/访谈/课堂观察/日志）、信效度检验",
        "ethics": "伦理审查须报告：机构审查（IRB/ERB）、知情同意、数据匿名与访问权限",
        "measurement": "量表须报告：来源（如 CLASS、CLASSIC、Friedl-Bechler PCK 量表）、Cronbach α、CFA 拟合指标",
        "systematic_review": "系统综述遵循 PRISMA 2020 声明",
    },
    conventions=(
        "教师培训研究遵循 TPACK、TPACK 扩展（TPeCK、TPACK+）与 Shulman 学科教学知识（PCK）框架",
        "课堂观察量表遵循 CLASS（课堂互动评估量表）、CLASS-D、CIT（儿童互动工具）、FROG（观察教师实践）",
        "教师反思工具遵循 Schön 反思性实践（反思于行动/行动中反思）与 Kolb 经验学习循环",
        "研究遵循 Kaupapa Māori（毛利本位研究法）如涉毛利教育；伦理审查遵循 APA 伦理准则",
        "符号约定：PCK（学科教学知识）、TPACK（技术-教学法-学科知识）、TPeCK（技术-教学法-学科-教育知识）首次出现须给出全称",
        "计量公式用 amsmath；系数报告附标准误；显著性用 *, **, *** 对应 10%/5%/1%",
    ),
    key_venues=(
        "Teachers College Record",
        "Journal of Teacher Education",
        "Teaching and Teacher Education",
        "Research in Teacher Education",
        "European Journal of Teacher Education",
        "Asia-Pacific Journal of Teacher Education",
    ),
    units_and_formulas_notes=(
        "样本量报告 n 与观测数 N；课堂观察评分用 CLASS 5 级评分（1=低、5=高）；量表信度用 Cronbach α",
        "公式用 amsmath；效应量用 Cohen's d、η²、r；混合效应模型（HLM）须报告随机截距与斜率",
        "显著性用 *, **, *** 对应 10%/5%/1%；p 值报告精确值（p < .001 或 p = .032）",
        "所有比率与效应量保留 3 位小数；样本量 N 与参与者人数 n 须完整标注",
        "TPACK/TPeCK 维度得分用 Likert 5/7 点量表；描述性统计报告 M ± SD 与 n",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Canvas LMS", "Google Classroom", "Zoom", "Google Forms", "SurveyMonkey", "NVivo", "Atlas.ti", "ELAN", "Transana", "Zotero", "EndNote", "SPSS", "R", "Stata", "Excel", "Power BI", "Tableau", "Google Docs", "Overleaf"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "ProQuest"),
)
