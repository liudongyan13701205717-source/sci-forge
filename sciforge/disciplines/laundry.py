"""洗涤学科论文支持：洗涤剂、洗涤工艺与衣物护理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="laundry",
    aliases=(
        "laundry",
        "洗涤",
        "Laundry Science",
        "洗涤剂",
        "Textile Care",
        "织物护理",
        "工业洗涤",
        "Cleaning Science",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题提出）",
            "methodology（方法与样品）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（洗涤分析）",
            "results（结论）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（背景综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 或 ISO 相关体例",
    reporting_standards={
        "k1": "洗涤条件（水温、时间、机械作用）与洗涤剂配方",
        "k2": "色牢度/白度/去污率的测量方法与仪器",
        "k3": "环境数据（COD/BOD）与能耗须标注",
    },
    conventions=(
        "去污率/白度/色牢度按 ISO 标准方法",
        "洗涤剂活性物含量注明百分比",
        "样品织物类型与克重披露",
        "结果给出重复次数与均值±标准差",
        "参考文献按引用顺序统一",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of Industrial Textiles",
        "Cleaning Science and Technology",
        "印染",
        "纺织学报",
    ),
    units_and_formulas_notes=(
        "温度 °C；pH 无量纲",
        "去污率 = (初始白度 − 洗后白度) / (空白 − 洗后) × 100%",
        "能耗 kJ/kg 或 kWh/kg",
        "活性物含量 g/L 或 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Whiteness Spectrophotometer", "Colorimeter", "Aqueous COD Analyzer", "FTIR 光谱仪", "HPLC 液相色谱", "Surface Tension Meter", "Zeta Potential Analyzer", "Turbidity Meter", "pH 计", "Conductivity Meter", "Bleach Strength Meter", "Rubbing Fastness Tester", "Water Softening System", "LaundroLab 试验机", "GretagMacbeth", "Datacolor", "SpectroShade", "OriginPro", "Minitab", "LaTeX"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
