"""劳动安全学科论文支持：事故预防、风险评估、应急救援与安全管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="labour_security",
    aliases=(
        "labour_security",
        "劳动安全",
        "Industrial Safety",
        "Workplace Safety Management",
        "Labour Security",
        "Occupational Safety",
        "Process Safety",
        "Industrial Safety Engineering",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（绪论）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA",
    reporting_standards={
        "k1": "GB 18218 危险化学品重大危险源辨识",
        "k2": "IEC 61508 功能安全标准",
        "k3": "ISO 22301 业务连续性管理体系",
    },
    conventions=(
        "事故分析须采用事故树（FTA）与事件树（ETA）",
        "风险矩阵须标明可能性与严重性分级",
        "安全措施须区分工程控制、管理措施与PPE",
        "应急演练数据须记录时间与恢复力指标",
        "安全系统须通过HAZID/HAZOP/LOPA评估",
    ),
    key_venues=(
        "Process Safety Progress",
        "Journal of Loss Prevention in the Process Industries",
        "Safety Science",
        "Journal of Hazardous Materials",
        "中国安全生产科学技术",
    ),
    units_and_formulas_notes=(
        "风险值R=L×S（可能性×严重性）",
        "安全完整性等级SIL: SIL1~SIL4",
        "平均失效前时间MTBF以h表示",
        "危险源辨识按GB 18218阈值判定",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SafetyCulture", "InteLex", "OSHA", "NIOSH", "ANSI", "EN ISO", "ASTM", "GB", "JIS", "DIN", "SHEL", "JSA", "HAZOP", "LOPA", "RiskMatrix", "ISO 45001", "IEC 61508", "SIFMA", "Plant Risk Management", "Process Safety Pro"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
