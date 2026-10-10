"""质量管理学科论文支持：全面质量管理、精益生产与质量改善方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="quality_management",
    aliases=("quality_management", "质量管理", "quality management", "QM", "TQM", "total quality management", "全面质量管理", "精益质量管理", "quality improvement"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "ISO 9001:2015 质量体系审核要求", "k2": "ISO 9004 质量管理指南", "k3": "六西格玛绿带/黑带方法学要求"},
    conventions=("结构化采用 PDCA 或 DMAIC 循环", "案例描述须含背景、方法、结果与反思", "统计显著性注明检验方法与 P 值", "工具与参数在方法部分明确列出", "结论须给出可执行的持续改善项"),
    key_venues=("Total Quality Management & Excellence", "International Journal of Quality and Reliability Management", "Quality Management Journal", "Journal of Industrial Technology", "Journal of Operations Management"),
    units_and_formulas_notes=("过程能力指数 Cp、Cpk 需区分单侧双侧", "缺陷率以 DPPM 或 PPM 表示", "测量不确定度按 GUM 框架报告", "样本量按六西格玛置信水平设定"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Minitab", "SigmaXL", "JMP Statistical Discovery", "QI Macros for Excel", "ISO 9001 Management System", "ISO 9004 Quality Management", "Six Sigma DMAIC Software", "MasterControl QMS", "SAP Quality Management", "Veeva Vault Quality", "Qualio QMS", "Qualtrics Survey", "Microsoft Visio Process Map", "Ishikawa Fishbone Diagram", "5 Why Root Cause Tool", "Lean Kaizen Board", "Python Pandas", "R quality Package", "SPC for Six Sigma", "ASQ Six Sigma Certification Platform"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
