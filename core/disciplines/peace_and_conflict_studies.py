"""和平与冲突研究学科论文支持：社会科学/国际关系体裁、APA 引用样式与冲突分析记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="peace_and_conflict_studies",
    aliases=("peace and conflict studies", "和平与冲突研究", "和平冲突研究", "和平学", "conflict studies", "国际关系", "国际政治", "国际安全", "冲突学"),
    paper_types={
        "research": ("abstract", "introduction（冲突背景与研究问题）", "methodology（数据/案例/分析框架）", "results（冲突演化与影响）", "discussion（和平建构启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（冲突当事方与时间线）", "analysis（动因、动力学与和谈）", "results（事件结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（和平学理论流派）", "evidence synthesis（干预与结果证据）", "future directions", "references"),
    },
    citation_style="APA 样式（国际关系/和平学主流；报告与政策文件按官方文号引用）",
    reporting_standards={"casemethod": "案例研究须遵循 Yin/Seale 案例研究规范", "data": "冲突事件数据（UCDP/ACLED/Warpeace）须注明来源与编码规则", "ethics": "田野研究伦理审查与受访者知情同意须声明", "statistical": "定量分析须报告统计假设、稳健性与效应量", "geospatial": "地理编码须报告精度与坐标系统"},
    conventions=("冲突当事方按国际惯例（UN/UNHRC）命名", "时间线使用 ISO 8601；地域冲突命名遵循联合国或国际主流", "术语（结构性暴力、直接暴力、建设和平）首次出现给出定义", "引用政府/NGO 报告注明日期与版本", "涉及敏感群体时须脱敏与匿名处理"),
    key_venues=("International Studies Quarterly", "International Studies Review", "Peace & Change", "Journal of Peace Research", "Conflict, Security & Development", "Global Society"),
    units_and_formulas_notes=("冲突强度按 UCDP 或 PRIO 分级定义须明确", "伤亡数据按来源与口径注明来源（Killed/Injured）", "地理坐标用经纬度（WGS84）与投影方法", "统计效应量用 Cohen's d/OR 与 95% CI"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("UCDP/PRIO 数据集", "Uppsala 冲突数据", "NATIS 难民数据", "GeoBound 地理编码", "Gephi 网络分析", "NodeXL 网络分析", "ArcGIS 地理信息系统", "QGIS 地理信息系统", "NVivo 质性分析", "Atlas.ti 质性分析", "Lexicoder 主题编码", "Dedoose 质性分析", "SPSS 统计分析", "R (crayon, sf) 统计", "Stata 统计分析", "JANUS 文本分析", "Google Earth Pro", "World Bank Data API", "GeoPandas（地理空间分析）", "Humanitarian Data Exchange（人道主义数据平台）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACLED 冲突事件数据库", "Warpeace 数据库"),
)
