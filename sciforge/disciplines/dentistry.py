"""口腔医学科论文支持：CONSORT/STROBE 按研究设计路由与 Vancouver 引用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dentistry",
    aliases=("dentistry", "口腔医学", "口腔", "牙科", "dental",
             "stomatology", "牙体牙髓", "牙周", "正畸", "修复"),
    paper_types={
        "rct": (
            "structured abstract",
            "introduction（临床问题与假设）",
            "methods（设计、牙位选择、随机化、盲法、结局指标）",
            "results（失访流程、基线表、成功率与并发症）",
            "discussion（临床意义与局限）",
            "references",
        ),
        "cohort_study": (
            "structured abstract",
            "introduction",
            "methods（队列定义、暴露与结局、混杂控制）",
            "results（生存/留存曲线、效应量）",
            "discussion（预测因素与临床应用）",
            "references",
        ),
        "in_vitro_study": (
            "abstract",
            "introduction（研究目的与材料机制）",
            "methods（样本制备、分组、测试标准、统计方法）",
            "results（力学/微渗漏等测试结果表）",
            "discussion（与文献对照、局限）",
            "references",
        ),
        "case_series": (
            "abstract",
            "introduction",
            "case presentation（主诉、牙位、检查、影像、治疗经过）",
            "discussion（鉴别诊断与随访证据）",
            "references",
        ),
        "systematic_review": (
            "structured abstract",
            "introduction",
            "methods（PICO、检索、纳排、偏倚评估）",
            "results（森林图、GRADE 证据等级）",
            "discussion",
            "references",
        ),
    },
    citation_style="Vancouver（按引用顺序编号，口腔期刊主流样式）",
    reporting_standards={
        "case_series": "CARE",
        "cohort": "STROBE",
        "case_control": "STROBE",
        "randomized_trial": "CONSORT",
        "systematic_review": "PRISMA",
        "diagnostic_accuracy": "STARD（影像与龋病诊断研究）",
        "in_vitro": "ISO 材料测试标准（如 ISO 4049、ISO 14801）+ 测试协议披露",
    },
    conventions=(
        "牙位记录统一使用 FDI 两位数表示法（如 16、36）",
        "伦理：人体研究给 IRB 批准与知情同意；离体牙研究说明来源与知情",
        "材料报告给出品牌、批次、成分与固化参数",
        "影像检查注明设备、曝光参数与评估者盲法",
        "临床结局区分客观指标与患者报告结局（如 VAS 疼痛）",
    ),
    key_venues=(
        "Journal of Dental Research (JDR)",
        "Journal of Clinical Periodontology",
        "Dental Materials",
        "Journal of Endodontics",
        "Caries Research",
    ),
    units_and_formulas_notes=(
        "力学量给 SI 单位：力 N、粘接强度 MPa、扭矩 N·cm",
        "磨损/边缘密合给 μm 口径；微渗漏评分注明分级标准",
        "生存分析给留存率与 95% CI，注明随访时长与删失",
        "样本量以牙位/患者为独立单位，必要时说明聚类（cluster）校正",
        "剂量（如氟化物 ppm F、麻醉 mg/kg）与给药途径完整",
    ),
)
