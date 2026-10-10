"""纤维纺织与编织艺术学科论文支持：手工纤维艺术、编织工艺与纺织创意体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fibre_textile_and_weaving_arts",
    aliases=(
        "fibre_textile_and_weaving_arts", "纤维纺织与编织艺术",
        "纤维艺术", "编织艺术",
        "fibre arts", "textile arts",
        "weaving arts", "手工纺织", "纤维创作", "编织工艺",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（纤维艺术问题与文化语境）",
            "methodology（材料实验、编织工艺、视觉分析）",
            "results（创作成果与分析）",
            "discussion（与工艺研究、视觉文化对话）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（艺术家/织品/展览描述）",
            "analysis（工艺技法与视觉语言）",
            "results（案例发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（纤维艺术史论综述）",
            "evidence synthesis（现有研究与缺口）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份；纤维艺术论著亦常见注-书目）",
    reporting_standards={
        "materials": "材料描述须注明纤维种类、粗细与来源",
        "weaving": "编织工艺须注明组织、经纬密度与上机方式",
        "dyeing": "染色工艺须注明染料类型、温度与时间",
        "conservation": "保存状态评估须注明光照、湿度与虫害",
    },
    conventions=(
        "纤维细度用 dtex 或 denier 表示",
        "织物结构用经纬密（根/10cm）描述",
        "染色用色卡（Pantone / RAL / 传统色谱）标注",
        "尺寸用 cm 表示",
        "手工与机械工艺须区分注明",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of Craft",
        "Fashion, Textiles and Culture",
        "Textile Culture",
        "Visual Arts Research",
    ),
    units_and_formulas_notes=(
        "细度用 dtex 或 denier；织物密度用根/10cm",
        "染色温度 °C；染色时间 min",
        "色牢度用灰卡级（1-5 级）",
        "尺寸用 cm 表示",
        "光照用 lux 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Jacquard 提花织机", "Shafts 多综提织机", "Rigging 框架织机", "Power Loom 电动织机", "Weaving 编织软件（Jacquard Designer）", "Adobe Illustrator", "Adobe Photoshop", "Procreate", "Inklings 编织设计软件", "Colorway 编织配色工具", "Yarn Testing 纤维测试仪", "Digital 数字化织造", "Loom 织布机（手工）", "Dye 染色设备", "Textile Scanning 织物扫描仪", "Endnote", "Mendeley", "Zotero", "NVivo", "Tableau"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
