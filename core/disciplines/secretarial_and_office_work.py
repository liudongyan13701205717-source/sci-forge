"""秘书与办公学科论文支持：办公管理/文书处理/档案管理/行政效率体裁、APA 7 管理学学术引用样式与办公度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="secretarial_and_office_work",
    aliases=("secretarial_and_office_work", "秘书与办公", "办公管理", "文书处理", "secretarial studies", "office administration"),
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
        "data": "办公流程数据须报告采集方式、样本量与质量控制",
        "efficiency": "效率评估须报告指标定义、计算公式与基准对比",
        "ethics": "涉及员工数据研究须报告伦理审查与知情同意",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "办公流程须注明标准作业程序（SOP）版本与生效日期",
        "效率指标须统一口径：处理时间用 min/件，错误率用 %",
        "档案分类须注明分类标准与编号规则",
        "引用行政文件须标注文号、发文机关与发文日期",
        "软件工具须注明版本与配置参数",
    ),
    key_venues=(
        "Journal of Business and Economics",
        "Administrative Quarterly",
        "Public Administration Review",
        "Journal of Management Studies",
        "MIS Quarterly",
    ),
    units_and_formulas_notes=(
        "处理时间用 min/件；错误率用 %；满意度用 Likert 5 级量表",
        "效率提升用 % 或倍数；成本节约用货币单位标注币种",
        "公式用 amsmath；效率计算公式须编号",
        "统计结果给出均值 ± 标准差与样本量；显著性用 p 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Office 办公套件", "Google Workspace 协作办公", "Adobe Acrobat 文档处理", "Tesseract OCR 文字识别", "EndNote 参考文献管理", "Evernote 笔记管理", "Notion 知识管理", "Trello 项目管理", "Asana 任务管理", "Microsoft Teams 协作", "Slack 即时通讯", "Docusign 电子签名", "SharePoint 文档管理", "Microsoft Outlook 邮件管理", "Google Drive 云存储", "Excel 数据分析", "LaTeX 排版", "Python 自动化脚本", "SPSS 统计分析", "Origin 绘图"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)