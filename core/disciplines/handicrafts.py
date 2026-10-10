"""手工艺学科论文支持：传统工艺技法、材料工艺与文化遗产保护研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="handicrafts",
    aliases=("handicrafts", "手工艺", "民间工艺", "传统工艺", "手工技艺", "工艺设计", "工艺美术"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（工艺方法与实验）", "results（工艺效果）", "discussion（讨论与传承意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（工艺分析）", "results（效果评价）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "工艺实验遵循 CONSORT", "k2": "田野调查遵循 STROBE", "k3": "系统综述遵循 PRISMA"},
    conventions=("工艺材料须注明产地与处理工序", "工具型号与规格须标注", "工艺参数（温度/时间/压力）须量化记录", "传统技法名称须注明地域流派", "成品须注明尺寸与材料成分"),
    key_venues=("Journal of Craft Research", "Craft", "Archives of Material Science", "Journal of Traditional Engineering", "非物质文化遗产研究"),
    units_and_formulas_notes=("纤维直径：μm", "烧结温度：°C", "压力：MPa", "材料密度：g/cm³"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("3D 扫描仪（三维重建）", "电子显微镜（SEM）", "X 射线衍射仪（XRD）", "拉曼光谱仪", "傅里叶变换红外光谱仪（FTIR）", "热分析仪（DSC/TGA）", "万能材料试验机", "纤维光学显微镜", "3D 打印快速成型机", "数控雕刻机（CNC）", "激光切割机", "陶瓷拉坯机", "织布机（传统/数控）", "金属锻造设备", "手工工具数字化记录系统", "工艺影像采集设备", "材料成分分析仪", "纤维拉伸强度测试仪", "工艺传承数字孪生平台", "SPSS"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
