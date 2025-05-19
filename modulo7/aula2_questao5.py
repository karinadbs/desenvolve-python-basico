import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []

    for palavra in palavras:
        if len(palavra) <= 3:
            nova_frase.append(palavra)
        else:
            inicio = palavra[0]
            meio = list(palavra[1:-1])
            fim = palavra[-1]
            
            random.shuffle(meio)
            palavra_embaralhada = inicio + ''.join(meio) + fim
            nova_frase.append(palavra_embaralhada)

    return ' '.join(nova_frase)

frase = "Python é uma linguagem de programação"

resultado = embaralhar_palavras(frase)

print(resultado)