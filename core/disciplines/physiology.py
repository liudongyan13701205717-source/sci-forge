"""生理学学科论文支持：器官系统生理/稳态体裁、APS 引用样式与生理学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="physiology",
    aliases=("physiology", "生理学", "人体生理学", "human physiology", "器官生理",
             "organ physiology", "神经生理学", "neurophysiology", "心血管生理", "cardiovascular physiology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与生理过程）",
            "materials and methods（动物/人体实验与测定）",
            "results（生理数据）",
            "discussion（机制与意义）",
            "references",
        ),
        "clinical": (
            "abstract",
            "introduction",
            "methods（受试者与方案）",
            "results（生理指标变化）",
            "discussion（临床意义）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按系统/机制综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APS 样式（作者-年份；Am. J. Physiol. 遵循 APS 规范）",
    reporting_standards={
        "subject_info": "受试者/动物信息（物种、性别、年龄、体重）须报告",
        "experimental_protocol": "实验方案（麻醉、给药、测量）须完整",
        "measurement_methods": "生理指标测量方法（血压、血流、电生理）须报告",
        "ethics": "伦理审批（IACUC/IRB）须给出",
        "statistics": "统计检验与样本量须给出",
    },
    conventions=(
        "生理参数符号（BP、HR、CO、SV）首次出现处给出全称",
        "单位规范（mmHg、bpm、mL/min）",
        "给药剂量与途径（iv、ip、po）标注",
        "电生理记录（膜电位、电流钳、电压钳）术语统一",
        "统计显著性标注统一",
    ),
    key_venues=(
        "American Journal of Physiology",
        "Journal of Physiology",
        "Journal of Applied Physiology",
        "Physiological Reviews",
        "Hypertension",
        "Circulation Research",
    ),
    units_and_formulas_notes=(
        "血压用 mmHg；心率用 bpm；流量用 mL/min",
        "浓度用 mmol/L、μmol/L",
        "公式用 amsmath；血流动力学与电生理公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SEM 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "多道生理记录仪",
        "示波器",
        "Langendorff 离体心脏灌流装置",
        "GraphPad Prism",
        "R (tidyverse)",
    ),
    category="理学",
    databases=(
        "PubMed",
        "OpenAlex",
        "Europe PMC",
        "Crossref",
    ),
)