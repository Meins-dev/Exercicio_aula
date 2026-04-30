lista_pedidos = [] #Lista dos Pedidos adicionados (cada produto com suas informações divididos em listas)
loop_pedidos = True #Fazer o loop para adicionar mais de um produto.
while loop_pedidos == True:
    lista_produto2 = [item for sublista in lista_produto for item in sublista]
    adicionar_pedidos = int(input("Digite o código do produto que será inserido ao carrinho:\n"))
    posicao_produto = (lista_produto2.index(str(adicionar_pedidos))-2) #Essa variável é o nome do produto a partir de seu código, descendo duas casas da lista.
    print(f"O produto selecionado é: {lista_produto2[(posicao_produto)]}")
    print(f"O preço do produto é R${lista_produto2[(posicao_produto)+1]}")
    lista_pedidos.append([lista_produto2[(posicao_produto)], lista_produto2[(posicao_produto)+1], lista_produto2[(posicao_produto)+2]]) #Aqui ele adiciona na lista de produtos adicionados os produtos que o usuário seleciona, dividindo cada produto e suas informações em uma lista cada.
    print("Produto adicionado aos pedidos com sucesso!")
    while True: #Aqui é o loop para saber se deseja adicionar mais um produto ou não.
        loop_pedidos2 = int(input("Deseja adicionar outro produto?\n1 - Sim\n2 - Não\n"))
        if loop_pedidos2 == 1:
            loop_pedidos = True
            break
        elif loop_pedidos2 == 2:
            loop_pedidos = False
            break
        else:
            print("Opção Inválida.")
            continue