lista_produto=[] #lista principal
 #Fluxo do código. Garante a repetição do cadastro
informacoes=[] #sublista dos produtos. Forma de separar cada produto com seu respectivo preço e código
produto_nome=str(input("Digite o nome do produto:\n"))
informacoes.append(produto_nome)
produto_preco=float(input("Digite o preço:\n"))
informacoes.append(produto_preco)
produto_cod = str(input("Digite o código:\n"))
informacoes.append(produto_cod)
lista_produto.append(informacoes)
print("Produto cadastrado com sucesso")

print(lista_produto)


atualizar_produto = True

#nome_do_produto ; valor_do_produto ; codigo_do_produto

if atualizar_produto == True:


    while atualizar_produto == True:

        print("====================================================================")
        print("                     ATUALIZANDO PRODUTOS                           ")
        print("====================================================================")
        print("Quantidade de produtos: ")
        print(len(lista_produto))
        print("====================================================================\n")

        for i, produto in enumerate(lista_produto):
            print(f"{i} - Nome: {produto[0]}, Preço:{produto[1]},Código:{produto[2]}")

        indice = int=(input("Digite o número do produto que deseja atualizar: "))

        print("1- Nome")
        print("2- Preço")
        print("1- Código")

        opcao = input("O que deseja atualizar?")

        if opcao == "1":
            nome_do_produto = input("Index de qual item vc quer?")
            for sublista in lista_produto:
                if nome_do_produto in sublista:
                    index = sublista.index(nome_do_produto)
            nome_atualizar = input("Por qual produto vc quer subtituir")

        elif opcao == "2":
            novo_preco = float(input("Novo Preço:"))
            lista_produto[indice][1] = novo_preco
        elif opcao == "3":
            novo_codigo = input("Novo Código:")
            lista_produto[indice][2] = novo_codigo

        else:
            print("Opção inválida")
        print("Produto Atualizado!")