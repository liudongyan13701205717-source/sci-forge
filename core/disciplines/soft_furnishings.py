"""软装饰品设计与应用学科论文支持：材料工艺/视觉设计/场景应用体裁、GB/T 7714 引用样式与材料性能注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="soft_furnishings",
    aliases=("soft_furnishings", "软装饰品", "软装配饰", "软饰设计", "软装设计", "家居饰品"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="GB/T 7714（顺序编码制；设计类期刊常用）",
    reporting_standards={
        "materials": "材料性能测试须注明国标/行业标准编号与试件数量",
        "aesthetic_evaluation": "主观评价须报告样本量、评分量表与评定者一致性",
        "reproducibility": "设计稿须给出材料清单（BOM）与工艺参数以支持复现",
    },
    conventions=(
        "设计图纸标注比例、单位与图例；效果图注明渲染软件与视角",
        "材料命名中英文并列（亚麻 linen、丝绒 velvet、胡桃木 walnut）",
        "色彩须给标准色值（Pantone/CMYK/RGB）而非口语描述",
        "风格谱系须交代流派来源（极简、侘寂、中古风等）",
        "案例描述与理论诠释分层呈现",
    ),
    key_venues=(
        "装饰",
        "艺术与设计研究",
        "艺术百家",
        "室内设计与装修",
        "Journal of Textile Science and Technology",
    ),
    units_and_formulas_notes=(
        "尺寸单位用 mm/cm，面积用 m²，长度用 m",
        "色温用 K 表示，显色指数用 Ra（CRI）",
        "织物密度用 经纬根数/m（或 每英寸密度 D）表示",
        "阻燃/甲醛指标注明检测标准（GB 18401、GB/T 24128）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "3ds Max", "SketchUp", "AutoCAD", "Rhino", "V-Ray", "Corona", "Enscape", "Lumion", "D5 Render", "Blender", "Marvelous Designer", "KeyShot", "Artlantis", "Pantone Connect", "Material Library", "Adobe Substance 3D Sampler", "Adobe Substance 3D Painter"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
