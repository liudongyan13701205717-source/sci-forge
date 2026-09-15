"""材料科学学科论文支持：XRD/SEM/TEM/Raman 表征规范与性能对比。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="materials_science",
    aliases=("materials science", "材料科学", "材料", "materials", "纳米",
             "nanomaterials", "薄膜", "thin film", "电池材料", "battery"),
    paper_types={
        "research": (
            "abstract",
            "introduction（性能瓶颈与设计思路）",
            "results and discussion（合成—结构—性能证据链）",
            "conclusion",
            "experimental section（合成与表征方法）",
            "supporting information（补充表征与计算）",
            "references",
        ),
        "communication": (
            "abstract",
            "introduction（简短动机）",
            "results and discussion",
            "conclusion",
            "experimental section",
            "references",
        ),
        "review": (
            "abstract",
            "introduction（领域范围与分类框架）",
            "main developments（按材料体系/机理组织）",
            "summary and outlook（挑战与路线）",
            "references",
        ),
    },
    citation_style="编号（Wiley/ACS 风格，期刊缩写按 CASSI）",
    reporting_standards={
        "characterization": "表征规范：XRD 给仪器参数（靶材/扫描范围/步长）与 PDF 卡号；SEM/TEM 给加速电压与标尺",
        "spectroscopy": "Raman 给激光波长与功率；XPS 给荷电校正与结合能参考",
        "synthesis": "合成步骤可复现：前驱体纯度/比例、温度程序、气氛与产率",
        "data": "晶体数据以 CIF 存档并给 CCDC 号；原始谱图数据可获取",
        "performance": "性能对比表给文献值出处与测试条件（倍率、温度、循环数）",
    },
    conventions=(
        "样品命名全文一致（如 S-1、S-500°C），图注与正文对应",
        "性能对比表加粗最优并给文献出处与测试条件",
        "误差棒给重复次数（n）与误差含义（SD/SEM）",
        "晶体结构图标注晶面指数与空间群",
        "缩写首次出现给出全称（如 SEI、CV、EIS）",
    ),
    key_venues=(
        "Nature Materials",
        "Advanced Materials",
        "Advanced Functional Materials",
        "ACS Nano",
        "Nature Energy",
    ),
    units_and_formulas_notes=(
        "粒径 nm；强度 MPa/GPa；电导率 S·m⁻¹；比容量 mAh·g⁻¹",
        "XRD 峰位以 2θ（度）与晶面 (hkl) 标注",
        "电化学测试给电流密度（mA·g⁻¹ 或 C 倍率）与电压窗口",
        "比表面积 BET 给脱气条件；孔径分布给模型（BJH/DFT）",
        "力学/热学性能给测试标准（ASTM/ISO）与升温/加载速率",
    ),
)
