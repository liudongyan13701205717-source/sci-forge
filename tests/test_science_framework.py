import pytest
from sciforge.science.connector import (
    Connector, ConnectorHit, ConnectorRegistry, DOMAINS,
)


def test_domains_constant():
    assert "literature" in DOMAINS
    assert "proteins" in DOMAINS
    assert "chemistry" in DOMAINS
    assert "genomics" in DOMAINS


def test_connector_hit_to_dict():
    h = ConnectorHit(id="x", title="T", summary="S", url="http://x", score=1.0)
    d = h.to_dict()
    assert d["id"] == "x" and d["title"] == "T" and d["score"] == 1.0


def test_registry_register_and_get():
    reg = ConnectorRegistry()
    c = Connector(id="demo", name="Demo", domain="literature", description="d", search=None)
    reg.register(c)
    assert reg.has("demo")
    assert reg.get("demo").name == "Demo"
    assert reg.all()[0].id == "demo"


def test_registry_by_domain():
    reg = ConnectorRegistry()
    reg.register(Connector(id="a", name="A", domain="chemistry", description="", search=None))
    reg.register(Connector(id="b", name="B", domain="literature", description="", search=None))
    chem = reg.by_domain("chemistry")
    assert len(chem) == 1 and chem[0].id == "a"


def test_registry_catalog_shape():
    reg = ConnectorRegistry()
    reg.register(Connector(id="x", name="X", domain="genomics", description="desc", search=None))
    cat = reg.catalog()
    assert cat[0]["id"] == "x" and "domain" in cat[0] and "requires_key" in cat[0]


def test_registry_get_missing_returns_none():
    assert ConnectorRegistry().get("nope") is None


def test_registry_has_missing():
    assert ConnectorRegistry().has("nope") is False


def test_registry_duplicate_id_last_wins():
    reg = ConnectorRegistry()
    reg.register(Connector(id="d", name="V1", domain="literature", description="", search=None))
    reg.register(Connector(id="d", name="V2", domain="literature", description="", search=None))
    assert reg.get("d").name == "V2"
    assert len(reg.all()) == 1
