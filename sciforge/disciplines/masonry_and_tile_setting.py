"""砌筑与瓷砖铺设学科论文支持：砌体结构、砖石工艺、铺装与质量检验体裁、建工规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="masonry_and_tile_setting",
    aliases=("masonry_and_tile_setting", "砌筑与瓷砖铺设", "砌筑工程", "砌石工程", "砖石工程",
             "Masonry", "Tile Setting", "Brickwork", "砌体工程", "瓦工工程"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与工程问题）",
            "methodology（材料、工艺与试验方法）",
            "results（强度、变形与耐久结果）",
            "discussion（工程启示与适用边界）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工程/墙面描述）",
            "analysis（工艺瓶颈与改进）",
            "results（前后对比与验收）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（砌体材料与工艺综述）",
            "evidence synthesis（现场与试验证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="BibTeX 样式（工程编号制）",
    reporting_standards={
        "materials": "材料性能须遵循 GB/T 1196（烧结普通砖）与 GB/T 1194（砌筑砂浆）",
        "wall_quality": "墙体质量须遵循 GB 50203《砌体结构工程施工质量验收规范》",
        "tile_quality": "瓷砖铺设须遵循 GB 50327《建筑装饰装修工程质量验收标准》",
        "structural": "砌体结构须遵循 GB 50003《砌体结构设计规范》",
        "environmental": "施工环保须遵循所在国/地区建筑环保规范",
    },
    conventions=(
        "采用 SI 单位，长度单位：mm 或 m",
        "砂浆强度单位：MPa；稠度单位：mm",
        "墙面垂直度、平整度、灰缝厚度须遵循 GB 50203 允许偏差",
        "瓷砖空鼓率须按 GB 50327 报告（≤5% 且单片≤15%）",
        "试验样品须注明龄期（7d/28d）与养护条件",
    ),
    key_venues=(
        "Construction and Building Materials",
        "Materials and Structures",
        "International Journal of Masonry Structures and Monuments",
        "Building and Environment",
        "Journal of Building Engineering",
        "中国土木工程学报",
    ),
    units_and_formulas_notes=(
        "砌体抗压强度单位：MPa；砂浆稠度单位：mm",
        "砖块吸水率单位：%",
        "灰缝厚度：水平 8-12 mm、竖直 10-15 mm",
        "垂直度允许偏差：每层 ≤5 mm；全高 ≤10 mm",
        "砂浆强度 f_m = α₁ f_b β + α₂ f_s（砌体抗压强度公式）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("压力试验机（Instron）", "万能试验机（MTS）", "砂浆稠度仪", "抗折试验机", "游标卡尺/电子测距仪", "靠尺与塞尺（平整度检测）", "激光测距仪", "水准仪（Leica）", "全站仪", "空鼓锤", "温湿度计（环境与试件）", "养护箱与温湿度记录（温湿度记录仪）", "混凝土/砂浆搅拌机", "瓷砖切割机（Makita）", "砌筑与铺砖工具（抹刀/角尺）", "脚手架（施工与安全）", "施工安全装备（头盔/护目镜）", "施工管理软件（AutoCAD/BIM）", "BIM 模型（Revit）", "工程图像记录（相机/无人机）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
