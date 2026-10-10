"""健康护理计划学科论文支持：循证护理实践、护理评估与患者结局研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="health_care_programmes",
    aliases=("health_care_programmes", "健康护理计划", "护理实践", "循证护理", "护理评估", "患者管理", "护理教育"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（护理研究与设计）", "results（护理结局）", "discussion（讨论与循证实践）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例描述）", "analysis（护理问题分析）", "results（护理效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（护理理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "RCT 遵循 CONSORT", "k2": "观察性研究遵循 STROBE", "k3": "系统综述遵循 PRISMA"},
    conventions=("NANDA-I 诊断名称须注明版本", "护理干预须注明频率与持续时间", "结局指标须注明测量工具与版本", "患者结局须注明测量时点", "量表信效度须注明具体数值"),
    key_venues=("Journal of Advanced Nursing", "Nursing Research", "International Journal of Nursing Studies", "中华护理杂志", "中国全科医学"),
    units_and_formulas_notes=("疼痛评分：0-10 分（NRS）", "焦虑抑郁评分：分（量表得分）", "住院时间：d", "护理满意度：1-5 分制"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("电子护理信息系统（EHR）", "护理评估量表系统（NOC）", "疼痛评估电子记录系统", "SPSS", "Stata", "SAS", "R（统计分析）", "REDCap 电子数据采集", "Meta 分析软件（RevMan）", "患者结局管理信息系统（POM）", "护理敏感质量指标监测系统", "护士排班与人力配置系统", "远程护理监测平台", "伤口护理评估系统", "压疮风险评估工具（Braden）", "跌倒风险评估系统（HES）", "护理效果评价指标系统", "护士职业暴露监测系统", "护理循证实践指南工具", "护士培训模拟系统"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "循证护理实践平台（Cochrane Library）", "NANDA-I 护理诊断数据库"),
)
