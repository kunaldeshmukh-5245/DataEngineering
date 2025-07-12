from utils.file_reader import read_json_logs
from utils.analytics import (
    count_status_codes,
    top_n_ips,
    top_n_urls,
    avg_response_time,
    error_rate
)
from utils.alerting import detect_error_spike, detect_slow_responses

import csv
import os
from datetime import datetime

def write_summary_to_csv(logs, error_alert, slow_alert):
    report_path = "output/reports/daily_summary.csv"
    file_exists = os.path.isfile(report_path)

    from utils.analytics import (
        avg_response_time,
        error_rate,
        top_n_ips,
        top_n_urls,
        count_status_codes,
    )

    top_ip = top_n_ips(logs, n=1)[0][0] if top_n_ips(logs, 1) else "N/A"
    top_url = top_n_urls(logs, n=1)[0][0] if top_n_urls(logs, 1) else "N/A"

    summary = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_logs": len(logs),
        "avg_response_time": avg_response_time(logs),
        "error_rate": error_rate(logs),
        "error_alert": error_alert,
        "slow_alert": slow_alert,
        "top_ip": top_ip,
        "top_url": top_url
    }

    with open(report_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=summary.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(summary)


def main():
    file_path = "data/sample_logs.txt"
    logs = read_json_logs(file_path)

    print(f"\n✅ Total logs read: {len(logs)}")
    print(f"📊 Status Code Counts: {count_status_codes(logs)}")
    print(f"🌐 Top IPs: {top_n_ips(logs)}")
    print(f"🔗 Top URLs: {top_n_urls(logs)}")
    print(f"⏱️ Avg Response Time: {avg_response_time(logs)} ms")
    print(f"❗ Error Rate: {error_rate(logs)} %")

    # Alerts
    print("\n🔔 ALERT CHECKS")
    err_alert, err_msg = detect_error_spike(logs)
    slow_alert, slow_msg = detect_slow_responses(logs)
    print("🚨" if err_alert else "✅", err_msg)
    print("🚨" if slow_alert else "✅", slow_msg)

    # Reporting
    write_summary_to_csv(logs, err_alert, slow_alert)
    print("📁 Report written to output/reports/daily_summary.csv ✅")


if __name__ == "__main__":
    main()
