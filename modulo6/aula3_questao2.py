enderecos= []

while True:
    entrada = input('Digite um endereço WEB (URL) ou "fim": ')
    if entrada.lower() == 'fim':
        break
    else:
            url = (entrada)
            enderecos.append(url)
            dominio=[url[4:-4] for url in enderecos]

print(f'URLs: {enderecos}')
print(f'Dominios: {dominio}')