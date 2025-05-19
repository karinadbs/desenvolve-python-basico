import os

frase = input("Digite uma frase: ")

arquivo = "frase.txt"

caminho_absoluto = os.path.abspath(arquivo)

with open(caminho_absoluto, "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

print(f"Frase salva em {caminho_absoluto}")