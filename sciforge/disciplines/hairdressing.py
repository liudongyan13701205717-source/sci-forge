"""美发学科论文支持：染发机理、烫发化学、发型设计与人发生物学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hairdressing",
    aliases=("hairdressing", "美发", "发型设计", "染发", "烫发", "美发技术", "发型研究"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（材料与实验设计）", "results（实验结果）", "discussion（讨论与机理）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（技术分析）", "results（效果评价）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "RCT 遵循 CONSORT", "k2": "观察性研究遵循 STROBE", "k3": "系统综述遵循 PRISMA"},
    conventions=("染膏成分须注明 INCI 名称", "烫发剂 pH 值与浓度须标注", "毛发类型须注明 Andreasen 分级", "实验周期须注明温度与湿度条件", "色号须标注系统（如 Wella/Beautylab）"),
    key_venues=("Journal of Cosmetic Science", "International Journal of Cosmetic Science", "Cosmetics", "Journal of Cosmetic Dermatology", "Dermatology"),
    units_and_formulas_notes=("过氧化氢浓度：% w/w", "烫发剂 pH 值：无量纲", "毛发直径：μm", "颜色 ΔE 值：CIE 色度单位"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("头皮检测仪", "毛发拉拔仪（Tensile Tester）", "发色分光光度计", "pH 试纸与 pH 计", "电子天平（分析天平）", "恒温水浴锅", "比色卡（Gretag Macbeth）", "发丝显微成像系统", "染发剂氧化还原电位仪", "毛发含水量仪（水分测定仪）", "毛发脆化测试机", "烫发剂浓度检测仪", "紫外线老化箱", "毛发弹性测试机", "发型设计 3D 建模软件", "虚拟发型试戴系统", "染发剂成分分析软件", "毛发健康评级量表", "烫发工艺参数记录系统", "SPSS"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
