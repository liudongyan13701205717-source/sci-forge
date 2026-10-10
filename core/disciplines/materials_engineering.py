"""材料工程学科论文支持：工艺—性能—可靠性链条与工艺窗口表征。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="materials_engineering",
    aliases=("materials engineering", "材料工程", "工艺工程", "工艺窗口",
             "工艺性能", "热加工", "热处理", "凝固", "增材制造", "焊接"),
    paper_types={
        "research": ("abstract", "introduction（工程问题与工艺目标）", "methodology（工艺参数与试样制备）", "results（工艺—微观组织—性能关联）", "discussion（工艺窗口与工程化）", "references"),
        "case_study": ("abstract", "introduction", "case description（工程部件与工艺路线）", "analysis（工艺缺陷与组织分析）", "results（服役性能与失效评估）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（工艺分类与机制）", "evidence synthesis（工艺-性能数据归纳）", "future directions", "references"),
    },
    citation_style="编号（MSSP/ASM 风格）",
    reporting_standards={
        "process_parameters": "工艺参数须完整列出：温度、压力、时间、冷却速率、气氛与设备型号",
        "specimen_preparation": "试样切取方向、尺寸、去应力状态须明确",
        "standard_testing": "力学/热学测试遵循 ASTM/ISO 编号并给测试速率",
    },
    conventions=(
        "工艺—组织—性能链条用流程图与组织图联合呈现",
        "工艺窗口以二维/三维图给出，标注安全区与失效区",
        "失效分析遵循「失效模式」命名（疲劳/蠕变/应力腐蚀等）",
        "热循环/应变速率给单位（K/s、s⁻¹）",
        "工程化建议须给出成本/加工性/回收性的权衡",
    ),
    key_venues=(
        "Materials Science and Engineering A",
        "Acta Materialia",
        "Journal of Materials Processing Technology",
        "Additive Manufacturing",
        "International Journal of Advanced Manufacturing Technology",
    ),
    units_and_formulas_notes=(
        "温度 ℃ 或 K；压力 MPa；速率 mm/min 或 K/s",
        "应变速率 s⁻¹；硬度 HV/HRB/HRC；晶粒尺寸 ASTM 级或 μm",
        "微观定量用体积分数 vol% 与相比例",
        "增材制造给激光功率 W、扫描速度 mm/s、层高 μm",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("真空感应熔炼炉（VIM）", "电渣重熔炉（ESR）", "连续铸造线", "轧机/锻造线", "感应加热炉", "淬火/回火炉（盐浴/气淬）", "等离子喷涂机", "激光增材制造（EOSINT/SLM）", "电子束选区熔化（EBM）", "焊接机器人（KUKA/Fanuc）", "Dilauder 稀释仪", "显微硬度计（Vickers/Knoop）", "金相显微镜（Zeiss AxioVert）", "热膨胀仪（DIL805）", "差热分析（DSC/TG）", "X 射线应力测量仪", "疲劳试验机（MTS）", "Minitab", "JMatPro", "DEFORM/QForm 成形仿真"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
