"""职业安全学科论文支持：职业安全/伤害流行病学体裁、APA 引用样式与安全指标记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="job_safety",
    aliases=("job_safety", "职业安全", "劳动安全", "职业安全与卫生", "job safety", "occupational safety", "workplace safety", "safety at work"),
    paper_types={
        "research": ("abstract", "introduction（安全背景与问题）", "methodology（事故调查与测量方法）", "results（指标与统计）", "discussion（干预与对策）", "references"),
        "case_study": ("abstract", "introduction", "case description（事故案例）", "analysis（根因分析）", "results（整改效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（安全理论）", "evidence synthesis（证据综述）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Safety Science 遵循 APA 规范）",
    reporting_standards={"accident": "事故研究遵循事故报告规范（STROP）", "intervention": "干预研究遵循 CONSORT 声明", "systematic_review": "系统综述遵循 PRISMA 声明"},
    conventions=("事故率指标（LTIR、TRIR）须定义与基数", "暴露时间与工人数须报告", "风险等级与评分标准须说明", "干预前后对照须标注混杂因素", "数据匿名与合规须声明"),
    key_venues=("Safety Science", "Journal of Safety Research", "Applied Ergonomics", "Safety and Health", "Accident Analysis & Prevention"),
    units_and_formulas_notes=("事故率用每百万工时（per MLE）", "LTIR = 损失工时事故数 / 总工时 × 10⁶", "暴露限值用 TWA 与 STEL（mg/m³）", "时延与随访期须明确"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("STAMP/STARA（事故建模）", "HAZOP 分析工具", "FMEA 工具", "风险矩阵（Risk Matrix）", "SPSS（统计）", "R（生存分析）", "ArcGIS（地理风险）", "QRA 定量风险软件", "热成像仪（隐患检测）", "噪声计（Sound Level Meter）", "光照度计", "测厚仪（腐蚀）", "安全帽冲击测试仪", "便携式气体检测仪", "OSHA 29 CFR 法规库", "NIST 标准库", "ANSI Z490 个人护具", "ISO 45001 审核工具", "Minitab（SPC）", "职业接触限值评估软件"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "LAP（事故数据库）"),
)
