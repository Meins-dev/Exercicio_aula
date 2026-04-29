lista_produto = []
contador = 0

quantidade = int(input("Qual a quantidade de produtos? "))

while contador < quantidade:
    preco = float(input("Digite o preço: "))
    
    if preco >= 0:
        if preco == 0:
            print("O valor do produto é 0")
        lista_produto.append(preco)
        contador += 1 
    else:
        print("Valor inválido")

valor_total = 0
indice = 0

while indice < len(lista_produto):
    valor_total += lista_produto[indice]
    indice += 1

print("Valor total:", valor_total)