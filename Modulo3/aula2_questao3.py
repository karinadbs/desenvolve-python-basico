idade= int(input('Digite a sua idade: '))
jogos_tabuleiro= input('Já jogou pelo menos 3 jogos de tabuleiro? (Digite True or False) ')
qtd_venceu= int(input('Quantos jogos já venceu? '))

venceu= (idade>=16 and idade<=18) and jogos_tabuleiro=='True' and qtd_venceu>=1

print (f'Apto para ingressar no clube de jogos de tabuleiro: {venceu}')