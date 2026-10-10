"""金工工艺学科论文支持：金属首饰制作/工艺与材料研究体裁、APA 引用样式与金工参数记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="jewellery_making",
    aliases=("jewellery_making", "金工工艺", "首饰制作", "金属工艺", "jewellery making", "jewelry making", "metal craft", "fine metalsmithing"),
    paper_types={
        "research": ("abstract", "introduction（工艺背景与问题）", "methodology（制作方法与参数）", "results（成品与测量）", "discussion（工艺评析）", "references"),
        "case_study": ("abstract", "introduction", "case description（制件案例）", "analysis（工艺路径分析）", "results（成品性能）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（工艺理论）", "evidence synthesis（工艺与材料综述）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Craft Research 与 Metals Technology 遵循 APA 规范）",
    reporting_standards={"material": "材料性能测试遵循 ASTM 金工测试标准", "process": "工艺流程记录遵循可复现工艺记录规范", "review": "工艺评述遵循批判性工艺评审规范"},
    conventions=("材料牌号与纯度须标注（如 S925、K14）", "工艺参数（炉温、时间、锤击次数）须量化", "焊接保护气体与气氛须说明", "成品尺寸与克重须报告", "工具与设备型号须注明"),
    key_venues=("Craft Research", "Metals Technology", "Jewellery Design Review", "International Journal of Design", "Annals of the Faculty of Fine Arts"),
    units_and_formulas_notes=("金属纯度用千分比", "炉温用 ℃（标注热电偶位置）", "克重用 g/mg（精确到 0.01 g）", "硬度用 HV 或 HRB"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("火焰喷枪（氧-乙炔）", "金工锤子", "焊接工具组", "激光焊接机", "研磨机", "抛光机", "失蜡铸造炉", "电铸设备", "台钳与夹具", "锉刀组", "线锯（弓锯）", "千分尺（0.01 mm）", "天平（0.001 g）", "硬度计（维氏）", "金相显微镜", "XRF 光谱仪", "pH 试纸（酸洗）", "退火炉（箱式）", "电铸直流电源", "Adobe Illustrator（图纸）"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
