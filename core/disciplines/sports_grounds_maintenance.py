"""体育场地维护学科论文支持：草坪/天然草/合成草场地养护体裁、APA 引用样式与草皮学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sports_grounds_maintenance",
    aliases=("sports_grounds_maintenance", "体育场地维护", "草坪维护",
             "场地养护", "sports grounds maintenance", "turfgrass maintenance"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7th（草坪学主流；Crop Science 类期刊遵循 Crop Science 规范）",
    reporting_standards={
        "turf_measurement": "天然草测试遵循 STRI/Exova CTS 国际测试规程（含球滚动、可渗透性、抗冲击、草皮硬度）",
        "field_design": "场地设计遵循 IAAF/World Athletics 场地技术规格",
        "experiment_design": "草皮试验须报告试验小区面积、重复数、修剪高度与养护强度",
    },
    conventions=(
        "草种须列出学名（斜体）与品种名，注明混播比例",
        "修剪高度、灌溉量、施肥速率须以 SI 单位给出",
        "球滚动距离以 m 报告；抗冲击强度以 G 报告",
        "养护周期与季节须明确（如生长季 6-9 月）",
        "土壤理化性质报告 pH、EC、有机质、质地",
    ),
    key_venues=(
        "Journal of Turfgrass Science & Management",
        "Crop Science",
        "Horticultural Science",
        "Agronomy Journal",
        "Sports Turfgrass News",
    ),
    units_and_formulas_notes=(
        "修剪高度以 cm 报告；灌溉量以 mm/天 报告",
        "土壤 EC 用 mS/cm；pH 在 1:5 土水比测得",
        "球滚动距离以 m 报告，测试速度按 STRI 规程",
        "公式用 amsmath；养分施用量换算 N-P-K 比例须明确",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Clegg Impact Soil Tester", "Gopher 土壤采样器", "Trimble NDVI 绿度仪", "DJI Agras 无人机", "GSSI 探地雷达", "Infiltrometer 渗水率仪", "Toro 场地推剪", "Verticutter 顶切机", "Aerification 打孔机", "Hunter 灌溉控制器", "Orbit 喷灌系统", "Dragline 拖拽喷灌", "Scotts 撒布机", "TDR 土壤水分传感器", "土壤 pH/EC 计", "Davis 气象站", "EXOVEA 天然草测试系统", "Exova CTS 运动场地测试", "Trimble Agriculture 平台", "STRI 运动场地测试协议"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
