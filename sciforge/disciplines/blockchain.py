"""区块链学科论文支持：共识/协议/应用体裁、ACM 引用样式与密码学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="blockchain",
    aliases=("blockchain", "区块链", "分布式账本", "智能合约"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "protocol design（协议设计）",
            "security analysis（安全性分析）",
            "evaluation（评估）",
            "references",
        ),
        "consensus_paper": (
            "abstract",
            "introduction",
            "background（背景：共识机制）",
            "protocol（协议）",
            "security analysis（安全性分析）",
            "evaluation（评估与对比）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；CCS/FC 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "实验遵循区块链系统评估规范",
        "security": "安全性分析遵循形式化证明报告规范",
        "benchmark": "基准测试遵循标准负载报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "economic_analysis": "经济分析遵循代币经济模型报告规范",
    },
    conventions=(
        "共识机制（PoW/PoS/PBFT 等）须明确",
        "安全假设与威胁模型须报告",
        "吞吐与延迟须同时报告",
        "分叉与最终性定义须一致",
        "智能合约须附形式化或审计说明",
    ),
    key_venues=(
        "ACM Conference on Computer and Communications Security (CCS)",
        "Financial Cryptography and Data Security (FC)",
        "IEEE Symposium on Security and Privacy (S&P)",
        "IEEE Transactions on Information Forensics and Security",
        "ACM Advances in Financial Technologies (AFT)",
        "IEEE International Conference on Blockchain",
    ),
    units_and_formulas_notes=(
        "吞吐用 TPS；延迟用 s；区块大小用 MB",
        "安全参数用 λ；概率用 Pr[·]",
        "公式用 amsmath；共识安全证明须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "Gas 成本用 gas 单位并注明价格",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Python", "Solidity", "Ethereum", "Geth"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)