from enum import Enum

class Grupo(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10
    K = 11
    L = 12

class Fase(Enum):
    Grupo = 1
    Desesseis_avos = 2
    Oitavas = 3
    Quartas = 4
    Semi_finais = 5
    Terceiro_lugar = 6
    Finais = 7

class Pais:
    def __init__(self, nome, id, sigla, grupo):
        self.set_nome(nome)
        self.set_id(id)
        self.set_sigla(sigla)
        self.set_grupo(grupo)

    def set_nome(self, nome):
        if nome == " ": raise ValueError()
        self.__nome = nome

    def set_id(self, id):
        pass