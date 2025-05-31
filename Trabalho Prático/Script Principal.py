import csv

def carregar_usuarios():
    usuarios = {}
    try:
        with open('usuarios.csv', 'r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                usuarios[int(linha['id'])] = {
                    'nome': linha['nome'],
                    'senha': linha['senha'],
                    'perfil': linha['perfil']
                }
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
    return usuarios

def salvar_usuarios(usuarios):
    with open('usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
        campos = ['id', 'nome', 'senha', 'perfil']
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        for id, dados in usuarios.items():
            linha = {'id': id, **dados}
            escritor.writerow(linha)

def carregar_produtos():
    produtos = {}
    try:
        with open('produtos.csv', 'r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                produtos[int(linha['id'])] = {
                    'nome': linha['nome'],
                    'preco': float(linha['preco']),
                    'quantidade': int(linha['quantidade'])
                }
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
    return produtos

def salvar_produtos(produtos):
    with open('produtos.csv', 'w', newline='', encoding='utf-8') as arquivo:
        campos = ['id', 'nome', 'preco', 'quantidade']
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        for id, dados in produtos.items():
            linha = {'id': id, **dados}
            escritor.writerow(linha)

def login(usuarios):
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    for id, dados in usuarios.items():
        if dados['nome'] == nome and dados['senha'] == senha:
            print(f"Bem-vindo, {nome} ({dados['perfil']})!")
            return dados['perfil']
    print("Login inválido.")
    return None

def menu_usuarios(usuarios):
    while True:
        print("\n==== Gerenciamento de Usuários ====")
        print("[1] Listar")
        print("[2] Adicionar")
        print("[3] Atualizar")
        print("[4] Remover")
        print("[0] Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            for id, dados in usuarios.items():
                print(f"ID: {id}, Nome: {dados['nome']}, Perfil: {dados['perfil']}")
        elif opcao == '2':
            id = max(usuarios.keys(), default=0) + 1
            nome = input("Nome: ")
            senha = input("Senha: ")
            perfil = input("Perfil (gerente/analista/tecnico): ")
            usuarios[id] = {'nome': nome, 'senha': senha, 'perfil': perfil}
            salvar_usuarios(usuarios)
            print("Usuário adicionado.")
        elif opcao == '3':
            id = int(input("ID do usuário a atualizar: "))
            if id in usuarios:
                nome = input("Novo nome: ")
                senha = input("Nova senha: ")
                perfil = input("Novo perfil: ")
                usuarios[id] = {'nome': nome, 'senha': senha, 'perfil': perfil}
                salvar_usuarios(usuarios)
                print("Usuário atualizado.")
            else:
                print("ID não encontrado.")
        elif opcao == '4':
            id = int(input("ID do usuário a remover: "))
            if id in usuarios:
                usuarios.pop(id)
                salvar_usuarios(usuarios)
                print("Usuário removido.")
            else:
                print("ID não encontrado.")
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

def menu_produtos(produtos):
    while True:
        print("\n==== Gerenciamento de Produtos ====")
        print("[1] Listar")
        print("[2] Adicionar")
        print("[3] Atualizar")
        print("[4] Remover")
        print("[5] Buscar por nome")
        print("[6] Ordenar por nome")
        print("[7] Ordenar por preço")
        print("[0] Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            for id, dados in produtos.items():
                print(f"ID: {id}, Nome: {dados['nome']}, Preço: {dados['preco']}, Qtd: {dados['quantidade']}")
        elif opcao == '2':
            id = max(produtos.keys(), default=0) + 1
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            produtos[id] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
            salvar_produtos(produtos)
            print("Produto adicionado.")
        elif opcao == '3':
            id = int(input("ID do produto a atualizar: "))
            if id in produtos:
                nome = input("Novo nome: ")
                preco = float(input("Novo preço: "))
                quantidade = int(input("Nova quantidade: "))
                produtos[id] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
                salvar_produtos(produtos)
                print("Produto atualizado.")
            else:
                print("ID não encontrado.")
        elif opcao == '4':
            id = int(input("ID do produto a remover: "))
            if id in produtos:
                produtos.pop(id)
                salvar_produtos(produtos)
                print("Produto removido.")
            else:
                print("ID não encontrado.")
        elif opcao == '5':
            nome = input("Digite o nome para buscar: ").lower()
            for id, dados in produtos.items():
                if nome in dados['nome'].lower():
                    print(f"ID: {id}, Nome: {dados['nome']}, Preço: {dados['preco']}, Qtd: {dados['quantidade']}")
        elif opcao == '6':
            ordenado = sorted(produtos.items(), key=lambda x: x[1]['nome'])
            for id, dados in ordenado:
                print(f"ID: {id}, Nome: {dados['nome']}, Preço: {dados['preco']}, Qtd: {dados['quantidade']}")
        elif opcao == '7':
            ordenado = sorted(produtos.items(), key=lambda x: x[1]['preco'])
            for id, dados in ordenado:
                print(f"ID: {id}, Nome: {dados['nome']}, Preço: {dados['preco']}, Qtd: {dados['quantidade']}")
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

def main():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()

    perfil = login(usuarios)

    if perfil:
        while True:
            print("\n==== Menu Principal ====")
            print("[1] Gerenciar Produtos")
            if perfil == 'gerente':
                print("[2] Gerenciar Usuários")
            print("[0] Sair")
            opcao = input("Escolha: ")

            if opcao == '1':
                menu_produtos(produtos)
            elif opcao == '2' and perfil == 'gerente':
                menu_usuarios(usuarios)
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    main()
