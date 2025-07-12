import pytest
from .analytics import (
    count_status_codes,
    top_n_ips,
    top_n_urls,
    avg_response_time,
    error_rate
)


sample_logs = [
    {"ip": "1.1.1.1", "url": "/home", "status": 200, "response_time": 100},
    {"ip": "1.1.1.1", "url": "/home", "status": 200, "response_time": 150},
    {"ip": "2.2.2.2", "url": "/login", "status": 500, "response_time": 300},
]

def test_count_status_codes():
    assert count_status_codes(sample_logs) == {200: 2, 500: 1}

def test_top_n_ips():
    assert top_n_ips(sample_logs, n=1)[0][0] == "1.1.1.1"

def test_top_n_urls():
    assert top_n_urls(sample_logs, n=1)[0][0] == "/home"

def test_avg_response_time():
    assert avg_response_time(sample_logs) == pytest.approx(183.33, 0.1)

def test_error_rate():
    assert error_rate(sample_logs) == pytest.approx(33.33, 0.1)
