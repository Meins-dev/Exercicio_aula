while True:
    print('''
    +-------MENU PRINCIPAL-------+
    |1-Clientes                  |     
    |2-Funcionarios              | 
    |3-Produtos                  |     
    |4-Pedidos                   |
    |5-Carrinho                  |
    |6-Entregas                  | 
    |0-Sair                      |
    +----------------------------+
    ''')

    menuPrincipal = int(input("Selecione uma opção baseado no número do menu principal: "))

    if menuPrincipal == 1: #Menu dos clientes
        print('''
        +----------CLIENTES----------+
        |  1-Cadastrar clientes      |
        |  2-Atualizar clientes      |
        |  3-Lista de clientes       |
        |  4-Excluir clientes        |
        |  0-Sair                    |
        +----------------------------+
        ''')

        menuClientes = int(input("Selecione uma opção baseado no número do menu dos clientes: "))

        while True:
            if menuClientes == 1: #Cadastrar clientes
                print("\n+--------------+\n")


                menuClientes = int(input("Selecione uma opção baseado no número do menu dos clientes: "))
            elif menuClientes == 2: #Atualizar clientes
                print("\n+--------------+\n")


                menuClientes = int(input("Selecione uma opção baseado no número do menu dos clientes: "))
            elif menuClientes == 3: #Lista de clientes
                print("\n+--------------+\n")


                menuClientes = int(input("Selecione uma opção baseado no número do menu dos clientes: "))
            elif menuClientes == 4: #Excluir clientes
                print("\n+--------------+\n")


                menuClientes = int(input("Selecione uma opção baseado no número do menu dos clientes: "))
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
            if menuFuncionarios == 1: #Cadastrar funcionários
                print("\n+--------------+\n")


                menuFuncionarios = int(input("Selecione uma opção baseado no número do menu dos funcionários: "))
            elif menuFuncionarios == 2: #Excluir funcionários
                print("\n+--------------+\n")

 
                menuFuncionarios = int(input("Selecione uma opção baseado no número do menu dos funcionários: "))
            elif menuFuncionarios == 0: #Sair do Menu
                break
            else:
                print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")

    elif menuPrincipal == 3: #Menu dos produtos

        print('''
        +----------PRODUTOS----------+
        |  1-Cadastrar produtos      |
        |  2-Lista de produtos       |
        |  3-Atualizar produtos      |
        |  4-Excluir produtos        |
        |  0-Sair                    |
        +----------------------------+
        ''')

        menuProdutos = int(input("Selecione uma opção baseado no número do menu dos produtos: "))

        while True:
            if menuProdutos == 1: #Cadastrar produtos
                print("\n+--------------+\n")


                menuProdutos = int(input("Selecione uma opção baseado no número do menu dos produtos: "))
            elif menuProdutos == 2: #Lista de produtos
                print("\n+--------------+\n")


 
                menuProdutos = int(input("Selecione uma opção baseado no número do menu dos produtos: "))
            elif menuProdutos == 3: #Atualizar produtos
                print("\n+--------------+\n")


                menuProdutos = int(input("Selecione uma opção baseado no número do menu dos produtos: "))
            elif menuProdutos == 4: #Excluir produtos
                print("\n+--------------+\n")


                menuProdutos = int(input("Selecione uma opção baseado no número do menu dos produtos: "))
            elif menuProdutos == 0: #Sair do menu
                break
            else:
                print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")

    elif menuPrincipal == 4: #Menu dos pedidos

        print('''
        +-----------PEDIDOS----------+
        |  1-Finalizar pedidos       |
        |  2-Excluir pedidos         |
        |  0-Sair                    |
        +----------------------------+
        ''')

        menuPedidos = int(input("Selecione uma opção baseado no número do menu dos pedidos: "))

        while True:
            if menuPedidos == 1: #Finalizar pedidos
                print("\n+--------------+\n")


                menuPedidos = int(input("Selecione uma opção baseado no número do menu dos pedidos: "))
            elif menuPedidos == 2: #Excluir pedidos
                print("\n+--------------+\n")


                menuPedidos = int(input("Selecione uma opção baseado no número do menu dos pedidos: "))
            elif menuPedidos == 0: #Sair do menu
                break
            else:
                print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")
    elif menuPrincipal == 5: #Menu do carrinho

        print('''
        +-----------CARRINHO---------+
        |  1-Adicionar item          |
        |  2-Visualizar itens        |
        |  3-Excluir item            |
        |  0-Sair                    |
        +----------------------------+
        ''')

        menuCarrinho = int(input("Selecione uma opção baseado no número do menu dos carrinho: "))

        while True:
            if menuCarrinho == 1: #Adicionar item ao carrinho
                print("\n+--------------+\n")


                menuCarrinho = int(input("Selecione uma opção baseado no número do menu do carrinho "))
            elif menuCarrinho == 2: #Visualizar itens do carrinho
                print("\n+--------------+\n")

 
                menuCarrinho = int(input("Selecione uma opção baseado no número do menu do carrinho: "))
            elif menuCarrinho == 3: #Excluir item do carrinho
                print("\n+--------------+\n")


                menuCarrinho = int(input("Selecione uma opção baseado no número do menu do carrinho: "))
            elif menuCarrinho == 0: #Sair do menu
                break
            else:
                print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")
    elif menuPrincipal == 6: #Menu das entregas

        print('''
        +-----------ENTREGAS---------+
        |  1-Cadastrar entregas      |
        |  0-Sair                    |
        +----------------------------+
        ''')

        menuEntregas = int(input("Selecione uma opção baseado no número do menu das entregas: "))

        while True:
            if menuEntregas == 1: #Cadastrar entregas
                print("\n+--------------+\n")


                menuEntregas = int(input("Selecione uma opção baseado no número do menu das entregas: "))
                break
            elif menuEntregas== 0: #Sair do menu
                break
            else:
                print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")
    elif menuPrincipal == 0:
        break
    else:
        print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")