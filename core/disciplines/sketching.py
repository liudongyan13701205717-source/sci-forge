"""素描学科论文支持：视觉艺术技法、素描教育评价与艺术创作理论体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sketching",
    aliases=(
        "sketching",
        "素描",
        "sketch",
        "速写",
        "Drawing",
        "Visual Art Education",
        "绘画技法",
        "艺术基础",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methods（实验/作品分析/访谈方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（作品/教学案例）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份）",
    reporting_standards={
        "art_critique": "作品评价须采用明确的艺术评价维度（构图/线条/明暗/质感）",
        "experimental": "艺术教育实验须报告前后测作品评分与信度",
        "ethics": "涉及学生作品须获得知情同意与匿名化处理",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "作品照片须采用统一曝光参数（ISO、光圈、快门）",
        "评分量表须给出评价维度权重与信度（Cronbach's α）",
        "工具分类遵循 ISO 9578 铅笔硬度标准（9B-9H）",
        "图像分析须标注分辨率（dpi）与观察角度",
        "术语首次出现须给出中英文对照",
    ),
    key_venues=(
        "Journal of Aesthetic Education",
        "Studies in Art Education",
        "Leonardo",
        "International Journal of Art & Design Education",
        "美术",
    ),
    units_and_formulas_notes=(
        "铅笔硬度按 ISO 9578 分 B/H/F 级（9B-9H）",
        "画幅尺寸以 cm 或 mm 计（如 A4、8K）",
        "评分采用 Likert 5 级量表；信度以 Cronbach's α 报告",
        "色域采用 CIE L*a*b* 或 Munsell 色卡编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Procreate", "Adobe Photoshop", "Adobe Illustrator", "Clip Studio Paint", "Cangrejo", "Krita", "GIMP", "Affinity Photo", "Affinity Designer", "InkScape", "Autodesk SketchBook", "Medibang Paint", "Concepts", "Notability", "LaTeX", "Endnote", "iMovie", "OBS Studio", "Adobe InDesign", "Canva"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus", "Arts Humanities Citation"),
)
