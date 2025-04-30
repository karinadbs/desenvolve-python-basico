lista= []
lista_par= []
lista_impar= []

print("Digite pelo menos 4 números inteiros. Digite 'fim' para encerrar.")

while True:
    entrada = input("Digite um número ou 'fim': ")
    if entrada.lower() == 'fim':
        if len(lista) < 4:
            print("Você precisa digitar pelo menos 4 números.")
        else:
            break
    else:
            numero = int(entrada)
            lista.append(numero)

print(f'Lista original: {lista}')
print(f'Os 3 primeiros elementos: {lista[:3]}')
print(f'Os 2 últimos elementos: {lista[-2:]}')
print(f'A Lista invertida: {lista[::-1]}')

for i in range(len(lista)):
    if i % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])

print(f'Elementos de índice par: {lista_par}')
print(f'Elementos de índice ímpar: {lista_impar}')