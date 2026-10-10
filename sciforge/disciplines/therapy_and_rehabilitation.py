"""康复治疗学科论文支持：物理治疗、作业治疗与言语治疗干预研究体裁、Vancouver 引用样式与量表评分注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="therapy_and_rehabilitation",
    aliases=(
        "therapy_and_rehabilitation",
        "Therapy and rehabilitation",
        "康复治疗",
        "物理治疗",
        "作业治疗",
        "言语治疗",
        "Rehabilitation medicine",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（临床背景与研究问题）",
            "methods（设计、参与者、干预、评估工具与统计）",
            "results",
            "discussion（临床意义与局限）",
            "conclusions",
            "references",
        ),
        "clinical_report": (
            "abstract",
            "introduction",
            "case presentation（临床病史与主诉）",
            "intervention（治疗方案）",
            "outcome（随访与结局）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "search strategy（检索策略）",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver 样式（编号引用，医学领域常用）",
    reporting_standards={
        "trial": "随机对照试验遵循 CONSORT 声明",
        "diagnostic": "诊断试验/量表研究遵循 STARD 声明",
        "review": "系统综述遵循 PRISMA 声明",
        "case": "病例报告遵循 CARE 指南",
        "register": "临床试验须在注册平台登记并给出注册号",
    },
    conventions=(
        "评估量表须注明版本与常模来源，报告评分范围与切分值",
        "疗效指标须报告最小临床重要差异（MCID）",
        "样本量须报告估算依据（效应量与检验效能）",
        "缺失数据与失访须说明处理方式",
        "统计结果报告点估计与 95% 置信区间",
    ),
    key_venues=(
        "Journal of Physical Therapy Science",
        "Archives of Physical Medicine and Rehabilitation",
        "British Journal of Occupational Therapy",
        "Journal of Speech, Language, and Hearing Research",
        "中国康复医学杂志",
    ),
    units_and_formulas_notes=(
        "肌力用 MMT 分级（0-5）或牛顿·米（N·m）",
        "关节活动度用角度（°）",
        "疼痛用 VAS/NRS（0-10）",
        "随访时间用周（week）或月（month），终点须明确",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("OpenSIM", "Vicon Motion Systems", "Kinescope（Delsys EMG）", "Biodex 等速测力台", "NORAX 平衡仪", "Fugl-Meyer 评估量表", "6 分钟步行测试", "MyTrace 步态分析", "MATLAB", "Python (NumPy, SciPy)", "R", "SPSS", "Stata", "GraphPad Prism", "JMP", "EndNote", "Zotero", "RayBan 肌电/运动捕捉集线器", "3D 打印机（助具定制）", "虚拟现实康复系统"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI"),
)
