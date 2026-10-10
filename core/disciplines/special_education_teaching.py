"""特殊教育教学学科论文支持：IEP 干预设计/个别化教育/融合教育体裁、APA 7 与 SRQR 注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="special_education_teaching",
    aliases=("special_education_teaching", "特殊教育教学", "Special Education Teaching", "特殊教育", "个别化教育", "融合教育", "IEP", "special education", "残障教育"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份；教育研究主流样式）",
    reporting_standards={
        "intervention_design": "报告干预内容、频次、时长、实施者与理论依据（CONSORT 精神）",
        "single_case": "单被试设计须报告基线/干预期、稳定性与重叠百分比（PND/CUSUM）",
        "qualitative": "质性研究遵循 COREQ/SRQR，须说明编码流程与信度",
    },
    conventions=(
        "诊断用 ICD-11 或 DSM-5-TR 并标注版本，年龄等效值随测",
        "伦理批准号与知情同意（监护人+学生双签）须显式声明",
        "被试个人信息去标识化，用化名与字母编号",
        "干预效果报效应量（Cohen's d / SMD）与 95% CI",
        "量表给出信度（Cronbach's α/ICC）与常模来源",
    ),
    key_venues=(
        "Exceptional Children",
        "Journal of Special Education",
        "Remedial and Special Education",
        "Journal of Applied Research in Intellectual Disabilities",
        "Education and Training in Autism and Developmental Disabilities",
    ),
    units_and_formulas_notes=(
        "智力测验以 IQ ± SD 报告（WAIS-IV / WISC-V，SD = 15）",
        "适应行为用 Vineland-II 分量表原始分与百分位",
        "单被试分析报 PND（百分比非重叠数据）与 CUSUM",
        "教育测量以年级当量 GE 与百分等级 PR 分列，不得混用",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "NVivo", "ATLAS.ti", "MaxQDA", "Tobii Pro 眼动追踪", "Pupil Labs 眼动追踪", "EyeLink 1500", "EEG (g.tec)", "ActiGraph 加速度计", "Kinect v2 动作捕捉", "Tableau", "PowerPoint", "Google Forms", "Qualtrics", "EndNote", "Mendeley", "Zotero", "Microsoft Excel"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
