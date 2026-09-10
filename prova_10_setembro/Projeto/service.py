from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.convenio import Convenio
from models.conveniodao import ConvenioDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        obj = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)




    def convenio_inserir(nome, contato, fone):
        obj = Convenio(0, nome, contato, fone)
        ConvenioDAO().inserir(obj)
    @staticmethod
    def convenio_listar():
        return ConvenioDAO().listar()
    @staticmethod
    def convenio_listar_id(id):
        return ConvenioDAO().listar_id(id)
    @staticmethod
    def convenio_atualizar(id, nome, contato, fone):
        obj = Convenio(id, nome, contato, fone)
        ConvenioDAO().atualizar(obj)
    @staticmethod
    def convenio_excluir(id):
        ConvenioDAO().excluir(id)





    