"""老年学学科论文支持：衰老生物学/生命周期理论体裁、AGS 引用样式与老年学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="gerontology",
    aliases=("gerontology", "老年学", "衰老学", "生物学老年学", "社会老年学", "心理老年学", "生命周期理论"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（设计与人群）", "results（衰老标志与结局）", "discussion（机制与意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（个案描述）", "analysis（分析）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（衰老理论）", "evidence synthesis（证据综述）", "future directions", "references"),
    },
    citation_style="AGS 样式（作者-年份；Journals of Gerontology 遵循 AGS 规范）",
    reporting_standards={"k1": "实验研究遵循 ARRIVE", "k2": "观察性研究遵循 STROBE", "k3": "系统综述遵循 PRISMA"},
    conventions=("衰老模型（人/动物/细胞）须明确", "表型定义须一致", "年龄分期须标注", "干预须说明剂量与周期", "生物标志物须注明方法"),
    key_venues=("The Journals of Gerontology Series A", "The Journals of Gerontology Series B", "Mechanisms of Ageing and Development", "Ageing Research Reviews", "BMC Geriatrics"),
    units_and_formulas_notes=("衰老标志物给单位与检测方法", "公式用 amsmath，端粒长度/表观年龄须明确", "数值结果给均值 ± SD 与样本量", "时间以月/年计"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("端粒长度检测（Southern blot）", "DNA 甲基化时钟（Horvath/GrimAge）", "衰老细胞 SA-β-gal 染色", "人源老年细胞培养体系", "小鼠衰老模型（SAM）", "线粒体功能评估（Seahorse）", "蛋白质组学平台（LC-MS/MS）", "转录组测序（RNA-seq）", "CRISPR 基因编辑（衰老基因）", "SPSS", "R", "Prism 生存分析", "衰老相关炎性表型（SASP）检测（ELISA）", "端粒酶活性检测（TRAP）", "衰老蛋白组（iPSC 重编程）", "表观遗传时钟计算（DNA Methylation Clock）", "KEGG 通路分析", "衰老小鼠代谢组学平台", "小鼠活动监测系统", "组织学染色与成像系统"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Seer 衰老生物标志物数据库", "GEO 公共数据库"),
)
