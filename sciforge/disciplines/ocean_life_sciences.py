"""海洋生命学科论文支持：海洋生物/生态体裁、AGU 样式与海洋生物记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ocean_life_sciences",
    aliases=("ocean_life_sciences", "海洋生命学", "海洋生物学", "海洋生态", "marine biology", "maritime sciences"),
    paper_types={
        "research": ("abstract", "introduction（背景与生态问题）", "methodology（采样与方法）", "results（群落与动态）", "discussion（生态与机理）", "references"),
        "case_study": ("abstract", "introduction", "case description（生态事件）", "analysis（成因分析）", "results（后果与修复）", "discussion（教训与对策）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="AGU/Journal of Geophysical Research 样式",
    reporting_standards={"observational": "遵循观测数据报告规范", "systematic_review": "遵循 PRISMA 声明", "case_report": "遵循 CARE 指南"},
    conventions=("物种命名须用学名（斜体）", "采样位置须给出经纬度与深度", "样本量须报告", "统计分析须注明方法", "单位须一致（SI）"),
    key_venues=("Deep-Sea Research Part II", "Limnology and Oceanography", "Marine Ecology Progress Series", "Journal of Plankton Research", "ICES Journal of Marine Science"),
    units_and_formulas_notes=("盐度用 PSU", "温度用 °C", "叶绿素用 µg/L", "叶绿素荧光用 µg chl-a/m³", "公式用 amsmath"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("CTD 剖面仪", "YSI 多参数水质仪", "荧光分光光度计", "叶绿素荧光仪", "浮游生物网具", "Niskin 瓶", "BGC-Argo 浮标", "海洋滑翔机", "水下摄像头 ROV", "DNA barcoding 测序仪", "QIIME 2", "Mothur", "Bio-Rad CFX", "Illumina NovaSeq", "R", "Python", "MATLAB", "ImageJ", "PRIMER+", "Cytoscape"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
