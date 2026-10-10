"""假体技术学科论文支持：康复工程体裁、CONSORT 报告规范与生物力学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="prosthetic_technology",
    aliases=(
        "prosthetic_technology",
        "假体技术",
        "假肢技术",
        "Prosthetics",
        "义肢",
        "假肢与矫形器",
        "康复工程",
        "康复辅具",
        "Rehabilitation engineering",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（临床需求）",
            "methodology（设计与方法）",
            "results（生物力学结果）",
            "discussion（临床意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（患者案例描述）",
            "analysis（适配与分析）",
            "results（功能结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（假体学综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；医学期刊亦可采用 Vancouver 样式）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "device_evaluation": "设备评估遵循 ISO 13482 报告规范",
        "biomechanical": "生物力学研究遵循 STARD-Extension 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "残肢形态与解剖学标记须图示说明",
        "生物力学量须给出单位（N、Nm、m/s）",
        "假肢-残肢界面力学须报告峰值与均值",
        "材料与加工工艺须完整披露",
        "临床试验须有伦理审批与知情同意",
    ),
    key_venues=(
        "Journal of Rehabilitation Research and Development",
        "Prosthetics and Orthotics International",
        "Journal of Prosthetics and Orthotics",
        "Gait & Posture",
        "IEEE Transactions on Neural Systems and Rehabilitation Engineering",
        "IEEE Transactions on Biomedical Engineering",
    ),
    units_and_formulas_notes=(
        "力以牛顿（N）计，力矩以牛米（Nm）计",
        "速度与加速度以 m/s、m/s² 计",
        "能量代谢率以 %MET 或 W/kg 报告",
        "公式用 amsmath；刚度与阻尼定义式须明确",
        "步态相位以百分比步态周期标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Geomagic", "3D Systems Design", "Zeiss GOM Inspect", "Artec 3D", "Shining 3D", "Formlabs Form", "Ultimaker", "Stratasys", "Zeiss Contura", "BTS Innovations", "Delsys Trigno", "Xsens MVN", "Vicon", "OptiTrack", "AMTI Force Plate", "Zebris Z-Med", "Kinesiology", "MATLAB", "OpenSim", "AnyBody"),
    category="工学",
    databases=("OpenAlex", "Crossref", "PubMed", "CNKI"),
)
