"""家政学科论文支持：家政管理、生活技能教育与家庭发展研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="home_economics",
    aliases=("home_economics", "家政学", "家政", "家庭经济学", "生活技能教育", "Home Economics", "Family and Consumer Sciences", "Home Management", "Domestic Science"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "AFTERS 家政与家庭生活教育报告规范", "k2": "CRESST 消费者教育研究规范", "k3": "GB/T 30324 家政服务标准"},
    conventions=("家庭人口学指标须注明城乡与地区", "消费金额须标注本币与年代", "技能测评须注明量信效度", "访谈转录须脱敏并标注家庭编码", "教学实验须注明班数与课时"),
    key_venues=("Journal of Family and Consumer Sciences", "Family and Consumer Sciences Research Journal", "Journal of Extension", "Journal of Home Economics", "Housing Science"),
    units_and_formulas_notes=("收入/支出：元/年 或 美元/年", "面积：m²", "温度：℃", "量表得分须注明计分方向"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R（统计建模）", "Stata", "NVivo（质性分析）", "MAXQDA", "ATLAS.ti", "Google Forms（问卷）", "Qualtrics", "SurveyMonkey", "Adobe InDesign（教材排版）", "Microsoft Excel", "Origin（数据绘图）", "JASP", "EndNote", "Zotero", "RefWorks", "Kitchen Scale 计量设备", "Thermometer 温度计", "Sewing Machine 缝纫机（教学设备）", "Home Energy Monitor 家庭能耗监测仪"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
