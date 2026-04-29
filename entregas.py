print("=== CADASTRO DE ENTREGA ===") 
 
rua = input("Digite a rua: ") 
numero = input("Digite o número: ") 
bairro = input("Digite o bairro: ") 
cidade = input("Digite a cidade: ") 
estado = input("Digite o estado: ") 
cep = input("Digite o CEP: ") 

valor_mercadoria = float(input("Digite o valor da mercadoria: R$ "))
valor_frete = float(input("Digite o valor do frete: R$ "))  
valor_total = valor_mercadoria + valor_frete  
endereco_completo = f"{rua}, {numero} - {bairro}, {cidade} - {estado}, CEP: {cep}"  
print("\n=== RESUMO DA ENTREGA ===") 
print(f"Endereço: {endereco_completo}") 
print(f"Valor da mercadoria: R$ {valor_mercadoria:.2f}") 
print(f"Valor do frete: R$ {valor_frete:.2f}") 
print(f"Valor total: R$ {valor_total:.2f}")