from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO

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

    @staticmethod
    def profissional_inserir(nome, email, especialidade):
        obj = Profissional(0, nome, email, especialidade)
        ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar():
        return ProfissionalDAO().listar()
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade):
        obj = Profissional(id, nome, email, especialidade)
        ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)
