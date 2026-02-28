import subprocess


def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL)
        return result.decode().strip()
    except:
        return "Error"


def check_firewall():
    output = run_command("ufw status")
    if "Status: active" in output:
        return ("Firewall", "PASS", "UFW firewall is active.", "")
    else:
        return ("Firewall", "FAIL", "Firewall is not active.", "Enable firewall using: sudo ufw enable")


def check_ssh_root_login():
    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            data = f.read()
            if "PermitRootLogin no" in data:
                return ("SSH Root Login", "PASS", "Root login disabled.", "")
            else:
                return ("SSH Root Login", "FAIL", "Root login may be enabled.", "Set 'PermitRootLogin no' in /etc/ssh/sshd_config")
    except:
        return ("SSH Root Login", "ERROR", "Could not read SSH config.", "")


def check_password_policy():
    try:
        with open("/etc/login.defs", "r") as f:
            data = f.read()
            if "PASS_MAX_DAYS" in data:
                return ("Password Policy", "PASS", "Password aging policy configured.", "")
            else:
                return ("Password Policy", "FAIL", "Password aging policy missing.", "Configure PASS_MAX_DAYS in /etc/login.defs")
    except:
        return ("Password Policy", "ERROR", "Could not read login.defs.", "")


def check_suid_files():
    output = run_command("find / -perm -4000 -type f 2>/dev/null | wc -l")
    return ("SUID Files", "INFO", f"Number of SUID files found: {output}", "")


def check_world_writable():
    output = run_command("find / -xdev -type f -perm -0002 2>/dev/null | wc -l")
    return ("World Writable Files", "INFO", f"World-writable files found: {output}", "")


def check_uid_zero_accounts():
    try:
        with open("/etc/passwd", "r") as f:
            users = f.readlines()

        uid_zero_users = [line.split(":")[0] for line in users if ":0:" in line]

        if len(uid_zero_users) == 1 and uid_zero_users[0] == "root":
            return ("UID 0 Accounts", "PASS", "Only root has UID 0.", "")
        else:
            return ("UID 0 Accounts", "FAIL",
                    f"Multiple UID 0 accounts detected: {', '.join(uid_zero_users)}",
                    "Remove or restrict additional UID 0 accounts.")

    except:
        return ("UID 0 Accounts", "ERROR", "Could not read /etc/passwd.", "")


def check_listening_ports():
    output = run_command("ss -tuln | grep LISTEN | wc -l")
    return ("Listening Services", "INFO",
            f"Number of listening ports: {output}",
            "")


def run_all_checks():
    checks = [
        check_firewall(),
        check_ssh_root_login(),
        check_password_policy(),
        check_suid_files(),
        check_world_writable(),
        check_uid_zero_accounts(),
        check_listening_ports()
    ]

    score = 0
    max_score = 4  # Only PASS/FAIL checks count toward compliance

    for check in checks:
        if check[1] == "PASS":
            score += 1

    compliance_percentage = (score / max_score) * 100

    return checks, compliance_percentage
