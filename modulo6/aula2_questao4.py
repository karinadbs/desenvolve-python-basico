lista1, lista2, lista3 = [], [], []

quantidade = int(input('Digite a quantidade de elementos da lista 1: '))
print(f'Digite os {quantidade} elementos da lista 1:')
for i in range(quantidade):
    lista1.append(int(input()))

quantidade2 = int(input('Digite a quantidade de elementos da lista 2: '))
print(f'Digite os {quantidade2} elementos da lista 2:')
for i in range(quantidade2):
    lista2.append(int(input()))

tamanho_max = max(len(lista1), len(lista2))
for i in range(tamanho_max):
    if i < len(lista1):
        lista3.append(lista1[i])
    if i < len(lista2):
        lista3.append(lista2[i])

print("Lista intercalada:", *lista3)