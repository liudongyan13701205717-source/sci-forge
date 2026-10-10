"""葡萄酒储藏陈酿学科论文支持：橡木桶陈酿与瓶储演化体裁、ACS 引用样式与陈酿记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wine_storingmaturing",
    aliases=("wine storing and maturing", "葡萄酒储藏陈酿", "葡萄酒陈酿", "葡萄酒窖藏", "橡木桶陈酿",
             "wine aging", "wine maturation", "barrel aging"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与陈酿问题）",
            "materials and methods（酒样、容器与分析方法）",
            "results（成分演化与感官数据）",
            "discussion（陈酿机理与品质意义）",
            "references",
        ),
        "storage_study": (
            "abstract",
            "introduction",
            "materials and methods（储存条件与取样方案）",
            "results（时序演化数据）",
            "discussion（储存优化建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份或编号；J. Agric. Food Chem. 遵循 ACS 规范）",
    reporting_standards={
        "analytical": "分析化学须报告方法、仪器、标准品与验证参数",
        "storage_trial": "储存试验须报告温度、湿度、光照与取样时点",
        "sensory": "感官评价须报告评价员、标度与统计方法",
        "statistical": "须报告重复数、统计方法与显著性",
    },
    conventions=(
        "陈酿容器（橡木桶/不锈钢/瓶）与容量须注明",
        "橡木桶烘烤程度与使用次数须交代",
        "储存温湿度与时间须量化",
        "SO₂ 与溶解氧水平须报告",
        "感官描述须使用标准风味术语",
    ),
    key_venues=(
        "Journal of Agricultural and Food Chemistry",
        "American Journal of Enology and Viticulture",
        "Food Chemistry",
        "Australian Journal of Grape and Wine Research",
        "Food Research International",
        "Molecules",
    ),
    units_and_formulas_notes=(
        "温度用 °C；湿度用 % RH；时间用 月/年",
        "SO₂ 用 mg/L；溶解氧用 mg/L 或 ppb",
        "橡木内酯用 μg/L；多酚用 mg/L（没食子酸当量）",
        "色度用吸光度；氧化指标须注明测定方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("温湿度监控系统", "橡木桶 (oak barrel)", "不锈钢储罐 (stainless steel tank)", "酒窖管理系统", "SO₂ 分析仪", "溶解氧测定仪", "pH 计", "紫外-可见分光光度计", "自动滴定仪", "气相色谱-质谱联用仪 (GC-MS)", "高效液相色谱 (HPLC)", "酒泥搅拌系统 (bâtonnage)", "微氧处理设备 (micro-oxygenation)", "膜过滤系统", "惰性气体保护系统", "Foss WineScan", "Vintrace 软件", "温度记录仪 (data logger)", "瓶塞质量检测仪", "感官品评系统"),
    category="农学",
    databases=("AGRIS", "OpenAlex", "Crossref", "FSTA"),
)
