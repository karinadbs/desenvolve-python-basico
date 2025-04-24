import random

num_elementos = random.randint(5,20)

elementos = [random.randint(1,10) for i in range(num_elementos)]

print(elementos)

soma=0

for i in (elementos):
    soma+=i

print(f'A soma dos valores da lista é: {soma}')

media=0

for i in (elementos):
    media+=i/len(elementos)
  

print(f'A média dos valores da lista é: {media}')