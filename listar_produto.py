#listar produto
#o código espera uma variável de lista com a seguinte formatação:
#lista_produto = [[nome_produto, preco_produto, codigo_produto], [nome_produto, preco_produto, codigo_produto]]

if len(lista_produto) > 0:
    for i in range(len(lista_produto)):
        print(f"{i + 1}. Nome do Produto: {lista_produto[i][0]} - Preço: R$ {lista_produto[i][1]:.2f} - Código: {lista_produto[i][2]}")
else:
    print("Nenhum produto cadastrado.")