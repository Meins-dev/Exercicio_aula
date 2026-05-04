#Atualizar clientes
clientes = []

def add_cliente():
    if clientes:
    #Busca o maior ID atual ou começa em 1 se a lista estiver vazia
        novo_id = clientes[-1]['id'] + 1
    else:
     novo_id = 1
    print ("\n ---Capturando novo cliente---")
    novo_cliente = {
        "id": novo_id,
        "nome": input("Nome: "),
        "email": input("Email: "),
        "telefone":input ("Telefone: "),
        "cpf": input ("Cpf: "),
    }
    clientes.append(novo_cliente)
def atualizar_cliente():
    if not clientes:
        print ("\n A Lista está vazia! Não há ninguém para atualizar.")
        return
    try:
        id_alvo = int(input("Digite o ID do cliente que deseja atualzar: "))
    except ValueError:
        print("Erro: digite somente números para o ID.")
        return
    for cliente in clientes:
        if cliente["id"] == id_alvo:
           print (f"Atualizando:{cliente["nome"]}")
           cliente["nome"] = input("\nDigite um novo nome: ")
           cliente["email"] = input("\nDigite um novo email: ")
           cliente["telefone"] = input("\nDigite um novo telefone: ")
           cliente["cpf"] = input ("\nDigite um novo CPF: ")
           print ("Atualizado! \n")
           return
#chamadas de teste
add_cliente() # isso vai disparar a tela de cadastro
atualizar_cliente() # isso vai disparar a tela de atualização.
