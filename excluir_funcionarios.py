escolha = 1
funcionarios = []
senhas = []

while escolha != 0:

    escolha = str (input ("Digite 1 para selecionar um funcionario ou 0 para voltar: "))

    if escolha == "1":
        excluir = str (input ("\nDigite o nome do funcionário que deseja excluir: "))
        if excluir in funcionarios:
            x = funcionarios.index (excluir)
            funcionarios.pop (x)
            senhas.pop (x)
            print ("\nCliente Excluido!\n")
        else:
            print ("\nFuncuinário não encontrado!\n")
    elif escolha == "0":
        print ("\nRetornando ao Menu...\n")
        break