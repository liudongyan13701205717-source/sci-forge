"""美甲学学科论文支持：皮肤/足部健康与美甲工艺体裁、医学/美容技术引用样式与操作记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pedicure",
    aliases=("pedicure", "美甲", "足部护理", "pedicure care", "指甲护理", "足病护理", "足部皮肤", "美容技术", "podiatry"),
    paper_types={
        "research": ("abstract", "introduction（美甲/足部问题）", "methodology（操作/材料/评估方法）", "results（皮肤与指甲变化）", "discussion（机理与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（对象与初始状态）", "analysis（操作与观察）", "results（结局与并发症）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（皮肤/指甲理论）", "evidence synthesis（材料/操作综述）", "future directions", "references"),
    },
    citation_style="Vancouver/医学样式（皮肤与美甲领域；材料标准按 ISO/GB 编号引用）",
    reporting_standards={"informed_consent": "涉及人体操作须说明知情同意与风险告知", "infection_control": "器械消毒与生物安全遵循 CDC/HAS 指南", "materials": "美甲材料（光固化/凝胶/树脂）须标注成分与相关法规", "clinical": "涉及病理状态须由执业医师评估并转诊", "outcome": "临床终点（皮肤 pH、水分、菌落、疼痛）须定量"},
    conventions=("指甲/皮肤部位命名遵循解剖学命名（如远端甲沟、甲周皮肤）", "材料名称按成分与光固化波长（如 365 nm UV/LED）标注", "操作时长与力度单位须明确", "疼痛评分用 VAS 或 NRS", "图像记录遵循统一角度与光照条件"),
    key_venues=("Journal of the American Podiatric Medical Association", "British Journal of Dermatology", "Journal of Cutaneous Medicine and Surgery", "Cosmetics", "International Journal of Cosmetic Science", "Cosmetics and Toiletries"),
    units_and_formulas_notes=("皮肤 pH 用无量纲；水分用 % 或 corneometry 单位", "光固化波长用 nm；照射时间用 s", "疼痛评分 VAS 0-10", "样本量与统计检验须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("皮肤 pH 计", "皮肤水分仪（Corneometer）", "皮肤弹性仪", "体视显微镜", "LED/UV 光固化灯", "打磨器（电动打磨机）", "指甲抛光机", "灭菌高压锅", "生物安全柜", "皮肤镜（Dermatoscope）", "显微摄影（显微成像）", "菌落计数仪", "电子天平", "SPSS 统计分析", "R 统计分析", "Python (Pandas)", "Stata 统计", "MedCalc 统计分析", "ImageJ 图像分析", "无菌操作台"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "ISO/GB 美甲材料标准数据库"),
)
