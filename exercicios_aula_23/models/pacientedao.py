from models.paciente import Paciente
import json

class PacienteDao:
    def __init__(self):
        self.__arquivo = "servicos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_cpf(self, cpf):
        for obj in self.__objetos:
            if obj.get_cpf() == cpf: return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_cpf(obj.get_cpf())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, cpf):
        aux = self.listar_cpf(cpf)
        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode="r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self.__objetos = []
            for dic in list_dic:
                obj = Paciente.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError:
            pass

    def __salvar(self):
        arquivo = open(self.__arquivo, mode="w")
        json.dump(self.__objetos, arquivo, default=Paciente.to_json, indent=2)
        arquivo.close()