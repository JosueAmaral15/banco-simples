menu = """

    Banco Amaral
    
    Opções:
    
    [d] depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

saldo = 0
limite = 0
extrato = "Saldo: R$ 0.00\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        print (f"\n{'Depósito'.center(20,'#')}")
        valor = input("\nInforme qual seria o valor do depósito: ")
        if valor.replace(".","").isdecimal():
            valor = round(float(valor),2)
            if valor > 0:
                saldo += valor
                extrato+= f"Valor depositado: R$ {valor:.2f}\nSaldo: R$ {saldo:.2f}\n"
                print (f"\nO depósito de R$ {valor:.2f} foi realizado com sucesso!\n")
            else:
                print("O valor de depósito deve ser maior que zero!\n")
        else:
            print("Informe um valor válido!\n")
        print("#"*20)
    elif opcao == 's':
        print(f"\n{'Saque'.center(20,'#')}")
        if numero_saques < LIMITE_SAQUES:
            valor = input("\nInforme qual seria o valor do saque: ")
            if valor.replace(".","").isdecimal():
                valor = round(float(valor),2)
                if valor > 0:
                    if valor <= 500:
                        if saldo -valor > 0:  
                            saldo -= valor
                            extrato+= f"Valor sacado: R$ {valor:.2f}\nSaldo: R$ {saldo:.2f}\n"
                            print (f"\nO saque de R$ {valor:.2f} foi realizado com sucesso!\n")
                            numero_saques+=1
                        else:
                            print("Saldo insuficiente para o saque!\n")
                    else:
                        print("O valor do saque não pode ser maior que R$ 500.00!\n")
                else:
                    print("O valor de saque deve ser maior que zero!\n")
            else:
                print("Informe um valor válido!\n")
        else:
            print("Quantidade máxima de saques (3) alcançada!\n")
        print("#"*20)
    elif opcao == 'e':
        print(f"\n{'Extrato'.center(20,'#')}")
        print(f"\n{extrato}\n{'#'*20}")
    elif opcao == 'q':
        break
    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada\n")