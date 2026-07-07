from models.servico import Servico
from models.servicodao import ServicoDao

class Service:
    @staticmethod
    def servico_inserir(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDao().inserir(obj)

    @staticmethod
    def servico_listar():
        return ServicoDao().listar()

    @staticmethod
    def servico_listar_id(id):
        return ServicoDao().listar_id(id)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDao().atualizar(obj)

    @staticmethod
    def servico_excluir(id):
        ServicoDao().excluir(id)