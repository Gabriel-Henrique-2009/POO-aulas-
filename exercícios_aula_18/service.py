from models.cliente import Cliente
from models.clientedao import ClienteDao
class Service:
    @staticmethod
    def cliente_inserir(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDao().inserir(obj)

    @staticmethod
    def cliente_listar():
        return ClienteDao().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDao().listar_id(id)
    
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDao().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDao().excluir(id)
    