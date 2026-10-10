"""工艺、民间艺术和手工艺学科论文支持：传统工艺/非物质文化遗产体裁、APA 引用样式与工艺研究约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="crafts_folk_arts_and_artisan",
    aliases=(
        "工艺", "民间艺术", "手工艺", "Crafts",
        "Folk Arts", "Artisan Crafts", "非物质文化遗产",
        "传统手工艺", "Traditional Crafts",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
        "heritage_documentation": (
            "概述",
            "工艺背景",
            "技艺记录",
            "传承现状",
            "保护建议",
            "参考文献",
        ),
        "field_study": (
            "研究背景",
            "田野方法",
            "技艺分析",
            "传承人访谈",
            "传承与保护策略",
        ),
    },
    citation_style="APA 第 7 版（文化遗产研究可用 Chicago 样式）",
    reporting_standards={
        "materials": "原材料须注明来源、产地与采集方法",
        "technique": "传统技艺须记录完整工序与传承脉络",
        "fieldwork": "田野调查须遵循人类学伦理准则",
        "conservation": "保护措施须符合相关法规（如 UNESCO 公约）",
    },
    conventions=(
        "工艺名称须注明地域与民族归属",
        "传承人信息须注明称谓与传承谱系",
        "田野调查须遵循人类学知情同意原则",
        "技艺流程须按工序顺序详细记录",
        "引用传统文献须注明抄本来源与年代",
    ),
    key_venues=(
        "Journal of Craft Research",
        "Heritage & Society",
        "International Journal of Traditional Craft",
        "Craft Journal",
        "Journal of Material Culture",
        "中国工艺",
    ),
    units_and_formulas_notes=(
        "材料物理性能按国家标准报告",
        "田野记录使用标准化格式",
        "工艺尺寸使用厘米（cm）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Adobe Photoshop（工艺图像记录）", "Adobe Illustrator（工艺图案设计）", "3D 扫描软件（工艺三维记录）", "Fotogrammetria（摄影测量）", "RealityCapture（三维重建）", "Agisoft（摄影测量软件）", "Pix4D（摄影测量与建模）", "Meshroom（开源三维重建）", "Blender（三维建模与渲染）", "Cultural Heritage GIS（文化遗产地理信息系统）", "QGIS（文化遗产制图）", "ArcGIS（文化遗产空间分析）", "NVivo（传承人访谈质性分析）", "ATLAS.ti", "SPSS（田野数据统计分析）", "Tableau（文化遗产数据可视化）", "Unreal Engine（虚拟展示平台）", "Unity3D（虚拟工艺展示）", "Sketchfab（三维模型分享平台）", "Heritage at Risk Register（遗产风险登记系统）"),
    category="艺术学",
    databases=("Scopus", "Web of Science", "ProQuest", "中国知网", "UNESCO ICH Portal（非物质文化遗产数据库）", "China ICH Database（中国非遗数据库）"),
)
