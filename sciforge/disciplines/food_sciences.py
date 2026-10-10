"""食品科学学科论文支持：食品科学基础、食品质量与安全体系。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_sciences",
    aliases=("food_sciences", "食品科学", "食品与安全", "food sciences", "食品质量", "食品工程", "食品安全", "食品营养"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "HACCP 食品安全计划（HACCP 计划）", "k2": "食品微生物学标准（国标/AOAC）", "k3": "食品质量标准与检测规范（ISO/国标）"},
    conventions=("微生物指标报告 CFU/g 或 CFU/mL", "农残与重金属用国标或 AOAC 方法", "营养标签须按国标 GB 28050 标注", "质量控制须说明抽样方案与检验标准", "讨论须关联食品安全风险"),
    key_venues=("Food Control", "Food Microbiology", "Journal of Food Safety", "International Journal of Food Microbiology", "Food and Bioprocess Technology"),
    units_and_formulas_notes=("微生物用 CFU/g 或 CFU/mL", "农残/重金属用 mg/kg（ppm）或 μg/kg（ppb）", "水分活度 aw 无量纲（0-1）", "货架期以天或月为单位"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("HPLC 高效液相色谱仪", "GC-MS 气相色谱质谱联用仪", "食品微生物 PCR 检测仪", "食品菌落总数快速检测仪", "食品水分活度仪", "食品质构仪 Texture Analyzer", "近红外光谱仪 NIR", "食品电子鼻 E-nose", "食品离心机", "食品色度计", "食品电子温度记录仪", "食品 X 射线荧光仪 XRF", "食品气相检测仪", "食品离心脱水机", "食品冷冻干燥机冻干机", "FTIR 傅里叶变换红外光谱仪", "食品真空包装测试机", "食品电子舌 E-tongue", "食品 X 射线检测系统", "食品离心喷雾干燥机"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
