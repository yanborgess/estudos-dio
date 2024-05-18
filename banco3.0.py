
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUE = 3
contas =[]
usuarios = []





menu ='''
    ==========MENU==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Nova conta
    [q] Sair 
    =>  '''

def depositar(saldo,valor,extrato):
    if valor > 0:
        saldo += valor
        
    else:
        print('OPERAÇÃO INVALIDA!!') 
    return saldo,extrato

def sacar(valor, saldo,limite, numero_saques,limite_saques):
    exedeu_limite = valor > limite
    exedeu_saldo = valor > saldo 
    exedeu_saques = numero_saques >= limite_saques
    if valor > 0:
        saldo -= valor 
        numero_saques +=1
        
        print('Saque realizado com sucesso!')
    
    elif exedeu_limite:
        print('Operação cancelada! Limite atingido')
    elif exedeu_saldo:
        print('Operação cancelada! Saldo indisponivel')
    elif exedeu_saques:
        print('Operação cancelada! Numero de saques atingido')
    return saldo

def extrato(extrato):
    print('EXTRATO ')
    print(f'SALDO {saldo:.2f}')
    return extrato


while True:
    
    opcao  = input(menu)

    if opcao == 'd':
        valor  =  float(input('Digite o valor do deposito: '))

        saldo, extrato = depositar(saldo, valor, extrato)
        
    elif opcao == 's':
        valor =  float(input('Digite o valor do saque: '))
        saldo = sacar(valor=valor,saldo=saldo, limite=limite,numero_saques=numero_saques, limite_saques=LIMITE_SAQUE)
    
    elif opcao == 'e':
        extrato(saldo)

    elif opcao == 'q':
        break
    







  



