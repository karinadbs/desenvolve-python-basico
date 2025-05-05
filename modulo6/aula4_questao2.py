frase = input("Digite uma frase: ")

vogais_lista = 'aeiou'

vogais = sorted([letra.lower() for letra in frase if letra in vogais_lista and letra.isalpha( )])

consoantes = [letra for letra in frase if letra and letra not in vogais_lista and letra.isalpha( )]

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")