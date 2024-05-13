usuarios = []
contas = []
numero_conta = 1

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

def criar_conta_corrente(usuario_cpf):
    global numero_conta
    for usuario in usuarios:
        if usuario['cpf'] == usuario_cpf:
            contas.append({'agencia': '0001', 'numero_conta': numero_conta, 'usuario': usuario})
            numero_conta += 1
            print("Conta criada com sucesso.")
            return
    print("Usuário não encontrado.")

def listar_contas():
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")

def main():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Criar Usuário
    [a] Criar Conta Corrente
    [l] Listar Contas
    [q] Sair

    => """
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu).strip().lower()

        if opcao not in ['d', 's', 'e', 'c', 'a', 'l', 'q']:
            print("Opção inválida, por favor selecione novamente a operação desejada.")
            continue

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                                    numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            extrato(saldo, extrato=extrato)

        elif opcao == "c":
            nome = input("Informe o nome do usuário: ")
            data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
            cpf = input("Informe o CPF: ")
            endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "a":
            cpf = input("Informe o CPF do titular: ")
            criar_conta_corrente(cpf)

        elif opcao == "l":
            listar_contas()

        elif opcao == "q":
            break

if __name__ == "__main__":
    main()
