from audit_checks import run_all_checks
from report_generator import generate_report


def main():
    print("=== Linux Hardening Audit Tool v1.0 ===\n")

    results, compliance = run_all_checks()

    report = generate_report(results, compliance)

    print("\nReport saved as audit_report.txt")


if __name__ == "__main__":
    main()
