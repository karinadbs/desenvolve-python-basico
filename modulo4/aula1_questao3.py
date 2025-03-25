n1= float(input('Digite o valor de n1: '))
n2= float(input('Digite o valor de n2: '))
n3= float(input('Digite o valor de n3: '))

m= (n1+n2+n3)/3

while True:
    if(m>60):
        print('Aprovado')
        break
    elif (m>=40):
        print('Recuperação')
        break
    else:
        print('Reprovado')
        break
print ('Fim')