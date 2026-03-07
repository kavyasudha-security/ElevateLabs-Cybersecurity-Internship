def generate_report(total_attempts, suspicious_ips, ip_counts):

    report = []
    report.append("=== Intrusion Detection Report ===\n")

    report.append(f"Total Failed Login Attempts: {total_attempts}\n")

    report.append("IP Attempt Counts:")
    for ip, count in ip_counts.items():
        report.append(f"{ip} -> {count} attempts")

    report.append("\nSuspicious IPs (Possible Brute Force):")

    if suspicious_ips:
        for ip, data in suspicious_ips.items():
            risk_level, count = data
            report.append(f"{ip} -> {count} attempts ({risk_level})")
    else:
        report.append("No brute-force attacks detected.")

    report_text = "\n".join(report)

    with open("intrusion_report.txt", "w") as f:
        f.write(report_text)

    return report_text