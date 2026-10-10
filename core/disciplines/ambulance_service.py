"""急救医疗服务学科论文支持：院前急救/调度/复苏/重症转运体裁、CONSORT/CARE 与急救时间窗注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ambulance_service",
    aliases=("ambulance service", "急救医疗服务", "EMS",
             "emergency medical services", "院前急救", "pre-hospital care",
             "救护调度", "emergency dispatch", "急诊医学", "emergency medicine",
             "resuscitation", "复苏", "advanced life support", "ALS",
             "basic life support", "BLS", "critical care transport", "重症转运",
             "trauma system", "创伤体系", "time-critical care", "时间窗救治"),
    paper_types={
        "research": (
            "abstract",
            "introduction（急救问题、时间窗与临床假设）",
            "methods（人群、分级、派车算法与终点定义）",
            "results（时间参数、结局与安全数据）",
            "discussion（调度-救治-交接链条与可推广性）",
            "limitations（缺失时间戳、季节性与转诊偏差）",
            "references",
        ),
        "dispatch_audit": (
            "abstract",
            "introduction",
            "methods（CAD 队列、地理划分、派车规则与对照）",
            "results（响应时间分布、分位数与容量瓶颈）",
            "discussion（容量规划与政策建议）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction（病例的临床意义与新颖性声明）",
            "case presentation（基线、检查与实验室证据）",
            "resuscitation course（按 STOBEC 顺序的时间线）",
            "outcome and discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "methods（检索策略、纳入排除与质量评价）",
            "results",
            "outlook",
            "references",
        ),
    },
    citation_style="Vancouver/NLM 样式（编号制；Prehospital Emerg. Care 遵循 CMA 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "case_series": "病例报告遵循 CARE 指南",
        "audit": "质量改进与审计遵循 SQUIRE 2.0 指南",
        "triage": "分级标准（ESI 2011、Manchester）须注明版本与使用层级",
        "dispatch": "调度研究须报告 CAD 队列、派车算法与地理服务半径",
    },
    conventions=(
        "时间参数以 s/min 计，并明确起点（到达现场、送达急诊、完成交接）",
        "分级与严重程度（ESI、ISS、SIRS）须注明版本与判定时点",
        "复苏操作按 STOBEC（Scene/Tamponade/Oxygen/Breathing/Compressions/ECG）顺序表述",
        "药物剂量按 mg 或 mg/kg 报告，并注明给药途径与泵速",
        "转运过程不良事件（心跳骤停、脱管、跌落）须完整记录并报告",
        "统计以均值 ± SD 或中位数 [IQR] 报告，救援时间用秒级分辨率",
    ),
    key_venues=(
        "Prehospital Emergency Care",
        "Resuscitation",
        "European Journal of Emergency Medicine",
        "Journal of Trauma and Acute Care Surgery",
        "Western Journal of Emergency Medicine",
        "Emergency Medicine Journal",
        "Resuscitation Plus",
    ),
    units_and_formulas_notes=(
        "时间用 s/min；距离用 km；位置以 GPS 十进制度报告",
        "血压用 mmHg；心率用 bpm；血氧饱和度用 %",
        "急救响应时间给出均值、中位数与 P90（用于调度容量规划）",
        "存活率与转运成功率以 % 报告并附 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("EMSim", "EMSCOPE", "Laerdal SimMan 3G", "Zoll CPRD", "Ambu HeartStart XR", "Life in the Balance", "Epic EMS Response", "EPiC EMS (Avidis)", "Avidity CarePoint", "Harris Command Center CAD", "Motorola CAD", "eMIS", "SPOTRACK", "Samsara Track", "Philips IntelliVue MX", "Sonosite EdgePoint", "i-STAT Handheld", "GloFocal 20", "EDAN iMonitor V9", "Masimo Radical-7"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC"),
)
