lista_produto=[] #Exemplo de Produtos
op1=1 #Opção de Concluir Pagamento
op2=2 #Opção de Cancelar Pagamento
senha=1234 #Senha para concluir o pagamento
while True: 
 print("Escolha a forma de pagamento:")
 print("1 - Crédito")
 print("2 - Débito")
 print("3 - Pix")
 print("4 - Sair")
 opcao=int(input("Digite a opção desejada: "))
 if opcao > 4:
            print("Opção inválida.")
 if opcao == 1:
    print("Pagamento no crédito selecionado.")
    vlrproduto=sum(lista_produto) #Soma do valor dos produtos
    print(f"O valor final do produto é: R${vlrproduto:.2f}")
    print(lista_produto)
    vlrpago=float(input('R$'))
    op=int(input('1-Concluir\n2-Cancelar\n '))
    if op==op1:
       if vlrpago==vlrproduto:
         print('Valor R$',vlrpago)
         sn=int(input("Digite sua senha: "))
         if sn==senha:
           print('Pagamento Concluído')
           break
         else:
            print('Senha Icorreta')
       else:
         print('Valor pago insuficiente. Pagamento não concluído.')
    if op==op2:
        print('Pagamento Cancelado')
        break
    else:
        print('Esta opção não existe')
        break
 if opcao == 2:
    print("Pagamento no débito selecionado.")
    vlrproduto=sum(lista_produto) #Soma do valor dos produtos
    print(f"O valor final do produto é: R${vlrproduto:.2f}")
    print(lista_produto)
    vlrpago=float(input('R$'))
    op=int(input('1-Concluir\n2-Cancelar\n '))
    if op==op1:
        if vlrpago==vlrproduto:
         print('Valor R$',vlrpago)
         sn=int(input("Digite sua senha: "))
         if sn==senha:
           print('Pagamento Concluído')
           break
         else:
            print('Senha Icorreta')
        else:
         print('Valor pago insuficiente. Pagamento não concluído.')
    if op==op2:
        print('Pagamento Cancelado')
        break
    else:
        print('Esta opção não existe')
        break
 if opcao == 3:
    print("Pagamento no Pix selecionado.")
    vlrproduto=sum(lista_produto) #Soma do valor dos produtos
    print(f"O valor final do produto é: R${vlrproduto:.2f}")
    print(lista_produto)
    vlrpago=float(input('R$'))
    op=int(input('1-Concluir\n2-Cancelar\n '))
    if op==op1:
        if vlrpago==vlrproduto:
         print('Valor R$',vlrpago)
         sn=int(input("Digite sua senha: "))
         if sn==senha:
           print('Pagamento Concluído')
           break
         else:
            print('Senha Icorreta')
        else:
         print('Valor pago insuficiente. Pagamento não concluído.')
    if op==op2:
        print('Pagamento Cancelado')
        break
    else:
        print('Esta opção não existe')
        break
 if opcao==4:
    print("Saindo do programa. Obrigado por comprar conosco!")
    break