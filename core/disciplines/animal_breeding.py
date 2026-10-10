"""动物育种学科论文支持：遗传育种/基因组选择/群体遗传体裁、ASA 样式与育种统计注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="animal_breeding",
    aliases=("animal breeding", "动物育种学", "畜禽遗传育种",
             "animal genetics and breeding", "畜禽良种繁育",
             "育种值估计", "breeding value estimation", "基因组选择",
             "genomic selection", "群体遗传学", "population genetics",
             "分子标记辅助选择", "marker-assisted selection",
             "数量性状基因座", "QTL", "quantitative trait loci",
             "畜牧育种", "livestock breeding", "家畜改良", "animal improvement"),
    paper_types={
        "research": (
            "abstract",
            "introduction（育种问题与遗传假设）",
            "materials and methods（群体、表型、标记与模型）",
            "results（遗传参数、标记与基因组预测）",
            "discussion（与既有模型比较及育种意义）",
            "limitations",
            "references",
        ),
        "genomic_selection": (
            "abstract",
            "introduction",
            "methods（参考群/目标群、标记 QC、预测模型与交叉验证）",
            "results（训练集/验证集表现与预测准确性）",
            "discussion（成本、可扩展性与生产转化）",
            "references",
        ),
        "marker_discovery": (
            "abstract",
            "introduction",
            "genotyping and QC（芯片/测序平台、覆盖度与 QC 阈值）",
            "association mapping（GWAS 或 QTL 定位）",
            "validation",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按性状的模型与方法演进）",
            "outlook",
            "references",
        ),
    },
    citation_style="ASA（美国动物科学会）/APA 样式（作者-年份；J. Anim. Sci. 遵循 ASA 规范）",
    reporting_standards={
        "population": "群体来源、样本量、性别构成与采集时间须完整",
        "phenotype": "表型定义、测量工具与重复次数须报告",
        "genotyping": "芯片/测序平台、覆盖度、标记密度与 QC 阈值须报告",
        "model": "混合模型、随机效应、协方差结构与软件版本须明确",
        "prediction": "基因组预测须报告训练/验证集划分与交叉验证方案",
    },
    conventions=(
        "家系以标准谱系（pedigree）报告；标记须给出染色体坐标与参考基因组版本",
        "遗传参数（h^2、r_g、r_p）与预测准确性定义须给出并标注样本",
        "统计与遗传符号全文一致（h^2 遗传力、π 遗传漂变率）",
        "分子标记命名引用权威数据库（如 Btau、Sus、ARS-UCD1.2）",
        "有效群体大小 Ne 与样本量 n 须分别标注，不得混用",
    ),
    key_venues=(
        "Journal of Animal Science",
        "Animal Genetics",
        "Animal",
        "Journal of Animal Science and Technology",
        "Mammal Research",
        "BMC Genetics",
        "Livestock Science",
    ),
    units_and_formulas_notes=(
        "遗传参数无量纲，取值范围须注明（h^2 在 [0,1]）并给出置信区间",
        "标记密度用 markers/个体或 M/Mb 报告；覆盖度用 ×fold",
        "基因组预测准确率以 r(pred, true) 或 r_g 报告",
        "统计结果给出均值 ± SE、p 值与多重检验校正方法",
        "样本量 n、有效样本量与有效群体大小 Ne 须分别标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("DMU", "Wombat", "ASReml", "BLUPF90", "MTDFREML", "BGS", "MGBLUP", "Breedbase (R)", "R/qtl2", "GCTA-CV", "PLINK", "GEMMA", "GAPIT", "GATK", "BCFtools", "SAMtools", "FreeBayes", "STACKS", "TAS (TASU-Breeder)", "COW-IQ 3000i", "SDAM (SNP and Density Array Manager)", "VCFtools", "Angsd", "Illumina Infinium", "Illumina GoldenGate"),
    category="农学",
    databases=("Crossref", "OpenAlex", "GenBank", "CNKI"),
)
