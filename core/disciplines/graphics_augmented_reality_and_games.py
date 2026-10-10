"""图形、增强现实与游戏学科论文支持：实时渲染、XR 交互与游戏化实验的方法、平台与评估注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="graphics_augmented_reality_and_games",
    aliases=("graphics_augmented_reality_and_games", "图形学", "增强现实", "augmented reality", "视频游戏", "video games", "real-time rendering", "实时渲染", "XR"),
    paper_types={
        "research": ("abstract", "introduction（图形学或交互问题与研究动机）", "methodology（算法、平台与实验设计）", "results（渲染质量、延迟与用户表现）", "discussion（性能、感知与可用性权衡）", "references"),
        "case_study": ("abstract", "introduction", "case description（作品类型、平台与设计目标）", "analysis（管线、交互模型与关卡结构）", "results（性能数据与用户测试）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（渲染管线与交互理论）", "evidence synthesis（算法、设备与实验文献综合）", "future directions", "references"),
    },
    citation_style="IEEE 样式",
    reporting_standards={"hardware": "实验硬件（终端、GPU、跟踪方案）与固件版本须列出", "experiment": "参与者人数、任务设计与指标（延迟、掉帧率、注视点误差）须报告", "ethics": "涉及人体实验须说明知情同意与伦理审查编号"},
    conventions=("渲染管线（光栅化或路径追踪）、分辨率与刷新率须声明", "延迟须报告端到端 motion-to-photon 延迟（ms）", "代码、实验参数与资产随文提交数据集或模型链接", "图形学公式统一用 LaTeX（amsmath），向量与矩阵符号保持一致", "引用 SIGGRAPH 或 CHI 论文须标注会议年份与 proceedings 全称"),
    key_venues=("ACM Transactions on Graphics", "IEEE Transactions on Visualization and Computer Graphics", "Computer Graphics Forum", "ACM CHI Conference on Human Factors in Computing", "IEEE Transactions on Games"),
    units_and_formulas_notes=("时间用 ms；帧率用 fps；延迟 = 交互输入到画面更新", "空间单位分 m（世界坐标）与 px（屏幕）分别标注", "视场角用 °；注视点误差用 mrad 或 px", "功耗用 W 并说明采集时长；帧耗时（ms）与预算（1000/fps）对照给出"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Unity", "Unreal Engine", "Godot", "Blender", "Autodesk Maya", "Autodesk 3ds Max", "SideFX Houdini", "Substance Painter", "Substance Designer", "ZBrush", "NVIDIA Omniverse", "RealityCapture", "ARKit", "ARCore", "Unity XR Interaction Toolkit", "OpenXR", "Vulkan", "DirectX 12", "PlayFab", "Autodesk SketchBook"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
