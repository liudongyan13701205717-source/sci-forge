"""室内装潢（软包）学科论文支持：家具软包与面料工艺体裁、APA 引用样式与工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="upholstery",
    aliases=("upholstery", "室内装潢", "家具软包", "软包工艺", "座椅包覆",
             "furniture upholstery", "soft furnishing", "装潢工艺"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与工艺问题）",
            "materials and methods（材料、工艺与测试）",
            "results（性能、耐久与外观数据）",
            "discussion（工艺机理与应用）",
            "references",
        ),
        "process_study": (
            "abstract",
            "introduction",
            "materials and methods（工序、设备与参数）",
            "results（质量与效率数据）",
            "discussion（工艺优化建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；材料与工业期刊多用 APA/Elsevier）",
    reporting_standards={
        "material_testing": "材料测试须报告标准（ASTM/ISO）、试样与条件",
        "durability": "耐久性测试须报告循环次数、载荷与判定标准",
        "process_documentation": "工艺研究须报告设备、参数与工序步骤",
        "statistical": "须报告重复数、统计方法与显著性",
    },
    conventions=(
        "面料名称与成分须完整给出（含克重）",
        "缝纫/绷缝工艺参数（针距、张力）须量化",
        "泡沫密度用 kg/m³，硬度用压陷载荷报告",
        "测试标准（ASTM/ISO）须注明版本",
        "尺寸以 mm/cm 报告并说明公差",
    ),
    key_venues=(
        "Journal of Industrial Textiles",
        "Textile Research Journal",
        "Journal of Engineered Fibers and Fabrics",
        "Materials & Design",
        "International Journal of Clothing Science and Technology",
        "Journal of Cleaner Production",
    ),
    units_and_formulas_notes=(
        "面料克重用 g/m²；泡沫密度用 kg/m³",
        "尺寸用 mm/cm；公差用 ±mm",
        "针距用 针/10cm；张力用 N 或 cN",
        "耐久循环用 次数；载荷用 N 或 kg",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Juki 工业缝纫机", "Singer 缝纫机", "气动钉枪 (staple gun)", "泡沫切割机 (foam cutter)", "面料裁剪机 (fabric cutter)", "绷缝机 (blindstitch machine)", "皮革缝纫机 (walking foot)", "热熔胶枪", "气动订书机", "电动裁剪刀", "锁眼机 (buttonhole machine)", "CNC 泡沫切割机", "三维扫描仪 (3D scanner)", "AutoCAD", "Optitex", "CLO 3D", "Gerber AccuMark", "喷胶设备 (adhesive spray)", "码边机 (overlock machine)", "面料张力测试仪"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
