# Sistema simples de cadastro de usuários e produtos/serviços
# Trabalho Prático – Programação Básica para Web

# -------------------------
# Carregamento de dados
# -------------------------

def carregar_registros(arquivo):
    dados = []
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split(';')
                    dados.append(partes)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado. Será criado ao salvar.")
    return dados


def salvar_registros(arquivo, dados):
    with open(arquivo, 'w', encoding='utf-8') as f:
        for registro in dados:
            linha = ';'.join(registro)
            f.write(linha + '\n')

# -------------------------
# CRUD Usuários
# -------------------------

def listar_usuarios(usuarios):
    print("\n-- Lista de Usuários --")
    for u in usuarios:
        print(f"Nome: {u[0]} | Email: {u[1]}")


def criar_usuario(usuarios):
    nome = input("Nome do usuário: ")
    email = input("Email do usuário: ")
    usuarios.append([nome, email])
    print("Usuário cadastrado com sucesso!")


def remover_usuario(usuarios):
    email = input("Digite o email do usuário a remover: ")
    for u in usuarios:
        if u[1] == email:
            usuarios.remove(u)
            print("Usuário removido!")
            return
    print("Usuário não encontrado.")

# -------------------------
# CRUD Produtos
# -------------------------

def listar_produtos(produtos):
    print("\n-- Lista de Produtos/Serviços --")
    for p in produtos:
        print(f"Nome: {p[0]} | Preço: R${p[1]}")


def criar_produto(produtos):
    nome = input("Nome do produto/serviço: ")
    preco = input("Preço: ")
    produtos.append([nome, preco])
    print("Produto cadastrado com sucesso!")


def remover_produto(produtos):
    nome = input("Digite o nome do produto a remover: ")
    for p in produtos:
        if p[0] == nome:
            produtos.remove(p)
            print("Produto removido!")
            return
    print("Produto não encontrado.")

# -------------------------
# Menu Principal
# -------------------------

def main():
    usuarios = carregar_registros("usuarios.txt")
    produtos = carregar_registros("produtos.txt")

    while True:
        print("\n===== Sistema Empresa =====")
        print("1 - Listar usuários")
        print("2 - Cadastrar usuário")
        print("3 - Remover usuário")
        print("4 - Listar produtos/serviços")
        print("5 - Cadastrar produto/serviço")
        print("6 - Remover produto/serviço")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == '1': listar_usuarios(usuarios)
        elif op == '2': criar_usuario(usuarios)
        elif op == '3': remover_usuario(usuarios)
        elif op == '4': listar_produtos(produtos)
        elif op == '5': criar_produto(produtos)
        elif op == '6': remover_produto(produtos)
        elif op == '0':
            salvar_registros("usuarios.txt", usuarios)
            salvar_registros("produtos.txt", produtos)
            print("Saindo... Dados Salvos!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
