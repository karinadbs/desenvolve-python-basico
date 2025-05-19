import string

def validador_senha(senha):

    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in string.punctuation:
            tem_especial = True

    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))