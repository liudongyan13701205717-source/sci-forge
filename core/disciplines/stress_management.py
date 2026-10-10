"""Stress management 学科论文支持：压力评估/干预/生物反馈/心理量表。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="stress_management",
    aliases=(
        "stress_management", "Stress management", "压力管理",
        "压力调节", "压力应对", "心理健康",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methods（评估工具与干预方案）",
            "results（压力指标变化）",
            "discussion（机制讨论与临床意义）",
            "references",
        ),
        "intervention_study": (
            "abstract",
            "introduction",
            "methods（随机化、盲法与统计）",
            "results（疗效与安全性终点）",
            "discussion（与既往干预对比）",
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
    citation_style="APA 7（作者-年份；括号式）",
    reporting_standards={
        "psychometric": "心理量表须报告 Cronbach's α、复测信度与因子结构",
        "intervention": "干预研究须报告随机化方案、盲法实施与脱落率",
        "biological_marker": "生物标志物须报告检测方法、参考范围与批间变异",
        "ethical_approval": "伦理审批与知情同意须声明",
    },
    conventions=(
        "量表名称与版本须注明（如 PSS-10）",
        "压力指标须注明测量时间与生理状态",
        "干预方案须报告频率、时长与具体内容",
        "统计检验须报告效应量（Cohen's d）与 95% CI",
        "伦理审批号与试验注册号须声明",
    ),
    key_venues=(
        "Journal of Applied Psychology",
        "Stress and Health",
        "Psychological Bulletin",
        "Frontiers in Psychology",
        "中国心理卫生杂志",
    ),
    units_and_formulas_notes=(
        "心率变异性（HRV）用 ms 或 bpm",
        "皮质醇用 nmol/L 或 μg/dL",
        "压力量表用 分（总分或均分）",
        "心理效应量用 Cohen's d 或 η²",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("心理量表（SAS/SDS/PSS）", "生物反馈仪", "正念冥想 APP（Headspace/Calm）", "皮质醇免疫酶分析仪", "可穿戴心率变异性监测（HRV）", "认知行为治疗平台（CBT）", "虚拟现实放松系统（VR）", "呼吸训练设备（Nadi）", "情绪识别软件", "睡眠监测仪（ActiGraph）", "压力日志 APP（Daylio）", "脑电波监测仪（EEG 放松训练）", "肌电图生物反馈仪（EMG）", "皮肤电导反应仪（GSR）", "心率变异性分析软件（Kubios）", "虚拟现实生物反馈系统", "正念减压课程平台（MBSR）", "企业 EAP 管理系统", "心理测评系统（MMPI/16PF）", "压力评估与干预软件"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC", "Semantic Scholar"),
)
