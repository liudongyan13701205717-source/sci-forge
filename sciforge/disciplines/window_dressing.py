"""橱窗陈列学科论文支持：视觉营销、橱窗美学设计与消费者吸引力研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="window_dressing",
    aliases=(
        "window dressing",
        "橱窗陈列",
        "视觉营销",
        "陈列设计",
        "visual merchandising",
        "display design",
        "橱窗设计",
        "视觉陈列",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "literature review（视觉营销理论综述）",
            "data and methods（实验设计/调查方法）",
            "findings（消费者反应与效果发现）",
            "discussion（设计原则与管理启示）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "store description（店铺背景描述）",
            "window design concept（设计构思与理念）",
            "implementation process（实施过程记录）",
            "performance evaluation（效果评估与数据分析）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "visual merchandising evolution（视觉陈列演变）",
            "color and light design（色彩与灯光设计综述）",
            "consumer behavior（消费者行为综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "design documentation": "设计方案须包含草图、效果图、材料清单与实施照片",
        "consumer testing": "消费者吸引力测试须报告样本量、测试方法（眼动/问卷/停留时间）",
        "performance metrics": "陈列效果须采用标准化指标（进店率、转化率、坪效）",
        "brand consistency": "设计须说明品牌视觉识别系统（VI）遵循情况",
    },
    conventions=(
        "色彩描述区分 Pantone 色号与 CMYK/RGB 值",
        "灯光设计标注色温（K）、显色指数（CRI）与照度（lux）",
        "橱窗面积单位 ㎡；高度单位 m",
        "消费者停留时间单位 秒或分钟",
        "陈列周期标注（如按季度/月度/周更新）",
    ),
    key_venues=(
        "Journal of Retailing",
        "Journal of Business Research",
        "International Journal of Retail & Distribution Management",
        "Fashion Theory",
        "Show & Tell: Visual Merchandising Magazine",
    ),
    units_and_formulas_notes=(
        "进店率 = 进店人数 / 路过人数×100%",
        "转化率 = 成交笔数 / 进店人数×100%",
        "坪效 = 销售额 / 店铺面积（元/㎡·月）",
        "照度单位 lux；色温单位 K（暖光 2700-3000K，中性 4000K，冷光 5000-6500K）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Photoshop 视觉效果图设计", "CorelDRAW 矢量设计软件", "SketchUp 3D 建模软件", "3ds Max 渲染与建模", "V-Ray 渲染器", "Adobe Illustrator 插画设计", "Procreate 手绘设计（iPad）", "Cinema 4D 三维动画", "Blender 开源 3D 软件", "眼动追踪设备（如 Tobii Pro）", "视频行为分析系统（如 Noldus Observer）", "消费者问卷平台（如问卷星/Qualtrics）", "Google Analytics 流量分析", "POS 销售数据系统", "Lighting Design 软件（DIALux evo）", "色彩管理系统（X-Rite ColorChecker）", "LaTeX 学术排版", "EndNote 文献管理", "Pinterest 灵感收集平台", "VosViewer 文献计量可视化"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
