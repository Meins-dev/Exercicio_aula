print('''
    +------------MENU------------+
    |1-Clientes                  |     
    |2-Funcionarios              | 
    |3-Produtos                  |     
    |4-Pedidos                   |   
    |5-Entregas                  | 
    |0-Sair                      |
    +----------------------------+
''')

while True:

    menuPrincipal = int(input("Selecione uma opção baseado no número do menu: "))

    if menuPrincipal == 1: #Menu dos clientes
        print('''
            +----------CLIENTES----------+
            |  1-Cadastrar clientes      |
            |  2-Atualizar clientes      |
            |  3-Excluir clientes        |
            |  0-Sair                    |
            +----------------------------+
        ''')

        menuClientes = int(input("Selecione uma opção baseado no número do menu dos clientes: "))

        while True:
            if menuClientes == 1: #Cadastrar clientes
                print("Estou cadastrando os clientes.")

                menuClientes = int(input("Selecione uma opção baseado no número do menu: "))
            elif menuClientes == 2: #Atualizar clientes
                print("Estou atualizando os clientes.")

                menuClientes = int(input("Selecione uma opção baseado no número do menu: "))
            elif menuClientes == 3: #Excluir clientes
                print("Estou excluindo os clientes.")

                menuClientes = int(input("Selecione uma opção baseado no número do menu: "))
            elif menuClientes == 0: #Sair do Menu
                break
            else:
                print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")
    elif menuPrincipal == 2: #Menu dos funcionários
        print('''
            +--------FUNCIONÁRIOS--------+
            |  1-Cadastrar funcionarios  |
            |  2-Excluir funcionarios    |
            |  0-Sair                    |
            +----------------------------+
        ''')

        menuFuncionarios = int(input("Selecione uma opção baseado no número do menu dos funcionários: "))

        while True:
            if menuClientes == 1: #Cadastrar clientes
                print("Estou cadastrando os clientes.")

                menuClientes = int(input("Selecione uma opção baseado no número do menu: "))
            elif menuClientes == 2: #Atualizar clientes
                print("Estou atualizando os clientes.")

                menuClientes = int(input("Selecione uma opção baseado no número do menu: "))
            elif menuClientes == 3: #Excluir clientes
                print("Estou excluindo os clientes.")

                menuClientes = int(input("Selecione uma opção baseado no número do menu: "))
            elif menuClientes == 0: #Sair do Menu
                break
            else:
                print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")

    elif menuPrincipal == 3: #Menu dos produtos

        print('''
            +----------PRODUTOS----------+
            |  1-Cadastrar produtos      |
            |  2-Listar produtos         |
            |  3-Excluir produtos        |
            |  4-Finalizar produtos      |
            |  0-Sair                    |
            +----------------------------+
        ''')

    elif menuPrincipal == 4: #Menu dos pedidos

        print('''
            +-----------PEDIDOS----------+
            |  1-Finalizar pedidos       |
            |  2-Listar produtos         |
            |  3-Excluir produtos        |
            |  0-Sair                    |
            +----------------------------+
        ''')
    elif menuPrincipal == 5: #Menu das entregas

        print("+----------ENTREGAS----------+")
    elif menuPrincipal == 0:
        break
    else:
        print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")