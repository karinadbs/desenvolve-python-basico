produto_1= input ('Digite o nome do produto 1: ')
preco_1= float(input ('Digite o preço unitário do produto 1: '))
quantidade_1= int(input ('Digite a quatidade do produto 1: '))
valortotal_1= float(preco_1*quantidade_1)

produto_2= input ('Digite o nome do produto 2: ')
preco_2= float(input ('Digite o preço unitário do produto 2: '))
quantidade_2= int(input ('Digite a quatidade do produto 2: '))
valortotal_2= float(preco_2*quantidade_2)

produto_3= input ('Digite o nome do produto 3: ')
preco_3= float(input ('Digite o preço unitário do produto 3: '))
quantidade_3= int(input ('Digite a quatidade do produto 3: '))
valortotal_3= float(preco_3*quantidade_3)

total= valortotal_1+valortotal_2+valortotal_3

print (f'Total R${total:,.2f}: ')