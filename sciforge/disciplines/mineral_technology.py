"""矿物加工技术学科论文支持：选矿/矿物加工/资源回收体裁、IOM 引用样式与选矿工艺参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mineral_technology",
    aliases=(
        "mineral_technology", "矿物加工技术", "矿物技术", "矿物加工", "选矿",
        "beneficiation", "矿物工艺", "矿物工程", "矿物提取"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与工艺问题）",
            "methodology（矿物加工与实验）",
            "results（选矿数据）",
            "discussion（机理与工艺改进）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（矿山/工厂案例）",
            "analysis（工艺参数分析）",
            "results（选矿回收率）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（选矿理论）",
            "evidence synthesis（工艺对比）",
            "future directions",
            "references",
        ),
    },
    citation_style="IOM 样式（作者-年份；Minerals Eng. 遵循 IOM 规范）",
    reporting_standards={
        "experimental": "矿物加工实验遵循 IOM 建议方法",
        "mineral_char": "矿物学表征遵循 IOM 矿物学描述规范",
        "pilot_test": "工业试验遵循矿物加工工业试验报告规范",
    },
    conventions=(
        "样品粒度与矿相须报告",
        "选矿回收率与品位须单位统一",
        "浮选药剂名称与用量须完整",
        "矿物加工术语须统一",
        "矿物学分析条件须说明",
    ),
    key_venues=(
        "Minerals Engineering",
        "Mineral Processing & Extractive Metallurgy Reviews",
        "International Journal of Mineral Processing",
        "Powder Technology",
        "Chemical Engineering Research and Design",
    ),
    units_and_formulas_notes=(
        "回收率用 %；品位用 % 或 g/t",
        "粒度用 μm；浓度用 wt% 或 g/L",
        "公式用 amsmath；回收率公式须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("X 射线衍射仪 (XRD)", "扫描电镜 (SEM)", "透射电镜 (TEM)", "电子探针 (EPMA)", "电感耦合等离子体质谱 (ICP-MS)", "激光诱导击穿光谱仪 (LIBS)", "浮选机", "球磨机", "磁选机", "重选设备", "化学浸出装置", "焙烧炉", "Python (NumPy/Pandas)", "MATLAB", "MINETAL-PRO", "高通量筛选平台", "纳米粒度分析仪", "比表面积分析仪", "R (数据处理)", "激光粒度分析仪"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
