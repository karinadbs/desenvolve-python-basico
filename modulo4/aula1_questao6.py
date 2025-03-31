n= int(input('Informe a quatidade de experimentos: '))
cont= 0
total_sapo, total_rato, total_coelho= 0,0,0

while cont<n:
    quantia=int(input('Inoforme a quatidade de cobaias: '))
    tipo=input('Informe o tipo da cobaia S-Sapo, R-Rato ou C-Coelho: ')
    
    if tipo=='S':
        total_sapo+=quantia
    elif tipo=='R':
        total_rato+=quantia       
    elif tipo=='C':
        total_coelho+=quantia

    cont+=1
#total= total_sapo+total_rato+total_coelho
#percentual_sapo= (total_sapo/total)*100
#percentual_rato= (total_rato/total)*100
#percentual_coelho= (total_coelho/total)*100

print(f'Total: {total_sapo+total_rato+total_coelho}')
print(f'Total de sapos: {total_sapo}')
print(f'Total de ratos: {total_rato}')
print(f'Total de coelhos: {total_coelho}')
print(f'Percentual de sapos: {(total_sapo/(total_sapo+total_rato+total_coelho))*100:.2F}%')
print(f'Percentual de ratos: {(total_rato/(total_sapo+total_rato+total_coelho))*100:.2F}%')
print(f'Percentual de coelhos: {(total_coelho/(total_sapo+total_rato+total_coelho))*100:.2F}%')        

