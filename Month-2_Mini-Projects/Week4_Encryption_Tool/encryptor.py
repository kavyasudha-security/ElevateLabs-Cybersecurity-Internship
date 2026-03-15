from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    return key

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    with open("encrypted_data.bin", "wb") as file:
        file.write(encrypted)

    print("File encrypted successfully.")