import re

def parse_logs(file_path):
    failed_attempts = []

    with open(file_path, "r") as file:
        logs = file.readlines()

    for line in logs:
        if "Failed password" in line:
            match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ip = match.group(1)
                failed_attempts.append(ip)

    return failed_attempts