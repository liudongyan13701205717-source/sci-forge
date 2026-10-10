"""Dental hygiene 学科论文支持：牙科卫生/口腔卫生研究体裁、牙周健康规范与数字化口腔工具。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dental_hygiene",
    aliases=(
        "dental_hygiene", "牙科卫生", "口腔卫生", "牙周卫生",
        "dental hygienist", "oral hygiene", "periodontal care",
        "dental cleaning", "口腔保健", "oral health",
        "dental prophylaxis", "dental therapy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与口腔健康需求）",
            "methods（研究设计与临床方法）",
            "results（牙周/口腔健康数据）",
            "discussion（临床意义与推广价值）",
            "references",
        ),
        "clinical_report": (
            "abstract",
            "introduction",
            "case_description（案例描述）",
            "intervention（干预过程）",
            "outcome（治疗前后对比）",
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
        "periodontal": "牙周检查须使用标准化探诊深度（mm）与出血指数（BOP）报告",
        "plaque": "菌斑指数须注明评分方法（如OHI-S、Plaque Index、Visibility-Plaque Index）",
        "education": "患者教育内容须描述教育方式（面询/视频/书面）与频次",
        "comparison": "治疗前后对比须使用相同评估标准，报告时间间隔与样本量",
        "imaging": "影像学数据须注明拍摄体位、曝光参数与阅片者一致性检验",
    },
    conventions=(
        "牙周检查须使用标准化探诊深度（mm）与出血指数（BOP）报告",
        "菌斑指数须注明评分方法（如OHI-S、Plaque Index、Visibility-Plaque Index）",
        "患者教育内容须描述教育方式（面询/视频/书面）与频次",
        "治疗前后对比须使用相同评估标准，报告时间间隔与样本量",
        "影像学数据须注明拍摄体位、曝光参数与阅片者一致性检验",
    ),
    key_venues=(
        "Journal of Dental Hygiene",
        "Journal of Periodontology",
        "Journal of Clinical Periodontology",
        "Community Dentistry and Oral Epidemiology",
        "Journal of Dentistry",
        "International Dental Journal",
        "Journal of the American Dental Association",
        "Journal of Clinical Dentistry",
    ),
    units_and_formulas_notes=(
        "牙周探诊深度用 mm；出血指数用 %（BOP %）",
        "菌斑指数用 0-1 评分；OHI-S 用 0-10 评分",
        "龋失补指数 DMF-T 用 无量纲",
        "统计学显著性用 α=0.05；95% 置信区间须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CBCT (Cone Beam CT)", "Intraoral Scanner", "Digital Dental X-ray", "Dental CAD/CAM", "Exocad", "3Shape", "Cerec", "Opaqdent", "PerioScan", "ProExaminer", "Air Polisher", "Ultrasonic Scaler", "Oral Camera", "Dental Charting Software", "Smile Design Software", "Plaque Detection System", "Water Pik (oral irrigator)", "Digital Impression System", "Bitewing Radiography System", "Gingival Recession Analyzer"),
    category="医学",
    databases=("PubMed", "CNKI", "万方", "OpenAlex", "Crossref"),
)
