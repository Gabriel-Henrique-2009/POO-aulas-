class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def set_estado(self, estado):
        self.estado = estado

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_estado(self):
        return self.estado

    def __str__(self):
        return f"ID: {self.id} - Time: {self.nome} - UF: {self.estado}"

class Jogador:
    def __init__(self, id, idTime, nome, camisa):
        self.set_id(id)
        self.set_idTime(idTime)
        self.set_nome(nome)
        self.set_camisa(camisa)

    def set_id(self, id):
        self.id = id

    def set_idTime(self, idTime):
        self.idTime = idTime

    def set_nome(self, nome):
        self.nome = nome

    def set_camisa(self, camisa):
        self.camisa = camisa

    def get_id(self):
        return self.id

    def get_idTime(self):
        return self.idTime

    def get_nome(self):
        return self.nome

    def get_camisa(self):
        return self.camisa

    def __str__(self):
        return f"ID: {self.id} - Nome: {self.nome} - N°: {self.camisa} - Time ID: {self.idTime}"

class UI:
    times = []
    jogadores = []

    @classmethod
    def main(cls):
        op = 0
        while op != 10:
            op = cls.menu()
            if op == 1: cls.inserir_time()
            if op == 2: cls.listar_time()
            if op == 3: cls.atualizar_time()
            if op == 4: cls.excluir_time()
            if op == 5: cls.inserir_jogador()
            if op == 6: cls.listar_jogador()
            if op == 7: cls.atualizar_jogador()
            if op == 8: cls.excluir_jogador()
            if op == 9: cls.listar_jogadores_do_time()
            if op == 10: cls.transferir_jogador()

    @staticmethod
    def menu():
        print("1-Inserir Time")
        print("2-Listar Times")
        print("3-Atualizar Time")
        print("4-Excluir Time")
        print("5-Inserir Jogador")
        print("6-Listar Jogadores")
        print("7-Atualizar Jogador")
        print("8-Excluir Jogador")
        print("9-Listar Jogadores de um Time")
        print("10-Transferir Jogador")
        print("11-Sair")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir_time(cls):
        id = int(input("ID do time: "))
        nome = input("Nome do time: ")
        estado = input("Estado (UF): ")
        cls.times.append(Time(id, nome, estado))

    @classmethod
    def listar_time(cls):
        for t in cls.times: print(t)

    @classmethod
    def atualizar_time(cls):
        id = int(input("ID do time para atualizar: "))
        for t in cls.times:
            if t.get_id() == id:
                t.set_nome(input("Novo nome: "))
                t.set_estado(input("Novo estado: "))

    @classmethod
    def excluir_time(cls):
        id = int(input("ID do time para excluir: "))
        cls.times = [t for t in cls.times if t.get_id() != id]

    @classmethod
    def inserir_jogador(cls):
        id = int(input("ID do jogador: "))
        id_t = int(input("ID do time: "))
        nome = input("Nome do jogador: ")
        camisa = int(input("Número da camisa: "))
        cls.jogadores.append(Jogador(id, id_t, nome, camisa))

    @classmethod
    def listar_jogador(cls):
        for j in cls.jogadores: print(j)

    @classmethod
    def atualizar_jogador(cls):
        id = int(input("ID do jogador para atualizar: "))
        for j in cls.jogadores:
            if j.get_id() == id:
                j.set_nome(input("Novo nome: "))
                j.set_camisa(int(input("Nova camisa: ")))

    @classmethod
    def excluir_jogador(cls):
        id = int(input("ID do jogador para excluir: "))
        cls.jogadores = [j for j in cls.jogadores if j.get_id() != id]

    @classmethod
    def listar_jogadores_do_time(cls):
        id_t = int(input("ID do time para listar jogadores: "))
        for j in cls.jogadores:
            if j.get_idTime() == id_t: print(j)

    @classmethod
    def transferir_jogador(cls):
        id_j = int(input("ID do jogador a transferir: "))
        novo_id_t = int(input("ID do novo time: "))
        for j in cls.jogadores:
            if j.get_id() == id_j:
                j.set_idTime(novo_id_t)

UI.main()