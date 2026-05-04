# 1- Prateleira de produtos e carrinho vazio
#Para a lista funcionar, precisa da variavel lista_produto
carrinho = []
contador = 0  # Começa em zero

while True:
        escolha = int(input("\nDigite o número do produto (1 a 4): "))
        escolha -=1
    
        item_escolhido = lista_produto[escolha]    
        carrinho.append(item_escolhido)

    
        print(f"Sucesso! {item_escolhido[0]} adicionado.")
        contador += 1
        print(f"Você tem {contador} item(s) no carrinho.")
        

    # Mensagem para continuar ou parar
    
        continuar = input("Deseja continuar? (s/n): ").lower()

        if  continuar == 's':
            print("Continuando...")
            continue
            

        elif continuar == 'n':
            print("Fechando o sistema...")
        break