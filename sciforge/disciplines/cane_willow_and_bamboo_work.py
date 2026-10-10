"""Cane, willow and bamboo work 学科论文支持：藤柳竹工艺体裁、手工艺研究标准与工具注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cane_willow_and_bamboo_work",
    aliases=("cane willow and bamboo work", "藤柳竹工艺", "藤艺", "竹编",
             "柳编", "rattan weaving", "willow work", "bamboo craft"),
    paper_types={
        "research": (
            "abstract",
            "introduction（工艺背景与研究问题）",
            "方法（材料、技法与制作流程）",
            "结果（成品与工艺分析）",
            "讨论（工艺传承与改进）",
            "references",
        ),
        "report": (
            "abstract",
            "项目概述",
            "制作执行（选材、技法、工序）",
            "成品评析",
            "经验总结",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；文献以中文为主，作品按手工艺惯例标注）",
    reporting_standards={
        "case_study": "个案须说明材料来源、规格与制作工艺全过程",
        "technique_doc": "技法记录须可复现，给出工序与参数",
        "heritage_doc": "非遗/传承研究须注明资料来源与传承人信息",
    },
    conventions=(
        "材料名称（藤/柳/竹的种类与规格）须准确，首现给出全称",
        "技法术语（编织、弯制、削切等）须与手工艺界通用一致",
        "成品照片须标注工序阶段，可复核",
        "尺寸/规格用统一单位（cm/mm）",
    ),
    key_venues=(
        "装饰",
        "美苑",
        "美术观察",
        "中国美术研究",
        "Furniture History",
        "Journal of Craft",
        "手工业杂志",
    ),
    units_and_formulas_notes=(
        "尺寸/直径用 mm/cm，须注明",
        "材料来源与地域须标注",
        "工序编号须连续，便于复现",
        "成品照片须含比例尺参照",
        "引用技法须注明来源",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("编织刀", "削刀", "弯藤机", "蒸煮设备", "竹篾刀", "篾工工具", "编织模具", "激光切割机", "3D 建模软件", "CAD 软件", "Photoshop", "Blender", "AutoCAD", "SolidWorks", "数码相", "摄影灯", "手工工具", "打磨机", "抛光机", "喷枪"),
    category="艺术学",
    databases=("CNKI", "OpenAlex"),
)
