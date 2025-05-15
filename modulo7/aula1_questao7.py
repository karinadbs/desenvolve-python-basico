import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    
    nomes_criptografados = []

    for nome in nomes:
        nome_cript = ""
        for c in nome:
            novo_codigo = ord(c) + chave
            if novo_codigo > 126:
                novo_codigo = 33 + (novo_codigo - 127)
            nome_cript += chr(novo_codigo)
        nomes_criptografados.append(nome_cript)

    return nomes_criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
criptografados, chave = encrypt(nomes)

print("Chave de criptografia:", chave)
print("Nomes criptografados:", criptografados)