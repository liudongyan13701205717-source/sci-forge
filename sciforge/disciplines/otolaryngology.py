"""耳鼻喉科学学科论文支持：耳科、鼻科、喉科疾病诊治与听觉科学临床-基础研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="otolaryngology",
    aliases=("Otolaryngology", "耳鼻喉科学", "ENT", "Otorhinolaryngology", "Audiology", "Otology", "Rhinology", "Laryngology"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={
        "k1": "听力评估遵循ISO 8253纯音听力图报告格式", "k2": "临床试验遵循CONSORT报告规范", "k3": "观察/队列研究遵循STROBE报告规范"
    },
    conventions=("使用ICD-11编码与ENT术语（如鼓膜穿孔、听力损失分级）", "影像报告须注明体位、切面、增强剂与测量方法", "手术描述须遵循术式规范化命名（如乳突根治术类型）", "听觉评估须报告测试频率范围、声场条件与设备型号", "儿童ENT研究须符合儿科伦理与父母知情同意要求"),
    key_venues=("European Archives of Oto-Rhino-Laryngology", "Laryngoscope", "Journal Of The American Academy Of Otolaryngology-Head And Neck Surgery", "American Journal Of Otolaryngology", "Clinical & Experimental Otolaryngology", "Journal of Laryngology and Otology"),
    units_and_formulas_notes=("纯音听力测试：频率dB HL、声级校准遵循ISO 389标准", "鼓室图报告须给出压力范围(kPa)、声阻抗与容积(cc H2O)", "嗓音评估使用基频(Hz)、微扰(%jitter/%shimmer)参数", "影像报告须标明解剖体位、切面方向与测量单位(mm)"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Pure Tone Audiometer", "Tympanometer", "OAE Analyzer", "ABR Instrument", "Videoendoscope", "Stroboscope", "Acoustic Meatal Thermometer", "Sinus CT Scanner", "MR Imaging System", "Otoacoustic Emissions System", "Speech Sound Analysis Software", "Praat", "LabChart", "BioSig", "SPSS", "R", "Stata", "SAS", "RevMan", "Impedance Audiometer"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "PubMed"),
)
