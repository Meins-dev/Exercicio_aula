nome_produto = []
preco_produto = []
cod_produto = []

lista_produto_produto = [nome_produto [ preco_produto [ cod_produto ]]]

while True:
    lista_produto = [nome_produto [ preco_produto [ cod_produto ]]]

    nome_produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    preco_produto = input("Digite o preço do produto (ou 'sair' para encerrar): ")
    cod_produto = input("Digite o código do produto (ou 'sair' para encerrar): ")
    
    
    
    
    
    if nome_produto.lower() or preco_produto.lower() or cod_produto.lower() == 'sair':
        break
    
    lista_produto.append(nome_produto)
    lista_produto.append(preco_produto, "reais")
    lista_produto.append(cod_produto)
    lista_produto = [nome_produto [ preco_produto [ cod_produto ]]]

    
print(lista_produto)

