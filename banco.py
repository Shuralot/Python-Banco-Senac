class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
    
    def verificar_saldo(self):
        return self.saldo
    
    def depositar(self, deposito):
        self.saldo += deposito

    def sacar(self, saque):
        if saque > self.saldo:
            raise ValueError("Você não tem saldo suficiente")
        self.saldo -= saque
        return self.saldo