print('''
    +------------MENU------------+
    |1-Clientes                  |
    |  -Cadastrar clientes    |
    |  -Excluir clientes      |
    |2-Funcionarios              |
    |  -Cadastrar funcionarios|
    |  -Excluir funcionarios  |
    |3-Produtos                  |
    |  -Cadastrar produtos    |
    |  -Lista de produtos     |
    |  -Excluir produtos      |
    |4-Pedidos                   | 
    |  -Finalizar pedidos     |
    |5-Sair                      |
    +----------------------------+
''')

'''
    +----------CLIENTES----------+
    |  1-Cadastrar clientes      |
    |  2-Excluir clientes        |
    +----------------------------+

    +--------FUNCIONARIOS--------+
    |  1-Cadastrar funcionarios  |
    |  2-Excluir funcionarios    |
    +----------------------------+

    +----------CLIENTES----------+
    |  1-Cadastrar clientes      |
    |  2-Excluir clientes        |
    +----------------------------+
'''

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