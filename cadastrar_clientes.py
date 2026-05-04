clientes = []  #para o código rodar

while True:
    print("====Cadastro Dos Clientes====")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")
    cpf = input("Digite seu CPF: ")

    cliente = [nome, email, telefone, cpf]

    clientes.append(cliente)

    print("Cliente cadstrado com sucesso !!!")

    continuar_cadastro = input("Deseja cadastrar outro cliente ? (sim/não): ").lower()

    if continuar_cadastro == "sim":
        pass 
    else:
        break  