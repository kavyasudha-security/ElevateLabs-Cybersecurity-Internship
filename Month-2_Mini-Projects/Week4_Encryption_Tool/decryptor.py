from cryptography.fernet import Fernet
from encryptor import load_key

def decrypt_file():
    key = load_key()
    fernet = Fernet(key)

    with open("encrypted_data.bin", "rb") as file:
        encrypted_data = file.read()

    decrypted = fernet.decrypt(encrypted_data)

    with open("decrypted_data.txt", "wb") as file:
        file.write(decrypted)

    print("File decrypted successfully.")