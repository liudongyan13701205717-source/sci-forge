"""纺织、服装与鞋类设计与材料学科论文支持：纺织产品设计、材料创新与可持续性研究体裁、MLA 引用样式与工艺注释注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="textiles_clothing_and_footwear",
    aliases=(
        "textiles_clothing_and_footwear",
        "Textiles, clothing and footwear",
        "纺织服装与鞋类设计",
        "纺织品设计",
        "服装与鞋类",
        "Textile and apparel design",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（设计背景与研究问题）",
            "methodology（设计方法、材料选择与制作流程）",
            "results（作品、样品与测试数据）",
            "discussion（设计意图与效果分析）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（作品与项目案例）",
            "analysis（设计与工艺分析）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="MLA 样式（艺术与设计领域常见）",
    reporting_standards={
        "design_process": "设计过程须记录（灵感来源、草图迭代、材料试验）",
        "material_testing": "材料性能测试须遵循标准并注明仪器",
        "user_evaluation": "用户评价须说明样本、方法与量表",
        "sustainability": "可持续性主张须有数据支持（生命周期评估或环保认证）",
    },
    conventions=(
        "作品图片须标注拍摄角度、比例与色彩校正状态",
        "材料须标注成分、克重与供应商或来源",
        "工艺步骤须可复现（含工具与参数）",
        "图表须标注数据来源与单位",
        "设计结论须结合具体作品分析，避免抽象化",
    ),
    key_venues=(
        "Textile Research Journal",
        "International Journal of Fashion Design, Technology and Education",
        "Footwear Style & Science",
        "Design Studies",
        "服装设计师",
    ),
    units_and_formulas_notes=(
        "面料克重用 g/m²，厚度用毫米（mm）",
        "色号标注须含色卡系统（Pantone、RAL）与批次",
        "缝制工艺标注线迹类型与针距（针/cm）",
        "环保指标用百分比或等级标注（如再生纤维占比 %）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Illustrator", "Adobe Photoshop", "Adobe InDesign", "CLO 3D", "Browzwear", "Texcel CAD", "MTEX", "ImageJ", "MATLAB", "Python (NumPy, SciPy)", "R", "Pro-E / Creo", "SolidWorks", "3D 扫描（Artec 3D）", "数码印花机", "激光切割机", "织造/针织原型机", "色差仪（Colorimeter）", "耐洗/耐摩擦测试仪", "Zotero"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
