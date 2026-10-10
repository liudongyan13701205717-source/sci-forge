"""车辆机械学科论文支持：底盘与动力总成结构机构、维修工艺与量具量法规范的体裁、IEEE 引用样式与测量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vehicle_mechanics",
    aliases=(
        "vehicle_mechanics",
        "车辆机械",
        "汽车机械结构",
        "汽车底盘机构",
        "车辆机构原理",
        "vehicle structure",
        "suspension mechanics",
        "底盘机构"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（结构与性能问题）",
            "methods（结构分析、试验与测量方案）",
            "results（性能与强度结果）",
            "discussion（失效机理与改进讨论）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（车辆对象与故障现象）",
            "analysis（机构与运动分析过程）",
            "results（修复结果与复测数据）",
            "discussion（同类问题推广）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（机构类型与技术路线综述）",
            "evidence synthesis（试验与故障案例证据归纳）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（数字编号 [1]，配 GB/T 标准引用）",
    reporting_standards={
        "量具与精度": "所有尺寸测量须注明量具名称、量程、分辨率与检定有效期，结果保留有效数字至分辨率一位",
        "调整规范": "间隙、预紧与力矩调整须对照维修手册规定值，报告规定值、实测值与判定结论",
        "复测验证": "修复后须复测关键性能项（制动、定位、间隙）并与修复前对比",
        "安全判定": "涉及制动、转向与承载件的结论须给出安全裕度或标准依据（如 GB 21861、GB 17675）"
    },
    conventions=(
        "全文采用 SI 单位：长度 mm、角度 deg、力矩 N·m、压力 MPa、刚度 N/mm",
        "间隙与预紧按“项目 = 实测值 ± 允差 单位”格式给出，并标注冷态/热态",
        "定位参数按 GB/T 12672 定义书写（如 camber -0.5°、toe -0.2 mm/1000 mm）",
        "图件须标注测量基准面与测量方向，剖视图标明剖切位置",
        "术语中英对照在首次出现处标注，同一部件全文用同一名称"
    ),
    key_venues=(
        "International Journal of Automotive Technology",
        "SAE International Journal of Commercial Vehicles",
        "Vehicle System Dynamics",
        "Mechanics & Industry",
        "汽车技术"
    ),
    units_and_formulas_notes=(
        "悬架刚度按 k = F/Δx 给出，单位 N/mm；横向刚度与侧倾角报告单位分别为 N/mm 与 deg",
        "定位角报告注明测量条件（整备质量、轮胎气压、路面平整）与补偿方法",
        "摩擦系数为无量纲比值；制动拖滞率按 % 报告并标注车速",
        "测量不确定度按 U = k·u_c 给出，k 取包含因子并注明置信水平"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Hunter HawkEye 四轮定位仪", "Hunter 车轮动平衡机", "Bosch CTA 高压共轨试验台", "Bosch ECU Test", "Tektronix 示波器", "Fluke 万用表", "气缸压力测试仪", "点火正时灯", "燃油压力测试仪", "真空表", "数显扭矩扳手", "内径千分尺", "百分表", "工业内窥镜", "双柱举升机", "液压拉马", "整车制动台", "油液磁微粒检测仪", "Python (pandas)", "Origin"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
