from collections import Counter

def detect_bruteforce(failed_ips):
    ip_counts = Counter(failed_ips)

    suspicious_ips = {}

    for ip, count in ip_counts.items():
        if count >= 5:
            suspicious_ips[ip] = ("HIGH RISK", count)
        elif count >= 3:
            suspicious_ips[ip] = ("MEDIUM RISK", count)

    return suspicious_ips, ip_counts