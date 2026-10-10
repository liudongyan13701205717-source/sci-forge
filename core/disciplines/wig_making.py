"""假发制作学科论文支持：假发艺术、纤维工艺与造型美学研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wig_making",
    aliases=(
        "wig making",
        "假发制作",
        "假发工艺",
        "义发制作",
        "wig artistry",
        "cosmetology",
        "假发造型",
        "义发艺术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（历史背景与问题）",
            "materials and methods（材料/纤维特性与工艺方法）",
            "fabrication process（制作流程描述）",
            "evaluation（性能评价与效果分析）",
            "discussion（美学与工艺讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "client profile（客户案例描述）",
            "design concept（设计构思）",
            "fabrication and fitting（制作与佩戴过程）",
            "outcome and feedback（效果与反馈）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "wig history（假发历史沿革）",
            "fiber technologies（纤维技术综述）",
            "styling techniques（造型技术综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "material specification": "纤维类型、直径、长度、颜色须明确标注并附测试数据",
        "process documentation": "制作工艺须逐步记录温度、时间、压力等参数",
        "performance testing": "成品测试须包括拉伸强度、回弹性、耐热性、色牢度等指标",
        "wearer comfort": "佩戴舒适度须包含体温感、通风性、头皮反应等主观与客观指标",
    },
    conventions=(
        "假发类型区分蕾丝前额（lace front）、全蕾丝（full lace）、机械假发（machine-made）",
        "纤维类型标注合成（synthetic）、真人发（human hair）、混纺（blend）",
        "尺寸标注使用行业标准尺寸（如 21-23 英寸为头围）",
        "色彩描述区分基底色（base color）与挑染/漂染效果",
        "佩戴效果照片须统一光线条件与拍摄角度",
    ),
    key_venues=(
        "Journal of Cosmetic Science",
        "International Journal of Cosmetic Science",
        "Journal of Hair Science and Technology",
        "Cosmetics journal (MDPI)",
        "Journal of the Society of Cosmetic Chemists",
    ),
    units_and_formulas_notes=(
        "发丝直径单位 μm；发长单位 cm 或英寸（in）",
        "拉伸强度单位 N（牛顿）或 cN/tex（厘牛顿/特克斯）",
        "耐热性测试温度单位 ℃（如合成纤维通常≤120℃）",
        "色牢度按 GB/T 3920 或 AATCC 8 标准评级（1-5 级）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("蕾丝假发台（Lace Wig Cap）", "假发基础头模（Mannequin Head）", "手工编织梳（Lattice Comb）", "蒸汽造型机（Steam Styling Machine）", "热风梳与风筒（Hot Air Brush & Dryer）", "发胶定型喷枪（Hair Setting Spray Gun）", "纤维色牢度测试仪（Colorfastness Tester）", "材料拉伸试验机（Universal Tensile Tester）", "分光光度计（Spectrophotometer，色差测量）", "电子天平（精度 0.01g）", "显微硬度计（Microhardness Tester）", "扫描电子显微镜（SEM，纤维截面分析）", "Photoshop 造型效果图设计", "CorelDRAW 矢量设计软件", "3D 头模建模软件（Rhino 3D）", "Procreate 手绘设计（iPad）", "LaTeX 学术排版", "EndNote 文献管理", "Citation 管理工具", "Google SketchUp 产品设计建模"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
