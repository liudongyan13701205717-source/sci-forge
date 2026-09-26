"""兽医学科论文支持：REFLECT/ARRIVE 按研究设计路由与 Vancouver 引用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="veterinary_science",
    aliases=("veterinary", "veterinary science", "兽医学", "兽医",
             "animal science", "动物科学", "动物医学", "livestock", "畜牧"),
    paper_types={
        "randomized_trial": (
            "structured abstract",
            "introduction（临床问题与假设）",
            "methods（设计、动物群与实验单位、随机化、盲法、结局指标）",
            "results（流程图、基线表、疗效与安全性）",
            "discussion（外推性与动物福利）",
            "references",
        ),
        "cohort_study": (
            "structured abstract",
            "introduction",
            "methods（群体定义、暴露与结局、混杂控制）",
            "results（发病/存活表、效应量）",
            "discussion（生产性能与疾病控制含义）",
            "references",
        ),
        "case_series": (
            "abstract",
            "introduction",
            "case presentation（物种、品种、年龄、病史、检查与诊疗）",
            "discussion（鉴别诊断与文献对照）",
            "references",
        ),
        "diagnostic_accuracy": (
            "abstract",
            "introduction",
            "methods（参考标准、样本、盲法、STARD 流程）",
            "results（敏感度/特异度、ROC、似然比）",
            "discussion",
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
    citation_style="Vancouver（JAVMA/AJVR 体例，按引用顺序编号）",
    reporting_standards={
        "case_series": "CARE",
        "cohort": "STROBE",
        "case_control": "STROBE",
        "randomized_trial": "REFLECT（家畜与食品安全 RCT 报告规范）/ CONSORT",
        "systematic_review": "PRISMA",
        "diagnostic_accuracy": "STARD",
        "animal_research": "ARRIVE 2.0（动物实验报告条目）",
    },
    conventions=(
        "动物伦理：IACUC/伦理委员会批准号；遵循 3R 原则（替代/减少/优化）",
        "物种与群体描述完整：品种、年龄、性别、体重、饲养管理与免疫背景",
        "实验单位明确（个体/栏/群），必要时说明聚类效应校正",
        "动物福利与人道终点预先定义并报告",
        "病例报告去标识化：不披露畜主可识别信息",
    ),
    key_venues=(
        "JAVMA (Journal of the American Veterinary Medical Association)",
        "AJVR (American Journal of Veterinary Research)",
        "Veterinary Record",
        "Preventive Veterinary Medicine",
        "Veterinary Radiology & Ultrasound",
    ),
    units_and_formulas_notes=(
        "药物剂量统一 mg/kg 并给给药途径与频次；体重给 kg",
        "血清学结果给滴度（如 1:256）与检测方法（SN/ELISA）",
        "效应量 RR/OR/HR 给 95% CI；发病率给 per 1000 animal-years 等口径",
        "生产性能指标（日均增重 ADG、饲料转化率 FCR）给定义与测量周期",
        "样本量给功效分析参数与实验单位数（heads/litters）",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("SPSS", "PCR 仪", "兽用超声诊断仪", "R", "酶联免疫分析仪"),
    category="农学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
