livros = [
    ("O Caçador de Pipas", "Khaled Hosseini", 2003, 368),
    ("Torto Arado", "Itamar Vieira Junior", 2019, 264),
    ("1984", "George Orwell", 1949, 328),
    ("Dom Casmurro", "Machado de Assis", 1899, 256),
    ("A Revolução dos Bichos", "George Orwell", 1945, 112),
    ("Grande Sertão: Veredas", "João Guimarães Rosa", 1956, 624),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96),
    ("Capitães da Areia", "Jorge Amado", 1937, 272),
    ("Ensaio sobre a Cegueira", "José Saramago", 1995, 312),
    ("A Menina que Roubava Livros", "Markus Zusak", 2005, 480)
]

nome_arquivo = "meus_livros.csv"

with open(nome_arquivo, "w", encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
        f.write(linha)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")