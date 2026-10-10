"""木工行业学科论文支持：木制品制造与装配工艺体裁、APA 引用样式与木工记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="woodwork_trades",
    aliases=("woodwork trades", "木工行业", "木工", "木制品制造", "木作工艺",
             "woodworking trade", "joinery", "cabinetmaking"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与工艺问题）",
            "materials and methods（材料、设备与工序）",
            "results（质量、精度与效率数据）",
            "discussion（工艺机理与应用）",
            "references",
        ),
        "process_study": (
            "abstract",
            "introduction",
            "materials and methods（工序、设备与参数）",
            "results（质量与效率数据）",
            "discussion（工艺优化建议）",
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
    citation_style="APA 样式（作者-年份；制造与职业期刊多用 APA）",
    reporting_standards={
        "process_documentation": "工艺研究须报告设备、参数与工序步骤",
        "quality_control": "质量控制须报告公差、检验方法与抽样方案",
        "material_testing": "材料测试须报告标准、试样与条件",
        "safety": "须报告木尘防护与职业安全措施",
    },
    conventions=(
        "木材树种与含水率须注明",
        "接合方式（榫卯/五金/胶合）须明确",
        "尺寸公差用 mm 并说明基准",
        "设备与刀具参数须量化",
        "安全防护（除尘/护具）须交代",
    ),
    key_venues=(
        "Forest Products Journal",
        "BioResources",
        "European Journal of Wood and Wood Products",
        "Journal of Wood Science",
        "Wood Science and Technology",
        "International Journal of Industrial Ergonomics",
    ),
    units_and_formulas_notes=(
        "尺寸用 mm/cm；公差用 ±mm",
        "含水率用 %；密度用 kg/m³",
        "转速用 rpm；进给用 m/min",
        "结合强度用 MPa；胶合参数（压力/温度）须注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("台锯 (table saw)", "带锯机 (band saw)", "圆锯 (circular saw)", "电刨 (power planer)", "电钻 (power drill)", "铣机 (router)", "砂光机 (sander)", "榫机 (mortiser)", "CNC 雕刻机", "木工车床 (wood lathe)", "气钉枪 (nail gun)", "木工夹具 (clamps)", "激光测距仪", "含水率测定仪", "AutoCAD", "SketchUp", "Fusion 360", "除尘系统 (dust collection)", "木工接合器 (domino joiner)", "磨刀设备 (sharpening system)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
