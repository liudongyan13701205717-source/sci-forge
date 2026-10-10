"""玻璃生产学科论文支持：玻璃熔制/成型体裁、AGU/材料学引用样式与玻璃工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="glass_production",
    aliases=("glass production", "玻璃生产", "玻璃制造", "玻璃熔制", "玻璃成型", "玻璃加工", "玻璃工艺"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（熔制与工艺）", "results（成分与性能）", "discussion（机理与工艺意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（生产线描述）", "analysis（工艺分析）", "results（性能结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（玻璃化学与结构）", "evidence synthesis（工艺综述）", "future directions", "references"),
    },
    citation_style="IUPAP/材料学作者-年份样式（玻璃生产与材料学通用）",
    reporting_standards={"k1": "熔制实验须记录配方/温度/时间", "k2": "性能测试遵循 ISO 7027", "k3": "产品规格须交代尺寸与标准"},
    conventions=("玻璃配方成分须列明（%wt）", "熔制温度制度须报告", "成型方法须定义", "缺陷须说明", "工艺参数须可复现"),
    key_venues=("Glass Technology", "Journal of Non-Crystalline Solids", "Ceramics International", "Materials Research Bulletin", "Glass Physics and Chemistry"),
    units_and_formulas_notes=("配方以 %wt 表示，温度用 °C", "公式用 amsmath，粘度须明确", "密度/热膨胀给单位", "强度给 MPa 与测试方法"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("池式炉（tanks）", "电熔炉", "锡液法（float glass）", "拉丝炉（drawn glass）", "压延机（rolled glass）", "退火炉（lehr）", "XRF 成分分析", "热膨胀仪（dilatometer）", "示差扫描量热仪（DSC）", "粘度计（viscometer）", "流变仪（rheometer）", "硬度计（Vickers）", "密度计（pycnometer）", "熔制记录系统（MES）", "玻璃成分软件（Glassworks）", "熔制动力学模拟（CFD/Fluent）", "在线质量监测（光学）", "玻璃 3D 打印（激光烧结）", "热成像监控（红外）", "热膨胀曲线分析系统"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "熔制数据库（GlassBase）"),
)
