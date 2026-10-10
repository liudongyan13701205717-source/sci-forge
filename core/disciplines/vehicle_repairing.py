"""车辆修理学科论文支持：故障判故、车身与总成交换修复、维修质量与成本控制的体裁、SAE 引用样式与维修规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vehicle_repairing",
    aliases=(
        "vehicle_repairing",
        "车辆修理",
        "汽车维修",
        "整车故障修复",
        "车辆检修",
        "vehicle repair",
        "automotive repair",
        "body repair"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（修理难题与目标）",
            "methods（诊断流程、修复方案与评价方法）",
            "results（修复前后对比数据）",
            "discussion（机理、可靠性与成本讨论）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（车辆履历、故障现象与检测数据）",
            "analysis（诊断与定位过程）",
            "results（修复实施与复测结论）",
            "discussion（经验总结与预防建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（修理技术与标准体系综述）",
            "evidence synthesis（案例与数据归纳）",
            "future directions",
            "references",
        ),
    },
    citation_style="SAE 期刊样式（数字编号，含标准号与 DOI）",
    reporting_standards={
        "故障描述": "按“现象-条件-频度”三段式记录故障，明确可复现条件与已排除项",
        "维修过程": "记录拆装顺序、扭矩规格、更换件来源与旧件状态，关键步骤附照片或波形",
        "验证闭环": "修复后须完成静态检查、路试与故障码清除验证，报告观察时长或里程",
        "质量追溯": "给出工时、备件成本与返修判定依据，涉及安全件须保留检验记录"
    },
    conventions=(
        "全文采用 SI 单位：力矩 N·m、温度 ℃、压力 MPa、长度 mm、时间 s/min",
        "故障码按标准格式书写（如 P0171、C0040），并注明协议（OBD-II/J1939）",
        "扭矩与间隙规格注明冷态/热态与润滑状态（干/涂油）",
        "案例论文须隐去车主个人信息，车辆信息以车型年款/底盘号后四位表示",
        "结论须区分“已验证修复”与“待观察”，并给出建议复检里程"
    ),
    key_venues=(
        "SAE International Journal of Commercial Vehicles",
        "International Journal of Automotive Technology",
        "Vehicle System Dynamics",
        "Mechanical Systems and Signal Processing",
        "汽车实用技术"
    ),
    units_and_formulas_notes=(
        "维修工时按标准工时（min）与实耗工时分别记录，效率 = 标准工时/实耗工时",
        "返修率按 返修次数/维修次数 × 100% 报告，并标注统计周期",
        "制动检验按 GB 21861 报告制动力与制动力平衡率（%），并给出判定点",
        "成本核算区分工时费、备件费与外协费，货币单位统一为元"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Autel MaxiSys", "Launch X431", "Snap-on Verus", "Bosch ECU Test", "Delphi DOS-4S", "Vector CANoe", "Tektronix 示波器", "Fluke 万用表", "整车制动台", "Hunter HawkEye 四轮定位仪", "车身大框架校正仪", "激光测量仪", "双柱举升机", "液压拉马", "工业内窥镜", "数显扭矩扳手", "百分表", "OBDLink EX2", "Python (pandas)", "Weibull++ Reliability"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
