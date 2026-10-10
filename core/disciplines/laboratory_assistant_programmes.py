"""实验室助理项目学科论文支持：基础实验操作、样本处理、仪器使用与实验室安全。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="laboratory_assistant_programmes",
    aliases=(
        "laboratory_assistant_programmes",
        "实验室助理项目",
        "Laboratory Assistant",
        "Lab Technician Foundation",
        "General Science Lab",
        "Pre-Lab Technology",
        "Clinical Lab Assistant",
        "Wet Lab Support",
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
        "k1": "CLSI GP33 生物安全基础",
        "k2": "ISO 9001 质量管理体系",
        "k3": "ISO/IEC 17025 检测和校准实验室",
    },
    conventions=(
        "样本编号须符合院内编码规范且可全程追溯",
        "仪器使用前须记录校准状态与效期",
        "试剂使用须遵循GHS危险品标识与SDS",
        "实验记录遵循ALCOA+原则",
        "生物安全等级BSL-1/BSL-2 操作按CLSI GP33",
    ),
    key_venues=(
        "Clinical Chemistry",
        "American Journal of Clinical Pathology",
        "Clinical Laboratory Science",
        "Medical Laboratory Sciences",
        "Laboratory Medicine",
    ),
    units_and_formulas_notes=(
        "浓度以mol/L、mg/L、% w/v 或 % v/v 表示",
        "温度：℃，体积：mL 或 L",
        "吸光度以nm波长与OD值标注",
        "时间用s、min、h",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("LabWare LIMS", "Benchling", "LabArchives", "OpenBench", "SmartLab", "SciGenie", "Labguru", "EHSpoint", "Qualitas", "SampleTracc", "Thermo Fisher SampleManager", "Agilent OpenLAB", "Waters Chromeleon", "STARLIMS", "Dotmatics", "Silex", "LabLogic", "OpenLab CDS", "LabSight", "LabSolutions"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
