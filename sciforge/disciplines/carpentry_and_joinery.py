"""木工（建筑）学科论文支持：木结构建造/节点设计/施工管理体裁与引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="carpentry_and_joinery",
    aliases=(
        "carpentry and joinery",
        "building joinery",
        "rough carpentry",
        "trim carpentry",
        "formwork",
        "木结构",
        "建筑木工",
        "建筑细木",
        "框架施工",
        "木模板",
        "框架木作",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程背景与结构体系选择）",
            "structural analysis（构件选型、荷载与节点计算）",
            "experimental results（节点试验与性能数据）",
            "discussion（承载能力、变形、耐久性与可施工性）",
            "conclusions",
            "references",
        ),
        "construction": (
            "abstract",
            "project overview（工程概况与工期）",
            "method statement（施工工艺与工序安排）",
            "quality and safety control（质量控制与安全管理）",
            "cost and schedule performance（成本与进度绩效）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "taxonomy（按结构体系/节点形式分类）",
            "state of the art",
            "challenges and outlook",
            "references",
        ),
    },
    citation_style="APA 7（管理类）；结构设计引用 EN 1995 / GB 50005 体系",
    reporting_standards={
        "grading": "木材等级须标注标准（H2S/H3S/H4S 或 C24/C27 结构材）",
        "connections": "连接件须列规格、数量、间距与偏心距",
        "nodes": "节点构造须给出详图与装配顺序",
        "moisture": "构件基准含水率与含水率调整系数须说明",
        "testing": "节点试验须报告加载制度、荷载-位移曲线与破坏模式",
    },
    conventions=(
        "木结构连接须按 EN 1995 / GB 50005 体系给出受剪承载力计算",
        "构件尺寸与材积须注明基准含水率与含水率调整系数",
        "连接件（螺栓/销/钉）须列规格、间距与偏心距",
        "节点构造须给出详图与装配顺序，标注构件编号",
        "试验报告须说明加载制度、数据采集频率与破坏判据",
    ),
    key_venues=(
        "Construction & Building Materials",
        "Building Research & Information",
        "Structural Engineering International",
        "Forest Products Journal",
        "Journal of Performance of Constructed Facilities",
        "Holz research",
    ),
    units_and_formulas_notes=(
        "应力与强度用 MPa；构件尺寸用 mm",
        "荷载用 kN/m 或 kN/m²；挠度限值用 1/span 形式",
        "含水率用 %；材积用 m³",
        "符号须与所引用标准（EN 1995 / GB 50005）保持一致",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Autodesk Revit", "Trimble Tekla Structures", "Bluebeam Revu", "Autodesk Construction Cloud", "Procore", "AutoCAD", "SketchUp", "Leica TS60 全站仪", "Topcon 3D 激光扫描仪", "Bostitch 气动钉枪", "SawStop 安全锯", "木材应力分级 X 射线系统", "Pinpoint 木材水分仪", "Vico Office 5D 造价", "Solvitum 木材自动分级线", "Bluefield 施工软件", "AutoCAD Civil 3D", "Festool 木工工具套装", "Veritas 刨刀", "Stanley 木工夹具"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
