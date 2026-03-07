from log_parser import parse_logs
from detector import detect_bruteforce
from report_generator import generate_report

def main():
    print("=== Log File Analyzer for Intrusion Detection ===\n")

    log_file = "sample_log.txt"

    failed_ips = parse_logs(log_file)

    suspicious_ips, ip_counts = detect_bruteforce(failed_ips)

    report = generate_report(len(failed_ips), suspicious_ips, ip_counts)

    print(report)

if __name__ == "__main__":
    main()