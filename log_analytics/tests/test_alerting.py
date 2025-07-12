import pytest
from utils.alerting import detect_error_spike, detect_slow_responses

sample_logs = [
    {"status": 200, "response_time": 100},
    {"status": 500, "response_time": 300},
]

def test_detect_error_spike():
    alert, msg = detect_error_spike(sample_logs, threshold=20)
    assert alert is True
    assert "High Error Rate" in msg

def test_detect_slow_responses():
    alert, msg = detect_slow_responses(sample_logs, threshold=20)
    assert alert is True
    assert "Slow Response Alert" in msg
