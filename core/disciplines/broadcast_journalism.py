"""广播新闻学科论文支持：新闻学/传播学体裁、新闻学引用样式与新闻记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="broadcast_journalism",
    aliases=(
        "broadcast_journalism",
        "Broadcast journalism",
        "广播新闻",
        "广播电视新闻",
        "广播与电视新闻",
        "电视新闻",
        "新闻学",
        "新闻传播",
        "broadcast news",
        "broadcasting",
        "新闻与传播",
        "journalism",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（样本、方法、伦理审查）",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "case": (
            "abstract",
            "introduction",
            "case description",
            "analysis",
            "discussion",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7（新闻学引用样式）",
    reporting_standards={
        "sample": "样本、数据来源须明确",
        "method": "方法（内容分析、采访、实验）须完整",
        "ethics": "伦理审查须符合 IRB 或大学伦理委员会",
        "reproducibility": "数据与代码须可获取",
    },
    conventions=(
        "新闻来源用中文术语（如'消息源'、'采访对象'、'权威人士'）",
        "时间用 ISO 8601 格式（YYYY-MM-DD）",
        "引用新闻源时须注明媒体名称、日期、记者",
        "采访记录须符合新闻伦理（匿名、化名、录音授权）",
        "新闻标题用中文或英文，全文一致",
    ),
    key_venues=(
        "Journalism",
        "Journalism and Communication",
        "Journalism Quarterly",
        "International Journal of Journalism",
        "Critical Studies in Television, Film and Media",
        "Television and New Media",
        "New Media & Society",
        "Journal of Communication",
    ),
    units_and_formulas_notes=(
        "时间用 ISO 8601 格式（YYYY-MM-DD）",
        "引用新闻源时须注明媒体名称、日期、记者",
        "采访记录须符合新闻伦理",
        "样本量 n 须明确",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Avid Media Composer", "Adobe Premiere Pro", "Final Cut Pro", "DaVinci Resolve", "Sony Vegas", "Adobe Audition", "Pro Tools", "Adobe After Effects", "Logic Pro X", "OBS Studio", "Camtasia", "Adobe Premiere Elements", "Adobe Photoshop", "Adobe Illustrator", "Sennheiser Microphone", "Shure Microphone", "Rode Microphone", "Zoom H5 Recorder", "Sony ZV Camera", "DJI"),
    category="文学",
    databases=("OpenAlex", "Google Scholar", "SSRN", "JSTOR", "ScienceDirect"),
)
