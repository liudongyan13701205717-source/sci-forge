"""美容美发服务学科论文支持：美发技术、皮肤护理与美容服务标准化研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hair_and_beauty_services",
    aliases=("hair_and_beauty_services", "美容美发服务", "美发服务", "美容服务", "美容技术", "皮肤护理", "美发艺术"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（方法与材料）", "results（结果与效果）", "discussion（讨论与机制）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（技术分析）", "results（效果评价）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "RCT 遵循 CONSORT", "k2": "观察性研究遵循 STROBE", "k3": "系统综述遵循 PRISMA"},
    conventions=("仪器型号与规格须完整标注", "操作参数（温度/时间/剂量）须量化记录", "皮肤/发质类型须注明分级标准", "客户满意度评分须给量表名称与版本", "效果评价须注明随访时间窗口"),
    key_venues=("Journal of Cosmetic Dermatology", "International Journal of Cosmetic Science", "Dermatologic Surgery", "Skin Research and Technology", "Journal of Cosmetic, Dermatological and Surgical Laser"),
    units_and_formulas_notes=("光照剂量：J/cm²", "射频功率：W/cm²", "pH 值无量纲", "温度：°C"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("VISIA 皮肤分析仪", "Wood's Lamp 伍德灯", "数字皮肤镜（Dermoscopy）", "光纤测厚仪（皮肤）", "生物阻抗皮肤水分仪", "pH 皮肤检测仪", "分光光度计（发色分析）", "紫外老化模拟仪", "热成像仪（红外）", "3D 皮肤扫描仪", "头皮显微镜", "毛发显微拉拔仪", "皮肤电导率仪", "光谱分析仪（荧光）", "超声波清洁仪", "LED 光疗设备", "射频美容仪（RF）", "冷冻溶脂仪", "激光脱毛仪", "SPSS"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
