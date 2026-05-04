
#Excluir pedidos
#Precisa da lista carrinho para funcionar
while True:
      if len(carrinho) != 0:
            escolha =  int(input("Digite o código do produto que deseja excluir:"))
            excluido = carrinho.pop(escolha)
            print(f"\nItem {excluido[0]} excluído")
            sair = input("Você deseja parar de excluir produtos? (s = sim / n = não)")
            if sair.lower() == 's':
                  break
      else:
            print("Nenhum produto no carrinho.")