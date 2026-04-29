#o código espera uma variável de lista com a seguinte formatação:
# cliente = [[nome, email, telefone, cpf], [nome, email, telefone, cpf]]

if len (cliente) > 0:
    print ("--- Clientes Cadastrados ---")
    for clientes in range (len(cliente)):
        print (f" {clientes + 1}. Nome do  cliente: {cliente[clientes][0]}.\nEmail do cliente: {cliente[clientes][1]}.\nTelefone do Cliente: {cliente[clientes][2]}.\nCPF do Cliente: {cliente[clientes][3]}")
else:
    print ("Não há resgistro de clientes...")