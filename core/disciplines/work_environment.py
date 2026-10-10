"""工作环境学科论文支持：职业卫生与人因工程体裁、APA 引用样式与职业暴露记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="work_environment",
    aliases=("work environment", "工作环境", "职业环境", "工作场所环境", "职业卫生",
             "occupational environment", "workplace environment", "occupational hygiene"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与职业健康问题）",
            "methods（场所、暴露测量与分析）",
            "results（暴露水平与健康指标）",
            "discussion（暴露机理与防护意义）",
            "references",
        ),
        "exposure_assessment": (
            "abstract",
            "introduction",
            "methods（采样策略、仪器与分析）",
            "results（暴露浓度与分布）",
            "discussion（职业接触限值对比）",
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
    citation_style="APA 样式（作者-年份；Occupational and Environmental Medicine 多用 APA/Vancouver）",
    reporting_standards={
        "exposure_assessment": "暴露评估须报告采样方法、仪器与检出限",
        "occupational_hygiene": "职业卫生研究须报告接触限值（OEL/TWA）与合规判定",
        "epidemiology": "流行病学研究遵循 STROBE 声明",
        "statistical": "须报告样本量、统计方法与混杂控制",
    },
    conventions=(
        "暴露浓度须与职业接触限值（OEL）对比",
        "采样时间与方式（个体/区域）须明确",
        "噪声用 dB(A)、照度用 lx、温度用 °C 报告",
        "测量仪器型号与校准须交代",
        "暴露时段（TWA/STEL）须说明",
    ),
    key_venues=(
        "Occupational and Environmental Medicine",
        "Annals of Work Exposures and Health",
        "Journal of Occupational and Environmental Hygiene",
        "Applied Ergonomics",
        "Ergonomics",
        "International Archives of Occupational and Environmental Health",
    ),
    units_and_formulas_notes=(
        "噪声用 dB(A)；照度用 lx；温度用 °C",
        "暴露浓度用 mg/m³ 或 ppm；接触限值用 OEL-TWA",
        "热应激用 WBGT（°C）；通风用 m/s 或 m³/h",
        "振动用 m/s² (A8)；统计量给出均值与标准差",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("声级计 (sound level meter)", "噪声剂量计 (noise dosimeter)", "照度计 (lux meter)", "温湿度记录仪", "CO₂ 监测仪", "风速仪 (anemometer)", "WBGT 热指数仪", "VOC 空气质量检测仪", "振动测量仪 (vibration meter)", "RULA/REBA 人体工学评估软件", "ErgoMaster", "心率监测仪", "OSHA 合规工具", "SPSS", "R", "Python (pandas)", "Qualtrics", "NVivo", "Tableau", "Power BI"),
    category="管理学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI"),
)
