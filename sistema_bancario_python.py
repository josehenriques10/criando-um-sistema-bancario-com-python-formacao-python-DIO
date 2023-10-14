menu = '''
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

? '''

saldo = 0
deposito = 0
saque = 0
numeros_saques = 0
extrato = []
verificador = 0
LIMITE_DESAQUES = 3
LIMITE_DOSAQUE = 500

def atualiza_saldo_deposito(saldo, deposito, verificador):

    deposito = int(input('R$ '))

    if deposito >= 100:
        saldo += deposito
        verificador = 1
    
    else:
        print('O valor mínimo para se fazer um depósito é de R$ 100,00.')
        verificador = 0

    return saldo, deposito, verificador

def atualiza_saldo_saque(saldo, saque, numeros_saques, verificador):

    saque = int(input('R$ '))
    
    if saque <= 0:
        print('O valor que você está tentando sacar e inválido.')
        verificador = 0
    
    elif numeros_saques >= LIMITE_DESAQUES:
        print(f'Você ja excedeu o limite diário de {LIMITE_DESAQUES} saques.')
        verificador = 0
    
    elif saque > LIMITE_DOSAQUE :
        print(f'O limite do valor do saque para sua conta é de: R$ {LIMITE_DOSAQUE:.2f}.')
        verificador = 0
    
    elif saque > saldo:
        print(f'Você não pode sacar um valor maior que o saldo atual de R$ {saldo:.2f}.')
        verificador = 0

    elif numeros_saques < LIMITE_DESAQUES and saque <= LIMITE_DOSAQUE and saque <= saldo:
        saldo -= saque
        numeros_saques += 1
        verificador = 1
        print(f'Saque de R$ {saque} realizado com sucesso.')
    
    return saldo, saque, numeros_saques, verificador

def extrato_bancario():

    print('EXTRATO...\n')

    for transacao in extrato:
        print(f'{transacao}')
        
    print(f'\n')

while True:

    print(f'Saldo: R$ {saldo:.2f}')
    opcao = input(menu)

    if opcao == 'D' or opcao == 'd':
        saldo, deposito, verificador = atualiza_saldo_deposito(saldo=saldo, deposito=deposito, verificador=verificador)

        if verificador == 1:
            extrato.append(f'+ R$ {deposito:.2f}')

    elif opcao == 'S' or opcao == 's':
        saldo, saque, numeros_saques, verificador = atualiza_saldo_saque(saldo=saldo, saque=saque, numeros_saques=numeros_saques, verificador=verificador)

        if verificador == 1:
            extrato.append(f'- R$ {saque:.2f}')

    elif opcao == 'E' or opcao == 'e':
        extrato_bancario()

    elif opcao == 'Q' or opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
    