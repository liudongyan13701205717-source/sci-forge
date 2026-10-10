"""信息检索学科论文支持：检索系统评估体裁、APA 引用样式与 IR 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information_searching",
    aliases=("information_searching", "信息检索", "情报检索", "IR", "信息科学检索", "检索系统", "信息发现", "知识组织", "信息行为", "文献检索", "digital libraries"),
    paper_types={
        "research": ("abstract", "introduction（检索场景与贡献）", "methodology（数据集与实验设计）", "results（检索指标分析）", "discussion（局限与展望）", "references"),
        "case_study": ("abstract", "introduction", "case description（检索系统/用户场景）", "analysis（检索过程与评价）", "results（可用性/有效性结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（IR 理论与评价框架）", "evidence synthesis（检索方法与证据）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"trec_format": "检索结果须用 TREC run 格式并报告标准指标", "evalprotocol": "评价协议（query/topic 集、相关性标注）须完整披露", "reproducibility": "实验参数与数据版本须可复现"},
    conventions=("指标用 P@k、MRR、nDCG、Recall@k 等标准 IR 度量并标注", "数据集与基准（TREC/CLEF/MQRAC）须注明版本", "查询与用户日志脱敏", "基线系统须用领域公认对照", "统计显著性检验方法须明确"),
    key_venues=("Journal of the American Society for Information Science and Technology", "Information Processing & Management", "ACM Transactions on Information Systems", "CIKM", "SIGIR"),
    units_and_formulas_notes=("指标定义须统一（nDCG 折扣曲线、位置 k 取值）", "查全查准换算注明标注口径", "时延用 ms 并声明硬件平台", "公式用 amsmath；概率与期望记法一致"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Elasticsearch", "Apache Lucene", "Solar", "TREC", "Terrier", "PyTerrier", "BEIR", "MARMOT", "Galois", "Voyan IR", "Clever", "Annoy", "Qdrant", "Milvus", "OpenSearch", "RankLib", "Python (Scikit-learn/Pandas)", "CiteULike", "Semantic Scholar API", "JinaAI Embeddings"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
