import os
import re

arquivo_entrada = os.path.abspath("frase.txt")
arquivo_saida = os.path.abspath("palavras.txt")

with open(arquivo_entrada, "r", encoding="utf-8") as f:
    frase = f.read()
palavras = re.findall(r'\b[a-zA-ZÀ-ÿ]+\b', frase)

with open(arquivo_saida, "w", encoding="utf-8") as f:
    for palavra in palavras:
        f.write(palavra + "\n")

with open(arquivo_saida, "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)