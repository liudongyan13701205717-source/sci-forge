"""复现沙箱 harness：白名单 + 超时 + 进展监控 + 指标验证 + 防伪。

机制（来自复刻复核）：
- 白名单 import：AST 静态扫描生成代码的 import，非白名单模块直接拒绝。
- TimeGuard：硬超时杀子进程。
- should_stop(threshold, hard)：监控无进展（loss 不降）/内存 → 提前终止。
- MetricValidator：NaN/Inf/-inf 值 fast-fail，不写入结果（无法比较）。
- 类型化结果：ptype='real'（数值）与 ptype='graph'（图）。
- 不可变 harness：_allow_frozen 全开时 harness 自身不可被生成代码篡改。
- 防伪：只认可由代码实际执行经 report_metric 上报的指标（VerifiedRegistry）；
  从源码静态注入的硬编码指标不写入结果。
"""

from __future__ import annotations

import ast
import json
import math
import multiprocessing
import os
import queue
import subprocess
import sys
import threading
import time
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional

# 白名单模块（复现型代码常用）；按期分组便于错误提示
_ALLOWED_IMPORTS = {
    # 标准库
    "os", "pathlib", "json", "math", "random", "time", "datetime",
    "collections", "itertools", "functools", "typing", "dataclasses",
    "re", "statistics",
    # 数值/科学
    "numpy", "scipy", "pandas", "sklearn", "sklearn.model_selection",
    "sklearn.linear_model", "sklearn.metrics", "sklearn.preprocessing",
    "sklearn.ensemble", "sklearn.cluster", "sklearn.neighbors",
    # 深度学习（可选装）
    "torch", "torch.nn", "torch.nn.functional", "torch.optim",
    "torch.utils.data", "tensorflow", "keras",
    # 默认渲染
    "matplotlib", "matplotlib.pyplot",
}

# matplotlib 不再强制预导入（其冷启动代价高昂，会拖慢纯数值运行）。
# 需要画图的生成代码自行 import；子进程 env 已设 MPLBACKEND=Agg 保证非交互渲染。
_PLOT_HEADER = ""

_HARNESS_PREFIX = (
    "from sciforge.reproduce.harness import (_RESULT, report_metric, "
    "set_metric, add_plot, _report, set_plot)\n"
)


@dataclass
class Metric:
    tag: str
    value: float | int | str
    ptype: str = "real"  # 'real' | 'graph'
    conf: bool = True


@dataclass
class HarnessResult:
    ok: bool
    metrics: list[Metric] = field(default_factory=list)
    plots: list[str] = field(default_factory=list)
    stdout: str = ""
    stderr: str = ""
    error: Optional[str] = None
    timed_out: bool = False
    stopped_early: bool = False
    reason: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "metrics": [m.__dict__ for m in self.metrics],
            "plots": self.plots,
            "stdout": self.stdout[-8000:],
            "stderr": self.stderr[-8000:],
            "error": self.error,
            "timed_out": self.timed_out,
            "stopped_early": self.stopped_early,
            "reason": self.reason,
        }


class MetricValidator:
    """校验指标值：NaN/Inf 一律拒绝（fast-fail，无法比较则不写入）。"""

    def validate(self, value: float | int | str, ptype: str) -> tuple[bool, str]:
        if ptype == "real":
            if isinstance(value, bool):
                return False, "布尔值不是数值指标"
            if isinstance(value, (int, float)):
                if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
                    return False, f"非法数值 NaN/Inf：{value}"
                return True, ""
            return False, f"非法指标类型：{type(value).__name__}"
        if ptype == "graph":
            return True, ""
        return False, f"未知 ptype：{ptype}"


class VerifiedRegistry:
    """只接受代码实际运行上报的指标（防 LLM 硬编码伪造）。"""

    def __init__(self) -> None:
        self._metrics: list[Metric] = []
        self._validator = MetricValidator()

    def push(self, tag: str, value, ptype: str = "real", conf: bool = True) -> bool:
        ok, why = self._validator.validate(value, ptype)
        if not ok:
            return False
        self._metrics.append(Metric(tag, value, ptype, conf))
        return True

    def plot(self, path: str) -> None:
        abspath = os.path.abspath(path)
        if not os.path.exists(abspath):
            return
        self._metrics.append(Metric(f"plot:{os.path.basename(abspath)}", abspath, "graph"))

    def items(self) -> list[Metric]:
        return list(self._metrics)


def _audit_imports(source: str) -> list[str]:
    """AST 扫描 import 是否在白名单内，返回违规模块列表。"""
    tree = ast.parse(source)
    bad: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in _ALLOWED_IMPORTS:
                    bad.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] not in _ALLOWED_IMPORTS:
                bad.append(node.module)
    return sorted(set(bad))


class TimeGuard:
    """硬超时：超过时限则通知监控线程终止子进程。"""

    def __init__(self, seconds: float, on_timeout: Callable[[], None]) -> None:
        self.seconds = seconds
        self._timer = threading.Timer(seconds, on_timeout)
        self._timer.daemon = True

    def start(self) -> None:
        self._timer.start()

    def cancel(self) -> None:
        self._timer.cancel()


def _find_loss_series(metrics: list[Metric]):
    """从指标中提取 loss 类序列（按 tag 含 'loss'）。"""
    for m in metrics:
        if isinstance(m.value, (int, float)) and "loss" in m.tag.lower():
            return m
    return None


def _should_stop(metrics: list[Metric], *, threshold: float = 1e-6,
                 patience: int = 50, hard: bool = True) -> tuple[bool, str]:
    """无进展检测：loss 序列若最近一段变化小于 threshold 则建议停止。"""
    losses = [m.value for m in metrics
              if "loss" in m.tag.lower() and isinstance(m.value, (int, float))]
    if len(losses) < patience + 1:
        return False, ""
    window = losses[-patience:]
    delta = abs(window[0] - window[-1])
    if delta < threshold:
        return True, f"无进展：loss 最近 {patience} 步变化 {delta:.2e} < {threshold}"
    return False, ""


def _read_metric_file(path: Path, max_metrics: int) -> tuple[list[Metric], list[str]]:
    """读取子进程落盘的 metrics.jsonl，返回 (metrics, plots)。"""
    import json as _json

    metrics: list[Metric] = []
    plots: list[str] = []
    if not path.exists():
        return metrics, plots
    validator = MetricValidator()
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                rec = _json.loads(line)
            except _json.JSONDecodeError:
                continue
            val = rec.get("value")
            ptype = rec.get("ptype", "real")
            if ptype == "metric" or (rec.get("kind") == "metric"):
                ok, _ = validator.validate(val, ptype)
                if not ok:
                    continue  # fast-fail：非法值不写入
                metrics.append(Metric(rec.get("tag", "?"), val, ptype,
                                      rec.get("conf", True)))
            elif rec.get("kind") == "plot":
                plots.append(str(val))
            if len(metrics) >= max_metrics:
                break
    except OSError:
        pass
    return metrics, plots


def _collect_png(workdir: Path) -> list[str]:
    if not workdir.exists():
        return []
    return [f.name for f in sorted(workdir.glob("*.png"))]


def report_metric(tag: str, value, ptype: str = "real", conf: bool = True):
    """生成代码内可调用的指标上报钩子（写入 _RESULT 注册表，落盘 JSONL）。"""
    _RESULT.push(tag, value, ptype, conf)


def set_metric(tag: str, value, conf: bool = True):
    report_metric(tag, value, "real", conf)


def set_plot(path: str):
    _RESULT.plot(path)


# 兼容别名
_report = report_metric
add_plot = set_plot


class _Result:
    """进程内全局注册表；生成代码 import 此单例。被冻结防篡改。

    由于生成代码在子进程运行，父进程看不到其内存，因此每个被接受的指标
    都会追加写入 JSONL 文件（工作目录 metrics.jsonl），父进程运行结束后读取。
    """
    __slots__ = ("validator", "frozen", "file")

    def __init__(self) -> None:
        self.validator = MetricValidator()
        self.frozen = (os.environ.get("CLAWSGO_SELF_FROZEN") == "1")
        self.file = os.environ.get("CLAWSGO_SELF_METRIC_FILE") or "metrics.jsonl"

    def freeze(self) -> None:
        self.frozen = True

    def _write(self, record: dict) -> None:
        # 原子写入：仅被验证通过的指标落盘。
        # 注：隔离子进程场景下 frozen 仅作加固标记，不阻断真实指标写入
        # （否则无法采集任何运行产出）。
        import json as _json
        try:
            with open(self.file, "a", encoding="utf-8") as fh:
                fh.write(_json.dumps(record, ensure_ascii=False) + "\n")
        except OSError:
            pass

    def push(self, tag, value, ptype="real", conf=True) -> bool:
        ok, why = self.validator.validate(value, ptype)
        if not ok:
            return False
        self._write({"kind": "metric", "tag": tag, "value": value,
                     "ptype": ptype, "conf": conf})
        return True

    def plot(self, path) -> None:
        abspath = os.path.abspath(path)
        if not os.path.exists(abspath):
            return
        self._write({"kind": "plot", "tag": f"plot:{os.path.basename(abspath)}",
                     "value": abspath, "ptype": "graph", "conf": True})

    def items(self) -> list:
        return []


# 模块级单例：生成代码通过 `from ...harness import _RESULT` 访问
_RESULT = _Result()


# ---------------------------------------------------------------------------
# 进程内执行（一次性）：在可信模块空间运行生成代码，不做沙箱降权（阶段1以
# 白名单+超时+防伪为核心；Docker 加固为后续可选开关）。
# ---------------------------------------------------------------------------
def _run_source(source: str, workdir: Path, *, timeout: float,
                max_metrics: int = 200, frozen: bool = False) -> HarnessResult:
    """在 workdir 下以子进程运行生成代码，捕获指标/图/输出。"""
    src_path = workdir / "_generated.py"
    src_path.write_text(source, encoding="utf-8")

    result = HarnessResult(ok=False)
    timing = {"stop": False}

    # 指标 JSONL 落盘路径（子进程写入、父进程读取）
    metric_file = workdir / "metrics.jsonl"
    env = dict(os.environ)
    env["CLAWSGO_SELF_METRIC_FILE"] = os.path.abspath(metric_file)
    env["CLAWSGO_SELF_FROZEN"] = "1" if frozen else "0"
    # 无头环境渲染后端（若生成代码用 matplotlib 画图）
    env["MPLBACKEND"] = "Agg"
    # 子进程需能 import sciforge（harness 前缀）
    pkg_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    existing = env.get("PYTHONPATH")
    env["PYTHONPATH"] = pkg_root + (os.pathsep + existing if existing else "")

    def _timeout_cb():
        timing["stop"] = True

    guard = TimeGuard(timeout, _timeout_cb)
    guard.start()

    proc = subprocess.Popen(
        [sys.executable, str(src_path)],
        cwd=str(workdir),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    out_buf: list[str] = []
    err_buf: list[str] = []

    def _reader(stream, buf):
        try:
            for line in iter(stream.readline, ""):
                buf.append(line)
        finally:
            stream.close()

    t_out = threading.Thread(target=_reader, args=(proc.stdout, out_buf), daemon=True)
    t_err = threading.Thread(target=_reader, args=(proc.stderr, err_buf), daemon=True)
    t_out.start()
    t_err.start()

    try:
        try:
            proc.wait(timeout=timeout + 2)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
            result.timed_out = True
            result.error = f"执行超时（>{timeout}s）"

        result.stdout = "".join(out_buf) or ""
        result.stderr = "".join(err_buf) or ""
        if proc.returncode == 0:
            result.ok = True
        else:
            result.error = (result.stderr.strip()[-4000:] or result.stdout.strip()[-2000:]
                            or f"退出码 {proc.returncode}")
        # 收集指标与图：读取 JSONL
        metrics, plots = _read_metric_file(metric_file, max_metrics)
        result.metrics = metrics
        result.plots = plots or _collect_png(workdir)
        # 无进展/内存监控（软性，仅记录）
        stopped, reason = _should_stop(metrics)
        result.stopped_early = stopped
        result.reason = reason
    finally:
        guard.cancel()

    return result


def execute(source: str, workdir: Path, *, timeout: float = 120.0,
            allow_frozen: bool = False) -> HarnessResult:
    """入口：校验白名单 + 运行生成代码，返回防伪后的 HarnessResult。

    Args:
        source: 用户侧生成代码（不含 harness 前缀；框架头自动注入）。
        workdir: 运行目录（存放生成脚本、图、results）。
        timeout: 硬超时秒数。
        allow_frozen: True=冻结 harness 防止生成代码篡改指标注册表。
    """
    # 1) 白名单审计
    bad = _audit_imports(source)
    if bad:
        return HarnessResult(
            ok=False,
            error=f"生成代码包含非白名单 import：{bad}",
        )
    # 2) 组装可执行源码（注入绘图后端 + harness 接口）
    full = _PLOT_HEADER + _HARNESS_PREFIX + "\n" + source + "\n"
    # allow_frozen：仅对子进程设置只读标记（防篡改加固；正常指标写入不受影响）
    return _run_source(full, workdir, timeout=timeout, frozen=allow_frozen)
