"""银匠工艺学科论文支持：贵金属加工工艺、珠宝设计与贵金属贸易研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="silversmithing",
    aliases=(
        "silversmithing",
        "银匠工艺",
        "贵金属加工",
        "珠宝设计",
        "Silver Smithing",
        "Jewellery Making",
        "Precious Metals",
        "金银器",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methods（工艺/实验方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（作品/工坊案例）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份）",
    reporting_standards={
        "craft": "工艺实验须报告金属纯度、温度区间与工艺参数（锤揲/焊接/抛光）",
        "metallurgy": "金属分析须给出 XRF/SEM-EDS 数据与检测限值",
        "heritage": "文物修复须遵循 ICOM-CC 伦理准则（可逆性、最小干预）",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "贵金属纯度以 ‰ 或 carat 报告（如 925/1000、18K、999/1000）",
        "工艺温度单位统一为 ℃；退火温度按合金类型给出范围",
        "作品尺寸以 mm 计；重量以 g 计",
        "文物年代须给出考据依据与检测技术（如 XRF、热释光）",
        "图表须标注工艺步骤、材料与成品照片",
    ),
    key_venues=(
        "Journal of Jewelry Design",
        "National Jewelry Review",
        "Journal of Archaeological Science",
        "Journal of Materials Research",
        "中国黄金报",
    ),
    units_and_formulas_notes=(
        "贵金属密度：银 10.49 g/cm³、金 19.32 g/cm³、铂 21.45 g/cm³",
        "焊接温度：低银焊 650 ℃、高银焊 750 ℃、硬钎焊 815 ℃",
        "延展性以延伸率（%）与断后伸长率报告",
        "颜色以 CIE L*a*b* 坐标或 Pantone 编号标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Autodesk Matrix", "Rhino 3D", "SolidWorks", "Fusion 360", "Grasshopper", "Photoshop", "Adobe Illustrator", "Substance Painter", "ZBrush", "Cinema 4D", "Blender", "XRF Analyzer (Thermo Fisher)", "SEM-EDS", "Koh-i-noor Hard-paste Wax", "Limpcast Wax", "Vacuum Casting Machine", "Laser Welder", "Ring Roller", "Annealing Kiln", "Pyrometric Cone"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus"),
)
