"""神经科学学科论文支持：BIDS 标准、电生理规范与影像统计校正。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="neuroscience",
    aliases=("neuroscience", "神经科学", "脑科学", "brain", "fMRI", "脑成像",
             "电生理", "electrophysiology", "神经回路", "neural circuit"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "results（结果先行，按证据链组织图版）",
            "discussion（解释、局限与模型含义）",
            "methods（被试、采集、预处理与分析，可入文末）",
            "references",
        ),
        "methods_paper": (
            "abstract",
            "introduction（方法动机与适用范围）",
            "results（方法验证与对比）",
            "discussion",
            "methods（实现细节与参数）",
            "references",
        ),
        "resource": (
            "abstract",
            "introduction（数据集/工具动机）",
            "results（数据集构成与质量控制）",
            "discussion（使用建议与局限）",
            "methods",
            "references",
        ),
    },
    citation_style="编号（Nature 系列样式）或作者-年份视期刊",
    reporting_standards={
        "data_structure": "神经影像数据遵循 BIDS 标准组织与共享（OpenNeuro 等）",
        "electrophysiology": "电生理规范：采样率、滤波参数、单元分选质量控制与 spike 判定标准",
        "statistics": "多重比较校正（FDR/permutation/cluster-based）须显式；独立重复数给出",
        "animals": "动物实验按 ARRIVE 2.0 报告；人类被试给 IRB 与知情同意",
        "code": "分析代码公开（可复现流水线与依赖版本）",
    },
    conventions=(
        "脑区命名随标准图谱（如 Allen/Schaefer/Desikan）并给出版本；坐标给空间基准（MNI/NMT）",
        "图版多面板 a/b/c 标注；解剖示意与数据图区分清晰",
        "被试 demographics（年龄、性别、利手）在方法中给出",
        "行为任务描述到可复现粒度（刺激、试次结构、时序）",
        "缩写首次出现给出全称并收入缩写表",
    ),
    key_venues=(
        "Nature Neuroscience",
        "Neuron",
        "eLife",
        "Journal of Neuroscience",
        "NeuroImage",
    ),
    units_and_formulas_notes=(
        "电生理单位 mV/ms/Hz；信噪比给出定义口径",
        "影像分辨率给 mm 与体素尺寸；TR/TE 等序列参数完整给出",
        "统计图给出 n（被试/单元/独立重复）与误差棒含义",
        "效应量与 CI 并列报告；相关给 r 与 p 并说明多重校正",
        "定位报告注明校正方式（如 p<0.05 FWE 校正，簇水平）",
    ),
)
