"""畜牧兽医辅助学科论文支持：场舍疫病监测、繁殖育种辅助与生产记录的体裁、Vancouver 引用样式与畜牧记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="veterinary_assisting",
    aliases=(
        "veterinary_assisting",
        "畜牧兽医",
        "兽医技术辅助",
        "动物饲养管理",
        "畜禽疫病防治",
        "livestock husbandry",
        "animal care assistant",
        "畜群健康管理"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（生产与防疫问题）",
            "methods（场区设计、采样与统计分析）",
            "results（疫病、繁殖与生产指标结果）",
            "discussion（影响因素与推广价值）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（场区、畜群规模与饲养条件）",
            "methods（监测与干预措施）",
            "results（指标变化与经济效益）",
            "discussion（经验与局限）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（饲养管理与防疫技术综述）",
            "evidence synthesis（实践证据归纳）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver 样式（数字编号，含 DOI 与 FAO/WOAH 标准引用）",
    reporting_standards={
        "畜群描述": "须报告物种、品种、月龄结构、饲养密度、日粮配方与饲养环境条件",
        "监测方法": "疫病监测须注明采样部位、样本量、检测方法（ELISA/PCR/临床检查）与判定阈值",
        "生物安全": "报告消毒、免疫程序、无害化处理与记录追溯制度，标注依据的规范或标准",
        "统计与效益": "指标按组间/期间对比报告（含 n 与检验方法），经济效益按单位畜只核算"
    },
    conventions=(
        "全文采用 SI 单位：体重 kg、体况评分 1-5 分、日粮营养浓度 g/kg 风干物质",
        "繁殖术语统一书写（如配种、返情、妊娠期、产仔数），首次出现处标注英文缩写",
        "免疫与用药记录按“日期-批号-剂量-途径-操作人”格式，剂量以 mg/kg 体重或 ml 计",
        "生产记录以舍/栏/群为单位汇总，注明统计周期与缺失数据处理方式",
        "统计结果给出 n、均值 ± 标准差与 P 值，效应量与置信区间建议同时报告"
    ),
    key_venues=(
        "Livestock Science",
        "Preventive Veterinary Medicine",
        "Animal Health",
        "Journal of Veterinary Diagnostic Investigation",
        "中国畜牧兽医"
    ),
    units_and_formulas_notes=(
        "生长性能按 ADFI（g/d）与料肉比 FCR = 采食量/增重（无量纲）报告，注明观察天数",
        "繁殖指标按情期受胎率、产仔（产卵）数与存活率报告，分母口径须写明",
        "疫病流行指标按发病率（%）与流行强度报告，群体免疫按保护率 = (对照发病率-免疫组发病率)/对照发病率 × 100% 计算",
        "生产效益按单位畜只投入产出核算，货币单位统一为元"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("兽用听诊器", "兽用电子体温计", "兽用保定笼", "B 超妊娠诊断仪", "奶牛挤奶机", "动物精液冷冻仪", "体细胞计数仪", "乳成分分析仪 (近红外)", "小型血球分析仪", "兽用便携显微镜", "ELISA 快速检测卡", "Bio-Rad CFX 便携 PCR", "兽用生命监护仪", "兽用麻醉机", "电子耳标读写器", "畜牧生产管理系统", "LIMS", "SPSS", "Epi Info", "Excel"),
    category="农学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI"),
)
