"""麻醉学学科论文支持：麻醉临床/药理体裁、ASA/Anesthesiology 引用样式与麻醉学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="anesthesiology",
    aliases=("anesthesiology", "麻醉学", "麻醉", "围术期医学",
             "perioperative medicine", "麻醉科"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与麻醉问题）",
            "methods（研究设计与人群）",
            "results（血流动力学与结局数据）",
            "discussion（机理与临床意义）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法与统计）",
            "results（疗效与安全性终点）",
            "discussion（与既往试验对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="ASA/Anesthesiology 样式（作者-年份；Anesthesiology 遵循 ASA 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "quality_improvement": "质量改进研究遵循 SQUIRE 2.0 指南",
    },
    conventions=(
        "ASA 分级（ASA I-VI）须注明",
        "麻醉方式（全麻/椎管内/区域阻滞）须报告",
        "血流动力学参数（MAP、HR）单位须规范",
        "药物剂量（mg/kg、mg/kg/h）须完整",
        "监测参数（SpO₂、EtCO₂）缩写首次出现给出全称",
    ),
    key_venues=(
        "Anesthesiology",
        "British Journal of Anaesthesia",
        "Anesthesia & Analgesia",
        "Journal of Clinical Anesthesia",
        "Anaesthesia",
        "Regional Anesthesia & Pain Medicine",
    ),
    units_and_formulas_notes=(
        "血压用 mmHg；心率用 bpm；剂量用 mg/kg",
        "公式用 amsmath；MAC 与药代参数计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "不良事件给出 RR/OR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("麻醉深度监测仪", "有创血压监测仪", "麻醉机", "神经肌肉传导监测仪", "R", "SPSS"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC"),
)