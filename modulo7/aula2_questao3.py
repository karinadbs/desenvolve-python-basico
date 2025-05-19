import string

def limpar_texto(texto):

    texto = texto.lower()
    texto = ''.join(c for c in texto if c.isalnum())
    return texto

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    if frase.lower() == "fim":
        break

    frase_limpa = limpar_texto(frase)
    if frase_limpa == frase_limpa[::-1]:
        print(f'"{frase}" é palíndromo\n')
    else:
        print(f'"{frase}" não é palíndromo\n')