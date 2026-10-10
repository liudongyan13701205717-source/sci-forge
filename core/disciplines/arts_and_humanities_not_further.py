"""Arts and humanities not further 学科论文支持：遗产、档案、策展与人文学科综合，偏数字存档与馆校合作。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="arts_and_humanities_not_further",
    aliases=(
        "arts_and_humanities_not_further",
        "arts and humanities not further defined",
        "遗产与档案管理",
        "cultural heritage",
        "博物馆学",
        "museum studies",
        "curatorial studies",
        "数字档案",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "context and problem statement",
            "collection / archival method（藏品/档案来源、编目、数字化流程）",
            "findings（馆藏分析、编目与展示策略）",
            "discussion",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "case introduction",
            "method and documentation",
            "case analysis",
            "implications",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical development",
            "current state",
            "outlook",
            "references",
        ),
    },
    citation_style="Chicago 17th Notes-Bibliography（博物馆/档案/艺术史通用）；引藏品须给出馆藏与目录号",
    reporting_standards={
        "collection": "藏品/档案的采集来源、许可、目录号与馆藏号须逐条标注",
        "digitization": "数字化分辨率（dpi）、色彩管理（ICC profile）、文件格式须报告",
        "cataloguing": "编目标准（EAD、DC、Dublin Core、CIDOC CRM）须报告",
        "conservation": "保护处理须报告材料与工艺、依据（AIC / ICOM-COM）",
        "ethics": "涉及原住民/私人物件须报告获取同意与归还路径（NAIDCPA、ICOM 准则）",
    },
    conventions=(
        "藏品首次出现给出「藏品名称/年份/材质/尺寸/馆藏号」五要素；后续用目录号简称",
        "档案引用按「档案全宗/目录号/盒/件/页」给出；数字档案给出检索路径与哈希",
        "编目标准用全称首次出现后缩写（DC、EAD、CIDOC CRM）",
        "图像引用须与图注一致（来源、拍摄者、版权状态、许可类型）",
        "保护材料/工艺用标准名；化学品用 IUPAC 名与 CAS 号",
        "统计报告藏品数量、类别占比与时间分布；缺失值显式说明",
    ),
    key_venues=(
        "Museum and Society",
        "Curator: The Museum Journal",
        "Journal of Cultural Heritage",
        "International Journal of Heritage Studies",
        "Museum Management and Curatorship",
        "Journal of Museum Education",
        "Archival Science",
    ),
    units_and_formulas_notes=(
        "分辨率 dpi；尺寸 cm × cm × cm；质量 g/kg",
        "湿度用 % RH；温度用 ℃；光照 lux / mW·m⁻²·sr⁻¹",
        "藏品统计报告数量、占比与 95% CI；缺失数据显式标记 N/A",
        "档案检索路径与哈希（SHA-256）须可复算",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Tropy", "Omeka S", "Scalar", "CONTENTdm", "CollectionSpace", "PastPerfect", "AtoM (Access to Memory)", "ArchivesSpace", "DSpace", "BePress", "IIIF / Universal Viewer", "CIDOC-CRM tools", "EAD editor", "Agisoft Metashape", "RealityCapture", "CloudCompare", "Blender", "OpenScan", "Unity", "Unreal Engine", "TouchDesigner", "Zotero", "EndNote"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "Europeana", "JSTOR", "ICOM Collections Committee", "Getty Research"),
)
