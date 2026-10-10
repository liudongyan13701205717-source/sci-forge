"""皮毛加工学科论文支持：皮革加工/毛皮工艺体裁、纺织与化工引用样式与工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pelt_worker",
    aliases=("pelt worker", "皮毛加工", "皮张加工", "pelt processing", "皮张处理", "毛皮加工", "fur processing", "制革", "皮革工程"),
    paper_types={
        "research": ("abstract", "introduction（加工问题与工艺目标）", "methodology（工艺路线与参数）", "results（质量/物理性能）", "discussion（机理与产业化）", "references"),
        "case_study": ("abstract", "introduction", "case description（原料皮与生产情境）", "analysis（工艺变量与结果）", "results（成品特性）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（皮革/毛皮材料理论）", "evidence synthesis（工艺综述）", "future directions", "references"),
    },
    citation_style="Vancouver/纺织化工样式（皮革工程领域常用；工艺标准按 GB/ISO 编号引用）",
    reporting_standards={"tanning": "鞣制工艺须报告鞣剂种类、用量、时间与温度", "dyeing": "染色工艺须报告染料种类、染料上染率与废水 COD", "testing": "物理性能测试遵循 ISO 或 GB（抗张强度、撕裂强度、渗透性）", "environmental": "环保合规（废水 COD、BOD、重金属）须报告", "sampling": "抽样方案与试验次数须明确"},
    conventions=("皮种命名用拉丁学名或商品名（如水貂/貂皮、羊皮、牛皮）", "鞣剂与染料名称按成分与标准编号标注", "温度用 °C；时间用 h/min；浓度用 g/L 或 %", "物理性能单位遵循 ISO/GB（N/mm²、mm、%）", "工艺流程图按标准图示绘制"),
    key_venues=("Leather Technology", "Journal of the Leather Science and Technology", "JLTST 材料工艺", "Polymer Degradation and Stability", "中国皮革", "J. Ind. Textile Res."),
    units_and_formulas_notes=("温度用 °C；时间用 h/min；浓度用 g/L", "抗张强度用 N/mm² 或 kPa", "渗透性/透气性按 ISO 单位", "废水指标（COD/BOD/氨氮）用 mg/L"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("脱毛滚筒", "鞣制转鼓", "染色机", "烘干设备", "加脂机", "剖层机", "削匀机", "抗张强度试验机", "撕裂强度试验机", "渗水透气性仪", "色差仪（Colorimeter）", "扫描电子显微镜（SEM）", "红外光谱仪（FTIR）", "X 射线衍射（XRD）", "SPSS 统计分析", "R 统计分析", "Python (Pandas)", "OriginPro 绘图", "Minitab 实验设计", "JMP 统计分析"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
