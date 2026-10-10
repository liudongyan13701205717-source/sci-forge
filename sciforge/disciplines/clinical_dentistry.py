"""Clinical Dentistry 学科论文支持：临床牙科/口腔医学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="clinical_dentistry",
    aliases=(
        "Clinical Dentistry", "临床牙科", "Dentistry", "牙科",
        "Oral Medicine", "口腔医学", "Oral Health", "口腔健康",
        "Dental Medicine",
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
    citation_style="Vancouver Style",
    reporting_standards={
        "ada_guidelines": "临床研究须遵循 ADA（美国牙科协会）报告规范",
        "consort": "随机对照试验遵循 CONSORT 报告规范",
        "radiation_protection": "放射学检查须声明有效剂量并遵循 ALARA 原则",
    },
    conventions=(
        "使用牙科标准（FDI 牙位、Zubler、Universal）",
        "引用牙科放射学时给出辐射剂量（ALARA 原则）",
        "引用牙体/牙髓治疗时使用 ADA、AAFP、AAPD 分类",
        "使用 CBCT 影像时给出有效剂量与 FOV",
        "报告应遵循 SDR/IDRA 与 AOM 规范",
    ),
    key_venues=(
        "Journal of Dentistry",
        "Journal of Dental Research",
        "Journal of Periodontology",
        "Clinical Oral Implants Research",
        "International Journal of Oral and Maxillofacial Implants",
        "Journal of Prosthetic Dentistry",
        "Community Dentistry and Oral Epidemiology",
        "Journal of Clinical Dentistry",
    ),
    units_and_formulas_notes=(
        "牙位使用 FDI 两位数记法（如 11 为上颌中切牙），须注明体系",
        "CBCT 有效剂量以 μSv 报告，须注明 FOV 与电压",
        "牙周探针深度以 mm 计，附出血指数与临床附着丧失值",
        "统计报告须附检验方法、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CBCT (Cone Beam Computed Tomography)", "iTero (Intraoral Scanner)", "CEREC", "3Shape", "exocad", "Dental Wings", "ProPlan CMF", "Planmeca Romexis", "BlueSky Implant", "Trios", "3M SpeedPro", "DentalCAD", "Digital X-ray Sensor (RVG)", "Intraoral Camera", "EMS Air Flow Polishing", "EMS Piezoelectric Ultrasonic Scaler", "Endodontic Rotary Instrument", "Dental Laser (Er,Cr:YSGG)", "iTero Element 5D", "Planmeca ProMax"),
    category="医学",
    databases=("OpenAlex", "PubMed", "Crossref"),
)
