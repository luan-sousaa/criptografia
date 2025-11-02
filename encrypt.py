#!/usr/bin/env python3
from cryptography.fernet import Fernet
import getpass

def main():
    # Você pode gerar uma nova chave ou colar uma existente.
    escolha = input("Gerar nova chave? (s/n) [s]: ").strip().lower() or "s"
    if escolha == "s":
        key = Fernet.generate_key()
        print("\n*** Guarde esta chave em local seguro (cole para a outra pessoa): ***")
        print(key.decode(), "\n")
    else:
        key = getpass.getpass("Cole a chave existente (será escondida enquanto digita): ").encode()

    f = Fernet(key)

    # Ler mensagem do usuário (pode colar texto grande)
    print("\nDigite/cole a mensagem (termina com Enter):")
    mensagem = input("> ").encode()

    token = f.encrypt(mensagem)

    print("\n*** Ciphertext (copie e envie para a outra pessoa): ***")
    # token já é base64 urlsafe; imprimimos como string
    print(token.decode())
    print("\nPronto — envie o ciphertext e passe a chave por outro canal seguro.")

if __name__ == "__main__":
    main()
