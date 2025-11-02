#!/usr/bin/env python3
from cryptography.fernet import Fernet
import getpass

def main():
    # A chave deve ser a mesma que foi usada para criptografar
    key = getpass.getpass("Cole a chave (será escondida enquanto digita): ").encode()

    # Ler ciphertext (token) — permite colar a string longa
    print("\nCole o ciphertext (copie do remetente) e pressione Enter:")
    token = input("> ").strip().encode()

    f = Fernet(key)
    try:
        plaintext = f.decrypt(token)
    except Exception:
        print("Falha ao descriptografar. Verifique chave e ciphertext.")
        return

    print("\n*** Mensagem descriptografada: ***")
    print(plaintext.decode())

if __name__ == "__main__":
    main()
