"""复现沙箱 harness 单元测试：白名单/超时/防伪/指标验证。"""

from __future__ import annotations

import math
import time

from sciforge.reproduce.harness import (
    MetricValidator,
    VerifiedRegistry,
    execute,
    _audit_imports,
)


def test_whitelist_rejects_bad_import(tmp_path):
    src = "import subprocess\nx = 1\n"
    res = execute(src, tmp_path, timeout=10)
    assert res.ok is False
    assert "非白名单" in res.error and "subprocess" in res.error


def test_whitelist_allows_numpy(tmp_path):
    src = (
        "import numpy as np\n"
        "a = np.array([1,2,3])\n"
        "set_metric('sum', float(a.sum()), 'real')\n"
    )
    res = execute(src, tmp_path, timeout=15)
    assert res.ok is True, res.stderr
    tags = [m.tag for m in res.metrics]
    assert "sum" in tags
    m = [m for m in res.metrics if m.tag == "sum"][0]
    assert m.value == 6.0


def test_nan_inf_rejected_fast_fail():
    v = MetricValidator()
    ok, _ = v.validate(float("nan"), "real")
    assert ok is False
    ok, _ = v.validate(float("inf"), "real")
    assert ok is False
    ok, _ = v.validate(float("-inf"), "real")
    assert ok is False
    # 正常数值通过
    ok, _ = v.validate(0.5, "real")
    assert ok is True


def test_registry_rejects_invalid():
    reg = VerifiedRegistry()
    assert reg.push("x", float("nan")) is False
    assert reg.push("x", 1.0) is True
    assert len(reg.items()) == 1


def test_hardcoded_source_metric_must_come_from_run(tmp_path):
    """防伪：仅 report_metric/set_metric 上报的值进入结果；直接局部变量不入。"""
    src = (
        "hardcoded_acc = 0.99\n"  # 非上报，不进入结果
        "set_metric('acc', 0.95)\n"  # 上报，进入
    )
    res = execute(src, tmp_path, timeout=10)
    assert res.ok is True, res.stderr
    tags = [m.tag for m in res.metrics]
    assert "acc" in tags
    assert "hardcoded_acc" not in tags


def test_timeout_kills_long_run(tmp_path):
    src = (
        "import time\n"
        "time.sleep(30)\n"
        "set_metric('never', 1.0)\n"
    )
    start = time.time()
    res = execute(src, tmp_path, timeout=2)
    elapsed = time.time() - start
    assert res.timed_out is True
    assert elapsed < 10
    # 超时后不应有指标
    assert all(m.tag != "never" for m in res.metrics)


def test_audit_imports_detects():
    assert _audit_imports("import subprocess") == ["subprocess"]
    assert _audit_imports("from os import system") == []  # os 在白名单内 → 空
    assert _audit_imports("import numpy") == []
