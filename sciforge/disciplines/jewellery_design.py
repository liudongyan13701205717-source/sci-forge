"""珠宝设计学科论文支持：珠宝设计/金属工艺/美学研究体裁、APA 引用样式与金工参数记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="jewellery_design",
    aliases=("jewellery_design", "珠宝设计", "首饰设计", "首饰造型", "珠宝造型设计", "珠宝与首饰设计", "jewellery design", "jewelry design"),
    paper_types={
        "research": ("abstract", "introduction（设计背景与问题）", "methodology（设计方法与流程）", "results（作品与参数）", "discussion（美学与工艺评析）", "references"),
        "case_study": ("abstract", "introduction", "case description（作品案例）", "analysis（设计语言分析）", "results（工艺与效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（设计理论）", "evidence synthesis（作品与文献综述）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Journal of Jewellery 与 Craft Research 遵循 APA 规范）",
    reporting_standards={"design": "设计研究遵循 ASDC 设计研究规范", "material": "材料性能测试遵循 ASTM 金工测试标准", "review": "设计评论遵循批判性设计评审规范"},
    conventions=("设计参数（尺寸、克重、金属种类）须标注", "材料成分（K 金比例、宝石 4C）须明确", "工艺路线（铸造、镶嵌、表面处理）须说明", "作品摄影（角度、光线、白平衡）须统一", "原创性与授权来源须声明"),
    key_venues=("Journal of Jewellery", "Craft Research", "Jewellery Design Review", "International Journal of Design", "Gemmology International"),
    units_and_formulas_notes=("金属纯度用千分比（如 750/1000）", "宝石重量用克拉（ct）", "硬度用莫氏硬度或维氏硬度（HV）", "尺寸用 mm、克重用 mg/g"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Rhino（珠宝 CAD 建模）", "Matrix Gold（珠宝建模）", "JewelCAD（渲染）", "ZBrush（数字雕刻）", "CastingMaster（铸造模拟）", "3D 打印树脂机", "失蜡铸造设备", "激光焊接机", "钻石显微镜", "宝石折射仪", "双折射仪", "紫外荧光仪", "光谱仪（能量色散 XRF）", "金工锉刀工具组", "镶爪工具", "研磨抛光机", "电镀设备", "热成像显微镜", "色彩分析仪（HunterLab）", "Adobe Illustrator（设计图纸）"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
