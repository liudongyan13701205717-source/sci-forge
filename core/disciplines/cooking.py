"""烹饪学科论文支持：烹饪科学/食品工程体裁、HARPER 引用样式与实验记录约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cooking",
    aliases=(
        "烹饪", "烹调", "烹饪艺术", "Cooking", "Cooking (home)",
        "Culinary Arts", "食品烹饪",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
        "experimental": (
            "摘要",
            "引言",
            "材料与方法",
            "实验过程",
            "结果与分析",
            "讨论",
            "参考文献",
        ),
        "recipe_evaluation": (
            "食谱概述",
            "原料与设备",
            "操作步骤与记录",
            "感官评价",
            "结论与建议",
        ),
    },
    citation_style="HARPER 风格（作者-年份，适用于食品科学期刊）",
    reporting_standards={
        "ingredients": "原料须注明品牌、产地、规格与日期",
        "equipment": "设备须注明型号与操作参数（温度、时间）",
        "reproducibility": "实验须保证可重复性，记录每次参数变化",
        "safety": "食品安全相关实验须符合 HACCP 规范",
    },
    conventions=(
        "温度单位统一使用摄氏度（°C），必要时附华氏度对照",
        "重量单位使用克（g）或千克（kg），容量使用毫升（mL）",
        "操作步骤须按时间顺序编号，关键节点标注时间点",
        "感官评价须使用标准化感官分析面板（如 9 点标度）",
        "食谱版本须标注编号与修改日期",
    ),
    key_venues=(
        "Journal of Culinary Science & Technology",
        "International Journal of Gastronomy and Food Science",
        "LWT - Food Science and Technology",
        "Food Research International",
        "British Food Journal",
        "中国烹饪",
    ),
    units_and_formulas_notes=(
        "比热容、热传导系数按国际标准单位报告",
        "pH 值、水分活度等指标须标注测量温度",
        "感官评分使用 1-9 或 1-10 标度并说明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Rational iCombi Pro（智能厨房系统）", "Kitchen Management System (KMS)", "Breville 智能厨房设备", "Thermocook（红外测温仪）", "Mettler Toledo 厨房天平", "Anton Paar 食品物性分析仪", "HACH pH 计（食品级）", "Water Activity Meter（水分活度仪）", "Sensory Evaluation Software (SENSOMETRICS)", "Tableau（烹饪数据可视化）", "R（统计分析）", "Python (NumPy/SciPy)", "ChefSteps Cooking Studio（食谱创作与协作）", "Kitchen Lab（厨房科研实验室平台）", "Fishtemperature（温度记录仪）", "CandyTherm（糖果温度计）", "Bamsey Digital（专业厨房秤）", "Luminex（颜色分析仪）", "Miele 智能厨房设备", "ThermoControl 温度控制系统"),
    category="工学",
    databases=("PubMed", "ScienceDirect", "Wiley Online Library", "中国知网", "SwissBake（瑞士烘焙配方数据库）", "Food Exponentia（食品数据库）"),
)
