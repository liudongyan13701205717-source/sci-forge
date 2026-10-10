"""Chiropractic 学科论文支持：脊椎调整/整脊医学体裁、APA 引用样式与整脊评估记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chiropractic",
    aliases=(
        "Chiropractic", "chiropractic", "chiropractors",
        "chiropractic care", "chiropractic medicine",
        "脊椎调整", "整脊医学", "整脊疗法", "手法医学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（临床问题与整脊假设）",
            "methods（试验设计、亚组与手法操作定义）",
            "results（疼痛/功能/影像/生物力学结果）",
            "discussion（临床意义与替代治疗比较）",
            "conclusion",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机/盲法/对照与 CONSORT 报告）",
            "results",
            "discussion",
            "adverse_events",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "search_strategy",
            "main_developments",
            "evidence_quality",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份；J Chiropr Med 遵循 APA 规范）",
    reporting_standards={
        "randomized_trial": "遵循 CONSORT 声明并预注册（ClinicalTrials.gov / ChiCTR）",
        "systematic_review": "遵循 PRISMA 2020 声明与 GRADE 证据分级",
        "patient_reported_outcomes": "疼痛报告遵循 ICHD-3；功能评估遵循 COMET 手册",
        "case_report": "遵循 CARE 2.0 声明",
        "safety": "副作用/不良事件须按 SAE 标准上报并完整统计",
    },
    conventions=(
        "脊柱解剖定位用 T1–T12、L1–L5 等标准节段标记；关节/椎间盘/软组织名称首次出现需中英文对照",
        "亚组分类（如 HVLA、肌能量、软组织松弛）须在方法处明确定义操作与力度",
        "疼痛评分用 VAS/NRS；功能评估（如 Oswestry、NDI、RMDQ）用标准量表全称与首次出现缩写",
        "影像结果须报告体位、序列参数与放射剂量；骨性改变与退行性征象分开描述",
        "亚组间统计量给出均值/中位数（IQR）与 95% CI；多亚组分析须校正",
    ),
    key_venues=(
        "Journal of Chiropractic Medicine",
        "Journal of Manipulative and Physiological Therapeutics",
        "Journal of Chiropractic Science",
        "Spine",
        "European Spine Journal",
        "Clinical Biomechanics",
    ),
    units_and_formulas_notes=(
        "疼痛 VAS/NRS 0–10；活动度用度（°）；力/扭矩用 N、N·m",
        "样本量计算须给出 α、1-β 与效应量；多亚组比较给出校正方法",
        "统计结果报告 p 值（<0.05）与效应量（Cohen's d、η²）",
        "骨密度、椎间高度以 mm、mg/cm² 报告；影像报告注明设备与序列",
        "所有量表引用最新版本与计分方向",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集", "专利"),
    tools=("Thomson 整脊治疗台", "Diversified 整脊台", "Activator Method 手法器械", "Arson 手指力计", "Mensuration 尺（脊柱活动度测量）", "数字放射摄影（DR）", "低剂量 CT", "MRI 磁共振成像", "Biodex 等速肌力测试系统", "MyotonPRO 肌硬度/振动分析仪", "Xsens 运动捕捉系统", "Qualisys Motion Capture", "Optex 脊柱姿态分析", "ChiroBase 整脊文献库", "R 统计软件", "SPSS Statistics", "Stata", "JASP", "REManMan 系统综述流程管理", "OSF 预注册平台"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref", "Cochrane Library"),
)
