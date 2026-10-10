"""车辆内饰与装饰装配学科论文支持：软内饰材料、粘接铆接工艺与车内空气质量控制的体裁、SAE 引用样式与材料记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vehicle_trimming",
    aliases=(
        "vehicle_trimming",
        "车辆内饰",
        "车内装饰装配",
        "软内饰",
        "vehicle interior",
        "trim assembly",
        "软饰件",
        "内饰装配"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（材料/工艺问题）",
            "methods（材料选择、装配工艺与测试方案）",
            "results（外观、强度、老化与气味结果）",
            "discussion（机理与工艺窗口讨论）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（车型、饰件总成与装配线条件）",
            "methods（装配工艺与检验方案）",
            "results（不良率、节拍与合格率）",
            "discussion（可复制性与改进建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（内饰材料与装配路线综述）",
            "evidence synthesis（材料-工艺-性能证据归纳）",
            "future directions",
            "references",
        ),
    },
    citation_style="SAE 期刊样式（数字编号，附标准号与 DOI）",
    reporting_standards={
        "材料标识": "软饰件材料须标注基材、面饰、涂层与供应商牌号，注明厚度与密度",
        "连接工艺": "粘接报告胶种、涂胶量、固化条件与剥离强度；铆接报告铆钉规格与拉拔力",
        "环保与安全": "VOC、甲醛与气味按 GB/T 或 ISO 14319-1 报告浓度与分级，注明试验舱条件与暴露时长",
        "装配验证": "给出装配不良类型统计与检验标准，涉及防火件须按 GB 8410 报告燃烧等级"
    },
    conventions=(
        "全文采用 SI 单位：厚度 mm、密度 g/cm³、强度 MPa/kN/m、气味等级 1-5 级",
        "材料牌号全文统一书写，首次出现处标注关键性能（如 PVC 80 g/㎡）",
        "颜色与纹理以色卡/样件编号标注，色差以 ΔE* 报告",
        "工艺参数以“参数名 = 数值 ± 公差 单位”格式给出",
        "试验样品数量、取样位置与状态处理须说明，结果给出均值与标准差"
    ),
    key_venues=(
        "Automotive Engineering International",
        "SAE International Journal of Materials and Manufacturing",
        "Journal of Manufacturing Systems",
        "Journal of Automotive Engineering Materials and Processes",
        "塑料工业"
    ),
    units_and_formulas_notes=(
        "剥离强度按 ASTM D3163 报告，单位 kN/m，注明剥离角度（90°/180°）",
        "拉拔强度按 R = P/S 计算（P 为破坏力 N，S 为铆接面积 mm²），单位 MPa",
        "气味按 ISO 14319-1 在 50 ℃ 环境舱暴露后评分，报告浓度等级与判定阈值",
        "燃烧性能按 GB 8410 报告续燃/阴燃时间与烧穿面积，判定等级须与标准一致"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("注塑成型机", "真空吸塑成型机", "皮革压花机", "高频热合机", "超声波焊接机", "自动涂胶机", "工业缝纫机", "气动铆钉枪", "卡扣安装枪", "数显扭矩扳手", "色差仪", "甲醛检测仪", "气相色谱仪 (VOC)", "燃烧性能试验箱", "耐磨试验机", "耐黄变试验箱", "盐雾试验箱", "环境舱 (ISO 14319)", "Minitab", "Python (pandas)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
