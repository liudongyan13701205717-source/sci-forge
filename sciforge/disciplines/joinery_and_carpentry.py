"""木工与建筑细木工学科论文支持：木工/材料/结构体裁、APA 引用样式与木材物性记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="joinery_and_carpentry",
    aliases=("joinery_and_carpentry", "木工", "建筑细木工", "木结构", "joinery and carpentry", "woodworking", "carpentry", "timber framing"),
    paper_types={
        "research": ("abstract", "introduction（材料背景与问题）", "methodology（试验设计与方法）", "results（力学与尺寸数据）", "discussion（结构与设计评析）", "references"),
        "case_study": ("abstract", "introduction", "case description（木构件案例）", "analysis（构造与工艺分析）", "results（性能与效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（木材科学）", "evidence synthesis（材料与结构综述）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Wood Science and Technology 遵循 APA 规范）",
    reporting_standards={"material": "木材力学性能测试遵循 EN 338 标准", "fire": "防火性能测试遵循 EN 13501 标准", "systematic_review": "系统综述遵循 PRISMA 声明"},
    conventions=("木材树种、含水率与密度须报告", "力学指标（抗弯、抗压、E）须注明试验条件", "连接节点（榫卯、钉、胶合）须说明", "构件尺寸与公差须量化", "干燥处理与防腐处理须交代"),
    key_venues=("Wood Science and Technology", "Construction and Building Materials", "Wood Fiber Science", "Journal of Wood Chemistry and Technology", "Engineering Structures"),
    units_and_formulas_notes=("应力用 MPa；弹性模量用 GPa", "含水率用 %（与标准温度对比）", "密度用 kg/m³", "含水率梯度与干燥速率须明确"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("木材含水率测定仪", "木材密度计", "万能试验机（Tinius Olsen）", "木材硬度计（Janka）", "木材干燥窑", "木材防腐处理设备", "木工机械（电锯、刨床、砂带机）", "激光切割机", "CNC 数控机床", "卡尺与千分尺", "木材成分分析仪（热重分析仪）", "红外光谱仪（FTIR）", "木材显微结构显微镜", "木材防腐压力处理罐", "木材阻燃剂处理设备", "木材胶粘剂测试设备", "木材力学性能测试软件", "木材质量分级标准库", "木材加工仿真软件", "木材行业规范与标准库"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
