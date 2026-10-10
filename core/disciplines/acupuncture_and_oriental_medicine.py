"""针灸与东方医学学科论文支持：TCSRT 报告规范、穴位定位与临床研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="acupuncture_and_oriental_medicine",
    aliases=(
        "acupuncture_and_oriental_medicine",
        "针灸与东方医学",
        "针灸学",
        "中医针灸",
        "东方医学",
        "传统东方医学",
        "Acupuncture",
        "Oriental Medicine",
        "Acupuncture Medicine",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、理论依据与研究目的）",
            "materials and methods（研究对象、穴位定位、干预方案、对照组设置、统计方法）",
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
            "treatment plan（辨证分析与治疗方案）",
            "outcome and follow-up",
            "discussion（理论解释与文献对照）",
            "references",
        ),
    },
    citation_style="APA 或 Vancouver 样式（中文期刊按《中国针灸》格式）",
    reporting_standards={
        "trial_design": "临床试验须报告研究设计类型（RCT/盲法/对照），并遵循 TCSRT 指南",
        "acupoint_localization": "穴位定位须引用国际标准 GB/T 12346，注明取穴方法",
        "intervention_detail": "干预描述须包含针刺深度、留针时间、刺激参数与操作者资质",
        "blinding": "盲法实施情况须明确说明（包括受试者盲、施针者盲、评估者盲）",
        "registration": "临床试验须注册于中国临床试验注册平台或 WHO ICTRP",
    },
    conventions=(
        "穴位名称使用国标编号（如 GB/T 12346）与国际通用名对照标注",
        "辨证论治过程须体现四诊信息（望闻问切），治疗方案与辨证结论之间逻辑自洽",
        "统计方法须明确报告主要终点、效应量与置信区间，非劣效试验须预先设定等效界值",
        "图片与图谱须标注体位、取穴侧别与测量参考线，比例尺不可省略",
    ),
    key_venues=(
        "Journal of Acupuncture and Meridiana Studies",
        "Acupuncture in Medicine",
        "Evidence-Based Complementary and Alternative Medicine",
        "Journal of Traditional Chinese Medicine",
        "中国针灸",
        "Complementary Therapies in Clinical Practice",
    ),
    units_and_formulas_notes=(
        "针刺深度以毫米（mm）为单位，留针时间以分钟（min）为单位",
        "电针仪参数须注明频率（Hz）、波形（疏密波/连续波）与强度（mA）",
        "疗效评价采用标准化量表（如 VAS、WHO 疼痛分级），须注明评分时间窗",
        "样本量计算须报告检验水平 α、检验效能 1-β 与预期效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("艾灸器具", "经穴模型", "红外热像仪", "表面肌电图仪", "电针仪", "脉冲电子针灸仪", "经穴定位仪", "生物反馈仪", "中医舌诊仪", "脉诊仪", "脑电图仪（EEG）", "SPSS", "RStudio", "RevMan（Cochrane）", "Stata", "3D 解剖学图谱软件", "MetaAnalyst", "JMP", "SAS", "EndNote"),
    category="医学",
    databases=("OpenAlex",),
)
