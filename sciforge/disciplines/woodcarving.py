"""木雕学科论文支持：木雕创作与雕刻工艺体裁、Chicago 引用样式与雕刻记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="woodcarving",
    aliases=("woodcarving", "木雕", "木雕艺术", "木刻", "雕刻工艺",
             "wood carving", "wood sculpture", "carving craft"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与创作问题）",
            "materials and methods（材料、工具与工艺）",
            "results（作品分析与工艺数据）",
            "discussion（艺术与工艺意义）",
            "references",
        ),
        "creative_practice": (
            "abstract",
            "introduction（创作背景与理念）",
            "process（创作过程与工艺决策）",
            "works（作品呈现与分析）",
            "reflection（反思与评价）",
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
    citation_style="Chicago 样式（注释-参考文献；艺术史期刊多用 Chicago）",
    reporting_standards={
        "creative_practice": "创作实践研究须报告材料、工具、工艺与创作过程",
        "material_documentation": "木材须报告树种、学名、含水率与来源",
        "visual_analysis": "作品分析须报告尺寸、技法与图像来源",
        "provenance": "涉及历史作品须报告来源与收藏信息",
    },
    conventions=(
        "木材树种须给出学名与产地",
        "作品尺寸用 cm/mm 并注明（高×宽×深）",
        "雕刻技法（浮雕/圆雕/透雕）须明确",
        "工具与工艺步骤须说明",
        "作品图像须注明摄影与版权信息",
    ),
    key_venues=(
        "Studies in the Decorative Arts",
        "The Burlington Magazine",
        "Journal of the History of Collections",
        "Sculpture Journal",
        "Art History",
        "Craft Research",
    ),
    units_and_formulas_notes=(
        "尺寸用 cm/mm（高×宽×深）",
        "木材含水率用 %；密度用 g/cm³",
        "图像分辨率用 dpi/ppi；比例尺须标注",
        "年代用 世纪/年 并注明纪年依据",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("木雕刀具 (carving gouges)", "雕刻刀 (chisels)", "木槌 (mallet)", "雕刻工作台", "CNC 雕刻机", "激光雕刻机", "电磨机 (rotary tool)", "带锯机 (band saw)", "线锯 (scroll saw)", "砂光机 (sander)", "含水率测定仪", "木材硬度计", "三维扫描仪", "Rhino", "Blender", "ZBrush", "ArtCAM", "除尘系统", "抛光设备", "木材识别工具"),
    category="艺术学",
    databases=("JSTOR", "OpenAlex", "Crossref", "CNKI"),
)
