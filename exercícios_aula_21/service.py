from models.cliente import Cliente
from models.clientedao import ClienteDao
from models.servico import Servico
from models.servicodao import ServicoDao
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDao

class Service:
    @staticmethod
    def cliente_inserir(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDao().inserir(obj)

    @staticmethod
    def cliente_listar():
        return ClienteDao().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDao().listar_id(id)

    @staticmethod
    def cliente_listar_nome(iniciais):
        return ClienteDao().listar_nome(iniciais)
    
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDao().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDao().excluir(id)

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
    def servico_listar_descricao(iniciais):
        return ServicoDao().listar_descricao(iniciais)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDao().atualizar(obj)

    @staticmethod
    def servico_excluir(id):
        ServicoDao().excluir(id)

    @staticmethod
    def profissional_inserir(id, nome, email, senha, especialidade):
        obj = Profissional(id, nome, email, senha, especialidade)
        ProfissionalDao().inserir(obj)

    @staticmethod
    def profissional_listar():
        return ProfissionalDao().listar()

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDao().listar_id(id)

    @staticmethod
    def profissional_listar_nome(iniciais):
        return ProfissionalDao().listar_nome(iniciais)

    @staticmethod
    def profissional_atualizar(id, nome, email, senha, especialidade):
        obj = Profissional(id, nome, email, senha, especialidade)
        ProfissionalDao().atualizar(obj)

    @staticmethod
    def profissional_excluir(id):
        ProfissionalDao().excluir(id)