import csv

ARQUIVO = 'livros.csv'

cabecalho = ["titulo", "autor", "codigo", "ano", "status"]

livros = []

# Cadastra um novo livro
def cadastro_livros (titulo, autor, codigo, ano, status = "Disponivel"):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "codigo": codigo,
        "ano": ano, 
        "status": status,
    }
    livros.append(livro)
    return livro

# Busca um livro pelo título
def buscar_livro(titulo):
    for livro in livros:
        if livro["titulo"] == titulo:
            return livro
    return None

# Salva os livros no arquivo CSV
def salvar_livros(livros):
    arquivo = open(ARQUIVO, 'w', encoding='UTF-8', newline='')
    escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
    escritor.writeheader()
    for livro in livros: 
        escritor.writerow(livro)
    arquivo.close()

# Carrega os livros do arquivo CSV
def carregar_livros():
    arquivo = open(ARQUIVO, 'r')
    leitor = csv.DictReader(arquivo)
    livros_carregados = []
    for livro in leitor: 
        livros_carregados.append(livro)
    arquivo.close()
    return livros_carregados 

# Mostra todos os livros
def listar_livros(livros):
    for livro in livros:
        print(livro)
    return livros 

# Ordena os livros pelo título, autor ou ano
def ordenar_livros(livros, criterio):
    livros_ordenados = sorted(livros, key=lambda livro: livro[criterio])
    return livros_ordenados

# Mostra o menu da biblioteca e executa as opções escolhidas pelo usuário
def menu():
    while True:
        print("----------MENU----------")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("4 - Emprestar livro")
        print("5 - Devolver livro")
        print("6 - Ordenar livros")
        print("7 - Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            titulo = input ("Digite o título: ")
            autor = input ("Digite o autor: ")
            codigo = input("Digite o código: ")
            ano = input ("Digite o ano: ")

            cadastro_livros(titulo, autor, codigo, ano)
            salvar_livros(livros)
            print ("Livro cadastrado!")

        elif opcao == 2: 
            listar_livros(livros)  

        elif opcao == 3: 
            titulo = input("Digite o título do livro: ")
            livro = buscar_livro(titulo)
            if livro: 
                print(livro)
            else: 
                print("Livro não econtrado!")

        elif opcao == 4: 
            # Empresta um livro disponível 
            titulo = input("Digite o título do livro: ")
            livro = buscar_livro(titulo)
            print("Títlo digitado:", titulo)
            print("Livros na lista:", livros)
            print("Resultado na busca:", livro)
            print(livro)
            if livro:
                print("STATUS:", repr(livro["status"]))
                if livro["status"] == "Disponivel":
                    livro["status"] = "Emprestado"
                    salvar_livros(livros)
                    print("Livro emprestado!")
                else:
                    print("Livro já está emprestado.")
            else:
                print("Livro não encontrado!")

        elif opcao == 5:
            # Devolve um livro emprestado
            titulo = input("Digite o título do livro: ")
            livro = buscar_livro(titulo)
            if livro: 
                if livro["status"] == "Emprestado":
                    livro["status"] = "Disponivel"
                    print("Livro devolvido.")
                else: 
                    print("O livro já está disponível.")
            else: 
                print("Livro não encontrado.")

        elif opcao == 6: 
            print("1 - Ordenar por título")
            print("2 - Ordenar por autor")
            print("3 - Ordenar por ano")
            escolha = int(input("Escolha uma opção: "))
            if escolha == 1:
                livros_ordenados = ordenar_livros(livros, "titulo")
            elif escolha == 2:
                livros_ordenados = ordenar_livros(livros, "autor")
            elif escolha == 3:
                livros_ordenados = ordenar_livros(livros, "ano")
            else: 
                livros_ordenados = []
            for livro in livros_ordenados: 
                print(livro)

        elif opcao == 7:
            print("Programa encerrado!")
            break
        else: 
            print("Opção inválida.")
livros = carregar_livros()

menu()