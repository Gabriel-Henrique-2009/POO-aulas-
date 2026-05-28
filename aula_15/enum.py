import enum
from datetime import datetime

class Pagamento (enum.Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor(valor)
        self.__data_pagamento = None
        self.__valor_pago = 0
        self.__situacao_pagamento = Pagamento.EM_ABERTO

    def set_cod_barras(self, cod):
        if len(cod) != 10: raise ValueError("O código deve ter 10 dígitos")
        self.__cod_barras = cod

    def set_data_emissao (self, emissao):
        if emissao > datetime.now(): raise ValueError("Data não pode ser no futuro")
        self.__data_emissao = emissao

    def set_data_vencimento (self, venc):
        if venc < datetime.now(): raise ValueError("Data não pode ser no passado")
        self.__data_vencimento = venc

    def set_valor (self, valor):
        if valor < 0: raise ValueError("Boleto não pode ter valor negativo")
        self.__valor_boleto = valor

    def pagar (self, valor_pago):
        if valor_pago < 0: raise ValueError("Valor pago não pode ter o valor negativo")
        if self.__situacao_pagamento != Pagamento.EM_ABERTO: raise ValueError("O boleto já foi pago")
        self.__valor_pago = valor_pago
        self.__data_pagamento = datetime.now()
        if self.__valor_boleto == self.__valor_pago: self.__situacao_pagamento = Pagamento.PAGO
        else: self.__situacao_pagamento = Pagamento.PAGO_PARCIAL 
    
    def get_cod_barras(self):  return self.__cod_barras

    def get_data_emissao (self): return self.__data_emissao

    def get_data_vencimento (self): return self.__data_vencimento

    def get_valor_boleto (self): return self.__valor_boleto

    def get_situacao_pagamento(self): return self.__situacao_pagamento          

    def get_valor_pago (self): return self.__valor_pago        

    def get_data_pagamento (self): return self.__data_pagamento

    def get_situacao_pagamento (self): return self.__situacao_pagamento

    def situacao(self): return self.__situacao_pagamento

    def __str__(self):
        s = f"Boleto: {self.__cod_barras} - Emissão: "
        
