"""秘书项目学科论文支持：秘书教育/职业培训/行政能力评估/办公技能认证体裁、APA 7 管理学学术引用样式与培训度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="secretarial_programmes",
    aliases=("secretarial_programmes", "秘书项目", "秘书培训", "行政培训", "secretarial training", "administrative training"),
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
        "training": "培训报告须报告课程设计、实施流程、评估方法与通过标准",
        "evaluation": "技能认证须报告考核内容、评分标准与合格率",
        "data": "培训数据须报告样本量、数据来源与质量控制",
        "ethics": "涉及学员数据研究须报告伦理审查与知情同意",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "培训课程须注明对应职业资格标准与学时要求",
        "技能考核须报告考核项目、评分标准与通过分数线",
        "培训效果须报告前置/后置测评对比与显著性检验",
        "软件操作须注明软件版本与配置环境",
        "引用职业资格标准须标注标准编号与年份版本",
    ),
    key_venues=(
        "Journal of Business and Economics",
        "Administrative Quarterly",
        "Human Resource Development Quarterly",
        "Journal of Vocational Technology",
        "MIS Quarterly",
    ),
    units_and_formulas_notes=(
        "培训时长用 h；通过率用 %；评分用百分制或五级制",
        "技能考核须注明考核项目数与每项分值",
        "公式用 amsmath；评估公式须编号",
        "统计结果给出均值 ± 标准差与样本量；显著性用 p 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Office 办公套件", "Google Workspace 协作办公", "Adobe Acrobat 文档处理", "Tesseract OCR 文字识别", "EndNote 参考文献管理", "Microsoft Outlook 邮件管理", "Google Drive 云存储", "SharePoint 文档管理", "Microsoft Teams 协作", "Docusign 电子签名", "LaTeX 排版", "Python 自动化脚本", "Excel 数据分析", "SPSS 统计分析", "Origin 绘图", "NVivo 质性分析", "Learning Management System (LMS)", "Trello 项目管理", "SurveyMonkey 问卷设计", "Google Forms 在线测评"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)