"""妇科学学科论文支持：生殖健康、宫颈筛查与腔镜手术的临床研究设计与报告规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="gynaecology",
    aliases=("gynaecology", "妇科学", "妇科", "gynecology", "生殖健康", "reproductive health", "宫颈筛查", "cervical screening", "腔镜手术"),
    paper_types={
        "research": ("abstract", "introduction（临床问题与研究假设）", "methodology（人群、设计、干预与终点）", "results（疗效、安全性与随访）", "discussion（与既往证据的比较）", "references"),
        "case_study": ("abstract", "introduction", "case description（病史、检查与体征）", "analysis（诊断思路与鉴别诊断）", "results（手术与治疗经过）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（生殖与宫颈病变机制）", "evidence synthesis（指南与系统评价综合）", "future directions", "references"),
    },
    citation_style="Vancouver (ICMJE) 样式",
    reporting_standards={"CONSORT": "随机对照试验按 CONSORT 2010 清单报告", "STROBE": "观察性研究按 STROBE 清单报告", "TRIPOD": "诊断或预测模型按 TRIPOD 清单报告"},
    conventions=("诊断按 ICD-10 与 FIGO 分期标注", "年龄与生殖史（孕产次、绝经状态）须报告", "用药报告药名、剂量、途径与疗程", "随访时长与失访比例须给出", "统计学用双尾检验，p 值保留 3 位有效数字"),
    key_venues=("American Journal of Obstetrics and Gynecology", "Human Reproduction", "Cancer", "BJOG: An International Journal of Obstetrics and Gynaecology", "中华妇产科杂志"),
    units_and_formulas_notes=("剂量用 mg 或 μg；浓度按 pg/mL 与 IU/mL 分别标注", "时间以 d、wk、月报告并说明起算点", "影像学测量以 mm 报告，并注明超声测量切面", "统计学用均值 ± 标准差；OR 或 HR 附 95% CI；公式用 LaTeX（amsmath）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Karl Storz", "Olympus EndoVision", "Kotter", "Collins & Brown", "Cusco Speculum", "Hologic LEEP", "Medtronic LigaSure", "GE Voluson E10", "Philips EPIQ", "Meditech Urodyne", "BD Cervista", "Roche cobas HPV 2", "BD SurePath", "Storz Colposcope", "Medicheck CryoPen", "Hegar Dilator", "Leica TCS SP8", "Zeiss Axio Observer.Z1", "Thermo Fisher QIAcube", "Beckman Coulter CytoDx"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
