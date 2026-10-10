"""劳动保护学科论文支持：职业安全健康、职业病防治、劳动条件与合规管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="labour_protection",
    aliases=(
        "labour_protection",
        "劳动保护",
        "Occupational Health and Safety",
        "OH&S",
        "Labour Protection",
        "Workplace Safety",
        "Occupational Hygiene",
        "Employee Protection",
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
        "k1": "ISO 45001:2018 职业健康安全管理体系",
        "k2": "GB/T 33000 企业安全生产标准化基本规范",
        "k3": "EU Framework Directive 89/391/EEC",
    },
    conventions=(
        "危害识别须采用JHA/HRA系统化方法",
        "剂量响应关系须引用权威职业接触限值（OEL/PC-TWA）",
        "事故数据须区分可记录事故率（TRIR）与总事故率",
        "合规报告须注明法规版本与生效日期",
        "个人防护装备（PPE）选用须按危害等级",
    ),
    key_venues=(
        "Safety Science",
        "Journal of Safety Research",
        "American Journal of Industrial Medicine",
        "International Journal of Occupational Safety",
        "中国安全生产科学技术",
    ),
    units_and_formulas_notes=(
        "噪声暴露以dB(A)表示，8h等效",
        "粉尘浓度以mg/m³表示",
        "职业接触限值（OEL）以mg/m³ 或 ppm 表示",
        "事故率（TRIR）=（可记录事故数/工时数）×200000",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SIFMA", "SafetyCulture", "InteLex", "OSHA", "NIOSH", "ANSI", "GB", "EN ISO", "ASTM", "DIN", "JIS", "SHEL", "JSA", "HAZOP", "FMEA", "RiskMatrix", "ISO 45001", "OHSAS 18001", "3M Safety", "NIOSH Pocket Guide"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
