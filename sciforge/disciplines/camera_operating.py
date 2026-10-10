"""Camera operating 学科论文支持：摄影/摄像制作体裁、影视行业报告标准与器材/软件注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="camera_operating",
    aliases=("camera operating", "摄影操作", "摄像", "电影摄影", "镜头操作",
             "film photography", "cinematography", "camera work"),
    paper_types={
        "research": (
            "abstract",
            "introduction（创作背景与视觉问题）",
            "方法（拍摄方案、器材与流程）",
            "结果（画面呈现与效果分析）",
            "讨论（创作反思与改进）",
            "references",
        ),
        "report": (
            "abstract",
            "项目概述",
            "拍摄执行（场景、器材、调度）",
            "成片分析",
            "经验总结",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；作品按影视行业惯例标注片名与年份）",
    reporting_standards={
        "case_study": "个案报告须说明拍摄条件（场地、器材、光线）与执行过程",
        "work_review": "作品评析须附片段时间码定位，可复核",
        "process_log": "流程记录须含场记表/拍摄日志要素",
    },
    conventions=(
        "提及镜头参数（焦段、光圈、快门）须给出数值与单位（如 35mm、f/1.4、1/50s）",
        "画面分析须使用准确术语（景深、运动模糊、白平衡），首现给出定义",
        "引用作品标注片名（年份）与具体场景/时间码",
        "器材名称用通用型号而非俗称，全文一致",
    ),
    key_venues=(
        "Cinematography",
        "Sight and Sound",
        "Film Quarterly",
        "Journal of Cinema and Media Studies",
        "Cahiers du Cinéma",
        "American Cinematographer",
    ),
    units_and_formulas_notes=(
        "镜头焦段/片幅/帧率用 mm/in/fps，须注明",
        "曝光三角（光圈、快门、ISO）表述须完整",
        "色彩空间与位深须标注（如 Rec.709、4:2:2 10-bit）",
        "数值结果给出可复核的拍摄参数",
        "引用镜头运动术语须与影片实际一致",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("ARRI Alexa 35", "Sony Cinealta 全画幅系列", "RED V-Raptor", "DJI Ronin 4D", "DaVinci Resolve", "Adobe Premiere Pro", "Adobe Lightroom", "Final Cut Pro", "ProShot", "ShotGrid", "Frame.io", "Avid Media Composer", "Capture One", "Magic Lantern", "Blackmagic DaVinci", "Hasselblad 相机", "Zeiss 镜头", "ARRI/Leica 摄影器材", "Kinefinity 机位", "Blackmagic Studio Camera 系列"),
    category="艺术学",
    databases=("OpenAlex", "CNKI"),
)
