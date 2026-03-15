# Secure Encryption Tool for Data Storage

## Overview
The Secure Encryption Tool is a Python-based application designed to encrypt and decrypt sensitive files using strong cryptographic techniques. The tool uses the Fernet encryption method from the cryptography library, which implements AES-based symmetric encryption.

This project demonstrates how sensitive data can be protected using encryption to ensure confidentiality and secure storage.

## Features
- Encrypts files using AES-based encryption
- Generates a secure encryption key
- Decrypts encrypted files using the stored key
- Command-line interface for user interaction
- Prevents unauthorized access to stored data

## Technologies Used
- Python
- Cryptography Library (Fernet encryption)
- File Handling

## Project Structure
Week4_Encryption_Tool
│
├── main.py
├── encryptor.py
├── decryptor.py
├── sample_data.txt
├── README.md
└── .gitignore

## How the Tool Works

1. The program generates a secure encryption key.
2. The selected file is encrypted using the generated key.
3. The encrypted data is stored in a binary file.
4. When the user chooses to decrypt, the stored key is used to restore the original data.
5. The decrypted file is saved for user access.

## Example Workflow

Encrypt File:
- Generates encryption key
- Encrypts sample_data.txt
- Creates encrypted_data.bin

Decrypt File:
- Reads encrypted_data.bin
- Uses stored key
- Restores decrypted_data.txt

## Learning Outcomes

- Understanding of file encryption concepts
- Implementation of AES-based encryption
- Secure key management
- Python-based cybersecurity automation

## Author
Cybersecurity Internship Project