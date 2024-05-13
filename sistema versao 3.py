class Cliente:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def mostrar_historico(self):
        for transacao in self.transacoes:
            print(transacao)


class Conta:
    numero_conta_sequencial = 1000

    def __init__(self, agencia, cliente):
        self.numero = Conta.numero_conta_sequencial
        Conta.numero_conta_sequencial += 1
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0.0
        self.historico = Historico()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(f"Depósito: R${valor:.2f}")
            print("Depósito realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque: R${valor:.2f}")
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def mostrar_extrato(self):
        print("\n======= EXTRATO =======")
        self.historico.mostrar_historico()
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("========================")


class ContaCorrente(Conta):
    def __init__(self, agencia, cliente, limite):
        super().__init__(agencia, cliente)
        self.limite = limite


# Simulação do sistema bancário
clientes = []
contas = []

def criar_cliente():
    nome = input("Informe o nome do cliente: ")
    cpf = input("Informe o CPF do cliente: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço: ")
    cliente = Cliente(cpf, nome, data_nascimento, endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso.")
    return cliente

def criar_conta_corrente():
    cpf = input("Informe o CPF do cliente para criar a conta: ")
    cliente = next((cliente for cliente in clientes if cliente.cpf == cpf), None)
    if cliente:
        limite = float(input("Informe o limite de crédito para a conta corrente: "))
        conta = ContaCorrente('0001', cliente, limite)
        contas.append(conta)
        print(f"Conta corrente criada com sucesso. Número da conta: {conta.numero}")
    else:
        print("Cliente não encontrado.")

def listar_contas():
    if contas:
        for conta in contas:
            print(f"Conta Número: {conta.numero}, Titular: {conta.cliente.nome}, Saldo: R${conta.saldo:.2f}")
    else:
        print("Nenhuma conta cadastrada.")

def depositar_em_conta():
    numero = int(input("Informe o número da conta para depósito: "))
    conta = next((conta for conta in contas if conta.numero == numero), None)
    if conta:
        valor = float(input("Informe o valor a depositar: "))
        conta.depositar(valor)
    else:
        print("Conta não encontrada.")

def sacar_de_conta():
    numero = int(input("Informe o número da conta para saque: "))
    conta = next((conta for conta in contas if conta.numero == numero), None)
    if conta:
        valor = float(input("Informe o valor a sacar: "))
        conta.sacar(valor)
    else:
        print("Conta não encontrada.")

def mostrar_extrato_conta():
    numero = int(input("Informe o número da conta para ver o extrato: "))
    conta = next((conta for conta in contas if conta.numero == numero), None)
    if conta:
        conta.mostrar_extrato()
    else:
        print("Conta não encontrada.")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Criar Cliente")
        print("2 - Criar Conta Corrente")
        print("3 - Listar Contas")
        print("4 - Depositar em Conta")
        print("5 - Sacar de Conta")
        print("6 - Mostrar Extrato")
        print("7 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_cliente()
        elif opcao == '2':
            criar_conta_corrente()
        elif opcao == '3':
            listar_contas()
        elif opcao == '4':
            depositar_em_conta()
        elif opcao == '5':
            sacar_de_conta()
        elif opcao == '6':
            mostrar_extrato_conta()
        elif opcao == '7':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida, por favor tente novamente.")

if __name__ == "__main__":
    menu()
