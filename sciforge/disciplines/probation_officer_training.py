"""缓刑官培训学科论文支持：社区矫正人员培训体系、能力评估与职业化建设研究体裁、APA 引用样式与培训评估注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="probation_officer_training",
    aliases=("probation_officer_training", "缓刑官培训", "社区矫正官培训", "probation officer", "社区矫正培训", "probation training", "司法辅助人员培训", "correctional services training", "社区矫正工作"),
    paper_types={
        "research": ("abstract", "introduction（培训问题与背景）", "methodology（培训体系设计、评估工具与数据采集）", "results（培训成效与能力变化）", "discussion（职业化建设与政策建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（机构、课程与参训人员描述）", "analysis（培训过程、考核与成效分析）", "results（能力评估与个案结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（社区矫正与培训理论综述）", "evidence synthesis（培训证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "培训课时、对象与考核方式须完整披露", "k2": "评估量表须注明版本、编制者与信效度", "k3": "个案处理记录须匿名化并声明伦理审查"},
    conventions=("培训层级与认证标准须注明", "评估量表须注明版本与信效度", "个案分析须区分事实陈述与判断", "再犯率用 % 表示并注明随访期", "国际比较须注明各国制度差异"),
    key_venues=("Journal of Correctional Education", "The Prison Journal", "Federal Probation", "Crime, Law and Society", "Crime, Delinquency and Social Control"),
    units_and_formulas_notes=("培训课时：学时；合格率：%", "再犯率用 % 表示并注明随访期", "量表用 Likert 5 级表示", "统计检验注明 p 值与效应量"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "SAS", "JASP", "Excel", "NVivo", "Atlas.ti", "MAXQDA", "RedCap", "Qualtrics", "Google Forms", "Moodle", "Canvas LMS", "LSI-R 再犯风险评估", "VAS 暴力风险评估量表", "SCL-90 症状自评量表", "社区矫正信息管理平台", "电子脚镣 GPS 定位系统", "远程视频会见系统"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
