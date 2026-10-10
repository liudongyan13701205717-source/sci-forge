"""监狱工作学科论文支持：在押管理、矫正干预、再犯评估与监狱政策研究体裁、法学引注样式与矫正记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="prison_work",
    aliases=("prison_work", "监狱工作", "监狱学", "监狱管理", "prison administration", "矫正工作", "corrections", "刑满释放管理", "监狱政策"),
    paper_types={
        "research": ("abstract", "introduction（矫正问题与研究动机）", "methodology（样本、量表与统计分析）", "results（在押状况、干预与再犯结果）", "discussion（政策与实践建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（机构、人员与个案描述）", "analysis（管理、干预与制度分析）", "results（个案与机构发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（监狱学与矫正理论综述）", "evidence synthesis（矫正证据综合）", "future directions", "references"),
    },
    citation_style="《法学引注手册》（中文稿）/ APA 7（英文稿）",
    reporting_standards={"k1": "再犯率须注明统计口径、分母与随访期", "k2": "在押人员信息须匿名化并声明伦理审查", "k3": "干预效果须给出对照组、效应量与置信区间"},
    conventions=("再犯率用 % 表示并注明随访期", "人均指标须注明统计期间与口径", "机构类型须分类说明（关押、教育、生产等）", "量表须注明版本、编制者与信效度", "敏感数据须匿名化处理"),
    key_venues=("监狱学刊", "犯罪学评论", "Journal of Correctional Education", "Federal Probation", "The Prison Journal"),
    units_and_formulas_notes=("再犯率用 % 并注明随访期（月/年）", "人均日支出：元/人·日；容量：人/平方米", "量表用 Likert 5 级表示", "统计检验注明 p 值与效应量 d 或 odds ratio"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "SAS", "JASP", "Excel", "NVivo", "Atlas.ti", "MAXQDA", "RedCap", "Qualtrics", "Google Forms", "LSI-R 再犯风险评估工具", "VAS 暴力风险评估量表", "PCL-R 精神变态检核表", "SCL-90 症状自评量表", "监狱管理信息系统", "远程视频会见系统", "电子脚镣定位系统", "生物识别门禁系统"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
