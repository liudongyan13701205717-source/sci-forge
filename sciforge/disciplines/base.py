"""学科论文支持基类：Discipline 声明式描述某学科论文的体裁、结构与规范。

所有字段均为声明式数据（离线、无计算逻辑）。新增学科只需在本包内新增
一个模块并定义模块级 Discipline 实例（或 Discipline 数据类子类，
重新声明字段默认值），registry 会零注册自动发现——这是批次 2
继续补学科的前提。
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Discipline:
    """学科论文支持条目（全声明式数据）。

    Attributes:
        name: 学科主键（英文小写 snake_case，如 "mathematics"）。
        aliases: 别名与匹配关键词（中英文，用于检索/路由/投稿建议）。
        paper_types: 体裁 -> 章节结构列表（每体裁给出该类论文的章节顺序）。
        citation_style: 主引用样式（如 "APA 7"、"Vancouver"）。
        reporting_standards: 报告规范路由（设计/主题 -> 标准名或要求）。
        conventions: 学科写作约定（定理环境、符号、图表、术语等）。
        key_venues: 代表性顶刊/顶会。
        units_and_formulas_notes: 单位与公式注记（SI、量纲、统计口径等）。
    """

    name: str = ""
    aliases: tuple[str, ...] = ()
    paper_types: dict[str, tuple[str, ...]] = field(default_factory=dict)
    citation_style: str = ""
    reporting_standards: dict[str, str] = field(default_factory=dict)
    conventions: tuple[str, ...] = ()
    key_venues: tuple[str, ...] = ()
    units_and_formulas_notes: tuple[str, ...] = ()
