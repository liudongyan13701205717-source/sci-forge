"""病理学学科论文支持：临床病理/分子病理体裁、Vancouver 引用样式与病理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pathology",
    aliases=("pathology", "病理学", "临床病理", "clinical pathology", "病理诊断", "病理诊断学", "病理检验", "病理学检验", "病理技术"),
    paper_types={
        "research": ("abstract", "introduction（疾病与病理问题）", "methodology（取材/染色/分子检测）", "results（形态学与分子发现）", "discussion（诊断与预后意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例与临床信息）", "analysis（大体与镜下观察）", "results（病理诊断与分型）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（疾病病理理论）", "evidence synthesis（诊断标准综述）", "future directions", "references"),
    },
    citation_style="Vancouver 样式（IJC 等病理学期刊标准；分子病理遵循 WHO 分类版次）",
    reporting_standards={"diagnostic_guidelines": "诊断须遵循 WHO 分类最新版本并标注", "ihc": "免疫组化报告须遵循 CAP/AMP 规范", "prognosis": "预后研究须报告生存分析方法与校正因素", "etech_rep": "诊断技术遵循 EQA 与室内质控要求", "clinical_path": "临床病理联合研究须说明对照与随访"},
    conventions=("组织标本制备（固定、包埋、切片）须报告参数", "染色名称（HE/IHC/特殊染色）与染色结果须明确", "细胞与肿瘤分期按 TNM 或 FIGO 版本给出", "分子检测用 IHC/FISH/NGS 术语规范化", "图像标注使用统一染色与放大倍数"),
    key_venues=("American Journal of Pathology", "Modern Pathology", "Histopathology", "Virchows Archiv", "Journal of Pathology", "Cancer"),
    units_and_formulas_notes=("长度用 μm；组织厚度用 μm", "免疫组化评分用 Allred 或 H-score 并注明", "生存分析给出 HR 与 95% CI", "pH/酶活性等按国际标准单位"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("包埋机", "切片机", "免疫组化自动染色仪（Ventana/Leica）", "荧光原位杂交（FISH）系统", "数字病理扫描仪（Aperio）", "全基因测序仪（Illumina NovaSeq）", "流式细胞仪（BD FACSCanto）", "显微成像系统（Zeiss/徕卡）", "病理切片机（Microtome）", "病理信息管理系统（LIS）", "QuPath 图像分析", "ImageJ/FIJI 图像处理", "SPSS 统计分析", "R (survival) 生存分析", "Python (scikit-image)", "MATLAB", "InCell Analyzer", "PathMiner 挖掘平台", "Tissuu 组织学平台", "TCGA 数据仓库"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
