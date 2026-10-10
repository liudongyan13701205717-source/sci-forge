"""工作场所健康与安全学科论文支持：职业卫生、安全防护与劳动保护研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="health_and_safety_in_the_work_place",
    aliases=("health_and_safety_in_the_work_place", "工作场所健康与安全", "职业卫生", "劳动安全", "职业防护", "工伤预防", "职业健康与安全"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（暴露评估方法）", "results（风险指标）", "discussion（讨论与防控建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（事故案例描述）", "analysis（危害因素分析）", "results（效果评价）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "RCT 遵循 CONSORT", "k2": "观察性研究遵循 STROBE", "k3": "系统综述遵循 PRISMA"},
    conventions=("职业暴露限值须注明标准来源（如 GBZ 2.1）", "监测方法须注明国标编号", "事故报告须注明时间/地点/工种", "防护用品须注明检测标准与等级", "统计周期须注明观测时长与单位"),
    key_venues=("Journal of Occupational and Environmental Medicine", "Scandinavian Journal of Work Environment & Health", "International Journal of Occupational Medicine and Environmental Health", "职业与健康", "中国工业卫生"),
    units_and_formulas_notes=("粉尘浓度：mg/m³", "噪声等效连续 A 声级：dB(A)", "温度：°C", "湿度：%RH"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("个人粉尘采样器", "噪声剂量计", "温湿度记录仪", "职业照度计", "通风换气量测试设备", "职业暴露生物监测分析仪", "工业 CT 扫描（X射线）", "可穿戴生命体征监测设备", "职业危害因素在线监测系统", "应急避难所模拟系统", "事故应急救援模拟训练平台", "职业健康监护信息管理系统", "工作危害分析（JHA）软件", "安全行为观察工具（BBS）", "职业安全健康培训平台", "个人防护用品佩戴检查系统", "职业卫生现场快速检测仪", "职业健康风险评估模型", "SPSS", "职业安全风险评估系统（FIRAS）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "职业接触限值（OEL）数据库"),
)
