"""免疫学论文支持：固有免疫、适应性免疫、免疫病理、疫苗学、肿瘤免疫。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="immunology",
    aliases=("immunology", "免疫学", "immune_system", "immunity"),
    paper_types={
        "research": ("abstract", "introduction", "materials and methods", "results", "discussion", "conclusions", "references"),
        "review": ("abstract", "introduction", "mechanisms", "clinical implications", "future directions", "conclusions", "references"),
        "vaccine": ("abstract", "introduction", "vaccine design", "immunogenicity", "efficacy", "safety", "discussion", "conclusions", "references"),
    },
    citation_style="Vancouver（编号），如 [1]；或 Immunity/JEM 风格",
    reporting_standards={
        "flow_cytometry": "流式须报告抗体克隆号/荧光素/稀释度、设门策略与仪器型号",
        "elisa": "ELISA 须报告试剂盒来源、标准曲线范围、检测限与重复次数",
        "knockout": "基因敲除须验证（Western blot/PCR）、表型描述与回补实验",
        "vaccine_trial": "疫苗试验须报告免疫原性终点（GMT/血清转化率）、安全性数据与随访时间",
    },
    conventions=(
        "免疫细胞用标准命名（CD4⁺ T cell/M1 macrophage/NK cell）",
        "细胞因子用标准缩写（IL-2/TNF-α/IFN-γ），首次出现写全称",
        "抗体用 克隆号 + 荧光素 + 公司名（如 anti-CD4-PE, clone RPA-T4, BioLegend）",
        "图：流式须含 FCS 文件来源；ELISA 须含标准曲线",
        "动物模型须报告品系、年龄、性别与饲养条件",
    ),
    key_venues=(
        "Immunity",
        "Journal of Experimental Medicine",
        "Nature Immunology",
        "Journal of Immunology",
        "Cell Reports Immunology",
    ),
    units_and_formulas_notes=(
        "抗体滴度用 reciprocal dilution",
        "细胞因子浓度用 pg/mL 或 ng/mL",
        "细胞频率用 % of parent gate",
        "效价用 ED50/ED80",
        "杀伤活性用 % specific lysis",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("FlowJo", "流式细胞仪", "ELISA 仪", "GraphPad Prism"),
    category="理学",
    databases=("PubMed", "Europe PMC", "GEO", "Reactome"),
)
