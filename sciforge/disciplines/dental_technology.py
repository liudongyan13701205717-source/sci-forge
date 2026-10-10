"""牙科技术学科论文支持：口腔修复与数字化技工技术体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dental_technology",
    aliases=(
        "dental_technology", "牙科技术", "口腔修复技术",
        "prosthodontic technology", "义齿加工技术",
        "dental ceramics", "牙科陶瓷技术",
        "dental metal technology", "金属修复体技术",
        "digital dentistry", "数字化牙科技术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（技术改进背景）",
            "materials and methods（材料选择与测试方案）",
            "results（测试数据）",
            "discussion（技术改进效果）",
            "references",
        ),
        "case_study": (
            "abstract",
            "case presentation（患者需求与修复方案）",
            "fabrication process（制作流程）",
            "clinical outcome（临床效果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology comparison（技术对比）",
            "current status（现状）",
            "future trends（趋势）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "materials": "材料须标注品牌、批号、成分",
        "testing": "力学测试遵循 ISO 标准",
        "clinical": "临床效果评估须注明评估者与时间",
    },
    conventions=(
        "材料性能数据须注明测试条件",
        "修复体制作步骤须逐步记录",
        "数字化文件注明格式（STL/PLY）与单位（mm）",
        "色差评估用 ΔE 值",
        "测试结果给出均值 ± SD",
    ),
    key_venues=(
        "Dental Materials",
        "Journal of Prosthetic Dentistry",
        "Clinical Oral Investigations",
        "Journal of Prosthodontic Research",
        "Dentistry Today",
    ),
    units_and_formulas_notes=(
        "强度用 MPa；挠度用 μm",
        "色差用 ΔE 值（CIE L*a*b*）",
        "热膨胀系数用 10⁻⁶/℃",
        "边缘间隙用 μm 表示",
        "测试结果给出均值 ± SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CAD/CAM 义齿设计软件", "数字化烧结炉", "万能试验机", "显微硬度计", "扫描电子显微镜", "X射线衍射仪", "色差仪", "体素显微镜", "3D 打印机（牙科树脂）", "CNC 切削机", "超声清洗器", "CAD/CAM 扫描仪", "石膏振动搅拌机", "蜡型切削机", "铸造机", "喷砂机", "抛光机", "体视显微镜", "SPSS", "Microsoft Excel"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
