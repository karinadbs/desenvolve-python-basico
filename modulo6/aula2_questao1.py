import random

lista = [random.randint(-100, 100) for i in range(20)]

lista_ordenada = sorted(lista)

indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

print(f'Lista ordenada (sem modificar a original): {lista_ordenada}')

print(f'Lista original: {lista}')

print(f"\nÍndice do maior valor ({max(lista)}): {indice_maior}")
print(f"Índice do menor valor ({min(lista)}): {indice_menor}")