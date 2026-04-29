produtos=['produto1','produto2','produto3','produto4','produto5'] #Exemplo de Produtos
vlrunit1=float(input('Valor produto 1:R$')) #Valor unitário do produto 1
vlrunit2=float(input('Valor produto 2:R$')) #Valor unitário do produto 2
vlrunit3=float(input('Valor produto 3:R$')) #Valor unitário do produto 3
vlrunit4=float(input('Valor produto 4:R$')) #Valor unitário do produto 4
vlrunit5=float(input('Valor produto 5:R$')) #Valor unitário do produto 5
vlrproduto=vlrunit1+vlrunit2+vlrunit3+vlrunit4+vlrunit5 #Soma dos valores unitários dos produtos
opcao=0 #Opção de Forma de Pagamento ou de Sair
op1=1 #Opção de Concluir Pagamento
op2=2 #Opção de Cancelar Pagamento
while opcao<=4: 
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
    print(f"O valor final do produto é: R${vlrproduto:.2f}")
    print(produtos[0],'- R$',vlrunit1)
    print(produtos[1],'- R$',vlrunit2)
    print(produtos[2],'- R$',vlrunit3)
    print(produtos[3],'- R$',vlrunit4)
    print(produtos[4],'- R$',vlrunit5)
    vlrpago=float(input('R$'))
    op=int(input('1-Concluir\n2-Cancelar\n '))
    if op==op1:
        if vlrpago==vlrproduto:
         print('Valor R$',vlrpago)
         print('Pagamento concluído com sucesso!')
         break
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
    print(f"O valor final do produto é: R${vlrproduto:.2f}")
    print(produtos[0],'- R$',vlrunit1)
    print(produtos[1],'- R$',vlrunit2)
    print(produtos[2],'- R$',vlrunit3)
    print(produtos[3],'- R$',vlrunit4)
    print(produtos[4],'- R$',vlrunit5)
    vlrpago=float(input('R$'))
    op=int(input('1-Concluir\n2-Cancelar\n '))
    if op==op1:
        if vlrpago==vlrproduto:
         print('Valor R$',vlrpago)
         print('Pagamento concluído com sucesso!')
         break
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
    print(f"O valor final do produto é: R${vlrproduto:.2f}")
    print(produtos[0],'- R$',vlrunit1)
    print(produtos[1],'- R$',vlrunit2)
    print(produtos[2],'- R$',vlrunit3)
    print(produtos[3],'- R$',vlrunit4)
    print(produtos[4],'- R$',vlrunit5)
    vlrpago=float(input('R$'))
    op=int(input('1-Concluir\n2-Cancelar\n '))
    if op==op1:
        if vlrpago==vlrproduto:
         print('Valor R$',vlrpago)
         print('Pagamento concluído com sucesso!')
         break
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