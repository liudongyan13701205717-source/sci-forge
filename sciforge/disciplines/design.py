"""设计学科论文支持：视觉传达/交互/产品设计体裁、设计研究报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="design",
    aliases=(
        "design", "设计", "艺术设计",
        "graphic design", "视觉传达设计",
        "interaction design", "交互设计",
        "product design", "产品设计",
        "user experience design", "用户体验设计",
        "visual communication design", "品牌设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（设计问题与研究背景）",
            "methodology（研究方法：用户研究/实验/案例）",
            "results（设计效果评估数据）",
            "discussion（设计启示与改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "design process（设计过程描述）",
            "evaluation（效果评估）",
            "discussion（经验总结）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview（设计史脉络）",
            "main trends（主要趋势）",
            "future directions（展望）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "user_research": "用户研究方法须明确（访谈/问卷/可用性测试）",
        "usability": "可用性评估遵循 ISO 9241-11 标准",
        "case_study": "案例研究须注明数据来源与时间",
        "design_process": "设计过程须记录关键决策点与迭代轮次",
    },
    conventions=(
        "设计作品须注明作者、时间、材料与尺寸",
        "用户研究注明样本量、抽样方法与知情同意",
        "可用性测试指标（任务完成时间、错误率、SUS 评分）须定义",
        "视觉作品首次出现给出编号与版权说明",
        "设计过程文档包含草图、线框图、高保真原型与最终稿",
    ),
    key_venues=(
        "Design Studies",
        "International Journal of Design",
        "Journal of Design Research",
        "Design and Culture",
        "Interaction Design and Architecture Magazine",
        "CHI Conference Proceedings",
    ),
    units_and_formulas_notes=(
        "色彩用 Pantone 编号或 CMYK/RGB/HEX 值",
        "字体用字体名称、字号与字重表示",
        "尺寸用 mm 或 px 表示并注明 DPI",
        "用户满意度用 Likert 量表或 SUS 评分",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe Creative Suite", "Figma", "Sketch", "Adobe InDesign", "Adobe Photoshop", "Adobe Illustrator", "Adobe XD", "Axure RP", "InVision", "Framer", "Blender", "Cinema 4D", "Maya", "AutoCAD", "SolidWorks", "Rhino 3D", "Fusion 360", "Microsoft Office", "XMind", "Miro"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "Design & Art Exchange"),
)
