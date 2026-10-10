"""影视制作学科论文支持：影史研究/纪录片批评/视听语言体裁、Chicago 引用样式与时间码记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sound_and_vision",
    aliases=("sound_and_vision", "影视制作", "Sound and Vision", "电影制作", "影视艺术", "视听媒介", "film production", "cinema", "影视技术"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="Chicago 手册样式（作者-年份或脚注尾注，视期刊而定）",
    reporting_standards={
        "screening_study": "报告观众规模、样本来源、问卷版本与作答时窗",
        "content_analysis": "编码本、双编码者一致性（κ）与随机片段时间须报告",
        "production_case": "设备型号、拍摄参数与制作周期须说明以达可复现粒度",
    },
    conventions=(
        "胶片/数字素材用帧率与分辨率联合标注（如 2.39:1 / 4K 24fps）",
        "时间码按 SMPTE 记法 HH:MM:SS:FF，全片统一 24fps 基准",
        "声画对位分析同时给出镜头时长、镜头序号与声音事件时点",
        "导演与制片人名用英文原名加中文通行译名，首次出现处并列",
        "引用电影片段时给出片名（年份）+ 时间码，非出版物给发行信息",
    ),
    key_venues=(
        "Journal of Film and Video",
        "Sight & Sound",
        "Cinema Journal",
        "Film History",
        "Journal of Audiovisual Media",
    ),
    units_and_formulas_notes=(
        "时长用 HH:MM:SS:FF（SMPTE 时间码），场记号用 scene/take/roll 三段式",
        "响度用 LUFS（ITU-R BS.1770，流媒体目标 −23 LUFS 立体声）",
        "画幅比标 1.85:1 / 2.39:1 / 1.33:1；色彩空间标 Rec.709 / DCI-P3",
        "分贝记 dBA（A 计权环境）与 dB SPL 分列，不得混用",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Adobe Premiere Pro", "DaVinci Resolve", "Avid Media Composer", "Adobe After Effects", "Pro Tools", "Nuendo", "Logic Pro X", "Final Cut Pro", "Blackmagic URSA Mini", "ARRI Alexa Mini", "Canon EOS R5 C", "Zoom F6 便携录音机", "Sennheiser MKH 416", "Shure MX418 无线麦克风", "Meyer Sound LEO 线阵系统", "Atem Mini 导播切换台", "Frame.io 审片平台", "FFmpeg", "Dalet Galaxy", "Adobe Prelude 素材管理"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
