from models.horario import Horario
from models.horariodao import HorarioDAO

class Service:
    __horario_dao = HorarioDAO()

    @classmethod
    def cliente_listar(cls):
        return []

    @classmethod
    def cliente_listar_id(cls, id):
        return None

    @classmethod
    def servico_listar(cls):
        return []

    @classmethod
    def servico_listar_id(cls, id):
        return None

    @classmethod
    def servico_inserir(cls, descr, valor):
        pass

    @classmethod
    def servico_atualizar(cls, id, descr, valor):
        pass

    @classmethod
    def servico_excluir(cls, id):
        pass

    @classmethod
    def profissional_listar(cls):
        return []

    @classmethod
    def profissional_inserir(cls, nome, email, especialidade):
        pass

    @classmethod
    def profissional_atualizar(cls, id, nome, email, especialidade):
        pass

    @classmethod
    def profissional_excluir(cls, id):
        pass

    @classmethod
    def horario_inserir(cls, data, confirmado, id_cliente, id_servico):
        obj = Horario(0, data)
        obj.set_confirmado(confirmado)
        if id_cliente != None: obj.set_id_cliente(id_cliente)
        if id_servico != None: obj.set_id_servico(id_servico)
        cls.__horario_dao.inserir(obj)

    @classmethod
    def horario_listar(cls):
        return cls.__horario_dao.listar()

    @classmethod
    def horario_listar_id(cls, id):
        return cls.__horario_dao.listar_id(id)

    @classmethod
    def horario_atualizar(cls, id, data, confirmado, id_cliente, id_servico):
        obj = Horario(id, data)
        obj.set_confirmado(confirmado)
        if id_cliente != None: obj.set_id_cliente(id_cliente)
        if id_servico != None: obj.set_id_servico(id_servico)
        cls.__horario_dao.atualizar(obj)

    @classmethod
    def horario_excluir(cls, id):
        cls.__horario_dao.excluir(id)

    # Métodos de Atendimento (redirecionados ou stubs)
    @classmethod
    def atendimento_listar(cls):
        return []

    @classmethod
    def atendimento_inserir(cls, data, queixa, historico, avaliacao, prescricao, id_horario):
        pass

    @classmethod
    def atendimento_atualizar(cls, id, data, queixa, historico, avaliacao, prescricao, id_horario):
        pass

    @classmethod
    def atendimento_excluir(cls, id):
        pass