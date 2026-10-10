"""涂装工（喷漆工）学科论文支持：表面涂装与喷涂工艺体裁、APA 引用样式与涂装记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="varnisherssprayers",
    aliases=("varnishers and sprayers", "涂装工", "喷漆工", "喷涂工", "油漆工",
             "spray painting", "surface coating", "finishing trades"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与涂装问题）",
            "materials and methods（涂料、工艺与测试）",
            "results（膜厚、附着力与外观数据）",
            "discussion（涂装机理与应用）",
            "references",
        ),
        "process_study": (
            "abstract",
            "introduction",
            "materials and methods（设备、参数与工序）",
            "results（质量与效率数据）",
            "discussion（工艺优化建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；材料与涂装期刊多用 APA/Elsevier）",
    reporting_standards={
        "coating_test": "涂层测试须报告标准（ASTM/ISO）、试样与条件",
        "adhesion": "附着力测试须报告方法（划格/拉拔）、等级与判定标准",
        "process_documentation": "工艺研究须报告设备、喷涂参数与环境条件",
        "safety": "须报告 VOCs 排放与职业防护措施",
    },
    conventions=(
        "涂料体系（底漆/面漆/清漆）与配方须说明",
        "膜厚用 μm 并给出各层厚度",
        "喷涂参数（气压、距离、走枪速度）须量化",
        "环境条件（温度、湿度）须报告",
        "测试标准（ASTM/ISO）须注明版本",
    ),
    key_venues=(
        "Progress in Organic Coatings",
        "Surface and Coatings Technology",
        "Journal of Coatings Technology and Research",
        "Coatings",
        "Journal of Cleaner Production",
        "Materials & Design",
    ),
    units_and_formulas_notes=(
        "膜厚用 μm；粗糙度用 μm (Ra)",
        "光泽度用 GU（gloss units）；色差用 ΔE",
        "粘度用 s（涂-4 杯）或 mPa·s",
        "附着力等级用 ASTM D3359 0-5 级或 ISO 0-5 级",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("HVLP 喷枪", "无气喷涂机 (airless sprayer)", "静电喷涂设备", "喷漆房 (spray booth)", "涂层测厚仪 (coating thickness gauge)", "光泽度计 (gloss meter)", "色差仪 (colorimeter)", "粘度杯 (viscosity cup)", "表面粗糙度仪", "红外测温仪", "湿度计 (moisture meter)", "打磨机 (sander)", "砂光机", "空气压缩机", "油漆搅拌器", "呼吸防护装备 (respirator)", "固化烘箱 (curing oven)", "喷涂机器人 (spray robot)", "附着力测试仪 (adhesion tester)", "涂料配方管理软件"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
