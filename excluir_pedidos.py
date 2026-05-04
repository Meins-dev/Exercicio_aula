
#Excluir pedidos



lista = ["carro","moto","bicicleta"] #Exemplo

item = (input("Digite o item que deseja excluir:")) #Recebe o item desejado para excluir

indice = lista.index(item)
lista.pop (indice)
print("\nItem excluído")
print("\nCarrinho:",item)