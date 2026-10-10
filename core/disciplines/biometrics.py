"""生物统计/生物计量论文支持：假设检验、样本量设计、Meta 分析与流行病学体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biometrics",
    aliases=(
        "biometrics",
        "biostatistics",
        "biometry",
        "quantitative_biology",
        "applied_statistics",
        "流行病学统计",
        "生物统计",
        "生物计量",
        "生物统计学",
        "定量生物学",
        "流行病学与生物统计",
        "临床试验统计",
    ),
    paper_types={
        "methodological": (
            "abstract",
            "introduction",
            "method（假设、估计量与检验统计量）",
            "simulation（模拟设计、参数与性能指标）",
            "empirical application",
            "discussion",
            "appendix（证明、代码与模拟细节）",
            "references",
        ),
        "analytical": (
            "abstract",
            "introduction",
            "materials and methods",
            "results",
            "discussion",
            "references",
        ),
        "meta_analysis": (
            "abstract",
            "introduction",
            "methods（检索式、异质性模型、偏倚评估）",
            "results",
            "discussion",
            "references",
        ),
    },
    citation_style="Vancouver（编号）或 AMA 样式（视期刊而定）",
    reporting_standards={
        "observational": "观察性研究按 STROBE 报告",
        "diagnostic": "诊断准确性研究按 STARD 2015 报告",
        "randomized": "随机试验按 CONSORT 2010 报告",
        "systematic_review": "系统综述按 PRISMA 2020 与 GRADE 评价证据质量",
        "genomic_association": "GWAS 结果按 MAGMA/GWAS 报告规范（含样本规模、校正方法、PQ 图）",
    },
    conventions=(
        "显著性水平 α 与检验方向（单尾/双尾）须先验声明",
        "所有估计量须报告点估计与 95% CI；非仅报告 p 值",
        "效应量须报告（OR/RR/HR/SMD），避免仅报告统计显著性",
        "多重比较校正须声明（Bonferroni/BH/FDR）与检验族（family-wise 或 FDR）",
        "缺失数据须声明处理方式（完全病例/多重插补），并做敏感性分析",
    ),
    key_venues=(
        "Biostatistics",
        "Statistics in Medicine",
        "American Journal of Epidemiology",
        "Epidemiology",
        "Journal of Clinical Epidemiology",
        "Biometrical Journal",
        "Journal of the Royal Statistical Society: Series C",
        "Annals of Applied Statistics",
    ),
    units_and_formulas_notes=(
        "样本量报告 n（每臂），并说明统计功效（1-β，常用 0.80/0.90）",
        "置信区间默认 95%，双侧；单侧时显式声明",
        "对数变换后的结果须报告几何均值（GM）与几何标准差",
        "方差分析须报告 F（df1, df2）、ηp² 与事后检验方法",
        "生存分析给出风险比 HR、事件数（events）与随访时长",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R", "RStudio", "SAS", "SPSS", "Stata", "GraphPad Prism", "Python（pandas / scikit-learn）", "Julia", "RevMan Web（Cochrane）", "JASP", "Jamovi", "G*Power", "PASS 15", "MedCalc", "Mplus", "OpenMx", "Stan", "PyMC", "EpiInfo 7", "PLINK", "GATK", "DESeq2", "limma", "lme4"),
    category="理学",
    databases=("PubMed", "Europe PMC", "Cochrane Library", "arXiv", "OpenAlex", "Zenodo"),
)
