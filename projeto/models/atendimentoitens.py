class Atendimento:
    def __init__(self, id, id_atendimento, id_servico, qtd, valor):
        self.set_id(id)
        self.set_id_atendimento(id_atendimento)
        self.set_id_servico(id_servico)
        self.set_qtd(qtd)
        self.set_valor(valor)

    def __str__(self):
        return f"{self.__id} - {self.__id_atendimento} - {self.__id_servico}"

    def get_id(self): return self.__id
    def get_id_atendimento(self): return self.__id_atendimento
    def get_id_servico(self): return self.__id_servico
    def get_qtd(self): return self.__qtd
    def get_valor(self): return self.__valor

    def set_id(self, id): self.__id = id
    def set_id_atendimento(self, id_atendimento): self.__id_atendimento = id_atendimento
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_qtd(self, qtd): self.__qtd = qtd 
    def set_valor(self, valor): self.__valor = valor 

    def to_json(self):
        dic = {"id":self.__id, "id_atendimento":self.__id_atendimento, \
            "id_servico":self.__id_servico, "qtd":self.__qtd,   \
            "valor":self.__valor}
        return dic

    @staticmethod
    def from_json(dic):
        return Atendimento(dic["id"], dic["id_atendimento"], dic["id_servico"],\
                           dic["qtd"], dic["valor"])