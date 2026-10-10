"""兽医学学科论文支持：动物疾病诊断、病原学与临床疗效评价的体裁、Vancouver 引用样式与兽医记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="veterinary",
    aliases=(
        "veterinary",
        "兽医学",
        "动物医学",
        "兽医临床",
        "动物疾病诊断",
        "veterinary medicine",
        "animal diseases",
        "畜禽疫病"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与立题依据）",
            "methods（动物分组、采样与统计分析）",
            "results（病原学、血清学与临床结果）",
            "discussion（机理与临床意义）",
            "conclusion",
            "references",
        ),
        "clinical_case_report": (
            "abstract",
            "introduction（病例背景）",
            "case presentation（主诉、病史与临床检查）",
            "clinical findings（影像、实验室与病理结果）",
            "treatment and outcome（治疗过程与转归）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（病因、流行病学与防治综述）",
            "evidence synthesis（证据等级归纳）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver 样式（数字编号，作者-年份缩写，含 PubMed ID/DOI）",
    reporting_standards={
        "动物伦理": "涉及动物实验须声明伦理审查批准号、3R 原则遵循情况与福利措施",
        "分组与样本": "报告物种、品种、月龄、体重区间与样本量确定依据，说明随机化与盲法",
        "诊断方法": "病原学检测须注明方法学（PCR 靶基因、抗体效价阈值、培养条件）与判读标准",
        "疗效与统计": "报告疗效终点定义、随访时长与统计方法（含 α、置信水平），不良事件须完整记录"
    },
    conventions=(
        "全文采用 SI 单位：体重 kg、体温 ℃、浓度 mg/dL 或 μg/L（须注明）、效价 1:稀释倍数",
        "物种名称用斜体双名法（如 Canis lupus familiaris），首次出现处标注学名与中文名",
        "药物名称用通用名，剂量以 mg/kg 体重表示并标注给药途径与频次",
        "实验室结果报告参考区间来源（物种/年龄/生理状态），异常值标注方向",
        "统计结果给出样本量 n、均值 ± 标准差与 P 值，显著性符号全文统一"
    ),
    key_venues=(
        "Veterinary Microbiology",
        "Preventive Veterinary Medicine",
        "Veterinary Journal",
        "BMC Veterinary Research",
        "中国兽医学报"
    ),
    units_and_formulas_notes=(
        "抗体效价按 1:稀释倍数报告（如 1:128），阳性判定阈值须注明来源与批间变异",
        "病原载量以 Ct 值与拷贝数/mL 同时报告，Ct 保留一位小数",
        "药物剂量按 mg/kg 体重表述，给药间隔以 h 计，血药浓度以 mg/L 报告",
        "疾病发生率按 发生数/观察动物数 × 100% 报告，并标注观察周期"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Sysmex 全自动血液分析仪", "iSTAT 便携血气分析仪", "兽用 B 超诊断仪", "DR 数字 X 光机", "兽用 MRI", "兽用麻醉机", "兽用生命监护仪", "荧光显微镜", "酶标仪 (ELISA Reader)", "qPCR 仪", "PCR 热循环仪", "Sanger 测序仪", "凝胶电泳系统", "流式细胞仪", "全自动尿液分析仪", "Western Blot 转膜仪", "SPSS", "R", "Epi Info", "LIMS"),
    category="农学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI"),
)
