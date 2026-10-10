"""针织工业学科论文支持：针织工艺、机械、纱线与产业研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="knitting",
    aliases=(
        "knitting",
        "针织工业",
        "针织技术",
        "Circular Knitting",
        "Flat Knitting",
        "Computerized Knitting",
        "Technical Textiles Knitting",
        "Textile Knitting",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（绪论）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
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
    citation_style="APA",
    reporting_standards={
        "k1": "ASTM D1114 针织物试验方法",
        "k2": "ISO 7211 针织物术语",
        "k3": "FZ/T 70002 针织单位产品物耗能源标准",
    },
    conventions=(
        "织物参数须标明针距、横密、纵密与线圈长度",
        "机械型号须注明品牌与型号（如Stoll KM 5-1、Santoni F16）",
        "测试须报告标准温湿度（20℃/65%RH）与预平衡时间",
        "纱线规格采用Ne（英制）与Tex（公制）双语标注",
        "样衣尺寸按EN ISO 8559/ASTM D5587 标注部位",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of Industrial Textiles",
        "Journal of Textile Machinery",
        "China Textile Journal",
        "针织工业",
    ),
    units_and_formulas_notes=(
        "针距以EPI（针/英寸）表示，横密用GPI",
        "线圈长度以毫米/线圈计",
        "纱支：Ne（英制）、Tex（公制）",
        "产量以g/h 或 m/min 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Stoll KM 5-1", "Stoll SMA 552", "Shima Seiki WH-380", "Shima Seiki APS4", "Santoni F16", "Santoni C168", "Karl Mayer CS 7.5", "Rhöner 8009", "GerberAccuMark", "Lectra Modaris", "CLO3D", "Adobe Illustrator", "AutoCAD", "SolidWorks", "Adobe Photoshop", "MDT", "MATLAB", "OriginPro", "Python", "QATM"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
