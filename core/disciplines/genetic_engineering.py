"""遗传工程学科论文支持：基因编辑、合成生物学与遗传操作。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="genetic_engineering",
    aliases=("genetic_engineering", "遗传工程", "基因工程", "genetic engineering", "基因编辑", "合成生物学", "基因操作", "转基因"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver（编号），如 [1]",
    reporting_standards={"k1": "基因编辑须报告 sgRNA 序列/脱靶分析/验证方法（编辑报告）", "k2": "转基因构建须报告载体/启动子/筛选标记（构建报告）", "k3": "生物安全评估须报告风险等级与实验条件（生物安全报告）"},
    conventions=("基因名：人类用斜体大写（BRCA1），小鼠用斜体首字母大写（Brca1）", "sgRNA/启动子/载体序列须完整列出或存入数据库", "基因编辑须报告切割效率与脱靶检测", "蛋白表达须注明诱导条件与时间", "生物安全等级（BSL）须说明"),
    key_venues=("Nature Biotechnology", "Molecular Therapy", "Nucleic Acids Research", "Gene Therapy", "Cell Systems"),
    units_and_formulas_notes=("基因编辑效率用 %（编辑效率）", "蛋白表达量用 ng/μg 总蛋白或 nM", "载体滴度用 TU/mL 或 IFU/mL", "转录本丰度用 TPM 或 FPKM", "细胞转染效率用 %（荧光标记）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CRISPR 基因编辑系统", "电转仪（电穿孔仪）", "基因枪（生物弹射仪）", "PCR 仪（梯度 PCR）", "凝胶成像系统", "质粒提取试剂盒", "流式细胞仪", "荧光显微镜", "超速离心仪", "RNA 测序平台（Illumina）", "基因表达分析软件（RNA-Seq）", "同源重组构建平台", "生物反应器（细胞培养）", "病毒包装系统（慢病毒/AAV）", "基因芯片（DNA 微阵列）", "蛋白印迹（Western Blot 系统）", "细胞培养箱（CO₂ 培养）", "DNA 合成仪（ABI 固相合成）", "基因测序仪（Illumina/HiFi）", "脱靶检测软件（CASOFFINDER）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
