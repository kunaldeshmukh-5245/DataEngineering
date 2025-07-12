

def detect_error_spike(logs, threshold=10):
    """
    Detects if there is an error spike in the logs.
    An error spike is defined as a percentage of error requests exceeding a threshold.
    """
    from .analytics import error_rate

    rate = error_rate(logs)
    if rate > threshold:
        return True,f"⚠️ High Error Rate! Error rate: {rate}% exceeds threshold of {threshold}%"
    return False,"✅ No error spike detected."

def detect_slow_responses(logs, threshold=500):
    """
    Detects if there are slow responses in the logs.
    A slow response is defined as a response time exceeding a threshold.
    """
    from .analytics import avg_response_time

    avg_time = avg_response_time(logs)
    if avg_time > threshold:
        return True, f"⚠️ Slow Response Alert! Average response time: {avg_time} ms exceeds threshold of {threshold} ms"
    return False, "✅ No slow responses detected."
