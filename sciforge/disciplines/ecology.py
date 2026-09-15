"""生态学论文支持：种群动态、群落结构、生态系统功能。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ecology",
    aliases=("ecology", "conservation", "biodiversity", "population", "community",
             "生态", "保护", "演化", "群落生态"),
    paper_types={
        "research": ("abstract", "introduction", "study area", "methods", "results", "discussion", "references"),
        "meta": ("abstract", "introduction", "criteria", "results", "interpretation", "references"),
        "note": ("abstract", "text", "references"),
    },
    citation_style="Ecology（Ecological Society of America）",
    reporting_standards={
        "design": "实验设计须说明对照、重复、随机区组",
        "sampling": "抽样框与抽样强度须给出；检测概率/努力度报告",
        "stats": "混合模型或 GAMM 须含随机效应结构；方差分解报告",
        "spp": "物种名除正式学名，可给当地的通用名和权威缩写",
        "conservation": "国际贸易公约（CITES）附录与采样许可引用",
    },
    conventions=(
        "栖息地分类用权威系统（如 IUCN）",
        "丰度与密度区分；原始数据存 Dryad"),
    key_venues=(
        "Ecology",
        "Ecology Letters",
        "Journal of Ecology",
        "Conservation Biology",
        "Global Ecology and Biogeography",
    ),
    units_and_formulas_notes=(
        "生物量 kg/ha；密度 ind./km² 或 ind./ha；Chao1 给出观测值和置信区间",
        "碳通量 t/ha/yr；周转速率",
        "社区完整性指数需要指点",
    ),
)