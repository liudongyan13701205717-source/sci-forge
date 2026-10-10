"""Arts not elsewhere classified 学科论文支持：视觉艺术、设计、绘画、雕塑、图形设计等未另列视觉艺术门类。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="arts_not_elsewhere_classified",
    aliases=(
        "arts_not_elsewhere_classified",
        "arts not elsewhere classified",
        "视觉艺术",
        "visual arts",
        "fine arts",
        "视觉传达设计",
        "graphic and visual design",
        "contemporary art practice",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "context and theoretical framing",
            "method / material and process",
            "work or case description",
            "analysis",
            "conclusion",
            "references",
        ),
        "practice_based": (
            "abstract",
            "context and problem",
            "process (making)",
            "work description",
            "critical reflection",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical and stylistic overview",
            "state of practice",
            "outlook",
            "references",
        ),
    },
    citation_style="Chicago 17th Notes-Bibliography（艺术史/视觉文化通用）；作品引用给出作者、标题、年份、材质、尺寸、馆藏",
    reporting_standards={
        "work": "作品首次出现给出作者、标题（斜体）、年份、材质与技法、尺寸、馆藏或藏家",
        "process": "材料/工艺/制作时间/协作人须报告；数字创作须列出软件与版本",
        "image": "图像引用须与图注一致；版权状态与许可须标明",
        "exhibition": "展览信息（主办方、场地、展期、图录号）须完整给出",
        "ethics": "涉及挪用、抄袭、临摹须明确标示来源与授权",
    },
    conventions=(
        "作品标题斜体，艺术家名与年份用正体；材质按材质/技法顺序列出",
        "图像尺寸按 cm × cm；单位统一；比例写 1:1、10:1 等",
        "色彩以 Pantone / CMYK / HEX 之一为主；跨材料时注明 ICC profile",
        "工艺流程用流程编号（step 1 / step 2），步骤与时间须完整",
        "展览与出版信息用全称首次出现后缩写；馆藏号须可核查",
        "批判反思段落须区分创作意图、执行结果与受众回应",
    ),
    key_venues=(
        "Art Journal",
        "Leonardo",
        "October",
        "The Art Bulletin",
        "Journal of Aesthetics and Art Criticism",
        "Journal of Visual Culture",
        "Configurations",
    ),
    units_and_formulas_notes=(
        "尺寸用 cm 或 mm；比例写比号；重量用 g/kg",
        "色彩：Pantone、CMYK 或 HEX 三选一；标注色域",
        "分辨率 dpi（印刷 ≥ 300 dpi）；显示色域 sRGB / Display P3",
        "作品数量、材料清单以表格形式给出；缺失字段标 N/A",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "Adobe Lightroom", "Adobe Fresco", "Corel Painter", "CorelDRAW", "Affinity Photo", "Procreate", "Clip Studio Paint", "Krita", "GIMP", "SketchBook", "ZBrush", "Substance 3D Painter", "Substance 3D Sampler", "Blender", "Maya", "Cinema 4D", "Rhino", "SketchUp", "Agisoft Metashape", "Tropy", "Omeka S", "Zotero", "EndNote"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "Getty Research", "C2RMF", "Artsy", "Artstor"),
)
