
while True:
    print('''
    +-------MENU PRINCIPAL-------+
    |1-Clientes                  |     
    |2-Funcionarios              | 
    |3-Produtos                  |     
    |4-Pedidos                   |   
    |5-Entregas                  | 
    |0-Sair                      |
    +----------------------------+
    ''')

    menuPrincipal = int(input("Selecione uma opção baseado no número do menu principal: "))

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
                print("\n+--------------+\n")
                print("Estou cadastrando os clientes.")

                menuClientes = int(input("Selecione uma opção baseado no número do menu dos clientes: "))

            elif menuClientes == 2: #Atualizar clientes
                print("\n+--------------+\n")
                print("Estou atualizando os clientes.")

                menuClientes = int(input("Selecione uma opção baseado no número do menu dos clientes: "))

            elif menuClientes == 3: #Excluir clientes
                print("\n+--------------+\n")
                print("Estou excluindo os clientes.")

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
                print("Estou cadastrando os funcionários.")

                menuFuncionarios = int(input("Selecione uma opção baseado no número do menu dos funcionários: "))
            elif menuFuncionarios == 2: #Excluir funcionários
                print("\n+--------------+\n")
                print("Estou excluindo os funcionários.")

 
                menuFuncionarios = int(input("Selecione uma opção baseado no número do menu dos funcionários: "))
            elif menuFuncionarios == 0: #Sair do Menu
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

        menuProdutos = int(input("Selecione uma opção baseado no número do menu dos produtos: "))

        while True:
            if menuProdutos == 1: #Cadastrar produtos
                print("\n+--------------+\n")
                print("Estou cadastrando os produtos.")

                menuProdutos = int(input("Selecione uma opção baseado no número do menu dos produtos: "))
            elif menuProdutos == 2: #Listar produtos
                print("\n+--------------+\n")
                print("Estou listando os produtos.")

 
                menuProdutos = int(input("Selecione uma opção baseado no número do menu dos produtos: "))
            elif menuProdutos == 3: #Excluir produtos
                print("\n+--------------+\n")
                print("Estou excluindo os produtos")

                menuProdutos = int(input("Selecione uma opção baseado no número do menu dos produtos: "))
            elif menuProdutos == 4: #Finalizar produtos
                print("\n+--------------+\n")
                print("Estou finalizando os produtos")

                menuProdutos = int(input("Selecione uma opção baseado no número do menu dos produtos: "))
            elif menuProdutos == 0: #Sair do menu
                break
            else:
                print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")

    elif menuPrincipal == 4: #Menu dos pedidos

        print('''
        +-----------PEDIDOS----------+
        |  1-Finalizar pedidos       |
        |  2-Listar pedidos          |
        |  3-Excluir pedidos         |
        |  0-Sair                    |
        +----------------------------+  
        ''')

        menuPedidos = int(input("Selecione uma opção baseado no número do menu dos pedidos: "))

        while True:
            if menuPedidos == 1: #Cadastrar pedidos
                print("\n+--------------+\n")
                print("Estou finalizando os pedidos.")

                menuPedidos = int(input("Selecione uma opção baseado no número do menu dos pedidos: "))
            elif menuPedidos == 2: #Listar pedidos
                
                print("\n+--------------+\n")
                print("Estou listando os pedidos.")

 
                menuPedidos = int(input("Selecione uma opção baseado no número do menu dos pedidos: "))
            elif menuPedidos == 3: #Excluir pedidos
                
                print("\n+--------------+\n")
                print("Estou excluindo os pedidos")

                menuPedidos = int(input("Selecione uma opção baseado no número do menu dos pedidos: "))
            elif menuPedidos == 0: #Sair do menu
                break
            else:
                print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")
    elif menuPrincipal == 5: #Menu das entregas

        print('''
        +-----------ENTREGAS---------+
        |  1-Cadastrar entregas      |
        +----------------------------+
        ''')

        menuEntregas = int(input("Selecione uma opção baseado no número do menu das entregas: "))

        while True:
            if menuEntregas == 1: #Cadastrar endereços
                print("\n+--------------+\n")
                print("Estou cadastrando as entregas.")

                menuEntregas = int(input("Selecione uma opção baseado no número do menu das entregas: "))
                break
            else:
                print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")
    elif menuPrincipal == 0:
        break
    else:
        print("[ERROR!] Algo deu errado! Reinicie o sistema e tente novamente")
 