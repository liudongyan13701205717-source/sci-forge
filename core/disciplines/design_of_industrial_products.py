"""工业设计学科论文支持：产品设计开发、人机工程与制造技术体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="design_of_industrial_products",
    aliases=(
        "design_of_industrial_products", "工业设计", "工业产品设计",
        "industrial product design", "产品设计开发",
        "product development", "产品开发设计",
        "ergonomic design", "人机工程设计",
        "interaction design", "交互设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（产品问题与设计背景）",
            "methodology（用户研究、形态生成、原型制作、测试）",
            "results（产品评估与用户反馈）",
            "discussion（设计改进与推广建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "design process（设计全过程描述）",
            "evaluation（市场效果与用户评价）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "classification（产品设计分类）",
            "comparison（方法/技术对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "user_research": "用户研究方法须明确（访谈/可用性测试/A/B测试）",
        "ergonomics": "人机工程评估遵循 ISO 9241 系列",
        "usability": "可用性测试遵循 ISO 9241-11",
        "manufacturing": "工艺参数与公差须明确标注",
    },
    conventions=(
        "产品三维模型须注明尺寸单位（mm）与比例",
        "CMF（色彩/材料/表面处理）方案须明确说明",
        "原型制作注明材料与工艺（3D打印/CNC/手板）",
        "用户测试给出任务完成时间与满意度评分",
        "设计图纸遵循 GB/T 制图标准",
    ),
    key_venues=(
        "Design Studies",
        "Journal of Product Innovation Management",
        "International Journal of Industrial Ergonomics",
        "Human Factors",
        "Journal of Mechanical Design",
        "Design and Engineering",
    ),
    units_and_formulas_notes=(
        "尺寸用 mm 表示",
        "质量用 kg 表示",
        "材料力学参数（屈服强度、硬度）用 MPa/HRC",
        "色差用 ΔE 值",
        "可用性测试评分用 SUS 量表",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Fusion 360", "SolidWorks", "Rhino 3D", "Blender", "Adobe Creative Suite", "Figma", "SketchUp", "3ds Max", "AutoCAD", "MATLAB", "ANSYS", "Abaqus", "SolidWorks Simulation", "ANSYS Fluent", "CATIA", "NX", "Creo", "Inventor", "KeyShot", "Dassault 3DEXPERIENCE"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Design & Art Exchange"),
)
