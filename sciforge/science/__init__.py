from sciforge.science.connector import Connector, ConnectorHit, ConnectorRegistry, DOMAINS

_REGISTRY = ConnectorRegistry()


def get_registry() -> ConnectorRegistry:
    return _REGISTRY


def register(c: Connector) -> None:
    _REGISTRY.register(c)


# 装载 41 个数据库 connector（需在 register 定义之后、包导入完成前执行）。
from sciforge.science import sources as _sources  # noqa: E402,F401

__all__ = ["Connector", "ConnectorHit", "ConnectorRegistry", "DOMAINS",
           "get_registry", "register"]
