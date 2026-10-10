"""Decorative metal crafts 学科论文支持：装饰金属工艺研究体裁、材料工艺规范与数字设计工具。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="decorative_metal_crafts",
    aliases=(
        "decorative_metal_crafts", "装饰金属工艺", "金属工艺", "金属艺术",
        "装饰金工", "metalwork", "metal arts", "ornamental metalwork",
        "metalcraft", "jewellery metalwork", "sculptural metalwork",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与创作动机）",
            "materials and methods（材料与工艺方法）",
            "results（作品分析与实验数据）",
            "discussion（艺术意义与工艺创新）",
            "references",
        ),
        "creative_practice": (
            "abstract",
            "introduction",
            "conceptual_framework（概念框架）",
            "process（创作过程与工艺描述）",
            "outcome（作品呈现与自我评价）",
            "references",
        ),
        "pedagogical": (
            "abstract",
            "introduction",
            "curriculum（课程设计与教学目标）",
            "teaching_methods（教学方法与评估）",
            "evaluation（教学效果评估）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "materials": "材料牌号与热处理参数须完整报告（钢种、硬度HRC、退火温度）",
        "process": "工艺流程须逐步描述，包括成型/连接/表面处理各工序参数",
        "imaging": "作品图片须附拍摄条件（光照、背景、比例尺）；尺寸须以厘米标注",
        "innovation": "创新点须明确区分传统技法与数字技术/新材料的应用",
    },
    conventions=(
        "材料牌号与热处理参数须完整报告（如钢种、硬度HRC、退火温度）",
        "工艺流程须逐步描述，包括成型/连接/表面处理各工序参数",
        "设计草图/效果图须标注比例尺与材质说明；3D模型须注明软件版本",
        "作品图片须附拍摄条件（光照、背景、比例尺）；尺寸须以厘米标注",
        "创新点须明确区分传统技法与数字技术/新材料的应用",
    ),
    key_venues=(
        "Studies in Conservation",
        "Journal of the Royal Society of Arts",
        "Metals and the Conservation of Archaeological Material",
        "Smithsonian Studies in History and Culture",
        "Craft Research International",
        "International Journal of Traditional Craft",
        "Journal of Metalsmithing",
        "Metals and Materials Review",
    ),
    units_and_formulas_notes=(
        "硬度用 HRC（洛氏C标尺）；强度用 MPa；延展性用 %",
        "温度用 ℃（摄氏度）；压力用 MPa 或 kN",
        "尺寸用 mm 或 cm；重量用 g 或 kg",
        "配方比例用质量分数（wt%）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "专利", "教案与教材", "报告", "数据集"),
    tools=("Rhino 3D", "Grasshopper", "Fusion 360", "SolidWorks", "Blender", "ZBrush", "Mastercam", "ArtCAM", "SpeedCast", "Adobe Illustrator", "CorelDRAW", "AutoCAD", "Creo (Pro/E)", "CATIA", "CNC Turning Center", "CNC Milling Machine", "Fiber Laser Cutter", "Plasma Cutter", "MIG Welder (MAG)", "TIG Welder (GTAW)"),
    category="艺术学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
