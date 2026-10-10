"""Agricultural, veterinary and food sciences 学科论文支持：农业/兽医/食品科学综合体裁、APA/Vancouver 与食品-动物注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agricultural_veterinary_and_food_sciences",
    aliases=(
        "agricultural veterinary and food sciences",
        "农业兽医食品科学",
        "食品科学",
        "兽医科学",
        "动物科学",
        "food science and technology",
        "veterinary science",
        "animal science",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "clinical": (
            "abstract",
            "introduction",
            "case presentation",
            "clinical findings",
            "diagnosis and treatment",
            "discussion",
            "references",
        ),
        "methods": (
            "abstract",
            "introduction",
            "principle",
            "protocol",
            "validation",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope",
            "findings",
            "research gaps",
            "references",
        ),
    },
    citation_style="APA 7 或 Vancouver（食品化学/兽医期刊多用 Elsevier numbered）",
    reporting_standards={
        "animal": "动物实验遵循 ARRIVE 2.0",
        "toxicology": "毒理试验遵循 OECD GLP",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "food": "食品安全试验遵循 Codex Alimentarius 与 ISO/IEC 17025",
        "data": "实验数据遵循 FAIR 与 AAAAM 惯例",
    },
    conventions=(
        "动物实验须报告物种、品系、性别、周龄与福利许可号",
        "生物安全等级（BSL-1/2/3）与操作规范须明确",
        "食品样品须注明采集地点、时间与储存条件",
        "检测方法须符合国标 GB 或 Codex 官方方法；给出检出限与回收率",
    ),
    key_venues=(
        "Food Chemistry",
        "Food Control",
        "Food Science and Technology International",
        "Journal of Agricultural and Food Chemistry",
        "Poultry Science",
        "Journal of Dairy Science",
        "Preventive Veterinary Medicine",
        "Food Microbiology",
    ),
    units_and_formulas_notes=(
        "食品中活性成分含量用 g/kg 或 mg/kg；水分用 %",
        "微生物计数用 CFU/g 或 CFU/mL；毒素用 μg/kg",
        "动物体重、日增重与料肉比按体重阶段分组报告",
        "统计显著性 p 值与效应量并列报告；置信区间给出",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MiniLab Protein Analyzer", "Kjeldahl Analyzer", "FTIR Spectrometer", "NMR", "Chromatograph GC", "HPLC", "Mass Spectrometer LC-MS/MS", "qPCR", "Illumina NovaSeq", "Sanger Sequencer", "Real-Time PCR", "Electrophoresis System", "HACCP Software", "ISO 22000 Management", "Food Safety Plan", "LIMS", "LabWare", "Sartorius Balance", "Texture Analyzer", "Colorimeter"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "PubMed", "FoodData Central", "USDA FoodData", "Codex Alimentarius", "ILSI"),
)
