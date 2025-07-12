
from collections import Counter
from statistics import mean

def count_status_codes(logs):
    """
    Returns a dictionary of status code counts.
    """
    status_counts = Counter()
    for log in logs:
        status = log.get("status")
        if status:
            status_counts[status] += 1
    return dict(status_counts)

def top_n_ips(logs, n=10):
    """
    Returns the top n IP addresses by request count.
    """
    ip_counts = Counter(log.get("ip")for log in logs if log.get("ip"))
    return ip_counts.most_common(n)

def top_n_urls(logs, n=10):
    """
    Returns the top n URLs by request count.
    """
    url_counts = Counter(log.get("url") for log in logs if log.get("url"))
    return url_counts.most_common(n)

def avg_response_time(logs):
    """
    Returns the average response time from the logs.
    """
    times = [log.get("response_time") for log in logs if isinstance(log.get("response_time"), (int, float))]
    return round(mean(times), 2) if times else 0

def error_rate(logs):
    """
    Returns the error rate as a percentage of total requests.
    """
    total_requests = len(logs)
    if total_requests == 0:
        return 0
    error_requests = [log for log in logs if 400 <= log.get("status", 0) < 600]
    return round((len(error_requests) / total_requests) * 100, 2)