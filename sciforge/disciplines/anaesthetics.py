"""麻醉学科论文支持（英式拼写传统）：麻醉技术/区域阻滞/术中管理/术后镇痛体裁、BMA 样式与麻醉学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="anaesthetics",
    aliases=("anaesthetics", "麻醉学", "麻醉", "anaesthesia",
             "麻醉技术", "anaesthetic technique", "区域麻醉", "regional anaesthesia",
             "神经阻滞", "nerve block", "镇静", "sedation",
             "急性疼痛管理", "acute pain management", "重症医学", "critical care",
             "anaesthesia and intensive care", "围术期麻醉管理",
             "perioperative care", "麻醉与危重症"),
    paper_types={
        "research": (
            "abstract",
            "introduction（麻醉问题与临床假设）",
            "methods（人群、分组、麻醉方案与终点）",
            "results（围术期生理与镇痛数据）",
            "discussion（机理、安全性与推广性）",
            "limitations",
            "references",
        ),
        "technique": (
            "abstract",
            "introduction（技术背景与创新点）",
            "methods（病例/人群、超声协议与质量评价）",
            "results（阻滞成功率、感觉/运动阻滞分布与并发症）",
            "discussion（与既有技术比较与操作要点）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction（新颖性声明）",
            "case presentation（基线、麻醉过程与并发症）",
            "management and outcomes（处置时间线与结局）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "methods",
            "results",
            "outlook",
            "references",
        ),
    },
    citation_style="BMA/British Journal of Anaesthesia 样式（作者-年份；Anaesthesia 遵循 BMA 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "systematic_review": "系统综述遵循 PRISMA 2020 与 GRADE 分级",
        "diagnostic_imaging": "超声引导阻滞的图像质量评价遵循 SQUIRE 2.0 相关条目",
    },
    conventions=(
        "ASA 分级（ASA I-VI）与年龄/体质量须完整报告",
        "区域阻滞须报告药物浓度、容量、针具与超声引导情况",
        "血流动力学与麻醉深度参数（MAP、HR、BIS、EtCO2）单位须规范",
        "术后镇痛与并发症按时间窗（术后 24 h/48 h）分别报告",
        "缩写首次出现给出全称（如 EtCO2 = end-tidal carbon dioxide）",
    ),
    key_venues=(
        "Anaesthesia",
        "European Journal of Anaesthesiology",
        "Anaesthesia & Intensive Care",
        "Paediatric Anaesthesia",
        "Anaesthesia Crit Care Practice",
        "British Journal of Anaesthesia",
        "Anaesthesia and ICU Practice",
    ),
    units_and_formulas_notes=(
        "血压用 mmHg；心率用 bpm；剂量用 mg/kg 或 mg/kg/h",
        "药代参数（t1/2、Vd、Cl）须给出单位与计算依据",
        "感觉与运动阻滞分级（Bromage 评分）须给出量表定义",
        "疼痛评分（VAS/NRS）须注明范围与时间点",
        "统计结果给出均值 ± SD 与 95% CI；不良事件给出 OR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("GE Vivid S6", "GE Venue GO", "SonoSite Corex Edge", "Mindray M9", "Fujifilm Sonoace", "Sonoscape X8", "GE Cielsix Aisys CS", "Dräger Perseus", "Philips IntelliVue MX750", "Aspect BIS", "Natus Neurofax-2", "NIM STIM 200", "Möller NerveStimulator 2", "U.S. Medical MPS 30", "U.S. Medical TOF-Watch 200", "B.Braun Infusomat Space", "Masimo SET", "Vsm 2500", "ANSIM", "NYSORA", "Philips Respimat"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC"),
)
