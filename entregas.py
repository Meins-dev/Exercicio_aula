print("=== CADASTRO DE ENTREGA ===") 
 
rua = input("Digite a rua: ") 
numero = input("Digite o número: ") 
bairro = input("Digite o bairro: ") 
cidade = input("Digite a cidade: ") 
estado = input("Digite o estado: ") 
cep = input("Digite o CEP: ") 
while True:
    codigo_mercadoria = str(input("Digite o codigo do produto:  "))
    localizar = codigo_mercadoria in lista_produto
    if localizar == True:
        localizacao = int(lista_produto.index(codigo_mercadoria))
        produto_entrega = (localizacao) - 2 
        valor_produto = (localizacao) - 1
        print(f"O produto selecionado é: {lista_produto[produto_entrega]}")
        break
    else:
        print("Esse código não existe.")
        continue

valor_frete = float(input("Digite o valor do frete: R$ "))  
valor_total = lista_produto[valor_produto] + valor_frete
endereco_completo = f"{rua}, {numero} - {bairro}, {cidade} - {estado}, CEP: {cep}"  
print("\n=== RESUMO DA ENTREGA ===") 
print(f"O produto selecionado é: {produto_entrega}")
print(f"Endereço: {endereco_completo}") 
print(f"Valor da mercadoria: R${lista_produto[valor_produto]:.2f}") 
print(f"Valor do frete: R${valor_frete:.2f}") 
print(f"Valor total: R${valor_total:.2f}")