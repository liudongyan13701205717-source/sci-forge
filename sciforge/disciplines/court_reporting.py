"""法庭记录学科论文支持：法律记录/司法速记/法庭语言处理体裁、法律引用样式与专业记录约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="court_reporting",
    aliases=(
        "法庭记录", "庭审速记", "司法记录", "Court reporting",
        "Court Reporting", "Judicial Reporting", "Verbatim Reporting",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
        "case_analysis": (
            "案件背景",
            "庭审过程记录",
            "记录分析",
            "语言特征分析",
            "结论",
        ),
        "methodology": (
            "方法论概述",
            "记录标准",
            "转录流程",
            "质量保证",
            "参考文献",
        ),
    },
    citation_style="Bluebook 法律引用样式",
    reporting_standards={
        "transcription_accuracy": "转录须逐字准确，保留发言顺序",
        "time_stamps": "关键语句须标注时间戳",
        "redaction": "涉及隐私信息须按规定脱敏处理",
        "certification": "正式记录须由认证法庭记录员签署",
    },
    conventions=(
        "法庭用语使用法律标准术语，首次出现附英文对照",
        "发言顺序按时间顺序标注，发言者标注角色",
        "专业术语首次出现时给出法律定义",
        "记录格式遵循 RIR 标准（Recording Information Requirements）",
        "引用法庭记录须注明案号、日期与法官",
    ),
    key_venues=(
        "Legal Communication",
        "Journal of the American Court Reporting Society",
        "Court Reporter (ACRS Quarterly)",
        "Forensic Linguistics: International Journal",
        "Journal of Law and Courts",
        "中国法学",
    ),
    units_and_formulas_notes=(
        "时间戳使用 HH:MM:SS 格式",
        "记录精度按逐字（verbatim）或大意（gist）标注",
        "字符数与词数按标准计数方法统计",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Dragon Medical One（语音识别软件）", "Nuance Communications（语音转写平台）", "Otter.ai（实时转录）", "Rev（法庭记录服务）", "Sonus（速记键盘）", "StenoPad（法庭速记设备）", "Courtlink（法庭记录系统）", "iLinking（法庭技术集成）", "WebEx（远程庭审平台）", "Zoom for Government（法庭远程会议）", "Microsoft Teams（法庭记录协作）", "SPSS", "R（统计与文本分析）", "NVivo（质性文本分析）", "ATLAS.ti", "AntConc（文本分析工具）", "Taguhi（法庭记录软件）", "CourtCase（法庭案件管理系统）", "Luminex（法庭录音系统）", "Verbit（庭审录音转写）"),
    category="法学",
    databases=("LexisNexis", "Westlaw", "HeinOnline", "Scopus", "中国裁判文书网", "LexisNexis（法律数据库）", "Westlaw（法律数据库）"),
)
