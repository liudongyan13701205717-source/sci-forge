"""程序设计学科论文支持：算法与实现、程序正确性与实证评估研究体裁、ACM 引用样式与可复现性注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="programming",
    aliases=("programming", "程序设计", "编程", "计算机程序设计", "computer programming", "软件编程", "programming techniques", "代码开发", "编程语言"),
    paper_types={
        "research": ("abstract", "introduction（问题、动机与贡献）", "methodology（算法设计、实现与实验方案）", "results（正确性、性能与实测结果）", "discussion（方法局限与推广建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（项目背景、需求与技术方案）", "analysis（实现方案、调试与测试分析）", "results（功能、性能与质量结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（程序设计理论与方法综述）", "evidence synthesis（实证证据综合）", "future directions", "references"),
    },
    citation_style="ACM/IEEE 样式（作者-年份或编号制，按目标期刊规范）",
    reporting_standards={"k1": "代码与运行环境须完整给出（版本、依赖与随机种子）", "k2": "性能指标须给出均值 ± SD 与样本量", "k3": "正确性须有测试用例或形式化验证说明"},
    conventions=("算法须以伪代码给出输入、输出与不变式", "复杂度以 O()/Θ()/Ω() 标注并注明度量对象", "代码示例须可编译、可运行，并附依赖说明", "图表须标注基准、版本与最优项", "统计结果须给出 p 值与效应量"),
    key_venues=("Journal of Software", "Empirical Software Engineering", "Software and System Modeling", "IEEE Transactions on Software Engineering", "Journal of Systems and Software"),
    units_and_formulas_notes=("时间：ms/s；吞吐：ops/s；内存：MB/GB", "精度：accuracy/F1；召回与准确率以 % 表示", "复杂度：O(n)、O(log n)、O(n log n)", "统计结果给出均值 ± SD 与样本量"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Python", "NumPy", "SciPy", "Java", "C/C++", "C#", "TypeScript", "Rust", "Go", "Visual Studio Code", "IntelliJ IDEA", "PyCharm", "Jupyter Notebook", "Git", "Docker", "MATLAB", "LaTeX", "EndNote", "Zotero", "JAMA 编程基准"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)
