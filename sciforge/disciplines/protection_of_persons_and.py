"""保护人员学科论文支持：安全实务体裁、CONSORT 报告规范与事件数据注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="protection_of_persons_and",
    aliases=(
        "protection_of_persons_and",
        "人员保护",
        "人身保护",
        "Protection of persons",
        "保安",
        "安保",
        "公共安全管理",
        "Security",
        "Private security",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与威胁）",
            "methodology（研究方法）",
            "results（实证结果）",
            "discussion（实践启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（事件案例描述）",
            "analysis（响应与处置分析）",
            "results（处置结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（安保理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "quantitative": "量化研究遵循 ASA 报告规范",
        "case_study": "案例研究遵循 DSR-CASE 规范",
        "survey": "问卷调查遵循 AERA 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "数据须脱敏并说明访问条件",
    },
    conventions=(
        "事件类型、频次与时段须明确",
        "警力配置与响应时间须报告",
        "处置结果须区分成功与失败",
        "个人身份信息须脱敏处理",
        "证据链完整性须符合法律要求",
    ),
    key_venues=(
        "Security Journal",
        "Journal of Criminal Justice",
        "Policing and Society",
        "Journal of Police and Criminal Psychology",
        "Asian Journal of Criminology",
    ),
    units_and_formulas_notes=(
        "人数以「人」计，时段以小时/日计",
        "响应时间以分钟计",
        "覆盖率以百分比计",
        "公式用 amsmath；风险等级定义式须明确",
        "置信区间须与样本量一并报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Access Control System", "Intrusion Detection System", "Video Surveillance", "Access Monitor", "Biometric Scanner", "CCTV", "Alarm System", "Risk Assessment", "Crisis Management", "First Aid Kit", "Body Worn Camera", "Thermal Imager", "Drone Inspection", "Radio Communication", "Mobile Patrol", "Access Log", "Incident Reporting", "SPSS", "R", "Excel"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
