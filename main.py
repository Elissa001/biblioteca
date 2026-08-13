import csv

ARQUIVO = 'livros.csv'

livros = []

def cadastro_livros (titulo, autor, codigo, ano, status = "Disponivel"):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "codigo": codigo,
        "ano": ano, 
        "status": status,
    }
    livros.append(livro)

def buscar_livro(titulo):
    for livro in livros:
        if livro["titulo"] == titulo:
            return livro
    return None

def menu():
    while True:
        print("Menu")
        print("1 - Cadastro de livros")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("4 - Sair")

        opcao = int(input("Digite a opção selecionada: "))

        if opcao == 1:
            titulo = input ("Digite o título: ")
            autor = input ("Digite o autor: ")
            codigo = input("Digite o código: ")
            ano = input ("Digite o ano: ")

            cadastro_livros(titulo, autor, codigo, ano)
            print ("Livro cadastrado!")

        elif opcao == 2: 
            for livro in livros:
                print(livro)   

        elif opcao == 3: 
            titulo = input("Digite o título do livro: ")
            livro = buscar_livro(titulo)
            if livro: 
                print(livro)
            else: 
                print("Livro não econtrado!")

        elif opcao == 4: 
            print("Programa encerrado!")
            break
menu()
