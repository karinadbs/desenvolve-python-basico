import datetime

data_atual = datetime.datetime.now()
print (f'Data: {data_atual.strftime("%d/%m/%Y")}')
print (f'Hora: {data_atual.strftime("%H:%M:%S")}')