menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
extrato = ''
limite = 500
numero_saque = 0 
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor do depósito: '))

        if valor > 0: 
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print('Operação falhou!! Valor é inválido')
    
    elif opcao =='s':
        valor = float(input('Digite o valor do saque: '))

        execedeu_saldo = valor > saldo 

        execedeu_limte = valor > limite

        execedeu_saque =  numero_saque >= LIMITE_SAQUE

        if execedeu_saldo:
            print('Operação falhou!! Você não tem saldo suficiente!')
    
        elif execedeu_limte:
            print('Operação falhou!! O valor do saque execede o limite!')
    
        elif execedeu_saque:
            print('Operação falhou! Você exedeu o limite de saques! ')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saque += 1
    
        else:
            print('Operação falhou! Valor informado é inválido')

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================") 
    
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')