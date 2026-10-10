"""石雕学科论文支持：石雕技艺传承、材料研究与保护修复研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="stone_carving",
    aliases=("stone_carving", "石雕", "石刻", "石刻画", "石雕艺术",
             "stone sculpture", "rock carving", "stone art", "石器雕刻",
             "石雕工艺", "宗教石刻"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methods（材料分析或技艺研究方法）",
            "results（分析结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（石雕作品或案例）",
            "analysis（技艺与材料分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（石雕技艺或历史综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式",
    reporting_standards={
        "materials": "石材类型、产地与物理参数须完整报告",
        "technique": "雕刻技法须注明（圆雕、浮雕、线刻、镂空等）",
        "conservation": "修复材料与方法须遵循文物保护原则",
        "provenance": "文物来源与传承谱系须注明",
    },
    conventions=(
        "石材名称须同时给出中文与拉丁学名（如花岗岩 Granodiorite）",
        "作品尺寸以 cm 报告",
        "硬度用莫氏硬度（Mohs scale）报告",
        "修复前后对比须附照片与年代",
        "艺术风格与时期须按学术共识分类",
    ),
    key_venues=(
        "Journal of Cultural Heritage",
        "Archaeometry",
        "Interventions in Conservation",
        "Bulletin of the Imperial War Museum",
        "文物保护研究",
    ),
    units_and_formulas_notes=(
        "尺寸：cm；重量：kg",
        "硬度：莫氏硬度（1–10）",
        "色差：ΔE（CIELAB 色差）",
        "年代测定：BP（公元前年）或 ka BP（千年前）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Carving chisel set", "Stone saw (handheld)", "Air compressor and pneumatic tools", "Diamond grinder", "Hand file set", "Stone cutting machine", "Waterjet cutter", "3D scanner (structured light)", "Digital sculpting software (ZBrush)", "CNC stone engraving machine", "Microscope", "X-ray fluorescence (XRF) analyzer", "Scanning electron microscope (SEM)", "Rock hardness tester", "Colorimeter", "Adobe Photoshop", "AutoCAD", "Rhino 3D", "TikZ", "LaTeX"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
