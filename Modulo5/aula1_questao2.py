import random, math

n= int(input('Insira o número de valores: '))
soma=0

print("Números gerados:")
for i in range(n):
    numero = random.randint(0, 100)
    print(numero)
    soma += numero

raiz = math.sqrt(soma)

print(f"\nSoma dos números: {soma}")
print(f"Raiz quadrada da soma: {raiz:.2f}")