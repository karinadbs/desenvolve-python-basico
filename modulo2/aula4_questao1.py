##comprimento do terreno
comprimento= int(input("Digite o comprimento do terreno: "))

#largura do terreno
largura= int(input("Digite a largura do terreno: "))

#valor do terreno
preco_m2=int(input("Digite o preço do m2: "))

#fórmulas
area = comprimento * largura
preco_total = preco_m2 * area

print (f'O terreno possui ({area})m2 e custa R${preco_total:,.2f}')