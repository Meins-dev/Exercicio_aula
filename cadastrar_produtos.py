produtos=[] #lista principal
loop_cadastro = True #Fluxo do código. Garante a repetição do cadastro
while loop_cadastro == True:
    informacoes=[] #sublista dos produtos. Forma de separar cada produto com seu respectivo preço e código
    produto_nome=str(input("Digite o nome do produto:\n"))
    informacoes.append(produto_nome)
    produto_preco=float(input("Digite o preço:\n"))
    informacoes.append(produto_preco)
    produto_cod=int(input("Digite o código:\n"))
    informacoes.append(produto_cod)
    produtos.append(informacoes)
    print("Produto cadastrado com sucesso")
    print(produtos)
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