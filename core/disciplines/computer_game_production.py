"""计算机游戏制作学科论文支持：游戏引擎/关卡/工具链/玩家研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_game_production",
    aliases=("computer game production", "计算机游戏制作", "游戏开发",
             "game design", "游戏设计", "game development", "level design",
             "关卡设计", "电子游戏工程", "gamedev", "game art"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "related work",
            "method/design",
            "implementation",
            "evaluation",
            "discussion",
            "references",
        ),
        "system_paper": (
            "abstract",
            "introduction",
            "background and motivation",
            "design and implementation",
            "evaluation",
            "playtest results",
            "conclusion",
            "references",
        ),
        "game_studies": (
            "abstract",
            "introduction",
            "literature review",
            "theoretical framework",
            "study design",
            "results",
            "discussion",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method",
            "taxonomy",
            "gaps and outlook",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；CHI/IEEETMC 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "实验须报告引擎版本、硬件平台与设置",
        "benchmark": "帧率/加载时间/内存须给定量指标",
        "playtest": "玩家研究须报告样本量、招募标准与任务清单",
        "reproducibility": "工具链与关卡资源须公开",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "引擎版本（Unity/Unreal/Godot）与目标平台须明确",
        "游戏机制、关卡结构与内容规模须图示化",
        "性能对比须同硬件同版本",
        "美术资产分辨率与压缩方式须说明",
        "玩家研究须声明招募标准与伦理审批",
    ),
    key_venues=(
        "Computer Graphics and Applications (CG&A)",
        "ACM Transactions on Multimedia Computing",
        "CHI",
        "Game Developers Conference (GDC)",
        "IEEE Conference on Games (CoG)",
        "International Conference on Intelligent Games and Game Theory (IGT)",
        "ACM SIGGRAPH",
        "Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)",
    ),
    units_and_formulas_notes=(
        "帧率用 fps；分辨率用 px；资产体积用 MB",
        "加载/输入延迟用 ms",
        "玩家完成率用 %；平均完成时间用 s/min",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Unity", "Unreal Engine 5", "Godot", "GameMaker Studio", "CryEngine", "Source Engine", "Blender", "Maya", "Substance Painter", "Substance Designer", "Houdini", "3ds Max", "ZBrush", "Marmoset Toolbag", "FMOD", "Wwise", "GitHub", "Perforce", "TeamCity", "Bolt", "Niagara", "PlayCanvas", "Phaser", "Cocos Creator", "Defold", "Steamworks"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)
