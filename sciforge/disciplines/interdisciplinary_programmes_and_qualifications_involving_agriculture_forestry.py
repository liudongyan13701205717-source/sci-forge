"""跨学科课程与资格（涉及农业与林业）学科论文支持：农林整合体裁、APA 引用样式与跨学科研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interdisciplinary_programmes_and_qualifications_involving_agriculture_forestry",
    aliases=("interdisciplinary_programmes_and_qualifications_involving_agriculture_forestry", "农林跨学科课程", "农林综合教育", "农林跨学科资格", "农业林业跨学科", "农林与环境", "sustainability agriculture", "农林生态", "农林系统", "可持续农业", "agroforestry"),
    paper_types={
        "research": ("abstract", "introduction（农林问题与整合逻辑）", "methodology（跨学科方法整合）", "results（农林系统发现）", "discussion（实践启示与局限）", "references"),
        "case_study": ("abstract", "introduction", "case description（农林实践背景）", "analysis（学科间对话分析）", "results（整合成效）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（农林相关理论谱系）", "evidence synthesis（跨学科证据综述）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"method_integration": "跨学科方法须声明来源学科与整合策略", "sampling": "田间/林区抽样与样地设计须完整", "ethics": "涉及土地/社区数据须说明伦理与脱敏"},
    conventions=("跨学科问题须明确界定与来源学科", "农林术语（土壤学/林学/生态学）首次出现处标注来源", "田间实验须报告处理、对照与重复", "土地利用类型与轮作安排须明确", "跨学科参考文献按来源学科均衡"),
    key_venues=("Journal of Sustainable Agriculture", "Agriculture, Ecosystems & Environment", "Forest Ecology and Management", "Ecology and Society", "Agricultural Systems"),
    units_and_formulas_notes=("土壤参数（pH、有机质、含水率）须报告单位与测试标准", "林分参数（胸径、树高、蓄积）须声明口径", "产量/生物量须报告单位与年份", "公式用 amsmath；统计口径一致"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("FieldGenius", "TerraGo", "R", "Python (Pandas/SciPy)", "SPSS", "SAS", "Stata", "QGIS", "ArcGIS", "ENVI", "Google Earth", "Excel", "LaTeX", "MATLAB", "Minitab", "G*Power", "NVivo", "AtLast", "Zotero", "Tableau"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
