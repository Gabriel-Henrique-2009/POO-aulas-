from models.paciente import Paciente
from models.pacientedao import PacienteDao

class Service:
    @staticmethod
    def servico_inserir(nome, cpf, telefone, nasc):
        obj = Paciente(nome, cpf, telefone, nasc)
        PacienteDao().inserir(obj)

    @staticmethod
    def servico_listar():
        return PacienteDao().listar()

    @staticmethod
    def servico_listar_cpf(cpf):
        return PacienteDao().listar_cpf(cpf)

    @staticmethod
    def servico_atualizar(nome, cpf, telefone, nasc):
        obj = Paciente(nome, cpf, telefone, nasc)
        PacienteDao().atualizar(obj)

    @staticmethod
    def servico_excluir(cpf):
        PacienteDao().excluir(cpf)