"""服装设计学科论文支持：服装设计与造型设计体裁、APA 引用样式与设计研究约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="costume_design",
    aliases=(
        "服装设计", "服装造型设计", "Costume Design",
        "Fashion Design", "戏服设计", "服装创意设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
        "design_critique": (
            "设计概述",
            "设计过程",
            "作品分析",
            "评价与反馈",
            "总结与展望",
        ),
        "historical_review": (
            "摘要",
            "历史背景",
            "风格演变",
            "代表人物与作品",
            "影响与启示",
            "参考文献",
        ),
    },
    citation_style="APA 第 7 版（设计研究可用 Chicago 样式）",
    reporting_standards={
        "materials": "面料与辅料须注明材质、来源与规格",
        "technique": "工艺技法须注明步骤与参数",
        "sizing": "尺寸须注明测量部位与单位",
        "ethics": "涉及人物形象的须获得肖像权许可",
    },
    conventions=(
        "面料材质须注明成分比例（如棉 60%/涤纶 40%）",
        "尺寸使用厘米（cm）或英寸（inch），标注测量方法",
        "色彩标注使用 Pantone 色号或 CMYK 值",
        "设计图须标注比例与视图（正面、背面、细节）",
        "引用历史作品须注明年代、设计师与出处",
    ),
    key_venues=(
        "Fashion Theory: The Journal of Dress, Gender, and Body",
        "Journal of Fashion Marketing and Management",
        "International Journal of Design",
        "Textile Research Journal",
        "Journal of Design History",
        "服装学报",
    ),
    units_and_formulas_notes=(
        "面料克重单位 g/m²",
        "纤维细度单位 denier 或 tex",
        "色彩数据使用 Pantone 或 CMYK 标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Illustrator", "Adobe Photoshop", "CLO 3D", "Marvelous Designer", "Blender（3D 服装建模）", "Vestiaire（虚拟试衣）", "Style3D（3D 服装排版）", "PatternMaster（服装制版软件）", "Gerber AccuMark（数字化打样）", "Optitex（服装 CAD 系统）", "CAD (Computer-Aided Design)", "TrueCAD（服装设计）", "SketchUp（服装原型设计）", "Rhino 3D（参数化建模）", "Procreate（数字绘画）", "Inkscape（矢量绘图）", "GIMP（图像处理）", "Adobe InDesign（排版设计）", "Pantone（色卡系统）", "ColorSnap（色彩匹配工具）"),
    category="艺术学",
    databases=("Scopus", "Web of Science", "ProQuest", "中国知网"),
)
