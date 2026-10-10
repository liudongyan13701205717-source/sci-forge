"""纺织纺纱学科论文支持：纺纱工艺/纱线性能/纤维工程体裁、ASTM 与 IEC 样式与纱支记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="spinning",
    aliases=(
        "spinning",
        "纺织纺纱",
        "Spinning",
        "纺纱工程",
        "纤维与纱线",
        "spinning technology",
        "纤维工程",
        "纺织工程",
        "纺纱工艺",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例）",
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
    citation_style="ASTM / 中文纺织学报样式（编号引用，如 [1]）",
    reporting_standards={
        "test_repeatability": "纱线性能测试须报告方法标准（如 ASTM D2256/D5025）、温湿度条件、重复次数与标准差",
        "process_params": "纺纱工艺参数须完整给出：纤维原料、加弹比、后加工、锭速/牵伸倍数等",
        "simulation": "纤维/纱线建模须报告几何与材料参数、边界条件与实验对照",
    },
    conventions=(
        "纱支标注体系须声明（Tex、Nm、Ne、Den、D），跨体系换算注明标准（如 59 号制）",
        "温湿度条件标 GB 6529（20±2 ℃ / 65±4% RH）或 ISO 139 平衡条件",
        "强力结果用 cN/tex 表示，长度用 m、张力用 cN、伸长率用 %",
        "纱疵与细节率按 Usterstat 版本报告（如 Usterstat 6 版）",
        "纤维细度单位 μm、强度 cN/dtex 或 cN/tex、断裂伸长率 %",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of Industrial Textiles",
        "Industrial and Engineering Chemistry Research",
        "Fiber & Textile Research Journal",
        "中国纺织学报 (Journal of Textile Research)",
    ),
    units_and_formulas_notes=(
        "纱支换算：Tex = 5905 / Ne（英制支数），Den = 9·Tex",
        "捻度单位 T/m（转/米），捻度系数 α = T·√Tex 或 T·√(Nm/3)",
        "断裂强力用 cN 或 cN/tex，断裂伸长率 %，CVb% 表示不匀率",
        "细度 μm 或 dtex（1 dtex = 1 g/10,000 m）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Toyota Autograph AG-5 细度强度仪", "Uster HVI 6 单纤维分析仪", "Uster Tester 6 纱线检验机", "Uster Quickum 12 纱线检验机", "Uster HVI Lab", "Usterstat 纱线质量分析", "Kern & Sobbe 纱疵分析仪", "ZwickRoell Z010 强力机", "Instron 5969 电子拉力机", "Toyota Autograph AGX 强力仪", "Karl Mayer WinGAT 织造 CAD", "Karl Mayer TAT-EX 提花 CAD", "Matlab", "COMSOL Multiphysics", "Simulia Abaqus 纤维力学仿真", "LS-DYNA", "SolidWorks", "LaTeX", "Zotero", "Microsoft Excel"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
