"""海洋生物学学科论文支持：物种生态、种群、群落与分类体裁、海洋采样规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="marine_biology",
    aliases=("marine_biology", "海洋生物学", "海洋生物学科学", "海洋动物学", "海洋植物学",
             "Marine Biology", "Oceanography Biology", "Marine Ecology", "海洋生态学", "海洋物种学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、生态问题与假设）",
            "study area（研究海域与生境描述）",
            "materials and methods（采样、鉴定、分析）",
            "results（种群结构、群落组成、分子证据）",
            "discussion（生态与保护意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（区域或事件描述）",
            "analysis（观测与生态解释）",
            "results（关键指标）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（分类/生态理论综述）",
            "evidence synthesis（区域或物种证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（系统发育用 Zoonorm/BioOne Taxonomy 样式）",
    reporting_standards={
        "sampling": "海洋采样须遵循 ICES/GOOS 规范并注明站位、深度、CTD 剖面",
        "species_id": "物种鉴定须给出拉丁名（斜体）、凭证号与模式产地",
        "molecular": "分子数据须给出引物、扩增片段与 GenBank 登录号",
        "ecological_stats": "群落分析须遵循 PRIMER/PCA- ordination 报告规范",
        "field_ethics": "涉濒危物种须遵循 CITES 与所在国野外调查许可",
    },
    conventions=(
        "物种名首次出现须给出拉丁名（斜体）与中文名",
        "站位坐标须以十进制度 WGS84 报告，深度给单位（m）",
        "采样时间须标注航次与船名，温度、盐度、DO 同步测量",
        "分子系统发育须使用最大似然/贝叶斯并注明模型",
        "群落指标须给出 Shannon/Simpson/Pielou 指数定义",
    ),
    key_venues=(
        "Marine Biology",
        "Marine Ecology Progress Series",
        "Journal of Experimental Marine Biology and Ecology",
        "Journal of Marine Systems",
        "Deep-Sea Research Part I",
        "Coral Reefs",
    ),
    units_and_formulas_notes=(
        "密度单位：个/m² 或个/m³；生物量单位：g/m²（湿重/干重须注明）",
        "Diversity 指数：Shannon H' = -Σ p_i ln p_i；Pielou J' = H'/ln S",
        "站位与网目：CTD 剖面采样深度须按 m 报告",
        "盐度单位：PSU；pH（SW 标尺，无单位）",
        "物种丰度报告须给 n 与采样窗口",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("CTD 剖面仪（Sea-Bird SBE）", "水下 ROV/AUV（Blue Robotics / Jason）", "拖网与浮游生物网（Bongo/Manta net）", "水下摄像机（GoPro + Light）", "DNA 条形码测序平台（Illumina/MiSeq）", "宏基因组测序（Novaseq）", "eDNA 采样与分析（BioManta）", "分光光度计与荧光计", "显微镜与体视显微镜（Zeiss）", "显微 CT（Micro-CT）", "标本库软件（Institutional Repository）", "标本保存液（福尔马林/乙醇）", "潜水与饱和潜水装备", "海洋调查船", "MATLAB/Python（群落统计）", "PRIMER-E（生态学统计）", "R（vegan 包）", "图像分析（ImageJ）", "标本库与基因库（NHMUK/NCBI GenBank）", "遥感卫星（Sentinel-2/Ocean Colour）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "GBIF", "WoRMS"),
)
