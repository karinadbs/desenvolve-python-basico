import os
import re

arquivo = os.path.abspath("estomago.txt")

with open(arquivo, "r", encoding="utf-8") as f:
    linhas = f.readlines()

print("=== Primeiras 25 linhas ===\n")
for linha in linhas[:25]:
    print(linha.rstrip())
print("\n")

num_linhas = len(linhas)
print(f"Total de linhas: {num_linhas}")

linha_maior = max(linhas, key=len)
print("\n=== Linha com maior número de caracteres ===")
print(linha_maior.rstrip())
print(f"(Comprimento: {len(linha_maior.strip())} caracteres)")

texto_completo = ''.join(linhas)

nonato_count = len(re.findall(r'\bnonato\b', texto_completo, re.IGNORECASE))
iria_count = len(re.findall(r'\bíria\b', texto_completo, re.IGNORECASE))

print(f"\nNúmero de menções a 'Nonato': {nonato_count}")
print(f"Número de menções a 'Íria': {iria_count}")