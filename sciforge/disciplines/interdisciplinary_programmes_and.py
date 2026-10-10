"""跨学科课程与资格学科论文支持：跨学科整合体裁、APA 引用样式与跨学科研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interdisciplinary_programmes_and",
    aliases=("interdisciplinary_programmes_and", "跨学科课程", "interdisciplinary studies", "跨学科课程与资格", "跨学科教育", "跨学科资格", "跨学科研究", "跨领域研究", "跨学科项目", "跨学科课程"),
    paper_types={
        "research": ("abstract", "introduction（跨学科问题与整合逻辑）", "methodology（跨学科方法整合）", "results（整合性发现）", "discussion（跨学科启示与局限）", "references"),
        "case_study": ("abstract", "introduction", "case description（跨学科实践背景）", "analysis（学科间对话分析）", "results（整合成效）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（相关学科理论谱系）", "evidence synthesis（跨学科证据综述）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"method_integration": "跨学科方法须声明来源学科与整合策略", "terminology": "跨学科术语须提供首次定义与来源学科", "acknowledgement": "致谢与学术伦理声明完整"},
    conventions=("跨学科问题须明确界定与来源学科", "术语在首次出现处标注来源学科", "方法整合逻辑须显式陈述", "参考文献按来源学科均衡分布", "研究局限须说明跨学科整合的挑战"),
    key_venues=("Research Policy", "Studies in Higher Education", "International Journal of Interdisciplinary Social Sciences", "Journal of Interdisciplinary Research", "Higher Education"),
    units_and_formulas_notes=("各学科指标须标注来源学科与换算关系", "跨学科数据口径须统一声明", "引用密度与学科分布须披露", "公式用 amsmath；记法与来源学科一致"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Zotero", "Mendeley", "EndNote", "RefWorks", "CiteULike", "Python (Pandas/SciPy)", "R", "SPSS", "NVivo", "Atlas.ti", "Gephi", "VOSviewer", "CiteSpace", "OpenRefine", "Bibliometrix", "Scite.ai", "Connected Papers", "Semantic Scholar", "ResearchGate", "Jupyter Notebook"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
