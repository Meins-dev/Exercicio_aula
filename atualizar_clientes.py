clientes = []

def add_cliente():
    print ("\n ---Capturando novo cliente---")
    novo_cliente = {
    "id": len(clientes) + 1,
    "nome": input("Nome: "),
    "Email": input("Email: "),
    "Telefone":input ("Telefone: "),
    "Cpf": input ("Cpf: "),
    }
    clientes.append(novo_cliente)
def atualizar_cliente():
    if not clientes:
        print ("\n A Lista está vazia! Não há ninguém para atualizar.")
        return
    id_alvo = int(input("\n Digite o ID do cliente que deseja atualizar: "))
    for cliente in clientes:
        if cliente["id"] == id_alvo:
            print ("a")
