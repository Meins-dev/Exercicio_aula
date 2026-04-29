#Cadastro de Produtos
lista_produto=[] #lista principal

while True:
    print('''
    +----------PRODUTOS----------+
    |  1-Cadastrar produtos      |
    |  2-Listar produtos         |
    |  3-Excluir produtos        |
    |  4-Finalizar produtos      |
    |  0-Sair                    |
    +----------------------------+
    ''')
    menuProdutos = int(input("Selecione uma opção baseado no número do menu dos produtos: "))

    if menuProdutos == 1: #Cadastrar produtos
        print("\n+--------------+\n")
        print("Estou cadastrando os produtos.")

        
        loop_cadastro = True #Fluxo do código. Garante a repetição do cadastro
        while loop_cadastro == True:
            produto_nome=str(input("Digite o nome do produto:\n"))
            produto_preco=float(input("Digite o preço:\n"))
            produto_cod = str(input("Digite o código:\n"))
            lista_produto.append([produto_nome,produto_preco,produto_cod])
            print("Produto cadastrado com sucesso")

            while True:
                loop = int(input("Deseja cadastrar outro?\n1 - Sim\n2 - Não \n")) #Escolha de repetição
                if loop == 1:
                    loop_cadastro = True
                    break
                elif loop == 2:
                    loop_cadastro = False
                    break
                else:
                    print("Opção Inválida.")
                    continue

    elif menuProdutos == 2: #Listar produtos
        print("\n+--------------+\n")
        print("Estou listando os produtos.")

        if len(lista_produto) > 0:
                for i in range(len(lista_produto)):
                    print(f"{i + 1}. Nome do Produto: {lista_produto[i][0]} - Preço: R$ {lista_produto[i][1]:.2f} - Código: {lista_produto[i][2]}")
        else:
                print("Nenhum produto cadastrado.")
    elif menuProdutos == 3: #Excluir produtos
        print("\n+--------------+\n")
        print("Estou excluindo os produtos")

        