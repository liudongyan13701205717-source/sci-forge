"""按摩（美容按摩/理疗按摩）学科论文支持：手法干预、人体反应与临床评价规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="massage",
    aliases=("massage", "按摩", "beauty massage", "bodywork", "手动康复",
             "手法治疗", "reflexology", "reflexology massage", "spa therapy"),
    paper_types={
        "research": ("abstract", "introduction（研究背景与假设）", "methodology（受试者、手法、剂量、随机化）", "results（疼痛/肌张力/生理指标变化）", "discussion（机制、局限与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（患者史与初始评估）", "analysis（手法选择与操作序列）", "results（功能与主观改善）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（按摩生理学与流派比较）", "evidence synthesis（RCT/系统综述证据分级）", "future directions", "references"),
    },
    citation_style="APA 7（临床手法类常用）",
    reporting_standards={
        "preregistration": "RCT 类研究须在 ClinicalTrials.gov 或 CNRI 预注册并给出注册号",
        "conventional_reporting": "干预类研究遵循 CONSORT 2010；回顾性研究遵循 STROBE",
        "blinding": "按摩属高难盲干预，须说明施术者/评估者/统计者三盲设计或替代方案",
    },
    conventions=(
        "手法名称首次出现给出国际通用名（ICM 编码）与所在流派（Swedish/Thai/Deep tissue 等）",
        "剂量三维表述：压力（kPa 或 N）× 时长（min）× 频次（次/周）",
        "疼痛评分统一使用 NRS/VAS 0-10 并给最小临床重要差异（MCID）",
        "人体测量与肌张力测给仪器型号、位置坐标与操作者资质",
        "涉及美容按摩时明确排除疾病主张，仅陈述舒适度与放松指标",
    ),
    key_venues=(
        "Journal of Bodywork and Movement Therapies",
        "Manual Therapy",
        "Complementary Therapies in Clinical Practice",
        "Journal of Clinical Densitometry",
        "Evidence-Based Complementary and Alternative Medicine",
    ),
    units_and_formulas_notes=(
        "压力单位 Pa/kPa；手法节奏以 bpm 或 每 10 秒循环次数记",
        "疼痛差值给 95% CI 与最小临床重要差异（如 NRS-3）",
        "肌张力/硬度测以 kPa·s 或 Shearography 单位",
        "热疗给温度 ℃、时长 min 与皮肤表面温度梯度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Kinesio taping 与弹性胶带", "Shiatsu 按摩床", "Reflexology 足底反射板", "TriggerPoint 手法探头", "Myoman 肌松仪", "GXT 2000XT 肌力测试仪", "Delsys Trigno EMG", "Kinexon Optotrak", "Optimus 6 治疗仪", "BioEMSYS 表面电极", "TENS 经皮神经电刺激仪", "热疗袋与冷敷包", "压力传感垫（Tekscan）", "肌骨超声探头", "Goniometer 量角器", "NRS/VAS 电子量表", "Statistical Package for Social Sciences (SPSS)", "R 统计软件", "Microsoft Excel", "LaTeX/BibTeX"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
