classe= input('Escolha a classe (guerreiro, mago ou arqueiro): ')
pontos_forca= int(input ('Digite os pontos de força (de 1 a 20): '))
pontos_magia= int(input('Digite os pontos de magia (de 1 a 20): '))



guerreiro= classe== 'guerreiro' and pontos_forca>=15 and pontos_magia<=10
magno= classe == 'magno' and pontos_forca<=10 and pontos_magia>=15
arqueiro= classe =='arqueiro' and (pontos_forca>5 and pontos_forca<=15) and (pontos_magia>5 and pontos_magia<=15)

print (f'Pontos de atributo consistentes com a classe guerreiro: {guerreiro}')
print (f'Pontos de atributo consistentes com a classe magno: {magno}')
print (f'Pontos de atributo consistentes com a classe arqueiro: {arqueiro}')