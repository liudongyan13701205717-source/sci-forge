"""传统与补充医学及疗法学科论文支持：整全医学/补充替代疗法临床体裁、CONSORT/STROBE/PRISMA 与器械参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="traditional_and_complementary_medicine_and_therapy",
    aliases=("traditional_and_complementary_medicine_and_therapy", "传统与补充医学及疗法",
             "传统补充医学疗法", "补充与替代医学", "整全医学",
             "complementary and alternative medicine", "CAM", "integrative medicine"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、理论依据与研究目的）",
            "methods（研究对象、干预方案、对照组设置、统计方法）",
            "results（主要终点与次要终点结果）",
            "discussion（结果解释、与既有研究比较、局限性）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "search strategy and inclusion criteria",
            "results（纳入研究特征与合并结果）",
            "discussion（证据质量评估与不确定性）",
            "conclusion",
            "references",
        ),
        "case_report": (
            "abstract",
            "case presentation（患者基本信息、主诉与现病史）",
            "treatment plan（治疗方案与依据）",
            "outcome and follow-up",
            "discussion",
            "references",
        ),
    },
    citation_style="APA 或 Vancouver 样式",
    reporting_standards={
        "trial_design": "临床试验须报告设计类型（RCT/盲法/对照），遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "intervention_detail": "干预描述须包含频次、时长、操作者与患者资质",
        "safety": "不良事件须按 MedDRA 术语报告",
    },
    conventions=(
        "干预名称须注明流派、操作者与疗程，避免笼统表述",
        "统计学方法须报告主要终点、效应量与置信区间",
        "安全性评价须报告不良事件分级与处理措施",
        "比较研究须说明对照组类型（安慰剂、假干预或常规治疗）",
        "图片须标注体位与测量参考线",
    ),
    key_venues=(
        "Journal of Integrative Medicine",
        "BMJ Evidence-Based Complementary and Alternative Medicine",
        "Complementary Therapies in Clinical Practice",
        "Evidence-Based Complementary and Alternative Medicine",
        "Frontiers in Public Health",
        "中国中西医结合杂志",
    ),
    units_and_formulas_notes=(
        "干预时长以分钟（min）为单位，频次以次/周为单位",
        "电刺激参数须注明频率（Hz）、波形与强度（mA）",
        "疗效评价采用标准化量表（如 VAS、WHO 分级），须注明评分时间窗",
        "样本量计算须报告检验水平 α、效能 1-β 与预期效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("红外热像仪", "表面肌电图仪", "生物反馈仪", "经皮神经电刺激仪", "经颅磁刺激仪", "经颅直流电刺激仪", "心率变异性分析仪", "皮肤电反应仪", "体成分分析仪", "骨密度仪（DXA）", "激光多普勒血流仪", "电针仪", "艾灸器具", "SPSS", "R", "RevMan（Cochrane）", "Stata", "MedCalc", "Prism 9", "NVivo"),
    category="医学",
    databases=("PubMed", "CNKI", "OpenAlex", "万方", "Cochrane Library"),
)
