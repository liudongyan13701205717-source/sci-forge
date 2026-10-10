"""纺织、服装与鞋类制造学科论文支持：服装与鞋类结构设计、工艺开发研究体裁、APA 引用样式与制版参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="textiles_clothes_footwear_and",
    aliases=(
        "textiles_clothes_footwear_and",
        "Textiles (clothes, footwear and",
        "服装与鞋类制造",
        "纺织服装制造",
        "皮革与鞋类",
        "Apparel and footwear manufacturing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（设计背景与研究问题）",
            "materials and methods（材料与制版方法）",
            "results（样衣/成品性能数据）",
            "discussion（工艺与结构设计分析）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（产品与生产案例）",
            "analysis（工艺与质量分析）",
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
    citation_style="APA 样式（作者-年份）",
    reporting_standards={
        "design_specification": "制版尺寸与公差须完整列出并标注测量方法",
        "material_testing": "面料与辅料性能须遵循标准测试并报告试样数",
        "production_protocol": "生产工艺流程须逐步记录（含参数、设备与人工）",
        "quality_control": "质量检验须注明 AQL 水平与检验标准",
    },
    conventions=(
        "服装码号须与国家标准体系一致（如 GB/T 1335、ISO 8559）",
        "鞋码标注须说明制式（欧码/美码/中国码）",
        "制版图须标注比例与基准线",
        "材料须标注成分百分比（天然与合成分别列出）",
        "工艺参数须注明设备型号与操作条件",
    ),
    key_venues=(
        "Journal of Textile Technology",
        "International Journal of Clothing Science and Technology",
        "Footwear Style & Science",
        "中国服装",
        "鞋类工业设计",
    ),
    units_and_formulas_notes=(
        "服装尺寸用厘米（cm），公差用 ±mm 表示",
        "面料厚度用毫米（mm），克重用 g/m²",
        "鞋内长用毫米（mm），楦高用厘米（cm）",
        "耐洗次数用洗涤循环次数（cycle）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CLO 3D", "Browzwear", "Marvelous Designer", "Optitex", "Gerber Accumark", "Gerber System 8", "CAD/CAM 制版系统", "TrueShape 鞋楦设计", "SolidWorks", "AutoCAD", "Adobe Illustrator", "Adobe Photoshop", "Pro-E / Creo", "CATIA", "3D 扫描（Structure Sensor）", "虚拟试衣系统", "自动化裁剪台", "工业缝纫机", "压力分布测试仪", "Zotero"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
