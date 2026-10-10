"""家禽养学科论文支持：家禽育种、营养饲养、疫病防控与生产环境研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="poultry_husbandry",
    aliases=(
        "poultry husbandry", "家禽养殖", "家禽饲养",
        "poultry science", "家禽科学",
        "poultry nutrition", "家禽营养",
        "poultry health", "家禽疫病防控",
        "egg production", "蛋鸡生产",
        "breeding", "家禽育种",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（生产问题与理论依据）",
            "methodology（试验设计、饲喂方案与统计分析）",
            "results（生产性能与肉质指标）",
            "discussion（机制解释与生产建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（场区基本情况与生产流程）",
            "analysis（饲养管理与疫病处置）",
            "results（经济效益与性能提升）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（育种与营养学理论）",
            "evidence synthesis（国内外研究证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "k1": "动物试验须报告伦理批准与伦理委员会编号",
        "k2": "饲养试验须报告随机化方案、重复数与试验周期",
        "k3": "疫病研究须报告临床病例定义与实验室确诊方法",
    },
    conventions=(
        "生产性能须分阶段报告（雏、育成、产蛋或出栏）",
        "料肉比与采食量须注明日龄与体重阶段",
        "随机区组设计须报告区组因素与小区数",
        "活重指标以平均体重与均匀度同时报告",
        "抗生素与药物治疗须注明用法用量及休药期合规性",
    ),
    key_venues=(
        "Poultry Science",
        "British Poultry Science",
        "World's Poultry Science Journal",
        "Animal Feed Science and Technology",
        "Poultry Science (Chinese Journal of Poultry Science)",
    ),
    units_and_formulas_notes=(
        "料肉比 = 采食总量 kg / 增重总量 kg，无量纲",
        "料蛋比 = 采食量 kg / 产蛋量 kg",
        "日增重以 g/d 表示并注明起始日龄",
        "成活率以百分比表示，分母为入舍羽数",
        "产蛋率 = 产蛋只数 / 在产母鸡数 × 100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SAS", "R (RStudio)", "SPSS", "Minitab", "GENESIS", "BLUPF90", "Python (pandas, scipy)", "MATLAB", "Excel", "Bodet 恒温恒湿鸡舍环境监测仪", "GasMetrix 禽舍气体检测仪", "In Vivo NIR 近红外饲料分析仪", "Mettler Toledo 电子天平", "Dumas 凯氏定氮仪", "COBAS 兽医临床生化分析仪", "Vetscan FS 禽病快速检测", "BioRad DxH 血球分析仪", "LaserTrack 遗传标记基因分型", "Agilent qPCR 实时荧光定量仪", "HerdLogic 生产管理软件"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
