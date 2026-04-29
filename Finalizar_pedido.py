vlrproduto=0
vlrpago=0
print("Escolha a forma de pagamento:")
print("1 - Crédito")
print("2 - Débito")
print("3 - Pix")

opcao=int(input("Digite a opção desejada: "))

if opcao == 1:
  
    print("Pagamento no crédito selecionado.")
    print(f"O valor final do produto é: R${vlrproduto:.2f}")
    vlrpago=float(input('R$'))
    print('Concluir pagamento')
    if vlrpago == vlrproduto:
        print('Pagamento concluído com sucesso!')
    else:
        print('Valor pago insuficiente. Pagamento não concluído.')

if opcao == 2:
    print("Pagamento no débito selecionado.")
    print(f"O valor final do produto é: R${vlrproduto:.2f}")
    vlrpago=float(input('R$'))
    print('Concluir pagamento')
    if vlrpago == vlrproduto:
        print('Pagamento concluído com sucesso!')
    else:
        print('Valor pago insuficiente. Pagamento não concluído.')

if opcao == 3:
    print("Pagamento no Pix selecionado.")
    print(f"O valor final do produto é: R${vlrproduto:.2f}")
    vlrpago=float(input('R$'))
    print('Concluir pagamento')
    if vlrpago == vlrproduto:
        print('Pagamento concluído com sucesso!')
    else:
        print('Valor pago insuficiente. Pagamento não concluído.')
else:
            print("Opção inválida. Por favor, selecione uma opção válida.")