"""车辆制造与车身构造学科论文支持：冲压成形、车身焊接与数字化制造的体裁、SAE 引用样式与成形工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vehicle_building",
    aliases=(
        "vehicle_building",
        "车辆制造",
        "车身构造",
        "车辆设计与制造",
        "vehicle manufacturing",
        "body in white",
        "BIW",
        "冲压成形"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工艺瓶颈与问题定义）",
            "methods（工艺方案/工艺参数/仿真模型）",
            "results（成形质量、尺寸精度与试验对比）",
            "discussion（工艺窗口与机理讨论）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（车型/产线与工装条件）",
            "methods（工艺优化与测量方案）",
            "results（不良率、合格率与节拍指标）",
            "discussion（可复制性讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（成形/连接/轻量化路线综述）",
            "evidence synthesis（材料-工艺-结构证据归纳）",
            "future directions",
            "references",
        ),
    },
    citation_style="SAE 期刊样式（数字编号，作者-年份备选，含 DOI 与页码）",
    reporting_standards={
        "材料数据": "材料性能须注明状态（如 DC06/DP600/AA6016-O）、来源批号与试验标准（GB/T 228、ASTM E8）",
        "成形仿真": "有限元模型须报告网格尺寸、接触算法、摩擦系数与硬化律，成形结果与实测回弹量对比",
        "尺寸链": "尺寸公差报告须给出测量方法与量具（如三坐标、激光跟踪仪），结果按公差带与合格率统计",
        "焊接与连接": "连接工艺须声明参数窗口（点焊电流/时间、激光功率/速度）、接头力学试验方法与样本数"
    },
    conventions=(
        "全文采用 SI 单位：力 N/kN、应力 MPa、厚度 mm、温度 ℃、节拍 s/pcs",
        "材料牌号全文统一书写（如 DP600 不写作双相钢600），首次出现处标注抗拉强度与屈强比",
        "工艺参数以“参数名 = 数值 ± 公差 单位”格式给出，试验工况与量产工况分开列表",
        "图件按 CAD 出图习惯编号（图 1、图 2），剖视与展开图标注回弹补偿量",
        "统计结果给出样本量 n、均值与标准差，不良类型按 Pareto 排序"
    ),
    key_venues=(
        "Journal of Manufacturing Systems",
        "SAE International Journal of Materials and Manufacturing",
        "Manufacturing Technology",
        "International Journal of Automotive Technology",
        "汽车工程"
    ),
    units_and_formulas_notes=(
        "塑性变形抗力按 n 律 σ = K·ε^n 描述，K 与 n 须注明来源试验条件",
        "成形极限图（FLD）以主应变 ε1、ε2 坐标给出，标注材料厚度与回弹补偿后的实测点",
        "点焊工艺窗口以电流-时间坐标表示，焊核直径单位 mm，合格判定按 GB/T 1979",
        "节拍与 OEE 按 OEE = 可用率 × 性能 × 良率 计算，三项分别给出数值"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Hypermesh", "LS-DYNA", "AutoFORM-R", "Dynaform", "PAM-STAMP", "MARC", "NASTRAN", "ANSYS Explicit Dynamics", "SolidWorks", "CATIA V5", "Siemens NX", "CATIA Digital Manufacturing", "Teamcenter PLM", "GOM ATOS 三维激光扫描", "Zeiss Calypso", "Fanuc 机器人焊接工作站", "IPG 光纤激光焊", "电阻点焊控制器", "自动落料冲压线", "Minitab"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
