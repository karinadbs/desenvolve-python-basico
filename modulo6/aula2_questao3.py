import random


lista1, lista2, interseccao= [],[],[]

for i in range (20):
    lista1.append(random.randint(0,50))
    lista2.append(random.randint(0,50))

for elemento in lista1:
    if elemento in lista2:
        interseccao.append(elemento)
        
print (lista1, lista2)

for elemento in interseccao:
        interseccao.sort()
        print (interseccao)
        break
print ('Lista 1')
for elemento in lista1:    
    print (f'{elemento:} {lista1.count(elemento)}')

print ('Lista 2')
for elemento in lista2:
    print (f'{elemento:} {lista2.count(elemento)}')