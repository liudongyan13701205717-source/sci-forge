"""能源工程论文支持：能效分析、可再生能源系统、储能设计。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="energy_engineering",
    aliases=("energy", "power", "renewable", "solar", "wind", "battery",
             "nuclear", "thermal", "energy conversion", "效率", "能效"),
    paper_types={
        "research": ("abstract", "introduction", "system description", "modeling", "results", "validation", "conclusions", "references"),
        "review": ("abstract", "introduction", "taxonomy", "technology comparison", "challenges", "references"),
        "feasibility": ("abstract", "introduction", "site assessment", "system design", "economic analysis", "sensitivity", "references"),
    },
    citation_style="Elsevier numbered（如 [1]），或 IEEE",
    reporting_standards={
        "efficiency": "效率定义（一阶/二阶、LHV/HHV）须明确",
        "exp_data": "实测数据须含工况和环境条件；仪表精度须写明",
        "simulation": "网格独立性验证须做（＜5% 变化）",
        "economics": "平准化成本 LCOE 计算假设须列全（折现率、寿命）",
        "carbon": "碳核算边界（Cradle-to-Gate/Grave）须声明",
    },
    conventions=(
        "能量单位用 kWh/J；功率 kW/MW；容量因子 %",
        "效率对比用相同边界条件（即同一输入输出定义）",
        "公式变量含单位检查；无量纲数 Re/Pr/Nu 写明定义",
        "系统示意图给能量流与损失；T-s 或 p-v 图配循环",
        "敏感性分析列出改变量最大的 3 个参数",
    ),
    key_venues=(
        "Joule",
        "Applied Energy",
        "Energy",
        "Energy Conversion and Management",
        "IEEE Transactions on Energy Conversion",
    ),
    units_and_formulas_notes=(
        "效率 η_out/η_in 声明基准（LHV/HHV）；储能效率 R 含自放电",
        "排放因子 kg/GJ 或 tCO2/MWh；CO2 强度按排放因子法",
        "投资回收期年；贴现率 % 注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("MATLAB", "ANSYS", "EnergyPlus"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)