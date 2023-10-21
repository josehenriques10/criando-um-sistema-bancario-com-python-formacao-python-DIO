import textwrap

def menu():
    menu = '''
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuário
    [0] Sair

    ? '''

    return int(input(menu))


def depositar(saldo, deposito, verificador, /):
    deposito = float(input('\nR$ '))

    if deposito >= 100:
        saldo += deposito
        verificador = 1

    else:
        print('O valor mínimo para se fazer um depósito é de R$ 100,00.')
        verificador = 0

    return saldo, deposito, verificador


def sacar(*, 
    saldo, 
    saque, 
    numeros_saques, 
    verificador, 
    LIMITE_SAQUES, 
    LIMITE_SAQUE
):
    saque = float(input('\nR$ '))

    if saque <= 0:
        print('O valor que você está tentando sacar e inválido.')
        verificador = 0

    elif numeros_saques >= LIMITE_SAQUES:
        print(f'Você ja excedeu o limite de {LIMITE_SAQUES} saques diários.')
        verificador = 0

    elif saque > LIMITE_SAQUE :
        print(
            f'O limite do valor do saque para sua conta é de: '
            f'R$ {LIMITE_SAQUE:.2f}.'
        )
        verificador = 0

    elif saque > saldo:
        print(
            f'Você não pode sacar um valor maior que o saldo atual de '
            f'R$ {saldo:.2f}.'
        )
        verificador = 0

    elif (
        numeros_saques < LIMITE_SAQUES 
        and saque <= LIMITE_SAQUE 
        and saque <= saldo
    ):
        saldo -= saque
        numeros_saques += 1
        verificador = 1
        print(f'Saque de R$ {saque} realizado com sucesso.')

    return saldo, saque, numeros_saques, verificador


def atualizar_extrato(extrato, deposito, saque, /, *, verificador, opcao):
    if verificador == 1 and opcao == 1:
            extrato.append(f' + R$ {deposito:.2f}')
    
    elif verificador == 1 and opcao == 2:
            extrato.append(f' - R$ {saque:.2f}')


def exibir_extrato(*, extrato, saldo, opcao):
    if opcao == 3:
        print('\n==== EXTRATO ====\n')

        for transacao in extrato:
            print(f'{transacao}')
        print(f'\n Saldo: {saldo:.2f}')
        print(f'\n=================\n')


def criar_usuario(usuarios):
    print('IFORME OS DADOS NECESSÁRIOS (Completos)\n')
    cpf = input('CPF (somente números): ')
    usuario = filtrar_usuario(usuarios=usuarios, cpf=cpf)

    if usuario:
        print('CPF já em uso! Verifque os números e tente novamente.')
        return

    nome = input('Nome: ')
    data_nascimento = input('Data de nascimento (DD-MM-AAAA): ')
    endereco = input('Endereço: ')
    usuarios.append(
        {
            'cpf': cpf, 
            'nome': nome, 
            'data_nascimento': data_nascimento, 
            'endereco': endereco
        }
    )
    
    print('Usuário adicionado com sucesso!')


def filtrar_usuario(*, usuarios, cpf):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf
    ]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(*, usuarios, AGENCIA, numero_conta):
    cpf = input('CPF (somente números): ')
    usuario = filtrar_usuario(usuarios=usuarios, cpf=cpf)

    if usuario:
        print('Nova conta criada com sucesso!')
        return {
            'agencia': AGENCIA, 
            'conta': numero_conta, 
            'usuario': usuario
        }
    
    print('Usuário não encontrado, fluxo de criação de conta encerrado!')


def listar_contas(*, contas):
    for conta in contas:
        listando_contas = f'''\
            Agência:\t{conta['agencia']}
            Conta:\t{conta['conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print("=" * 100)
        print(textwrap.dedent(listando_contas))


def main():
    LIMITE_SAQUE = 500
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    deposito = 0
    saque = 0
    numeros_saques = 0
    extrato = []
    usuarios = []
    contas = []
    verificador = 0

    while True:
        print(f'\nSaldo: R$ {saldo:.2f}')
        opcao = menu()
        print()

        if opcao == 1:
            saldo, deposito, verificador = depositar(
                saldo, 
                deposito, 
                verificador,
            )

            atualizar_extrato( 
                extrato, 
                deposito, 
                saque, 
                verificador=verificador, 
                opcao=opcao
            )

        elif opcao == 2:
            saldo, saque, numeros_saques, verificador = sacar(
                saldo=saldo, 
                saque=saque, 
                numeros_saques=numeros_saques, 
                verificador=verificador,
                LIMITE_SAQUES=LIMITE_SAQUES,
                LIMITE_SAQUE=LIMITE_SAQUE
            )
            
            atualizar_extrato( 
                extrato, 
                deposito, 
                saque, 
                verificador=verificador, 
                opcao=opcao
            )

        elif opcao == 3:
            exibir_extrato( 
                extrato=extrato,
                saldo=saldo, 
                opcao=opcao
            )

        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(
                usuarios=usuarios,
                AGENCIA=AGENCIA,
                numero_conta=numero_conta
            )

            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_contas(
                contas=contas
            )

        elif opcao == 6:
            criar_usuario(usuarios)

        elif opcao == 0:
            break

        else:
            print(
                'Operação inválida, por favor selecione novamente a '
                'operação desejada.'
            )
          

main()