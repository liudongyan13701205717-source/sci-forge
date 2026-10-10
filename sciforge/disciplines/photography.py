"""摄影学科论文支持：静物/人像/纪实体裁、APA 引用样式与摄影作品规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="photography",
    aliases=("photography", "摄影", "视觉艺术", "visual arts", "影像", "photograph",
             "纪实摄影", "documentary photography", "人像摄影", "portrait photography", "风光摄影"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与视觉问题）",
            "methodology（创作方法与流程）",
            "results（作品与效果）",
            "discussion（艺术语境与影响）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（作品/项目描述）",
            "analysis（视觉语言与技法分析）",
            "results（受众/评价）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（摄影理论与美学）",
            "evidence synthesis（流派、大师与作品汇编）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（摄影作品以图片 caption 或作品档案卡形式引用）",
    reporting_standards={
        "visual_artwork": "作品描述遵循视觉艺术著录规范（Title/Medium/Date/Dimensions）",
        "photo_history": "摄影史研究遵循 Visual Resources Association 引证规范",
        "case_study": "个案研究遵循 SRQR 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "ethical_consideration": "涉人/涉地作品须报告伦理审查与授权情况"
    },
    conventions=(
        "作品引用采用 Title, Year, Medium, Dimensions, Location/Owner 顺序",
        "技术参数（镜头、快门、光圈、ISO、光源）须按项目惯例完整报告",
        "黑白/彩色与印刷媒介（胶片、数码、打印）须区分标注",
        "涉及伦理的作品（纪实、人像、儿童、创伤）须描述知情同意与审查",
        "图像后处理（Adobe Photoshop/Lightroom）须标注处理范围"
    ),
    key_venues=(
        "Journal of Visual Culture",
        "Photography and Culture",
        "Journal of British Cinema and Television Studies",
        "Studies in Visual Arts and Design",
        "Journal of Photographic Science",
        "Journal of the History of Photography"
    ),
    units_and_formulas_notes=(
        "尺寸用 mm 或 cm（作品尺寸须以宽×高×深顺序）",
        "分辨率用 DPI/PPI（印刷 300 DPI 为标准）",
        "公式用 amsmath；摄影光学（景深、放大倍率）与曝光三角（光圈/快门/ISO）统一",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "图像元数据（EXIF）作为附件或数据附录保留"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Lightroom", "Capture One", "DxO PhotoLab", "Affinity Photo", "Adobe Premiere Pro", "DaVinci Resolve", "Canon EOS 单反相机", "Nikon 单反相机", "Sony Alpha 全画幅", "Medium Format 中画幅相机", "35mm 胶片相机", "Large Format 大画幅相机", "Adobe InDesign", "Adobe Illustrator", "Adobe After Effects", "Final Cut Pro", "X-Rite ICC 校色软件", "Photography 历史文献库", "Adobe Creative Cloud Library"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI", "Getty Images"),
)
