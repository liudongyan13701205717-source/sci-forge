"""血液学学科论文支持：血细胞分析、流式免疫分型、遗传与分子检测及临床血液学研究方法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="haematology",
    aliases=("haematology", "血液学", "hematology", "临床血液学", "白血病", "leukemia", "淋巴瘤", "lymphoma", "流式细胞术"),
    paper_types={
        "research": ("abstract", "introduction（临床问题与研究假设）", "methodology（人群、检测平台与终点）", "results（血象、流式、遗传学与预后）", "discussion（与既往证据的比较）", "references"),
        "case_study": ("abstract", "introduction", "case description（主诉、血象与体征）", "analysis（血液学表型与鉴别诊断）", "results（治疗经过与缓解评估）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（造血与血液肿瘤机制）", "evidence synthesis（指南与系统评价综合）", "future directions", "references"),
    },
    citation_style="Vancouver (ICMJE) 样式",
    reporting_standards={"STROBE": "观察性血液学研究按 STROBE 清单报告", "MIROC": "流式细胞术按 MIROC/ISTH 建议报告面板、门控与标准化", "CONSORT": "随机对照试验按 CONSORT 2010 清单报告"},
    conventions=("疾病按 WHO 分类与分期标注（如 2022 WHO、Ann Arbor 分期、IPI）", "细胞计数以 ×10⁹/L 报告，比例以 % 报告", "流式面板须报告抗体克隆号、荧光通道与门控策略", "分子与基因结果给出拷贝数、突变位点与变异等位基因频率（VAF）", "统计学连续变量报 M ± SD 或中位数（IQR），p 值保留 3 位有效数字"),
    key_venues=("Blood", "Leukemia", "British Journal of Haematology", "Haematologica", "中华血液学杂志"),
    units_and_formulas_notes=("血细胞计数用 ×10⁹/L；血红蛋白用 g/L；血小板用 ×10⁹/L", "流式结果按绝对计数与 % 分别报告", "VAF 用 % 报告；拷贝数变异用 CN 报告", "统计学 HR 或 RR 附 95% CI；公式用 LaTeX（amsmath）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Sysmex XN-9000", "Beckman Coulter DxH 900", "Mindray BC-5390", "Sysmex CS-5100", "BD FACSCanto II", "BD LSRFortessa", "Beckman Coulter CytoFLEX", "Thermo Fisher Attune", "Cytek Aurora", "Neubauer Chamber", "Sysmex CA-7100", "Diagnostica Stago STA-R Max", "WERFEN Coagulation Analyzer", "Dako EnVision", "Leica BOND MAX", "Roche Ventana", "BD PharmDx", "Illumina NovaSeq 6000", "Thermo Fisher Ion Genome System", "BD Rhapsody"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
