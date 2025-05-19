import random
import os

def carrega_palavras(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        return [linha.strip().lower() for linha in f if linha.strip()]

def carrega_enforcado(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()
        return conteudo.strip().split("\n\n")

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogo_forca():
    palavras = carrega_palavras("gabarito_forca.txt")
    estagios = carrega_enforcado("gabarito_enforcado.txt")

    palavra_secreta = random.choice(palavras)
    letras_descobertas = ["_" for _ in palavra_secreta]
    letras_erradas = []
    tentativas = 0
    max_erros = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra_secreta), "letras.")
    print(" ".join(letras_descobertas))

    while tentativas < max_erros and "_" in letras_descobertas:
        letra = input("Digite uma letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, digite apenas uma letra válida.")
            continue

        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_descobertas[i] = letra
            print("Acertou!")
        else:
            tentativas += 1
            letras_erradas.append(letra)
            print("Errou!")
            imprime_enforcado(tentativas, estagios)

        print("Palavra:", " ".join(letras_descobertas))
        print("Letras erradas:", ", ".join(letras_erradas))
        print("-" * 40)

    if "_" not in letras_descobertas:
        print("Parabéns! Você venceu! A palavra era:", palavra_secreta)
    else:
        print("Você perdeu! A palavra era:", palavra_secreta)
        imprime_enforcado(tentativas, estagios)

jogo_forca()