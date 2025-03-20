genero= input('Informe o seu gênero (M ou F): ')
idade= int(input('Informe a sua idade: '))
tempo_servico= int(input('Informe o seu tempo de serviço (apenas anos): '))

pode_aposentar=(genero=='F' and idade>60)or(genero=='M' and idade>=65)or(tempo_servico>=30) or(idade>=60 and tempo_servico>=25)

print(f'Pode apondentar:{pode_aposentar}')