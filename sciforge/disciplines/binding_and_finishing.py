"""装订与后期加工（Binding and Finishing）学科论文支持：印刷装订、后期加工、色彩与质量标准。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="binding_and_finishing",
    aliases=(
        "binding and finishing (printing)", "book binding", "印刷装订", "装订与后期加工",
        "post-press", "印后加工", "finishing", "胶订", "锁线胶订",
        "bookbinding", "装帧设计", "packaging finishing", "书刊装订",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与印刷工艺背景）",
            "materials and methods（纸张/油墨/胶/工艺参数）",
            "results（物理/色彩/工艺指标）",
            "discussion（机理与工艺改进）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "背景",
            "工艺与设备综述",
            "质量标准与测试方法",
            "outlook",
            "references",
        ),
        "case_study": (
            "abstract",
            "生产案例（版次/机型/规格）",
            "工艺路线与参数",
            "质量指标",
            "改进建议",
            "references",
        ),
    },
    citation_style="APA 7 或 ISO 690；印刷类遵循 GB/T 7714 或 ANSI/NISO Z39.63",
    reporting_standards={
        "print_quality": "印品质量遵循 ISO 12647、ISO 2846、ISO 12647-1 系列",
        "color": "色度学参数（ΔE*ab、L*C*h*）须按 CIE 1931 或 CIE 2000 计算",
        "color_management": "ICC 色彩配置文件、打样条件（D50 光源、中性环境）须交代",
        "materials": "纸张、油墨、胶、覆膜材料须列品牌/供应商与批次",
        "binding_spec": "装订参数（糊口宽度、锁线针距、书脊厚度、书口/天头地脚）须报告",
    },
    conventions=(
        "色度学参数与色彩空间转换按 CIE 标准表述",
        "工艺参数以 mm/°C/g 等给出，含不确定度",
        "装订工艺按 GB/T 34605、FIP 系列报告",
        "样张/打样照片须注明拍摄条件（光源、白平衡）",
        "色标/色卡（Pantone / HKS / NCS）须在正文给出",
    ),
    key_venues=(
        "Journal of Graphic Engineering",
        "Print Technology Journal",
        "Color Research & Application",
        "Journal of Packaging Engineering",
        "包装工程（CNKI 核心期刊）",
        "Journal of Applied Polymer Science",
    ),
    units_and_formulas_notes=(
        "色度用 CIELAB（L*C*h*），色彩差异用 ΔE*ab（CIE76）或 ΔE00",
        "分辨率 dpi/line；网点百分数 %；油墨密度按 ISO 12647-2",
        "纸张克重 g/m²，厚度 μm",
        "温度 °C；相对湿度 %RH（标准 23±1 °C，50±5%RH）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Heidelberg Speedmaster XL（胶印机）", "Heidelberg SM 系列（胶印机）", "Heidelberg Multiplex 34/40/52（折页机）", "Heidelberg CD102（自动折页机）", "Heidelberg Prinect（印前打样与流程控制）", "Heidelberg Speedmaster CX（数码印刷）", "HP Indigo（数码印刷）", "Konica Minolta AccurioPress（数码印刷）", "Müller Martini Perfect Binder", "Hoffmann Perfecbind（完美胶订）", "Beckermann 锁线胶订机", "Hoefer HBF 系列（精装/半精装）", "Rilex RBS 系列（精装）", "Curtiss-Magellan 折页机", "Zünd G3/G4（激光模切机）", "BOBST E-Series（模切/折页）", "Plocka 3000（胶订/锁线）", "Plocka X-Cut（裁切）", "Pura 1300/1500（切纸机）", "Müller Martini PowerBind", "3M 覆膜机/胶带", "Beckermann 圆压圆烫金", "DGM 装订工具", "X-Rite i1 Pro3（测色仪）", "Datacolor SpectroColor", "Epson ColorEdge 显示器（校色）", "X-Rite i1 Display3（显示器校色）", "Adobe Acrobat Pro（PDF/印前检查）", "Adobe Photoshop（图像处理）", "Adobe Illustrator（版面设计）", "QuarkXPress（桌面出版）", "Adobe InDesign（桌面出版）", "EFI Fiery（RIP）", "LaTeX", "Minitab（工艺质量统计）"),
    category="工学",
    databases=("OpenAlex", "Scopus", "CNKI", "Compendex"),
)
