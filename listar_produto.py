#listar produto

for i in range(len(lista_produto)):
    print(f"{i + 1}. Nome do Produto: {lista_produto[i][0]} - Preço: R$ {lista_produto[i][1]} - Código: {lista_produto[i][2]}")