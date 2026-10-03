"""学科论文支持 registry：importlib 自动发现包内 Discipline 条目。

零注册发现：扫描本包内所有模块，收集模块级 Discipline 实例与
Discipline 数据类子类（后者以默认值实例化，须为 @dataclass 并
重新声明字段默认值）。新增学科 = 新增一个模块文件，无需改动本文件——
这是批次 2（再补 ~18 学科）的前提。

暴露：DISCIPLINES / list_disciplines() / get_discipline(name)，
以及按 v2 字段过滤的 list_by_category() / list_by_contribution_form() /
list_by_tool() / list_by_database()。
"""

from __future__ import annotations

import importlib
import pkgutil

from sciforge.disciplines.base import Discipline


def _discover() -> dict[str, Discipline]:
    """扫描包内模块，收集 Discipline 实例与子类，键为学科名（小写）。"""
    found: dict[str, Discipline] = {}
    for mod in pkgutil.iter_modules(__path__):
        if mod.name.startswith("_"):
            continue  # 内部模块（base 等）不参与发现
        m = importlib.import_module(f"{__name__}.{mod.name}")
        for value in vars(m).values():
            entry = _coerce(value)
            if entry is not None and entry.name:
                found.setdefault(entry.name.lower(), entry)
    return found


def _coerce(value: Discipline | type[Discipline]) -> Discipline | None:
    """把 Discipline 实例或子类规约为实例；其余返回 None。"""
    if isinstance(value, Discipline):
        return value
    if isinstance(value, type) and issubclass(value, Discipline) and value is not Discipline:
        return value()
    return None


_DISCIPLINES: dict[str, Discipline] = _discover()

DISCIPLINES: dict[str, Discipline] = _DISCIPLINES


def list_disciplines() -> list[Discipline]:
    """返回全部已发现学科（按学科名排序）。"""
    return [DISCIPLINES[k] for k in sorted(DISCIPLINES)]


def get_discipline(name: str) -> Discipline | None:
    """按学科名或别名查学科（大小写不敏感）；未命中返回 None。"""
    low = name.strip().lower()
    if low in DISCIPLINES:
        return DISCIPLINES[low]
    for d in DISCIPLINES.values():
        if low in (a.lower() for a in d.aliases):
            return d
    return None


def _match_any(values: tuple[str, ...], needle: str) -> bool:
    """needle 是否为 values 中任一值的子串（大小写不敏感）。"""
    low = needle.strip().lower()
    return any(low in v.lower() for v in values)


def list_by_category(category: str) -> list[Discipline]:
    """按学科门类过滤（子串匹配、大小写不敏感），按学科名排序。"""
    return [
        d
        for d in list_disciplines()
        if _match_any((d.category,), category)
    ]


def list_by_contribution_form(form: str) -> list[Discipline]:
    """按产出形式过滤（子串匹配、大小写不敏感），按学科名排序。"""
    return [
        d
        for d in list_disciplines()
        if _match_any(d.contribution_forms, form)
    ]


def list_by_tool(tool: str) -> list[Discipline]:
    """按工具过滤（子串匹配、大小写不敏感），按学科名排序。"""
    return [
        d
        for d in list_disciplines()
        if _match_any(d.tools, tool)
    ]


def list_by_database(database: str) -> list[Discipline]:
    """按优先论文库/数据库过滤（子串匹配、大小写不敏感），按学科名排序。"""
    return [
        d
        for d in list_disciplines()
        if _match_any(d.databases, database)
    ]


__all__ = [
    "DISCIPLINES",
    "Discipline",
    "get_discipline",
    "list_by_category",
    "list_by_contribution_form",
    "list_by_database",
    "list_by_tool",
    "list_disciplines",
]
