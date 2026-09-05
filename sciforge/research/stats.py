"""显著性检验：纯标准库实现的 Welch t 检验与 Mann-Whitney U 检验。

用于把「本文 vs 基线」的多次运行指标差异给出 p 值与结论，无需 numpy/scipy。
"""

from __future__ import annotations

import math
from statistics import mean as _mean


def mean(xs) -> float:
    return _mean(xs) if xs else float("nan")


def variance(xs, *, ddof: int = 1) -> float:
    n = len(xs)
    if n - ddof <= 0:
        return float("nan")
    m = _mean(xs)
    return sum((v - m) ** 2 for v in xs) / (n - ddof)


def stddev(xs, *, ddof: int = 1) -> float:
    v = variance(xs, ddof=ddof)
    return math.sqrt(v) if math.isfinite(v) else float("nan")


def _betainc(x: float, a: float, b: float, *, max_iter: int = 300) -> float:
    """Regularized incomplete beta function I_x(a, b)。"""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    bt = math.exp(
        math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
        + a * math.log(x) + b * math.log1p(-x)
    )
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _beta_cf(a, b, x, max_iter=max_iter) / a
    return 1.0 - bt * _beta_cf(b, a, 1.0 - x, max_iter=max_iter) / b


def _beta_cf(a: float, b: float, x: float, *, max_iter: int, eps: float = 3e-14) -> float:
    """Lentz 连分数数值实现。"""
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    if abs(d) < 1e-30:
        d = 1e-30
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < 1e-30:
            d = 1e-30
        c = 1.0 + aa / c
        if abs(c) < 1e-30:
            c = 1e-30
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < 1e-30:
            d = 1e-30
        c = 1.0 + aa / c
        if abs(c) < 1e-30:
            c = 1e-30
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            break
    return h


def _normal_cdf(z: float) -> float:
    return 0.5 * math.erfc(-z / math.sqrt(2.0))


def _normal_sf(z: float) -> float:
    return 0.5 * math.erfc(z / math.sqrt(2.0))


def welch_t(x: list[float], y: list[float]) -> dict:
    """Welch 两样本 t 检验（不假设等方差）。

    返回 {n1,n2,mean1,mean2,var1,var2,t,df,p,different}，
    p 为双尾，different 表示 p<0.05。
    """
    n1, n2 = len(x), len(y)
    if n1 < 2 or n2 < 2:
        return {"n1": n1, "n2": n2, "p": float("nan"), "different": False,
                "reason": "每组至少需要 2 个样本"}
    m1, m2 = mean(x), mean(y)
    v1, v2 = variance(x), variance(y)
    if v1 <= 0 or v2 <= 0:
        t = float("nan")
        df = 0.0
    else:
        se2 = v1 / n1 + v2 / n2
        t = (m1 - m2) / math.sqrt(se2)
        num = se2 * se2
        den = ((v1 / n1) ** 2) / (n1 - 1) + ((v2 / n2) ** 2) / (n2 - 1)
        df = num / den if den > 0 else float("nan")
    if not (df > 0 and math.isfinite(t)):
        p = float("nan")
    else:
        x_ = df / (df + t * t)
        p = _betainc(x_, df / 2.0, 0.5)
    return {
        "n1": n1, "n2": n2, "mean1": m1, "mean2": m2,
        "std1": stddev(x), "std2": stddev(y),
        "var1": v1, "var2": v2, "t": t, "df": df,
        "p": p, "different": bool(math.isfinite(p) and p < 0.05),
    }


def _ranks(values: list[float]) -> list[float]:
    idx = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    n = len(values)
    while i < n:
        j = i
        while j + 1 < n and values[idx[j + 1]] == values[idx[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[idx[k]] = avg
        i = j + 1
    return ranks


def _tie_factor(values: list[float]) -> float:
    seen: list[tuple[int, float]] = []  # (count at this value)
    from collections import Counter

    cnt = Counter(values)
    total = 0
    for v, c in cnt.items():
        if c > 1:
            total += c ** 3 - c
    return total


def mann_whitney_u(x: list[float], y: list[float]) -> dict:
    """Mann-Whitney U 检验（正态近似 + 特处理平局）。

    返回 {n1,n2,u1,u2,z,p,different,better}，p 双尾。better 表示 x 严格优于 y
    且显著（按秩期望）。
    """
    n1, n2 = len(x), len(y)
    if n1 < 2 or n2 < 2:
        return {"n1": n1, "n2": n2, "p": float("nan"), "different": False,
                "reason": "每组至少需要 2 个样本"}
    pooled = x + y
    ranks = _ranks(pooled)
    r1 = sum(ranks[:n1])
    u1 = r1 - n1 * (n1 + 1) / 2.0
    u2 = n1 * n2 - u1
    mu = n1 * n2 / 2.0
    n = n1 + n2
    tie = _tie_factor(pooled)
    var = (n1 * n2 / 12.0) * ((n + 1.0) - tie / (n * (n - 1.0)))
    if var <= 0:
        return {"n1": n1, "n2": n2, "u1": u1, "u2": u2,
                "p": float("nan"), "different": False, "better": None,
                "reason": "样本方差奇异（全平局）"}
    sd = math.sqrt(var)
    z = (u1 - mu) / sd
    if z > 0:
        zc = (u1 - mu - 0.5) / sd
    elif z < 0:
        zc = (u1 - mu + 0.5) / sd
    else:
        zc = 0.0
    p = 2.0 * _normal_sf(abs(zc))
    if p > 1.0:
        p = 1.0
    better = None
    if math.isfinite(p) and p < 0.05:
        m1 = mean(x)
        m2 = mean(y)
        if m1 != m2:
            better = "x" if m1 > m2 else "y"
    return {
        "n1": n1, "n2": n2, "u1": u1, "u2": u2,
        "z": z, "p": p, "different": bool(math.isfinite(p) and p < 0.05),
        "better": better,
    }