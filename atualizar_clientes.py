<<<<<<< HEAD
#Atualizar clientes
=======
>>>>>>> 921ae7108d190c9f6e444c00f829870ccb0933ab
clientes = []

def add_cliente():
    print ("\n ---Capturando novo cliente---")
<<<<<<< HEAD
    novo_cliente = {
    "id": len(clientes) + 1,
    "nome": input("Nome: "),
    "email": input("Email: "),
    "telefone":input ("Telefone: "),
    "cpf": input ("Cpf: "),
    }
=======
    novo_cliente = [
        "id": len(clientes) + 1,
        "Nome": input("Nome: "),
        "Email": input("Email: "),
        "Telefone": input ("Telefone: "),
        "Cpf": input ("Cpf: "),
        ]
>>>>>>> 921ae7108d190c9f6e444c00f829870ccb0933ab
    clientes.append(novo_cliente)
def atualizar_cliente():
    if not clientes:
        print ("\n A Lista está vazia! Não há ninguém para atualizar.")
        return
    id_alvo = int(input("\n Digite o ID do cliente que deseja atualizar: "))
    for cliente in clientes:
        if cliente["id"] == id_alvo:
<<<<<<< HEAD
           print (f"Atualizando:{cliente["nome"]}")
           cliente["nome"] = input("\nDigite um novo nome: ")
           cliente["email"] = input("\nDigite um novo email: ")
           cliente["telefone"] = input("\nDigite um novo telefone: ")
           cliente["cpf"] = input ("\nDigite um novo CPF: ")
           print ("Atualizado! \n")
           return
print ("Cliente não encontrado.")
add_cliente() # isso vai disparar a tela de cadastro
atualizar_cliente() # isso vai disparar a tela de atualização.
=======
            print (f"Atualizando{cliente["Nome"]})
>>>>>>> 921ae7108d190c9f6e444c00f829870ccb0933ab
