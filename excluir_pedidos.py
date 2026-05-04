#Excluir pedidos



lista = ["Carro","Moto","Bicicleta"] #Exemplo

item = (input("Digite o item que deseja excluir:")) #Recebe o item que deseja excluir 

indice = lista.index(item)
lista.pop (indice)
print("\nItem excluído")
print("\nCarrinho:",lista)
