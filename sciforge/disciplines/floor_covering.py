"""地面铺装学科论文支持：地面材料与铺装工艺研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="floor_covering",
    aliases=("floor_covering", "地面铺装", "地面覆盖", "地板铺装", "地毯铺装", "地板工程", "地面装饰", "地板材料"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "ASTM F321 地面材料测试标准", "k2": "ISO 10580 弹性地板标准", "k3": "GB/T 11988 地面材料中国标准"},
    conventions=("铺装磨损率、耐磨转数（Taber）、抗滑系数（COF）等指标须给出测量条件", "材料成分与厚度须标注计量单位", "样品尺寸须注明（如 500 mm × 500 mm）", "寿命预测须给出统计方法", "对比试验须注明对照组条件"),
    key_venues=("Building and Environment", "Construction and Building Materials", "Materials & Design", "Journal of Materials in Civil Engineering", "Polymers"),
    units_and_formulas_notes=("硬度单位：邵氏 A/D 度", "耐磨转数：Taber 转数（500 g 载荷）", "抗滑系数 COF（BPN 值）", "厚度单位：mm，面积单位：m²"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Taber 磨耗测试仪", "COF 抗滑系数测试仪", "邵氏硬度计", "Universal Testing Machine (UTM)", "X射线衍射仪 (XRD)", "扫描电子显微镜 (SEM)", "傅里叶变换红外光谱 (FTIR)", "色差仪 (Colorimeter)", "VOC 气体分析仪", "加速老化试验机", "盐雾腐蚀试验箱", "耐磨纸板 (Taber Abrader)", "表面电阻测试仪", "热导率仪", "声级计 (Sound Level Meter)", "ANSYS（结构仿真）", "Origin（数据绘图）", "SPSS（统计检验）", "ImageJ（图像分析）", "R（统计建模）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
