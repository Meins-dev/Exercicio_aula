#Pro código funcionar precisa da variavel carrinho que vai vir como uma lista
soma = 0
for item in carrinho:
    soma += item[1]
print(f"O valor da soma é: R$ {soma:.2f}")