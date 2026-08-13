from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nasc = nasc

    def idade(self):
        hoje = datetime.now()
        idade = hoje.year - self.__nasc.year-((hoje.month, hoje.day) < (self.__nasc.month, self.__nasc.day))
        return idade
    
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nasc(self): return self.__nasc

    def __str__(self):
        return f'Nome: {self.__nome}, CPF: {self.__cpf}, Telefone {self.__telefone}, Nascimento: {self.__nasc}'
    
    def to_json(self):
            return {"nome": self.__nome, "cpf": self.__cpf, "telefone": self.__telefone, "nasc": self.__nasc}
    
    @staticmethod
    def from_json(dic):
            return Paciente(dic["nome"], dic["cpf"], dic["telefone"], dic["nasc"])    

        