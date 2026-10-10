"""木工与木匠学科论文支持：建筑木作与细木工体裁、APA 引用样式与木作记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="woodworking_and_carpentry",
    aliases=("woodworking and carpentry", "木工与木匠", "木作", "木匠工艺", "建筑木工",
             "carpentry", "woodworking", "timber framing"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与建造问题）",
            "materials and methods（材料、工具与工序）",
            "results（质量、精度与结构性能）",
            "discussion（建造机理与应用）",
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
    citation_style="APA 样式（作者-年份；建造与木材期刊多用 APA）",
    reporting_standards={
        "process_documentation": "工艺研究须报告设备、参数与工序步骤",
        "structural": "结构木作须报告载荷、连接方式与安全系数",
        "quality_control": "质量控制须报告公差、检验方法与抽样方案",
        "safety": "须报告木尘防护与高空作业安全措施",
    },
    conventions=(
        "木材树种、等级与含水率须注明",
        "连接方式（榫卯/钉/螺栓/金属连接件）须明确",
        "尺寸公差用 mm 并说明基准",
        "结构构件须标注截面尺寸与跨度",
        "安全防护措施须交代",
    ),
    key_venues=(
        "Forest Products Journal",
        "BioResources",
        "Construction and Building Materials",
        "European Journal of Wood and Wood Products",
        "Journal of Wood Science",
        "Engineering Structures",
    ),
    units_and_formulas_notes=(
        "尺寸用 mm/cm；跨度用 m",
        "含水率用 %；密度用 kg/m³",
        "强度用 MPa；载荷用 kN",
        "公差用 ±mm；角度用 °",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("台锯 (table saw)", "带锯机 (band saw)", "斜切锯 (miter saw)", "电刨 (power planer)", "铣机 (router)", "电钻/起子 (power drill)", "砂光机 (sander)", "榫机 (mortiser)", "气钉枪 (nail gun)", "CNC 雕刻机", "木工车床 (wood lathe)", "手持圆锯 (circular saw)", "激光测距仪", "激光水平仪 (laser level)", "含水率测定仪", "AutoCAD", "SketchUp", "Fusion 360", "木工夹具 (clamps)", "除尘系统 (dust collection)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
