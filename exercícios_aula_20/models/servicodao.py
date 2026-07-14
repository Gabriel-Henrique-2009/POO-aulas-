from models.servico import Servico
import json

class ServicoDao:
    def __init__(self):
        self.__arquivo = "servicos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        novo_id = 1
        if len(self.__objetos) > 0:
            novo_id = max(x.get_id() for x in self.__objetos) + 1
        obj.set_id(novo_id)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id: return obj
        return None

    def listar_descricao(self, iniciais):
        resultado = []
        for obj in self.__objetos:
            if obj.get_descricao().lower().startswith(iniciais.lower()):
                resultado.append(obj)
        return resultado

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
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
                obj = Servico.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError:
            pass

    def __salvar(self):
        arquivo = open(self.__arquivo, mode="w")
        json.dump(self.__objetos, arquivo, default=Servico.to_json, indent=2)
        arquivo.close()