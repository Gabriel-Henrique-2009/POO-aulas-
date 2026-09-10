from datetime import datetime

class Atendimento:
    def __init__(self, id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        self.set_id(id)
        self.set_data(data)
        self.set_queixa_principal(queixa_principal)
        self.set_historico_saude(historico_saude)
        self.set_avaliacao(avaliacao)
        self.set_prescricao(prescricao)
        self.set_id_horario(id_horario)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_data(self, data):
        if data > datetime.now(): raise ValueError("data não pode ser no futuro")
        self.__data = data

    def set_queixa_principal(self, queixa_principal):
        if queixa_principal == "": raise ValueError("queixa_principal deve ser informado")
        self.__queixa_principal = queixa_principal

    def set_historico_saude(self, historico_saude):
        if historico_saude == "": raise ValueError("historico_saude deve ser informado")
        self.__historico_saude = historico_saude

    def set_avaliacao(self, avaliacao):
        if avaliacao == "": raise ValueError("avaliacao deve ser informado")
        self.__avaliacao = avaliacao

    def set_prescricao(self, prescricao):
        if prescricao == "": raise ValueError("prescricao deve ser informado")
        self.__prescricao = prescricao
        
    def set_id_horario(self, id_horario):
        if id_horario < 0: raise ValueError("id_horario deve ser positivo")
        self.__id_horario = id_horario

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_queixa_principal(self): return self.__queixa_principal
    def get_historico_saude(self): return self.__historico_saude
    def get_avaliacao(self): return self.__avaliacao
    def get_prescricao(self): return self.__prescricao
    def get_id_horario(self): return self.__id_horario

    def __str__(self):
        data_str = self.__data.strftime("%d/%m/%Y %H:%M")
        return f"{self.__id} - {data_str} - {self.__queixa_principal} - {self.__historico_saude} - {self.__avaliacao} - {self.__prescricao} - {self.__id_horario}"
    
    def to_json(self):
        return { 
            "id": self.__id, 
            "data": self.__data.strftime("%d/%m/%Y %H:%M"), 
            "queixa_principal": self.__queixa_principal, 
            "historico_saude": self.__historico_saude, 
            "avaliacao": self.__avaliacao, 
            "prescricao": self.__prescricao, 
            "id_horario": self.__id_horario 
        }
    
    @staticmethod
    def from_json(dic):
        data_dt = datetime.strptime(dic["data"], "%d/%m/%Y %H:%M")
        return Atendimento(dic["id"], data_dt, dic["queixa_principal"], dic["historico_saude"], dic["avaliacao"], dic["prescricao"], dic["id_horario"])