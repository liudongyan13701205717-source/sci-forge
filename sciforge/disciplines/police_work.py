"""警务工作论文支持：刑事侦查、现场勘查、犯罪分析与执法实务研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="police_work",
    aliases=("police_work", "警务工作", "警察工作", "Police Work", "刑事侦查", "Criminal Investigation", "现场勘查", "Crime Scene Investigation", "侦查学", "Investigation"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"UCR/NIBRS": "犯罪报告统一分类标准", "ASTM E1412": "指纹记录报告规范", "ISO/IEC 17025": "检测和校准实验室能力认可"},
    conventions=("犯罪类别用 UCR/NIBRS 标准分类", "证据链完整性须记录并保全", "受害者信息须匿名化处理", "敏感数据须伦理审查声明", "统计须报告置信区间与效应量"),
    key_venues=("Policing: A Journal of Policy and Practice", "Journal of Criminal Justice", "Policing: Practice and Research", "中国人民公安大学学报", "公安学研究"),
    units_and_formulas_notes=("犯罪率用 per 100,000 population", "再犯率用 %", "时间序列用月/年数据", "空间分析须注明分析单元"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("AXON Body 3", "Digital Video Recorder", "ACE-VEK Fingerprint Kit", "QIAGEN DNA Extraction Kit", "Canon EOS-1D X", "Crime Scene Mapping Software", "Gunshot Residue Kit", "Latent Print Powder", "UV Light", "Body Composition Analyzer", "Stata", "R", "SPSS", "NVivo", "QGIS", "CrimeStat", "PredPol Analytic", "Tableau", "Python", "Microsoft Excel"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "SSRN", "ICPSR"),
)