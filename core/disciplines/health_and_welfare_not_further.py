"""卫生与福利（未进一步定义）学科论文支持：跨领域卫生服务与社会福利整合研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="health_and_welfare_not_further",
    aliases=("health_and_welfare_not_further", "卫生与福利（未进一步定义）", "社会卫生", "健康与福利", "社会福利", "医疗卫生", "卫生福利服务"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论与启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（服务整合分析）", "results（效果评价）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "RCT 遵循 CONSORT", "k2": "观察性研究遵循 STROBE", "k3": "系统综述遵循 PRISMA"},
    conventions=("福利服务分类须注明 ISCED 2011 编码", "卫生服务等级须标注（基层/二级/三级）", "服务对象年龄与性别须注明", "服务可及性须注明地理与经济维度", "统计口径须注明来源与年份"),
    key_venues=("Health and Social Care in Development", "Journal of Social and Personal Relationships", "International Journal of Health and Social Care", "医学与社会", "中国卫生事业管理"),
    units_and_formulas_notes=("服务覆盖率：%（实际/目标×100%）", "服务响应时间：h 或 min", "服务满意度：1-5 分制", "人口覆盖率：%（实际服务/目标人口）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("社会服务信息化管理平台", "健康风险评估工具", "社会需求调查系统", "服务整合评价指标体系", "SPSS", "Stata", "SAS", "R（社会科学统计）", "问卷星（在线调查）", "问卷系统（SurveyMonkey）", "社会服务数据分析工具", "社会需求图谱绘制系统", "社区健康服务管理系统", "公共卫生信息系统", "社会福利档案管理系统", "社区服务满意度测评系统", "社会服务标准化评估工具", "社会服务绩效评价指标系统", "社会服务资源分配模型", "社区卫生服务绩效仪表盘"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
