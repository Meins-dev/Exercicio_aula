#aqui caso queira inicializar o excluir o produto digite "lista_produto=[]" e selecione o produto dentro da caixa o produto selecionado que queira 
#  
if len(lista_produto) > 0:
    # o escolha abaixo seria para digitar seu produto que queira remover digitando o numero de seu produto
    escolha= int(input("\ndigite o numero do produto que deseja remover: "))
    indice = escolha -1 

    if indice >=0 and indice < len(lista_produto):
      removido=lista_produto.pop(indice)
      print(f"sucesso: produto '{removido[0]}' foi excluido.")
      print(lista_produto)
    else:
      print("\nerro esse numero do produto não existe.")
    