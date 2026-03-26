# métodos para realizar as operações de saque.
class dados_conta:
    def __init__(self, nome, n_da_cnta, dinheiro_em_cnta):
        self.titular = nome
        self.conta = n_da_cnta
        self.saldo = dinheiro_em_cnta

    def deposito(self, valor):
        self.saldo += valor
        print(f"sua conta tem o valor de {self.saldo:.2f} reais. Ela pertence a conta de número {self.conta} cujo titular é {self.titular}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"sua conta tem o valor de {self.saldo:.2f} reais. Ela pertence ao número {self.conta} cujo titular é {self.titular}")
        
        else:
            print("o dinheiro não deu")
        
d = dados_conta('Gabriel', 20251011110038, 2000)
d.deposito(2000)
print(d.deposito)
d.saque(300)
print(d.saque)
    

        