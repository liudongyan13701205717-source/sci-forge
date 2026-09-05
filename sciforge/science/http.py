from __future__ import annotations

import json
import os
import time
import threading
import urllib.error
import urllib.parse
import urllib.request
from typing import Optional

_USER_AGENT = "sciforge/0.1 (+connector-layer; no-key-public-api)"
_OFFLINE = "CLAWSGO_SELF_OFFLINE"

_rate_limits: dict[str, tuple[threading.Lock, float]] = {}
_rate_holder = threading.Lock()


def _offline() -> bool:
    return os.environ.get(_OFFLINE) == "1"


def _rate_limit(host: str, interval: float) -> None:
    with _rate_holder:
        if host not in _rate_limits:
            _rate_limits[host] = (threading.Lock(), 0.0)
    lock, _ = _rate_limits[host]
    with lock:
        _, last = _rate_limits[host]
        now = time.monotonic()
        wait = last + interval - now
        if wait > 0:
            time.sleep(wait)
        _rate_limits[host] = (lock, time.monotonic())


def http_get_json(url, *, timeout=25, headers=None, rate_interval=1.0, retries=2):
    if _offline():
        return None
    host = urllib.parse.urlparse(url).netloc
    _rate_limit(host, rate_interval)
    hdrs = {"User-Agent": _USER_AGENT}
    if headers:
        hdrs.update(headers)
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(2 ** attempt)
                continue
            return None
        except (urllib.error.URLError, OSError, ValueError):
            return None
    return None


def http_get_text(url, *, timeout=25, headers=None, rate_interval=1.0):
    if _offline():
        return None
    host = urllib.parse.urlparse(url).netloc
    _rate_limit(host, rate_interval)
    hdrs = {"User-Agent": _USER_AGENT}
    if headers:
        hdrs.update(headers)
    try:
        req = urllib.request.Request(url, headers=hdrs)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", "ignore")
    except (urllib.error.URLError, urllib.error.HTTPError, OSError):
        return None
