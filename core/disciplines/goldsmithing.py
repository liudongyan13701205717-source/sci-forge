"""金工学科论文支持：金银器/首饰工艺体裁、材料学引用样式与金工记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="goldsmithing",
    aliases=("goldsmithing", "金工", "金银器", "贵金属加工", "首饰制作", "錾刻工艺", "金属工艺"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（配方与工艺）", "results（件与性能）", "discussion（美学与工艺意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（件描述）", "analysis（工艺分析）", "results（成型结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（金属工艺理论）", "evidence synthesis（技法综述）", "future directions", "references"),
    },
    citation_style="IUPAP/材料学作者-年份样式（金工与材料学通用）",
    reporting_standards={"k1": "工艺实验须记录配方/温度/时间", "k2": "性能测试遵循 ASTM B", "k3": "件描述须交代材质与尺寸"},
    conventions=("金属纯度须列明（Karat/‰）", "热处理制度须报告", "成型技法须定义", "件须给尺寸与克重", "工艺参数须可复现"),
    key_venues=("Metals and Design", "Jornal de Metalurgia", "Ceramics International（金属方向）", "Metallurgical & Materials Transactions", "Goldsmithing Journal"),
    units_and_formulas_notes=("金属纯度以 Karat/‰ 表示", "公式用 amsmath，金相须明确", "件尺寸给 mm 与克重", "硬度给 Vickers 与测试方法"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("金工台（bench）", "金工夹具（bench dog）", "金工錾刻工具（chasing tools）", "金工熔炉（torti furnace）", "金工退火炉（annealing furnace）", "金工拉丝机（drawing machine）", "金工压模（press die）", "金工抛光机（polishing wheel）", "金工焊接（brazing torch）", "金工电铸（electroforming）", "XRF 成分分析", "金相显微镜（microscope）", "硬度计（Vickers）", "金工数字设计（Rhino/JewelCAD）", "金工 3D 打印（wax 3D print）", "金工失蜡铸造（lost-wax casting）", "金工件质量检查（AOI）", "金工记录表（log）", "金工验收标准（EN 10204）", "金工电子天平（0.01 g）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "金工数据库（GoldBase）"),
)
