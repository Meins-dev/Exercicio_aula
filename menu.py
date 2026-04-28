print('''
    +------------MENU------------+
    |1-Clientes                  |
    |  1.1-Cadastrar clientes    |
    |  1.2-Excluir clientes      |
    |2-Funcionarios              |
    |  2.1-Cadastrar funcionarios|
    |  2.2-Excluir funcionarios  |
    |3-Produtos                  |
    |  3.1-Cadastrar produtos    |
    |  3.2-Lista de produtos     |
    |  3.3-Excluir produtos      |
    |4-Pedidos                   | 
    |  4.1-Finalizar pedidos     |
    |5-Sair                      |
    +----------------------------+
''')

escolhaMenu = int(input("Selecione uma opção baseado no número do menu: "))

while escolhaMenu != 4:
    if escolhaMenu == 1: #Visualizar os clientes
        print("\n-----CLIENTES-----\n")

        escolhaMenu = int(input("Para ir para outra seção selecione uma opção baseado no número do menu: "))
    elif escolhaMenu == 2: #Visualizar os funcionários
        print("\n-----FUNCIONARIOS-----\n")

        escolhaMenu = int(input("Para ir para outra seção selecione uma opção baseado no número do menu: "))
    elif escolhaMenu == 3: #Visualizar os produtos
        print("\n-----PRODUTOS-----\n")

        escolhaMenu = int(input("Para ir para outra seção selecione uma opção baseado no número do menu: "))
    elif escolhaMenu == 5: #Sair do sistema
        print("\n-----SAIR DO SISTEMA-----\n")

        escolhaMenu = int(input("Para ir para outra seção selecione uma opção baseado no número do menu: "))
    else:
        print("Algo deu errado! Reinicie o sistema e tente novamente")