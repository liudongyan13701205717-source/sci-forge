"""摄影与胶片冲洗学科论文支持：摄影艺术/胶片工艺/数字影像体裁、Chicago/APA 引用样式与摄影工艺注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="photo_developing",
    aliases=("photo developing", "摄影与胶片冲洗", "摄影工艺",
             "darkroom", "darkroom photography", "胶片冲洗",
             "photography", "photography craft", "暗房工艺",
             "analog photography", "analog photography craft"),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与背景）",
            "methodology（工艺/方法）",
            "results（工艺结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（工艺分析）",
            "results（发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 或 APA 样式（艺术/工艺研究常用 Chicago）",
    reporting_standards={
        "experiment": "实验遵循摄影工艺传统",
        "chemical": "化学配方遵循 ASTM 规范",
        "digital": "数字摄影遵循 ISO 规范",
        "art_history": "摄影史遵循 Iconography 传统",
        "conservation": "胶片保存遵循 AIC/IMA 规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "胶片/药液给出品牌与批号",
        "显影时间/温度/搅拌须注明",
        "化学配方给出浓度与顺序",
        "暗房安全灯须注明色温",
        "档案保存遵循 AIC/IMA 规范",
    ),
    key_venues=(
        "Photographic Journal",
        "Journal of the Royal Photographic Society",
        "Journal of Imaging Science",
        "Studies in Conservation",
        "Photographs",
        "Journal of the Society for Imaging Science and Technology",
    ),
    units_and_formulas_notes=(
        "温度用 °C；浓度用 %",
        "显影时间用分钟/秒",
        "化学配方给出浓度与顺序",
        "胶片/药液给出品牌与批号",
        "显影剂/定影剂/停显液分别给出",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Ektar 显影液", "D-76 显影液", "Microphen 显影剂", "Rodinal 显影剂", "F-5 定影液", "Rapid Fixer 定影剂", "Stop bath 停显液", "显影罐（Paterson）", "显影盘（Saal Digital）", "放大机（enlarger, Durst）", "安全灯（safelight）", "温度计（thermometer）", "冲洗夹（clip）", "定时器（timer）", "冲洗夹/搅拌器（agitator）", "干燥架（drying rack）", "显影放大机（enlarger）", "胶片扫描仪（Epson V850）", "Photoshop（Adobe）", "Lightroom（Adobe）"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "ARTstor"),
)
