"""计算机辅助支持学科论文支持：IT 支持与服务管理体裁、IEEE/APA 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_support",
    aliases=(
        "computer support", "计算机辅助支持", "计算机支持", "IT support", "IT 支持",
        "IT 服务管理", "IT service management", "help desk", "helpdesk",
        "服务台", "服务支持", "computer aided support",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work",
            "method（支持流程/方法设计）",
            "evaluation（评估与数据）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context（组织与系统背景）",
            "intervention（干预/实施）",
            "results（效果与指标）",
            "discussion",
            "references",
        ),
        "report": (
            "abstract",
            "executive summary",
            "scope（范围与需求）",
            "findings（诊断与发现）",
            "recommendations（建议）",
            "references",
        ),
    },
    citation_style="APA 7（管理/信息科学常用）",
    reporting_standards={
        "case_study": "案例研究遵循 IS 案例研究方法学",
        "survey": "调查遵循问卷设计与样本报告规范",
        "metrics": "SLA/SLI 指标定义须明确",
    },
    conventions=(
        "工单编号、事件编号与 SLA 分级（P1–P4）术语统一",
        "评估须区分定量指标（MTTR/MTBF/首次解决率）与定性证据",
        "组织情境与利益相关方角色须先说明，避免脱离场景下的普适断言",
        "所有截图与日志须去除敏感信息（凭据、IP、内部路径）",
    ),
    key_venues=(
        "MIS Quarterly",
        "Journal of the Association for Information Systems (JAIS)",
        "Journal of Information Technology",
        "Journal of Enterprise Information Management",
        "International Journal of IT Standards & Standardization Research",
        "IT Professional (IEEE)",
        "Communications of the ACM",
    ),
    units_and_formulas_notes=(
        "时长用分钟/小时并明确时钟口径（工作日/自然日）",
        "SLA 用百分比标注有效小时口径（如 24×7 vs 9×5）",
        "公式用 amsmath；SLI/SLA 数学表达须一致",
        "工单等级须用 P1–P4 统一，MTTR/MTBF 须给计算口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Jira Service Management", "ServiceNow", "Zendesk", "Freshservice", "OSD (OTRS)", "BMC Helix", "Microsoft Service Manager", "Ivanti Service Desk", "Snipe-IT", "GLPI", "Zammad", "Lemonade Ticketing", "Rundeck", "Freshdesk", "Backstage", "PagerDuty", "Grafana", "Datadog", "New Relic", "Splunk"),
    category="工学",
    databases=("OpenAlex", "Crossref", "IEEE Xplore"),
)
