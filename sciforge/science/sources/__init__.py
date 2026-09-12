"""科学数据库 connector 装载：导入各来源插件并注册到全局 registry。

`sciforge.science` 在导入时会加载本模块（见 science/__init__.py 末尾），
从而把 41 个数据库 connector 注册进全局 ConnectorRegistry，避免
science_list_dbs / science_search 在生产环境查询失效。
"""

from __future__ import annotations

from sciforge.science.sources import (
    chemistry,
    datasets,
    genomics,
    literature,
    omics,
    pathways,
    proteins,
)

_PLUGINS = (chemistry, datasets, genomics, literature, omics, pathways, proteins)


def load_all() -> int:
    """注册全部来源插件，返回注册的 connector 总数。幂等。"""
    from sciforge.science import get_registry

    reg = get_registry()
    for plug in _PLUGINS:
        plug.register()
    return len(reg.all())


REGISTERED = load_all()