"""生物技术论文支持：基因工程、发酵工程、酶工程、细胞工程、生物制药。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biotechnology",
    aliases=(
        "biotechnology",
        "biotech",
        "genetic_engineering",
        "enzymatic_technology",
        "cell_engineering",
        "fermentation_engineering",
        "生物医药技术",
        "生物技术",
        "生物工程",
        "基因工程",
        "酶工程",
        "细胞工程",
        "发酵工程",
    ),
    paper_types={
        "research": ("abstract", "introduction", "materials and methods", "results", "discussion", "conclusions", "references"),
        "process": ("abstract", "introduction", "process design", "optimization", "scale-up", "results", "conclusions", "references"),
        "review": ("abstract", "introduction", "technologies", "applications", "challenges", "conclusions", "references"),
    },
    citation_style="ACS style（上标编号），如 ¹ 或 [1]",
    reporting_standards={
        "genetic_engineering": "基因工程须报告载体图谱、插入片段序列、密码子优化与表达条件",
        "fermentation": "发酵须报告培养基组成、培养条件（温度/pH/溶氧/转速）、发酵罐规格",
        "purification": "纯化须报告步骤、收率、纯度（SDS-PAGE/HPLC）、内毒素水平",
        "bioassay": "生物活性须报告检测方法、IC50/EC50、阳性对照与重复次数",
    },
    conventions=(
        "菌株用标准编号（ATCC/CGMCC/CCTCC）+ 来源",
        "酶用 EC 编号；基因用标准命名（斜体/下划线）",
        "质粒图用标准标注（启动子/选择标记/多克隆位点）",
        "发酵参数用表格汇总；产率用 g/L 或 U/mL",
        "安全性须声明生物安全等级（BSL-1/2/3）",
    ),
    key_venues=(
        "Nature Biotechnology",
        "Biotechnology and Bioengineering",
        "Metabolic Engineering",
        "Journal of Biotechnology",
        "Biotechnology Advances",
    ),
    units_and_formulas_notes=(
        "浓度用 mM/μM/mL⁻¹；OD 用 OD600",
        "酶活用 U/mg（比活）或 U/mL",
        "发酵产率用 g/L 或 mol/mol（摩尔转化率）",
        "基因拷贝数用 copies/cell 或 copies/ng DNA",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SnapGene", "Benchling", "Vector NTI", "Geneious Prime", "Primer3", "Cytoscape", "COBRA Toolbox（MATLAB）", "gPROMS", "MATLAB", "Python", "R", "GraphPad Prism", "Thermo Fisher QuantStudio 5", "Bio-Rad T100", "Bio-Rad Gene Pulser XCE", "Sartorius BioFlo R400", "Sartorius MultiQBioractor", "Sartorius Infors HT BioShaker", "Bio-Tek Synergy HTX", "Bio-Tek Cytation 5", "Thermo Fisher FPG1600", "Cytiva ÄKTA pure 25", "Cytiva ÄKTA explore", "Thermo Scientific V350", "Thermo NanoDrop One", "Beckman Optima XPN", "BD FACSCanto II", "BD FACSAria Fusion", "Miltenyi MACS EasySep", "Waters ACQUITY UPLC I-Class", "Waters Xevo TQ-S", "Thermo Scientific Q Exactive"),
    category="工学",
    databases=("PubMed", "Europe PMC", "PubChem", "ChEMBL", "BRENDA", "UniProt", "OpenAlex"),
)
