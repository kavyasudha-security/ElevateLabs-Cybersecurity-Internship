import tkinter as tk
from tkinter import messagebox
import math
import re
import json
from wordlist_generator import generate_wordlist

# Load config
def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

policy = load_config()


# Password evaluation logic
def check_password(password, policy):
    score = 0
    feedback = []

    if len(password) >= policy["min_length"]:
        score += 1
    else:
        feedback.append("Password is too short.")

    if policy["require_uppercase"] and re.search(r"[A-Z]", password):
        score += 1
    elif policy["require_uppercase"]:
        feedback.append("Add at least one uppercase letter.")

    if policy["require_lowercase"] and re.search(r"[a-z]", password):
        score += 1
    elif policy["require_lowercase"]:
        feedback.append("Add at least one lowercase letter.")

    if policy["require_digits"] and re.search(r"[0-9]", password):
        score += 1
    elif policy["require_digits"]:
        feedback.append("Add at least one digit.")

    if policy["require_special"] and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    elif policy["require_special"]:
        feedback.append("Add at least one special character.")

    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score in [3, 4]:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return score, strength, feedback, color


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


def toggle_password():
    if entry.cget("show") == "":
        entry.config(show="*")
    else:
        entry.config(show="")


def evaluate_password():
    password = entry.get()

    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    score, strength, feedback, color = check_password(password, policy)
    entropy = calculate_entropy(password)

    strength_label.config(text=f"Strength: {strength}", fg=color)
    score_label.config(text=f"Score: {score} / 5")
    entropy_label.config(text=f"Entropy: {entropy} bits")

    if feedback:
        recommendations = "\n".join([f"- {item}" for item in feedback])
    else:
        recommendations = "Password meets all policy requirements."

    feedback_label.config(text=recommendations)


def generate_wordlist_gui():
    name = name_entry.get().strip()
    pet = pet_entry.get().strip()
    dob = dob_entry.get().strip()
    keyword = keyword_entry.get().strip()

    # Ensure at least one field is filled
    if not any([name, pet, dob, keyword]):
        messagebox.showwarning("Input Error", "Please enter at least one field.")
        return

    try:
        count = generate_wordlist(name, pet, dob, keyword)

        messagebox.showinfo(
            "Success",
            f"Generated {count} passwords.\nSaved to custom_wordlist.txt"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("Password Policy Validator")
root.geometry("500x450")
root.configure(bg="#f4f6f7")

title_label = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Segoe UI", 18, "bold"),
    bg="#f4f6f7"
)
title_label.pack(pady=15)

entry = tk.Entry(root, width=30, show="*", font=("Segoe UI", 12))
entry.pack(pady=10)

toggle_button = tk.Button(
    root,
    text="Show / Hide",
    command=toggle_password
)
toggle_button.pack(pady=5)

check_button = tk.Button(
    root,
    text="Evaluate Password",
    font=("Segoe UI", 11, "bold"),
    bg="#2e86c1",
    fg="white",
    padx=10,
    pady=5,
    command=evaluate_password
)
check_button.pack(pady=15)

score_label = tk.Label(root, text="", font=("Segoe UI", 12), bg="#f4f6f7")
score_label.pack()

strength_label = tk.Label(root, text="", font=("Segoe UI", 12, "bold"), bg="#f4f6f7")
strength_label.pack()

entropy_label = tk.Label(root, text="", font=("Segoe UI", 12), bg="#f4f6f7")
entropy_label.pack(pady=5)

feedback_label = tk.Label(
    root,
    text="",
    justify="left",
    wraplength=450,
    bg="#f4f6f7",
    font=("Segoe UI", 11)
)
feedback_label.pack(pady=15)


tk.Label(root, text="Custom Wordlist Generator", font=("Segoe UI", 14, "bold"), bg="#f4f6f7").pack(pady=(20,5))

tk.Label(root, text="Name:", bg="#f4f6f7").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Pet Name:", bg="#f4f6f7").pack()
pet_entry = tk.Entry(root)
pet_entry.pack()

tk.Label(root, text="Birth Year (YYYY):", bg="#f4f6f7").pack()
dob_entry = tk.Entry(root)
dob_entry.pack()

tk.Label(root, text="Keyword:", bg="#f4f6f7").pack()
keyword_entry = tk.Entry(root)
keyword_entry.pack(pady=(0,10))

tk.Button(
    root,
    text="Generate Wordlist",
    bg="#28a745",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=generate_wordlist_gui
).pack(pady=10)

root.mainloop()