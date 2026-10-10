"""广播电视制作学科论文支持：节目策划、摄像制作与新媒体传播。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="radio_and_tv_production",
    aliases=("radio_and_tv_production", "广播电视制作", "radio and television production", "媒体制作", "media production", "电视制作", "广播制作", "广播影视", "影视制作"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="MLA 9",
    reporting_standards={"k1": "国家广播电视总局播出规范", "k2": "GB/T 19759 数字媒体制作规范", "k3": "EBU R128 音频响度标准"},
    conventions=("节目脚本采用标准电视剧本格式", "技术参数须列出分辨率与帧率", "音频响度以 LUFS 单位报告", "图表须列出时间码与时长", "参考文献按 MLA 9 著录"),
    key_venues=("Journal of Broadcasting & Electronic Media", "New Media & Society", "Journal of Media & Cultural Studies", "Screening the Past", "中国电视学刊"),
    units_and_formulas_notes=("音频响度使用 LUFS 与 dBFS", "视频分辨率使用 1920×1080 与 3840×2160", "帧率使用 fps（frames per second）", "时长使用秒（s）与毫秒（ms）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Avid Media Composer", "Adobe Premiere Pro", "Adobe After Effects", "Adobe Audition", "DaVinci Resolve", "Final Cut Pro", "Pro Tools", "Ableton Live", "Logic Pro X", "Blackmagic HyperDeck Studio", "Blackmagic Pocket Camera", "Sony Cinema Line Camera", "RED Digital Cinema Camera", "ARRI Lighting System", "Teleprompter Software", "OBS Studio", "vMix", "Wirecast", "NDI NewTek", "DJI Ronin Gimbal"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
