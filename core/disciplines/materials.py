"""材料学科论文支持：材料体系综述、组分-结构-性能关系与工艺—性能对比。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="materials",
    aliases=("materials", "材料", "material science", "先进材料", "先进材料体系",
             "高分子", "金属", "陶瓷", "复合材料", "先进复合材料", "先进材料"),
    paper_types={
        "research": ("abstract", "introduction（性能瓶颈与设计思路）", "methodology（合成/制备与表征）", "results（组分-结构-性能链条）", "discussion（机理、局限与工程应用）", "references"),
        "case_study": ("abstract", "introduction", "case description（材料体系与制备路线）", "analysis（成分工艺与性能关联）", "results（表征与测试证据）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（材料分类与理论框架）", "evidence synthesis（跨体系性能对比）", "future directions", "references"),
    },
    citation_style="编号（Wiley/ACS 风格，期刊缩写按 CASSI）",
    reporting_standards={
        "characterization": "表征规范：XRD 给靶材/扫描范围/步长与 PDF 卡号；SEM/TEM 给加速电压与标尺",
        "synthesis": "合成/制备步骤可复现：前驱体纯度、比例、温度程序、气氛与产率",
        "data": "晶体数据以 CIF 存档并给 CCDC 号；原始谱图与测试数据可获取",
    },
    conventions=(
        "样品命名全文一致（如 S-1、S-500°C），图注与正文对应",
        "性能对比表加粗最优并给文献出处与测试条件",
        "误差棒给重复次数（n）与误差含义（SD/SEM）",
        "晶体结构图标注晶面指数与空间群",
        "缩写首次出现给出全称（如 SEM、TEM、XRD）",
    ),
    key_venues=(
        "Nature Materials",
        "Advanced Materials",
        "Materials Science and Engineering R",
        "Acta Materialia",
        "Journal of Materials Chemistry A",
    ),
    units_and_formulas_notes=(
        "粒径 nm；强度 MPa/GPa；电导率 S·m⁻¹；比容量 mAh·g⁻¹",
        "XRD 峰位以 2θ（度）与晶面 (hkl) 标注",
        "比表面积 BET 给脱气条件；孔径分布给模型（BJH/DFT）",
        "力学/热学性能给测试标准（ASTM/ISO）与速率",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("X 射线衍射仪（Bruker D8 Advance）", "扫描电镜（SEM, FEI Quanta）", "透射电镜（TEM, JEOL 2100F）", "Raman 光谱仪", "X 射线光电子能谱（XPS）", "原子力显微镜（AFM）", "热分析仪 DSC/TGA", "万能材料试验机（Instron）", "Origin Pro", "Materials Studio", "VASP", "CASTEP", "Thermocalc", "Avizo", "ImageJ", "Python (NumPy/SciPy)", "Microsoft Excel", "Microsoft Visio", "LaTeX/BibTeX", "EndNote"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
