"""桌面出版学科论文支持：排版技术、印刷工艺与数字出版体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="desktop_publishing",
    aliases=(
        "desktop_publishing", "桌面出版", "DTP",
        "desktop publishing technology", "桌面出版技术",
        "digital publishing", "数字出版",
        "prepress technology", "印前技术",
        "typography", "排版技术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（排版问题与技术背景）",
            "methodology（版面设计、色彩管理、印刷测试）",
            "results（印刷质量评估数据）",
            "discussion（工艺优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "production process（制作流程）",
            "quality assessment（质量评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology evolution（技术发展史）",
            "current tools（当前工具对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "color": "色彩管理遵循 ISO 12647（商业印刷）/ ISO 12647-1",
        "printing": "印刷参数须标注（印刷方式、纸张、油墨、分辨率）",
        "quality": "印刷质量评估遵循 ISO 12647 或 ISO 2846 标准",
    },
    conventions=(
        "字体使用须注明字体名称、字号、字重与嵌入状态",
        "色彩模式（CMYK/RGB/Pantone）须统一标注",
        "图像分辨率注明 DPI（印刷≥300 DPI）",
        "出血/裁切标记须注明标准（如 ISO 12647）",
        "印前检查须包含字体嵌入、色彩转换与分辨率检查",
    ),
    key_venues=(
        "Journal of the European Ceramic Society",
        "Journal of Imaging and Technology",
        "Printing Technology",
        "DTP Magazine",
        "Publishing Research Quarterly",
    ),
    units_and_formulas_notes=(
        "图像分辨率用 DPI 表示",
        "色彩用 CMYK (%) 或 Pantone 编号",
        "字体大小用 pt 表示",
        "色差用 ΔE 值（CIE L*a*b*）",
        "印刷速度用页/小时或米/分钟表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe InDesign", "Adobe Photoshop", "Adobe Illustrator", "Adobe Acrobat", "Adobe Lightroom", "QuarkXPress", "Microsoft Publisher", "CorelDRAW", "Affinity Designer", "Affinity Publisher", "Affinity Photo", "Adobe Creative Cloud", "Acrobat Pro", "GIMP", "Inkscape", "FontForge", "Fontographer", "Adobe Type", "Adobe Bridge", "XMP Meta Editor"),
    category="工学",
    databases=("OpenAlex", "Crossref"),
)
