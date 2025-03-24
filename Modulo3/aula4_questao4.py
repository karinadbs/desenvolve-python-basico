distancia= int(input('Digite a distância da entrega em KM: '))
peso= int(input("Digite o peso do pacote em kg: "))

if (distancia<=100):
    frete=peso*1
    if(peso>10):
        frete=frete+10
    print(f'O valor do frete é de R${frete}')
    
if (distancia>100 and distancia<=300):
    frete=peso*1.5
    if(peso>10):
        frete=frete+10
    print(f'O valor do frete é de R${frete}')
    
if (distancia>300):
    frete=peso*2
    if(peso>10):
        frete=frete+10
    print(f'O valor do frete é de R${frete}')
               