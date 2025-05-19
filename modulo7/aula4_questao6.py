import csv

arquivo = "spotify-2023.csv"

top_musicas_por_ano = {}

with open(arquivo, encoding='latin-1') as f:
    leitor = csv.reader(f)
    
    print("Primeiras 5 linhas do arquivo:")
    for i, linha in enumerate(leitor):
        print(linha)
        if i == 4:
            break

with open(arquivo, encoding='latin-1') as f:
    leitor = csv.reader(f)
    cabecalho = next(leitor)
    for linha in leitor:
        if len(linha) < 9:
            continue
        
        track_name = linha[0]
        artist_name = linha[1]
        artist_count = linha[2]
        released_year = linha[3]
        streams = linha[8]
        if track_name.startswith('"') or artist_name.startswith('"'):
            continue
        
        try:
            ano = int(released_year)
            streams_int = int(streams)
        except ValueError:
            continue
        if ano < 2012 or ano > 2022:
            continue
        if (ano not in top_musicas_por_ano) or (streams_int > top_musicas_por_ano[ano][3]):
            top_musicas_por_ano[ano] = [track_name, artist_name, ano, streams_int]

lista_final = [top_musicas_por_ano[ano] for ano in sorted(top_musicas_por_ano.keys())]

print("\nMúsicas mais tocadas por ano de 2012 a 2022:")
for musica in lista_final:
    print(musica)