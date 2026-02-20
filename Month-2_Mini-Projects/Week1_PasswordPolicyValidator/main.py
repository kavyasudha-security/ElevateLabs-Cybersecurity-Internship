import json
import re
import datetime
import math

def load_config():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print("Error loading config file:", e)
        exit()


def check_password(password, policy):
    score = 0
    feedback = []

    # Length check
    if len(password) >= policy["min_length"]:
        score += 1
    else:
        feedback.append("Password is too short.")

    # Uppercase check
    if policy["require_uppercase"] and re.search(r"[A-Z]", password):
        score += 1
    elif policy["require_uppercase"]:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if policy["require_lowercase"] and re.search(r"[a-z]", password):
        score += 1
    elif policy["require_lowercase"]:
        feedback.append("Add at least one lowercase letter.")

    # Digit check
    if policy["require_digits"] and re.search(r"[0-9]", password):
        score += 1
    elif policy["require_digits"]:
        feedback.append("Add at least one digit.")

    # Special character check
    if policy["require_special"] and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    elif policy["require_special"]:
        feedback.append("Add at least one special character.")

    # Strength classification
    if score <= 2:
        strength = "Weak (High Risk)"
    elif score in [3, 4]:
        strength = "Moderate (Needs Improvement)"
    else:
        strength = "Strong (Compliant)"

    return {
        "Score": score,
        "Strength": strength,
        "Feedback": feedback if feedback else ["Password meets all policy requirements."]
    }
def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def main():
    policy = load_config()

    print("=" * 40)
    print("Password Policy Validator Tool")
    print("Checking password against security policy...")
    print("=" * 40)

    while True:
        password = input("\nEnter password to evaluate (or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("Exiting tool. Stay secure.")
            break

        result = check_password(password, policy)
        entropy = calculate_entropy(password)

        print("\n" + "=" * 40)
        print("      PASSWORD EVALUATION REPORT")
        print("=" * 40)

        print(f"Score     : {result['Score']} / 5")
        print(f"Strength  : {result['Strength']}")
        print(f"Entropy  : {entropy} bits")
        print("\nRecommendations:")

        for item in result["Feedback"]:
            print(f"  - {item}")

        print("=" * 40)
        with open("evaluation_log.txt", "a") as log_file:
           log_file.write(
            f"{datetime.datetime.now()} | "
            f"Length: {len(password)} | "
            f"Score: {result['Score']} | "
            f"Strength: {result['Strength']}\n"
        )

if __name__ == "__main__":
    main()