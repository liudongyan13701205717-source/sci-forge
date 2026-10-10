"""采石场监管学科论文支持：露天开采、边坡稳定与矿山生产管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="quarry_supervision",
    aliases=("quarry_supervision", "采石场监管", "quarry supervision", "quarry management", "露天开采", "open-pit mining", "矿山安全", "边坡稳定", "mine supervision"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "ISO 20345 露天矿工程规范", "k2": "国家矿山安全监察局规程", "k3": "GB 3948-2020 爆破安全规程"},
    conventions=("边坡参数须给出倾角与台阶高度", "爆破方案须列出药量与起爆顺序", "地质图使用标准图例", "测量仪器精度须列出误差范围", "参考文献按 GB/T 7714 著录"),
    key_venues=("Mining Engineering", "Journal of Rock Mechanics and Geotechnical Engineering", "International Journal of Mining and Reclamation", "煤炭学报", "岩石力学与工程学报"),
    units_and_formulas_notes=("长度使用米（m），高程使用海拔米", "角度使用度（°）与弧度（rad）", "爆破装药量使用千克（kg）", "边坡稳定系数无单位"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Trimble Total Station", "Leica Total Station", "Topcon GNSS", "Trimble Earthworks", "Leica Captivate", "AutoCAD Civil 3D", "Bentley OpenRoads", "Bentley MicroStation", "ArcGIS", "QGIS", "RS3 (RockSlope)", "Slide2", "GeoStudio", "Pit-Slope", "BlastMate", "PitVista", "Wholly3D", "BlastPro", "Trimble GeoDyne RTK", "DroneDeploy Surveying"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
