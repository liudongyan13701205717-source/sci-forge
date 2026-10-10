"""Dental assisting 学科论文支持：牙科助理/牙科辅助研究体裁、口腔数字化规范与牙科工具。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dental_assisting",
    aliases=(
        "dental_assisting", "牙科助理", "牙科辅助", "牙科助手",
        "dental assistant", "dental auxiliaries", "dental technician",
        "dental support", "口腔助理", "dental care support",
        "oral health assistant", "dental nursing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与临床需求）",
            "methods（研究设计与临床方法）",
            "results（治疗效果与患者数据）",
            "discussion（临床意义与推广价值）",
            "references",
        ),
        "clinical_report": (
            "abstract",
            "introduction",
            "case_description（案例描述）",
            "treatment（治疗过程）",
            "outcome（治疗效果）",
            "references",
        ),
        "training": (
            "abstract",
            "introduction",
            "curriculum（课程设计与教学目标）",
            "competency（能力标准与考核）",
            "evaluation（教学效果评估）",
            "references",
        ),
    },
    citation_style="Vancouver 样式（数字编号）",
    reporting_standards={
        "instruments": "操作描述须注明使用器械型号与操作参数（转速、角度、时长）",
        "ethics": "患者信息须匿名化处理；案例报告须附知情同意声明",
        "imaging": "影像学检查须注明拍摄体位、曝光参数与成像设备型号",
        "outcome": "治疗效果评估须使用标准化指标（如DMF-T、龋失补指数）",
        "comparison": "对比研究须报告样本量、纳入/排除标准与统计方法",
    },
    conventions=(
        "操作描述须注明使用器械型号与操作参数（转速、角度、时长）",
        "患者信息须匿名化处理；案例报告须附知情同意声明",
        "影像学检查须注明拍摄体位、曝光参数与成像设备型号",
        "治疗效果评估须使用标准化指标（如Caries-Free Years、龋失补指数DMF-T）",
        "对比研究须报告样本量、纳入/排除标准与统计方法",
    ),
    key_venues=(
        "Journal of Dental Education",
        "Journal of the American Dental Association",
        "Community Dentistry and Oral Epidemiology",
        "Journal of Clinical Dentistry",
        "International Dental Journal",
        "Journal of Dental Hygiene",
        "Clinical Oral Implants Research",
        "Journal of Esthetic and Restorative Dentistry",
    ),
    units_and_formulas_notes=(
        "牙科X射线曝光参数用 kVp、mA、s",
        "器械转速用 rpm；角度用 °（度）",
        "龋失补指数 DMF-T 用 无量纲（tooth surface）",
        "统计显著性用 α=0.05；95% 置信区间须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CBCT (Cone Beam CT)", "Intraoral Scanner", "Dental CAD/CAM", "Exocad", "3Shape", "Cerec", "Digital Dental X-ray", "Open Dental", "Dentrix", "Eaglesoft", "Dental 3D Printer", "Digital Impression System", "Ultrasonic Scaler", "Air Polisher", "Light Curing Unit", "Dental Handpiece", "Endodontic Motor", "Dental Laser", "Dental Compressor", "Bite Registration System"),
    category="医学",
    databases=("PubMed", "CNKI", "万方", "OpenAlex", "Crossref"),
)
