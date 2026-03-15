from encryptor import generate_key, encrypt_file
from decryptor import decrypt_file

def main():
    print("=== Secure Encryption Tool ===")

    print("1. Encrypt File")
    print("2. Decrypt File")

    choice = input("Enter choice: ")

    if choice == "1":
        generate_key()
        encrypt_file("sample_data.txt")

    elif choice == "2":
        decrypt_file()

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()