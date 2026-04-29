funcionario= []
idades = []
cargos= []
senhas= []

while True:
	print("\n--Cadastro de funcionario--")
	print("1 - Cadastrar funcionário: ")
	print("2 - Listar funcionário: ")
	print("3 - Buscar funcionário: ")
	print("0 - Sair")

	opcao=input("Escolha uma opção: ")
	
	if opcao=="1":
		nome=input("Nome do funcionário:")
		idade=input("Idade:")
		cargo=input("Cargo:")
		senha=input("Senha:")

		funcionario.append(nome)
		idades.append(idade)
		cargos.append(cargo)
		senhas.append (senha)
		print("Funcionário cadastrado com sucesso.")

	elif opcao=="2":
		print (funcionario)

	elif opcao=="3":
		busca=input("Digite o nome do funcionário: ")
		encontrado=False