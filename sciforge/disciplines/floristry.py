"""插花与花艺设计学科论文支持：花艺设计原理、美学评价与市场应用研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="floristry",
    aliases=("floristry", "花艺设计", "插花艺术", "花艺", "花卉设计", "花束设计", "婚礼花艺", "花店经营"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "ISO 507 切花分类标准", "k2": "AIFD 花艺设计评价准则", "k3": "GB/T 30889 花艺产品标准"},
    conventions=("花材品种须标注学名与俗名", "插花作品尺寸须给出三维参数", "作品保存时间须注明环境条件", "美学评分须注明评分人数与量表", "色彩参数须给出 CIELAB 色度坐标"),
    key_venues=("Horticulture Journal", "Acta Horticulturae", "Journal of Horticultural Science", "Gartenbauwissenschaft", "Floral Design Research"),
    units_and_formulas_notes=("花色须标注 L 值（明度）/ a 值 / b 值（CIELAB）", "花茎长度单位：cm", "作品重量：g", "保鲜液浓度：%（v/v）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("色差仪 (Minolta CM-3600)", "手持色度计", "多光谱相机", "植物组织水势仪 (Scholander)", "切花保鲜液配制设备", "恒温恒湿试验箱", "气相色谱仪 (GC)", "GC-MS（香气分析）", "电子鼻 (E-Nose)", "3D 扫描器 (photogrammetry)", "Adobe Illustrator（作品制图）", "Lightroom（摄影修图）", "SPSS（美学统计）", "Origin", "NVivo（质性分析）", "RStudio", "Plant Stress Analyzer", "手持光谱仪 (Ocean Puck)", "时间序列记录仪", "ImageJ"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
