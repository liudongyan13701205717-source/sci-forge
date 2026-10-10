"""精神科护理学科论文支持：护理实证/质性体裁、COREQ 报告规范与量表注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="psychiatric_nursing",
    aliases=(
        "psychiatric_nursing",
        "精神科护理",
        "精神护理",
        "Psychiatric nursing",
        "Mental health nursing",
        "心理护理",
        "精神卫生护理",
        "护理研究",
        "Nursing research",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与临床问题）",
            "methodology（研究设计与样本）",
            "results（量表与护理结果）",
            "discussion（护理启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（患者案例描述）",
            "analysis（护理过程分析）",
            "results（护理结局）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（护理理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；护理期刊亦可采用 Vancouver 样式）",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ 指南",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "rct": "随机对照试验遵循 CONSORT 声明",
        "quasi_experimental": "准实验遵循 STROBE 声明",
        "nursing_practice": "护理实践遵循 PICO 提问框架",
    },
    conventions=(
        "护理诊断、干预与结局须符合 NANDA-I/NIC/NOC 分类",
        "量表首次出现给出全称、条目数与评分范围",
        "伦理审批与知情同意须声明",
        "护理分级与风险评估须说明工具与阈值",
        "患者信息须去标识化",
    ),
    key_venues=(
        "International Journal of Mental Health Nursing",
        "Journal of Psychiatric and Mental Health Nursing",
        "Journal of Advanced Nursing",
        "Issues in Mental Health Nursing",
        "British Journal of Psychiatry",
    ),
    units_and_formulas_notes=(
        "量表分数无量纲，须报告均值 ± 标准差",
        "随访时间以周/月计",
        "护理指标须说明口径（如跌倒率 = 跌倒次数 / 护理人日）",
        "公式用 amsmath；信度与效度指标须报告",
        "样本量与流失率须说明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("NANDA-I", "NIC", "NOC", "Marsden Matrix", "BPRS", "HAMD", "HAMA", "PANSS", "SAS", "SDS", "NPI", "MNA-SF", "Cohen-Mansfield Agitation Inventory", "Electronic Health Record", "Cerner Millennium", "Epic", "SPSS", "R", "NVivo", "REFLECT"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
