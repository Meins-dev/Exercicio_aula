clientes = []

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
senha = input("Digite sua Senha: ")
confirmar_senha = input("Confirme sua senha: ")



if confirmar_senha == senha:
    print("CLIENTE CADASTRADO COM SUCESSO!!!!")

    clientes = [nome, email, senha]
    clientes.append(clientes)

else:
    print("SENHA DIFERENTE")
    