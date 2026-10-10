"""康复医学与康复科学学科论文支持：运动生物力学/功能评定/康复干预体裁、ICF 框架与运动学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="allied_health_and_rehabilitation_science",
    aliases=("allied health and rehabilitation science", "康复医学", "康复科学",
             "rehabilitation medicine", "rehabilitation science", "神经康复",
             "neurorehabilitation", "骨科康复", "orthopaedic rehabilitation",
             "物理治疗", "physical therapy", "作业治疗", "occupational therapy",
             "言语病理学", "speech-language pathology", "步态分析", "gait analysis",
             "运动控制", "motor control", "辅具技术", "assistive technology",
             "ICF", "国际功能、残疾和健康分类"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、功能问题与运动学假设）",
            "methods（人群、纳入标准、设备协议与 ICF 分层）",
            "results（运动学/动力学与功能量表数据）",
            "discussion（与 ICF 功能-活动-参与层级的对应）",
            "limitations（样本量、设备信度与外推性）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法、平行组设计与最小样本量）",
            "results（主要/次要终点、效应量与安全事件）",
            "discussion（与等效试验及临床最小改善量的对比）",
            "trial registration（注册号与首次入组日期）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction（病例的临床意义与新颖性声明）",
            "case presentation（基线量表、影像与运动学证据）",
            "intervention and outcomes（时间线、剂量与结局轨迹）",
            "discussion（与既往病例的异同与假设）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "methods（检索策略、纳入排除与质量评价）",
            "results（证据汇总表与亚组比较）",
            "outlook",
            "references",
        ),
    },
    citation_style="Vancouver/AMA 样式（编号制；Arch. Phys. Med. Rehabil. 遵循 AMA 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明（含 CONSORT-ExtenD 扩展）",
        "case_report": "病例报告遵循 CARE 指南",
        "systematic_review": "系统综述遵循 PRISMA 2020 与 Cochrane 标准",
        "health_economics": "卫生经济评价遵循 ISPOR 立场声明",
        "scale_development": "量表编制与修订遵循 COSMIC 指南",
    },
    conventions=(
        "患者功能描述按 ICF（WHO）层级组织：身体功能与结构、活动、参与、环境因素",
        "运动学参数（关节角度、角速度、地面反作用力）须给出定义、坐标系与采样率",
        "量表报告原始分、标准化分与临床最小改善量（MCID）三者并列",
        "干预剂量须完整报告（频次、时长、周期与依从率）",
        "结果以均值 ± SD/SEM 与最小二乘均值报告，组间比较给出效应量与 95% CI",
        "术语首次出现给出中英文全称（如 ground reaction force, GRF）",
    ),
    key_venues=(
        "Archives of Physical Medicine and Rehabilitation",
        "Neurorehabilitation and Neural Repair",
        "Journal of NeuroEngineering and Rehabilitation",
        "Clinical Rehabilitation",
        "Gait & Posture",
        "Disability and Rehabilitation",
        "Journal of Rehabilitation Medicine",
    ),
    units_and_formulas_notes=(
        "角度用 °、角速度用 °/s；长度用 m、力用 N、质量用 kg",
        "功率用 W；力矩单位须与坐标系标注一致（Nm、Nm/kg）",
        "步态时空参数（步长、步频、步速）须标明测量方式（惯性/足板/视频）",
        "统计量统一用均值 ± SD（正态）或中位数 [IQR]（偏态）并注明分布检验",
        "置信区间与显著性水平全文一致（95% CI, α=0.05）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("KINOVEA", "PhysioTools", "Vicon Nexus", "OptiTrack", "FinalCadence Motion", "Dartfish", "Cortex", "Biomechanics Toolbox", "OpenSim", "Lokomat", "Armeo Power", "EksoNR", "GaitRite", "Zebris Freshness Walk", "Xsens MVN", "BTS Inertial Sensing System", "K-Motion GaitView", "Delsys Trigno EMG", "RehaCom", "MyoRep", "3D Slicer", "SPSS"),
    category="医学",
    databases=(
        "PubMed",
        "Cochrane Library",
        "OpenAlex",
        "CNKI",
    ),
)
