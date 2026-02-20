# 🔐 Advanced Password Strength Analyzer & Custom Wordlist Generator

## 📌 Project Overview
This project is a Python-based security tool developed to analyze password strength and generate custom attack-style wordlists. It combines entropy-based password evaluation, configurable policy validation, and advanced combinational leetspeak wordlist generation.

The tool includes both CLI and GUI interfaces and demonstrates both defensive and offensive password security concepts.

---

## 🚀 Key Features

### 🔹 Password Strength Analyzer
- Policy-based validation using config.json
- Regex-based character checks
- Entropy calculation (mathematical password strength measurement)
- Strength classification (Weak / Moderate / Strong)
- Score system (0–5)
- GUI visualization

### 🔹 Custom Wordlist Generator
- Accepts user-specific inputs:
  - Name
  - Pet Name
  - Birth Year
  - Keyword
- Generates permutations of inputs
- Implements advanced combinational leetspeak transformations
- Appends year variations
- Removes duplicates automatically
- Exports output to `custom_wordlist.txt`
- Displays success popup with total count

---

## 🛠 Technologies Used
- Python 3
- Tkinter (GUI Development)
- Regex (Pattern Validation)
- itertools (Combinational Logic)
- JSON (Configuration Management)

---

## 📂 Project Structure

```
main.py                 # CLI version
gui.py                  # GUI interface
wordlist_generator.py   # Wordlist generation logic
config.json             # Password policy configuration
README.md
```

---

## ▶️ How to Run

### Run GUI Version:
```bash
python gui.py
```

### Run CLI Version:
```bash
python main.py
```

---

## 📊 Example Results
- Entropy Output: ~98+ bits (strong passwords)
- Generated Wordlist: 2800+ passwords (depending on input complexity)

---

## 🎯 Learning Outcomes
- Understanding password entropy calculation
- Implementing policy-based validation
- Developing GUI applications using Tkinter
- Building modular Python architecture
- Simulating real-world password attack patterns

---

## ⚠️ Disclaimer
This project is developed strictly for educational and cybersecurity awareness purposes.