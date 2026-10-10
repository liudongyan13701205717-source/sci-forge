"""婴儿卫生学学科论文支持：婴幼儿喂养、生长发育监测与儿童卫生干预研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="infant_hygiene",
    aliases=(
        "infant_hygiene",
        "婴儿卫生学",
        "婴幼儿保健",
        "小儿卫生学",
        "儿童营养与喂养",
        "infant and child health",
        "pediatric nutrition",
        "child development",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
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
    citation_style="Vancouver 样式（医学/儿科文献）",
    reporting_standards={
        "cohort_study": "队列研究须遵循 STROBE 声明",
        "randomized_trial": "RCT 须遵循 CONSORT 声明",
        "systematic_review": "系统综述须遵循 PRISMA 声明",
        "outbreak_report": "传染病暴发须遵循 ORION 指南",
    },
    conventions=(
        "生长发育指标须注明百分位与参照标准（WHO/中国儿童生长曲线）",
        "喂养方式分类须统一（纯母乳/混合/配方）",
        "年龄分组须按月龄标注，超过 1 岁用岁+月",
        "体重/身高单位用 kg/cm，须注明测得时间",
        "伦理审查与知情同意须说明（尤其婴幼儿研究）",
    ),
    key_venues=(
        "Pediatrics",
        "The Lancet Child & Adolescent Health",
        "Archives of Disease in Childhood",
        "Journal of Pediatrics",
        "中华儿科杂志",
    ),
    units_and_formulas_notes=(
        "体格指标须注明 WHO 曲线参照版本（如 2006 版）",
        "生长速度用 cm/月 或 kg/月 报告",
        "营养摄入量用 24h 回忆法或 3 天称重法，须注明方法",
        "发育量表（ASQ/Denver/Gesell）得分须注明版本与百分位",
        "统计推断须报告 95% CI 而非仅 p 值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("WHO 生长标准软件（WHO Anthro）", "Epi Info（流行病学统计）", "R（生存分析）", "Stata（纵向数据）", "SPSS", "SAS", "EpiData（调查录入与核查）", "OpenDataKit（现场数据收集）", "REDCap（电子病例报告）", "Python（pandas 数据处理）", "Matlab（生长发育曲线建模）", "Epi 7（队列分析）", "Stata（混合模型）", "Mplus（结构方程）", "LASSO（营养风险评估）", "Cox 生存分析（R survival 包）", "EpiAnalysis", "Pediatric Developmental Screener（PALS）", "BayesGrowth（贝叶斯生长模型）", "QI 工具（改善实践）"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "PubMed"),
)
