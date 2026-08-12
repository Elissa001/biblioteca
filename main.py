import csv

ARQUIVO = 'livros.csv'
def cadastro_livros (titulo, autor, codigo, ano, status = "Disponivel"):
    livros = {
        "titulo": titulo,
        "autor": autor 
        "codigo": codigo 
        "ano": ano 
        "status": status
    }
    livros.append (livro)
 
def menu():
    print("Menu")
    print("1 - Cadastro de livros" ("Digite a opção selecionada: "))
    if opcao == 1:
        titulo = input ("Digite o título: ")
        autor = input ("Digite o autor: ")
        codigo = input("Digite o código:")
        ano = input ("Digite o ano: ")
        cadastro_livros(titulo, autor, codigo, ano)
        rint ("livro cadastrado!")
   
menu()
