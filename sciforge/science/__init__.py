from sciforge.science.connector import Connector, ConnectorHit, ConnectorRegistry, DOMAINS

_REGISTRY = ConnectorRegistry()


def get_registry() -> ConnectorRegistry:
    return _REGISTRY


def register(c: Connector) -> None:
    _REGISTRY.register(c)


__all__ = ["Connector", "ConnectorHit", "ConnectorRegistry", "DOMAINS",
           "get_registry", "register"]
