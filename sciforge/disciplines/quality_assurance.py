"""质量保证学科论文支持：质量管控体系、六西格玛与质量管理工具。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="quality_assurance",
    aliases=("quality_assurance", "质量保证", "quality assurance", "QA", "quality control", "QC", "质量管控", "质量检验", "quality inspection"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "ISO 9001 质量管理体系符合性", "k2": "六西格玛 DMAIC 阶段报告", "k3": "IATF 16949 汽车行业质量要求"},
    conventions=("采用 DMAIC 结构化报告", "数据可视化使用控制图与 Pareto 图", "统计方法注明分布假设", "工具与参数在方法部分明确列出", "结论须给出可执行改进项"),
    key_venues=("Journal of Quality in Regulated Health Care", "Total Quality Management & Excellence", "International Journal of Quality and Reliability Management", "Journal of Industrial Technology", "Quality Engineering"),
    units_and_formulas_notes=("缺陷率以 DPPM 或 PPM 表示", "过程能力指数 Cp、Cpk 需区分单侧双侧", "测量不确定度按 GUM 框架报告", "样本量按六西格玛置信水平设定"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Minitab", "SigmaXL", "JMP Statistical Discovery", "QI Macros for Excel", "ASQ Six Sigma Tools", "ISO 9001 Compliance Software", "Gage R&R Analyzer (MSA)", "Process Capability Calculator", "SPC Plus for Six Sigma", "MasterControl QMS", "SAP Quality Management", "Veeva Vault Quality", "Qualio QMS", "Qualtrics Survey Tool", "Python SciPy", "Python Statsmodels", "R qcc Package", "Root Cause Analysis (Fishbone)", "Lean Six Sigma Toolbox", "ISO/IEC 17025 Laboratory Management"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
