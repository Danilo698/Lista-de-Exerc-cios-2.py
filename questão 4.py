class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def exibir_informacoes(self):
        print(f"Número da conta: {self.numero}")
        print(f"Titular da conta: {self.titular}")
        print(f"Saldo da conta: R${self.saldo:.2f}")


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo, limite_cheque_especial):
        super().__init__(numero, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Limite do cheque especial: R${self.limite_cheque_especial:.2f}")


class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def exibir_informacoes(self):
        print(f"Número da conta: {self.numero}")
        print(f"Titular da conta: {self.titular}")
        print(f"Saldo da conta: R${self.saldo:.2f}")


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo, limite_cheque_especial):
        super().__init__(numero, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Limite do cheque especial: R${self.limite_cheque_especial:.2f}")


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo, taxa_juros):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros
        
    #EXEMPLO:
        # Criando uma Conta Corrente e uma Conta Poupança
conta_corrente = ContaCorrente(numero="12345", titular="Alice", saldo=100.0, limite_cheque_especial=500.0)
conta_poupanca = ContaPoupanca(numero="67890", titular="Bob", saldo=500.0, taxa_juros=0.01)

# Simulação de operações na Conta Corrente
print("=== Conta Corrente ===")
conta_corrente.exibir_informacoes()
conta_corrente.depositar(200)   # Depositar 200 na conta corrente
conta_corrente.sacar(50)        # Sacar 50 da conta corrente
conta_corrente.sacar(800)       # Tentar sacar um valor que excede o limite de cheque especial
conta_corrente.exibir_informacoes()

# Simulação de operações na Conta Poupança
print("\n=== Conta Poupança ===")
conta_poupanca.exibir_informacoes()
conta_poupanca.depositar(100)   # Depositar 100 na conta poupança
conta_poupanca.sacar(600)       # Tentar sacar um valor que deixa o saldo negativo (não deve ser permitido)
conta_poupanca.sacar(50)        # Sacar 50 da conta poupança
conta_poupanca.exibir_informacoes()
