"""渔业科学学科论文支持：鱼类生物学、生态学与渔业生物学研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fisheries_sciences",
    aliases=("fisheries_sciences", "渔业科学", "fish biology", "fish ecology",
             "fisheries biology", "鱼类生物学", "aquatic ecology", "水生生态学",
             "fish population dynamics"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="CSE (Council of Science Editors)",
    reporting_standards={
        "population": "种群调查须报告样本量、采样方法与标记-重捕设计",
        "molecular": "分子生物学分析须说明标记类型、测序平台与系统发育方法",
        "ecosystem": "生态学研究须报告栖息地参数、环境变量与统计分析方法",
    },
    conventions=(
        "生长参数用 von Bertalanffy 模型表示（L∞, K, t₀）",
        "死亡率用 Z、M、F 分别表示总/自然/捕捞死亡率",
        "生物量用 t/km² 或 kg/ha 表示",
        "物种多样性用 Shannon-Wiener 指数 H' 表示",
        "年龄结构用 age class 或 cohort 表示",
    ),
    key_venues=(
        "Fisheries Research",
        "Journal of Fish Biology",
        "Marine Ecology Progress Series",
        "Aquatic Biology",
        "中国水产科学",
    ),
    units_and_formulas_notes=(
        "von Bertalanffy 生长方程 L_t = L∞(1 - e^(-K(t-t₀)))",
        "Shannon-Wiener 指数 H' = -Σ p_i·ln(p_i)",
        "捕捞死亡率 F 用 1/年 表示",
        "生物量密度用 kg/ha 或 t/km² 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("分子生物学分析仪", "基因测序仪 (Illumina)", "qPCR仪", "电泳仪", "流式细胞仪", "体视显微镜", "显微镜", "水质分析仪", "溶解氧仪", "光谱分析仪", "Geneious Prime", "R (fisheries biology packages)", "SPSS", "Excel", "Python (BioPython)", "MATLAB", "AutoCAD", "GIS (ArcGIS)", "环境因子记录仪", "鱼类形态测量仪"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)