from datetime import datetime
import json

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def generate_report(results, compliance_percentage):
    report = []
    json_report = {
        "generated_on": str(datetime.now()),
        "checks": [],
        "compliance_score": compliance_percentage,
        "system_status": ""
    }

    print(f"{BLUE}==== Linux Hardening Audit Report ===={RESET}")
    print(f"Generated on: {datetime.now()}\n")

    report.append("==== Linux Hardening Audit Report ====")
    report.append(f"Generated on: {datetime.now()}")
    report.append("")

    for check in results:
        name, status, message, recommendation = check

        # Color selection
        if status == "PASS":
            color = GREEN
        elif status == "FAIL":
            color = RED
        else:
            color = YELLOW

        print(f"{color}[{status}] {name} - {message}{RESET}")

        if status == "FAIL":
            print(f"  {RED}Recommendation: {recommendation}{RESET}")

        report.append(f"[{status}] {name} - {message}")
        if status == "FAIL":
            report.append(f"  Recommendation: {recommendation}")
        report.append("")

        json_report["checks"].append({
            "name": name,
            "status": status,
            "message": message,
            "recommendation": recommendation
        })

    report.append(f"Overall Compliance Score: {compliance_percentage:.2f}%")

    if compliance_percentage == 100:
        system_status = "SECURE"
        color = GREEN
    elif compliance_percentage >= 70:
        system_status = "MODERATE RISK"
        color = YELLOW
    else:
        system_status = "HIGH RISK"
        color = RED

    json_report["system_status"] = system_status

    print(f"\nOverall Compliance Score: {compliance_percentage:.2f}%")
    print(f"{color}System Status: {system_status}{RESET}")

    report.append(f"System Status: {system_status}")

    report_text = "\n".join(report)

    # Save TXT report
    with open("audit_report.txt", "w") as f:
        f.write(report_text)

    # Save JSON report
    with open("audit_report.json", "w") as f:
        json.dump(json_report, f, indent=4)

    print("\nReport saved as audit_report.txt and audit_report.json")

    return report_text
