"""Abseiling (leisure) 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="abseiling",
    aliases=(
        "Abseiling (leisure)",
        "下降运动",
        "Rappelling",
        "Sport Rappelling",
        "Rock Descending",
        "运动下降",
        "绳索下降",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA",
    reporting_standards={
        "uiua": "安全规程描述须遵循 UIAA 绳索下降安全标准",
        "nfpa": "绳索系统描述须标注 NFPA 1832 合规要求",
        "biomechanics": "运动生物力学数据须标注测量设备、采样率（Hz）与精度",
        "case_report": "伤害案例报告须遵循运动医学案例报告规范（CARE 声明）",
    },
    conventions=(
        "安全规程描述须遵循UIAA或NFPA绳索下降安全标准",
        "运动生物力学数据须标注测量设备与精度",
        "风险因素分析须包含环境条件、参与者技能水平与设备完整性",
        "案例报告须遵循运动医学报告规范",
    ),
    key_venues=(
        "Journal of Sports Sciences",
        "Sports Medicine",
        "Journal of Adventure Education and Outdoor Learning",
        "Outdoor Recreation",
        "Journal of Adventure Education",
        "Mountain Research and Application",
    ),
    units_and_formulas_notes=(
        "下降速度以米/秒（m/s）计量，绳索张力以千牛（kN）计量并标注测量传感器",
        "参与者体重以千克（kg）计量，安全系数以动载系数（ICF）报告（kN 值）",
        "高度测量以米（m）计量，误差须标注 GPS 或全站仪精度",
        "伤害发生率以每千次下降（per 1000 descents）计量，须注明观察窗口与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R", "SPSS", "JASP", "Stata", "Microsoft Excel", "EndNote", "NVivo", "Google Forms", "SurveyMonkey", "Qualtrics", "Adobe Premiere Pro", "Adobe Lightroom", "Canva", "Zoom", "Microsoft OneNote", "Tableau", "Microsoft Power BI", "Motion Analysis", "Kinovea", "Vicon Motion System"),
    category="教育学",
    databases=("OpenAlex",),
)
