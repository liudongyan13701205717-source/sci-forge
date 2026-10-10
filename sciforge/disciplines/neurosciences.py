"""神经科学学科论文支持：神经影像/脑电/神经回路体裁、APA 引用样式与神经科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="neurosciences",
    aliases=("neurosciences", "神经科学", "Neuroscience", "neural science",
             "神经影像", "neuroimaging", "脑科学", "brain science",
             "认知神经科学", "cognitive neuroscience"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与假设）",
            "methodology（被试、任务与采集）",
            "results（统计与效应）",
            "discussion（机制与局限）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例与病史）",
            "analysis（影像与电生理）",
            "results（诊断与预后）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（神经模型综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份）",
    reporting_standards={
        "neuroimaging": "神经影像遵循 ENIGMA 报告规范",
        "preregistration": "研究预注册遵循 OSF/AsPredicted",
        "ethics": "伦理批准号与被试知情同意须列出",
        "statistical": "统计结果须报告效应量与置信区间",
        "data_sharing": "数据集遵循 DRYAD/OpenNeuro 共享规范",
    },
    conventions=(
        "脑区命名遵循 Brodmann 分区或 AAL 分区",
        "MNI 坐标以 MNI-152 标准空间为准",
        "统计阈值须报告 FWE/FDR 校正",
        "样本量以 N（被试数）标注",
        "电极与体素单位须明确",
    ),
    key_venues=(
        "Nature Neuroscience",
        "Neuron",
        "Journal of Neuroscience",
        "NeuroImage",
        "Brain",
        "Trends in Neurosciences",
    ),
    units_and_formulas_notes=(
        "脑区坐标用 MNI 空间 mm；频率用 Hz",
        "统计用 amsmath；效应量 d/Cohen 须报告",
        "显示公式仅在被引用时编号",
        "数据用 N= 与 p/效应量/CI 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPM", "fMRIPrep", "MNE-Python", "EEGLAB", "FreeSurfer", "BrainVoyager", "Nipype", "Connectome Workbench", "MATLAB", "Python (NumPy, SciPy, TensorFlow)", "GraphPad Prism", "R", "Plexon", "Spike2", "NeuroExplorer", "Brainwave", "BrainSuite", "DICOM", "OpenNeuro", "BrainLab"),
    category="理学",
    databases=("OpenAlex", "Crossref", "PubMed", "CNKI"),
)
