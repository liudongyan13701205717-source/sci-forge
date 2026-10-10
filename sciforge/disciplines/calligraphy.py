"""书法学科论文支持：书法史论、书体研究、笔墨技法与数字书法体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="calligraphy",
    aliases=(
        "calligraphy",
        "书法",
        "中国书法",
        "硬笔书法",
        "软笔书法",
        "翰墨",
        "书学",
        "Calligraphy",
        "Chinese Calligraphy",
        "Hard-pen Calligraphy",
        "Chinese Brush Calligraphy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与研究定位）",
            "literature review（书学史研究综述）",
            "methodology（文献考据/风格分析/图像分析）",
            "analysis（书法本体分析）",
            "discussion",
            "conclusion",
            "references",
        ),
        "style_analysis": (
            "abstract",
            "introduction",
            "work description（作品基本信息与年代）",
            "formal analysis（章法、笔法、墨法、结构）",
            "historical context（风格脉络与师承）",
            "conclusion",
            "references",
        ),
        "teaching_research": (
            "abstract",
            "introduction",
            "instructional design（教学设计）",
            "implementation",
            "evaluation",
            "conclusion",
            "references",
        ),
    },
    citation_style="GB/T 7714 或艺术学领域惯用样式（艺术学引注须给出作品名、作者、年代、藏地）",
    reporting_standards={
        "work_citation": "作品引用须包含名称、作者、年代、材质、尺寸、藏地或出版信息",
        "calligraphy_analysis": "笔法/墨法分析须结合高清图与文献考据",
        "historical_studies": "史论研究须注明来源（碑帖/拓本/出版物）与著录",
        "digitization": "数字化采集须注明扫描分辨率、色彩管理与元数据",
    },
    conventions=(
        "书法作品引用须给出名称、作者、年代、材质、尺寸与著录",
        "碑帖引用须给出碑刻名、年代与拓本来源",
        "笔法术语须使用领域通行表述（如「侧锋」「逆入平出」「蚕头燕尾」）",
        "图像引用须注明分辨率、色彩管理与来源",
    ),
    key_venues=(
        "书法研究",
        "中国书法",
        "美术研究",
        "艺术评论",
        "艺术百家",
        "中国美术研究",
        "中国艺术研究院学报",
        "Art Journal",
        "Journal of Chinese Ink Painting Studies",
        "Journal of Aesthetics and Art Criticism",
        "荣宝斋",
    ),
    units_and_formulas_notes=(
        "作品尺寸以 cm 报告",
        "扫描分辨率以 dpi 报告（建议 300-600 dpi）",
        "色彩空间须注明（sRGB 或 Adobe RGB）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Epson Perfection V850 Pro（高精密扫描仪）", "Canon LiDE 120（扫描）", "iPad + Apple Pencil（数字书写）", "Procreate（数字书法）", "Adobe Photoshop", "Adobe Fresco", "Adobe Illustrator", "Adobe InDesign", "CorelDRAW", "汉仪书法字库", "方正硬笔书法", "文鼎科技字库", "集字圣手（集字软件）", "集字大师", "集字通", "书法字典 App", "Google Fonts 中文字库", "宣纸数字化采集系统", "毛笔数字化扫描装置", "硬笔书法练习板", "Canva", "Microsoft Word", "PowerPoint", "Microsoft Excel", "EndNote", "LaTeX（ctex 中文支持）"),
    category="艺术学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "中国书法网"),
)
