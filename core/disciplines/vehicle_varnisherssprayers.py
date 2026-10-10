"""车辆清漆与喷涂学科论文支持：喷涂工艺参数、膜厚均匀性与前处理工艺的体裁、Elsevier 材料类引用样式与工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vehicle_varnisherssprayers",
    aliases=(
        "vehicle_varnisherssprayers",
        "车辆清漆喷涂",
        "涂装喷涂作业",
        "表面涂装",
        "varnishing and spraying",
        "coating application",
        "喷涂工艺",
        "漆膜"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（喷涂缺陷与工艺瓶颈）",
            "methods（工艺参数设计与试验方案）",
            "results（膜厚、外观与附着性能结果）",
            "discussion（机理与工艺窗口讨论）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工件、表面状态与环境条件）",
            "analysis（缺陷定位与工艺排查）",
            "results（参数调整后复测结果）",
            "discussion（经验推广与预防）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（喷涂装备与工艺路线综述）",
            "evidence synthesis（参数-缺陷-性能证据归纳）",
            "future directions",
            "references",
        ),
    },
    citation_style="Elsevier 材料类样式（数字编号，作者-年份备选，附 DOI）",
    reporting_standards={
        "环境与工件": "报告喷涂环境温湿度、洁净等级与工件预处理等级（如 Sa 2.5），注明温度梯度控制",
        "工艺参数": "逐项列出雾化气压、喷涂距离、速度、扇幅、重叠率、稀释比与膜厚设定值",
        "膜厚测量": "按 GB/T 13452.2 或 ASTM D6051 报告测点数量、干膜厚度与变异系数",
        "缺陷判定": "按缺陷类型（流挂、橘皮、针孔、起皱、附着力不良）分级记录并附照片与量化数据"
    },
    conventions=(
        "全文采用 SI 单位：膜厚 μm、气压 kPa、粘度 s（KU）、温度 ℃、距离 mm",
        "雾化介质分无气、HVLP、静电喷涂分别标注，参数按各自定义书写",
        "干膜与湿膜厚度分别标注，换算须给出固含量",
        "样品命名体现“基材-前处理-涂层-参数组”四段式，全文一致",
        "对比试验须控制单一变量，报告组间差异与重复次数"
    ),
    key_venues=(
        "Journal of Coatings Technology and Research",
        "Progress in Organic Coatings",
        "Surface and Coatings Technology",
        "Thin Solid Films",
        "表面技术"
    ),
    units_and_formulas_notes=(
        "涂料粘度按 KU 值（s）报告并注明温度（如 23 ℃ / 28 s），换算注明溶剂类型",
        "膜厚以干膜计，单位 μm；均匀性以标准偏差或变异系数 CV = σ/μ × 100% 报告",
        "附着力按 ISO 2409 百格法报告等级（0-5 级）或 ISO 4624 拉拔力 MPa",
        "静电喷涂报告电压 kV 与转印率（%），注明工件接地方式"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Graco Magnum 无气喷涂机", "Wagner 静电喷涂机", "SATA 喷枪", "喷涂机器人 ABB", "静电喷粉房", "磷化喷淋前处理线", "喷砂房", "湿膜厚度仪", "BYK 旋转粘度计", "DeFelsko PosiTector 附着力拉拔仪", "膜厚测厚仪 Elcometer", "色差仪", "光泽度仪", "VOC 检测仪", "环境照度仪", "喷涂颗粒度测试筛", "FTIR 红外光谱仪", "烘干隧道炉", "环境温湿度记录仪", "Minitab"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
