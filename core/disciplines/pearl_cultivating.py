"""珍珠养殖学科论文支持：水产养殖/珍珠学体裁、水产科学引用样式与养殖记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pearl_cultivating",
    aliases=("pearl cultivating", "珍珠养殖", "珍珠学", "pearl aquaculture", "珍珠养殖技术", "淡水珍珠", "海水珍珠", "贝类养殖", "marine biology"),
    paper_types={
        "research": ("abstract", "introduction（养殖问题与科学目标）", "methodology（养殖环境与操作）", "results（成珠率与质量）", "discussion（生物学与产业意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（养殖海区/养殖品种）", "analysis（操作与环境响应）", "results（产量与品质）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（珍珠生物学与产业理论）", "evidence synthesis（养殖技术综述）", "future directions", "references"),
    },
    citation_style="Vancouver/水产科学样式（水产科学领域常用；养殖规范按国家标准引用）",
    reporting_standards={"environment": "养殖海区/湖泊环境参数（水温、盐度、溶解氧、pH）须按季度或月度报告", "grafting": "珠核操作（母贝选择、核规格、手术流程）须按标准操作规程报告", "quality": "珍珠质量按 GB/T 18783 或国际标准评级（光泽、瑕疵、形状、颜色）", "ethics": "母贝与水体生态影响须说明", "sampling": "抽样方案与统计方法须报告"},
    conventions=("母贝品种（Akoya/大珠母贝/三角帆蚌等）须用拉丁学名标注", "珠核规格用直径 mm 与材料（贝壳/树脂）", "养殖周期用月数并注明放流与收获时间", "光泽按 GB/T 或国际惯例分级", "水体采样与监测点分布须附图"),
    key_venues=("Aquaculture", "Aquaculture International", "Journal of Shellfish Research", "Aquaculture Research", "水产学报", "Marine and Freshwater Research"),
    units_and_formulas_notes=("温度用 °C；盐度用 psu；溶解氧用 mg/L", "珠核直径与母贝壳长用 mm", "成珠率用百分比表示，须报告母贝数与珠数", "生长曲线用月龄-质量曲线并标注拟合方法"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("贝类活体手术工具", "珠核打孔器", "母贝选育秤", "水质多参数监测仪（YSI/In Situ）", "溶解氧仪", "水温盐度记录仪", "母贝标记用 RFID/刺青", "珠核扫描仪", "珠层显微测厚仪", "光泽度仪（珍珠专用）", "电子天平", "显微镜（生物体检测）", "流式细胞仪（基因多样性）", "SPSS 统计分析", "R 统计分析", "Python (Pandas)", "OriginPro 绘图", "GIS (ArcGIS) 海区制图", "ImageJ 图像分析", "Seagrid 网格数据处理"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
