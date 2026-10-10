"""水泥施工学科论文支持：水泥/混凝土/砂浆材料体系与施工工艺体裁与引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cement_working",
    aliases=(
        "cement working",
        "concrete construction",
        "cement manufacture",
        "mortar",
        "ready-mixed concrete",
        "水泥施工",
        "混凝土施工",
        "水泥生产",
        "砂浆",
        "商品混凝土",
        "混凝土材料",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（材料体系与工程需求）",
            "materials and methods（原材料、配合比与试验方法）",
            "results（力学、耐久与工作性数据）",
            "discussion（微观机理与工程适用性）",
            "conclusions",
            "references",
        ),
        "materials": (
            "abstract",
            "introduction",
            "raw materials and mix design（原材料与配合比设计）",
            "characterization（宏观力学与微观表征）",
            "performance and durability（性能与耐久性）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "taxonomy（按水泥种类/骨料/外加剂分类）",
            "state of the art",
            "challenges and outlook",
            "references",
        ),
    },
    citation_style="Cement and Concrete Research 样式（Elsevier 编号）",
    reporting_standards={
        "cement": "水泥须报告标号（42.5/42.5R）与执行标准（GB 175 / EN 197）",
        "mix": "混凝土拌合物须报告配合比、坍落度与含气量",
        "strength": "强度试验须注明养护龄期与试件尺寸（GB/T 50081）",
        "admixture": "外加剂须报告掺量与固含量，标注母液/固粉",
        "microstructure": "微观表征须给出 SEM 条件、物相分析（XRD / Bogue 公式）",
    },
    conventions=(
        "水泥试验须报告标号（42.5/42.5R）与执行标准（GB 175 / EN 197）",
        "混凝土拌合物须报告配合比、坍落度与含气量",
        "强度试验须注明养护龄期与试件尺寸（GB/T 50081）",
        "外加剂须报告掺量与固含量，标注母液/固粉",
        "水泥熟料矿物须按 Bogue 公式或 XRD 报告",
    ),
    key_venues=(
        "Cement and Concrete Research",
        "Construction & Building Materials",
        "ACI Materials Journal",
        "Magazine of Concrete Research",
        "International Journal of Concrete Structures and Materials",
        "Journal of Materials in Civil Engineering",
    ),
    units_and_formulas_notes=(
        "强度用 MPa；坍落度用 mm；含气量用 %",
        "配合比用水泥:水:砂:石质量比表示；水胶比用小数",
        "掺量用 %（占胶材质量）；温度用 ℃",
        "微观数据须注明 XRD 条件（Cu Kα、扫描步长）与 SEM 加速电压",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("坍落度筒", "Proceq Schmidt 回弹仪", "MTS 压力试验机", "ASTM C109 水泥胶砂搅拌站", "混凝土振动台", "水泥净浆搅拌机", "Bruker D8 X 射线衍射仪", "ZEISS 扫描电子显微镜", "Mettler TGA 热重分析仪", "Autosize 压汞仪", "混凝土含气量仪", "混凝土搅拌站", "Putzmeister 混凝土泵", "水泥回转窑", "球磨机", "熟料冷却机", "Thermo ARL XRF 分析仪", "电子万能试验机", "混凝土渗透仪", "氯离子迁移测试仪"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
