"""实验室技术员项目学科论文支持：实验技术操作、仪器分析、质控与检测流程。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="laboratory_technician_programmes",
    aliases=(
        "laboratory_technician_programmes",
        "实验室技术员项目",
        "Laboratory Technician",
        "Lab Tech Training",
        "Advanced Lab Technician",
        "Lab Technician B",
        "Applied Laboratory Science",
        "Lab Analytical Technician",
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
        "k1": "CLSI EP10 精密度评估",
        "k2": "ISO 15189 医学实验室质量与能力",
        "k3": "CLIA 88 临床实验室改进法",
    },
    conventions=(
        "检测流程须遵循院内SOP且版本可追溯",
        "仪器校准须记录校准物批次与有效期",
        "质控数据须按Levey-Jennings图评估",
        "样本接收须记录时间、状态与温度",
        "检测异常须触发复检与报告流程",
    ),
    key_venues=(
        "Clinical Chemistry",
        "Journal of Clinical Laboratory Analysis",
        "Clinical Biochemistry",
        "Laboratory Medicine",
        "Medical Laboratory Sciences",
    ),
    units_and_formulas_notes=(
        "浓度以mol/L、mg/dL 或 IU/L 表示",
        "酶活性以U/L 表示，注明反应温度",
        "血红蛋白：g/L 或 g/dL",
        "细胞计数：×10⁹/L",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("LabWare", "STARLIMS", "Benchling", "LabArchives", "OpenBench", "SmartLab", "Dotmatics", "SciGenie", "Labguru", "Waters Chromeleon", "Agilent OpenLAB", "Thermo Fisher SampleManager", "Beckman Coulter DxH 900", "Sysmex XN-1000", "Roche Cobas 8000", "Abbott Architect c8000", "HITACHI Cobas e601", "Mindray BC-6800", "Bio-Rad DxC 800", "Qualitas"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
