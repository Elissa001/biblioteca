livros = []

while True: 
    print ("------BIBLIOTECA------")
    print ("1 - Cadastrar")
    print ("2 - Listar")
    print ("3 - Sair")

    opcao = input("Digite a opção selecionada: ")

    if opcao == "1":
        nome_livro = input ("Digite o nome do livro: ")
        livros.append(nome_livro)
        print (f"Livro '{nome_livro}' cadastrado!")

    elif opcao == "2":
        print (livros)

    elif opcao == "3":
        print ("Saindo da biblioteca...")
        break 

    else: 
        print ("Opção inválida!")
