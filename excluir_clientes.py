lista = ["Joana","Maria","Fernanda"]
print(lista)
excluir = input("DIgite o nome do(s) clientes que deseja remover do sistema : ")

y =lista.index(excluir)
print(y)
lista.pop(y)
print(lista)