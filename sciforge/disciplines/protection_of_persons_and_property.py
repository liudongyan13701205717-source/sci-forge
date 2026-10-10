"""保护人员与财产学科论文支持：安保实务体裁、CONSORT 报告规范与安防系统注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="protection_of_persons_and_property",
    aliases=(
        "protection_of_persons_and_property",
        "人员与财产保护",
        "保护人员与财产",
        "Protection of persons and property",
        "安保实务",
        "安防",
        "财产保护",
        "Security and safety",
        "风险防控",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与威胁）",
            "methodology（研究方法）",
            "results（实证结果）",
            "discussion（管理启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（事件案例描述）",
            "analysis（防控与分析）",
            "results（处置与效果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（安防理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "quantitative": "量化研究遵循 ASA 报告规范",
        "case_study": "案例研究遵循 DSR-CASE 规范",
        "risk_assessment": "风险评估遵循 NIST SP 800-30 规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "数据须脱敏并说明访问条件",
    },
    conventions=(
        "财产清单与安防设备清单须完整",
        "损失金额与赔付须说明口径",
        "监控录像须标注时间、地点与保留期",
        "风险评估模型须披露假设与阈值",
        "保险与合规要求须符合当地法规",
    ),
    key_venues=(
        "Journal of Loss Prevention",
        "Property and Safety International",
        "Security Journal",
        "Journal of Criminal Justice",
        "Fire Safety Journal",
    ),
    units_and_formulas_notes=(
        "损失金额以「元」计并说明币种",
        "响应时间以分钟计，报警时长以秒计",
        "风险等级以定性分级或概率报告",
        "公式用 amsmath；风险=威胁×脆弱性×影响须展开",
        "覆盖率与命中率须给出计算口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Access Control System", "Intrusion Detection System", "Video Surveillance", "CCTV", "Biometric Scanner", "Alarm System", "Risk Assessment Matrix", "Crisis Management Software", "Body Worn Camera", "Thermal Imager", "Drone Inspection", "Radio Communication", "Mobile Patrol GPS", "Access Log Audit", "Incident Reporting", "SPSS", "R", "Excel", "VBA", "SAS"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
