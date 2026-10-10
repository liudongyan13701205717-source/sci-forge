"""Data entry 学科论文支持：数据录入/数字化/OCR 分析体裁、APA 样式与数据质量注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="data_entry",
    aliases=(
        "data_entry", "数据录入", "数据输入", "data input", "数据采集",
        "数据标注", "data annotation", "digitization", "数字化", "OCR",
        "文档数字化", "转录", "transcription",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与数据录入问题）",
            "methodology（流程、工具与质量控制）",
            "results（准确率、效率与产出）",
            "discussion（权衡与改进）",
            "conclusions（结论与建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（案例背景）",
            "analysis（流程与问题分析）",
            "conclusions（结论与启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（工具与技术综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份）",
    reporting_standards={
        "quantitative": "定量报告遵循数据质量报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "human_evaluation": "人工评估须报告标注者、样本量与一致性",
    },
    conventions=(
        "数据来源、格式（纸质/电子/扫描件）与总量须报告",
        "录入准确率、单位时间吞吐量、错误类型与校验流程须明确",
        "涉及人工转录/标注时须报告标注者、指导手册与一致性（如 κ）",
        "所有录入数据须说明去标识化与访问控制措施",
        "工具版本与运行环境须报告",
    ),
    key_venues=(
        "Journal of the American Society for Information Science and Technology",
        "Digital Scholarship in the Humanities",
        "Journal of Documentation",
        "Library, Information and Knowledge Research",
        "Digital Humanities Journal",
        "Information Processing & Management",
        "Journal of Data and Information Quality",
    ),
    units_and_formulas_notes=(
        "数量用条/张/字/页；吞吐量用 行/小时 或 张/小时",
        "准确率/召回率用 % 或小数",
        "时间用 分:秒 或 小时",
        "公式用 amsmath；显示公式仅在被引用时编号",
        "所有变量首次出现时给出符号与单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Google Sheets", "Microsoft Excel", "Airtable", "Google Forms", "Typeform", "SurveyMonkey", "Qualtrics", "ABBYY FineReader", "Adobe Acrobat Pro", "Tesseract OCR", "Microsoft Azure AI Document Intelligence", "Amazon Textract", "Google Cloud Document AI", "Kofax TotalAgility", "Rozetta (Rocsoft)", "OpenRefine", "Zapier", "UiPath", "Automation Anywhere", "Blue Prism", "Power Automate", "Nintex", "Rossum", "Nanonets", "Label Studio", "CVAT", "Prodigy", "Doccano", "Amazon Mechanical Turk", "Remotasks", "Snowball", "InfluxDB"),
    category="管理学",
    databases=("arXiv", "OpenAlex", "Crossref", "DOAJ"),
)
