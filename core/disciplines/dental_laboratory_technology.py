"""牙科技工技术学科论文支持：修复体制作工艺、材料科学与质量检验体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dental_laboratory_technology",
    aliases=(
        "dental_laboratory_technology", "牙科技工技术", "牙科技工",
        "dental prosthesis technology", "牙科技工制作", "义齿加工技术",
        "dental ceramics technology", "全瓷修复体制作",
        "dental framework fabrication", "金属支架制作",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（材料问题与工艺背景）",
            "materials and methods（材料、模具、烧结参数与检测方法）",
            "results（力学/耐磨/生物相容性测试数据）",
            "discussion（工艺优化与临床应用前景）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "classification（材料/工艺分类）",
            "comparison（各工艺优劣对比）",
            "outlook（发展趋势）",
            "references",
        ),
        "case_study": (
            "abstract",
            "case description（修复体类型、患者需求与制作过程）",
            "method（工艺流程详解）",
            "result（最终成品评估）",
            "discussion",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "materials": "材料须标注品牌、批号、成分与供应商",
        "fabrication": "烧结/热压参数（温度、升温速率、保温时间）须完整报告",
        "testing": "力学测试遵循 ISO 标准（如 ISO 6872 弯曲强度）",
        "biocompatibility": "细胞毒性/生物相容性遵循 ISO 10993 系列",
    },
    conventions=(
        "材料名称首次出现给出中英文全称与商品名",
        "工艺参数（温度、压力、时间）须精确记录",
        "测试样本量不少于 5 个（力学测试建议 n≥10）",
        "显微组织观察给出放大倍数与成像条件",
        "边缘适合度用 μm 表示并注明测量方法",
    ),
    key_venues=(
        "Dental Materials",
        "Journal of Prosthodontic Research",
        "Journal of Dentistry",
        "Clinical Oral Investigations",
        "Journal of Mechanical Behavior of Biomedical Materials",
    ),
    units_and_formulas_notes=(
        "强度用 MPa；挠度用 μm；热膨胀系数用 10⁻⁶/℃",
        "烧结曲线参数须标注各阶段温度与时间",
        "色差用 ΔE 表示（CIE L*a*b* 色空间）",
        "数值结果给出均值 ± SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CAD/CAM 义齿设计软件", "数字化烧结炉", "万能试验机", "显微硬度计", "扫描电子显微镜", "X射线衍射仪", "热膨胀仪", "色差仪", "体素显微镜", "3D 打印机（牙科树脂）", "CNC 切削机", "超声清洗器", "CAD/CAM 扫描仪", "石膏振动搅拌机", "蜡型切削机", "铸造机", "喷砂机", "抛光机", "体视显微镜", "SPSS"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
