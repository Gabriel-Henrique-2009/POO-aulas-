from datetime import datetime, timedelta

class Treino:
    def __init__(self, id, data, dist, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_dist(dist)
        self.set_tempo(tempo)

    def set_id(self, id):
        if id < 0: raise ValueError("Valor errado")
        self.__id = id

    def set_data(self, data):
        if data > datetime.now(): raise ValueError("Não pode ser vazio")
        self.__data = data

    def set_dist(self, dist):
        if dist < 0: raise ValueError("Não pode ser vazio")
        self.__dist = dist

    def set_tempo(self, tempo):
        if tempo < 0 : raise ValueError("Não pode ser negativo")
        self.__tempo = tempo

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_dist(self):
        return self.__dist

    def get_tempo(self):
        return self.__tempo
    
    def Pace(self):
        pace = self.__tempo // self.__dist()  
        return timedelta(seconds=pace)

    def __str__(self):
        return f"- id: {self.__id} -\n- data: {self.__data} -\n- distância: {self.__dist} -\n- tempo: {self.__tempo} -"
    

class TreinoUI:
    __treino = []

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.atualizar()
            if op == 4: TreinoUI.excluir()
            if op == 5: TreinoUI.pesquisar()
            if op == 6: TreinoUI.aniversariante()

    @staticmethod
    def menu():
        print(" 1 - Inserir \n 2 - Listar \n 3 - Atualizar \n 4 - Excluir \n 5 - Pesquisar \n 6 - Aniversariantes \n 9 - Fim")
        return int(input("Escolha a opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Digite o id: "))
        nome = input("Digite o nome: ")
        cpf = input("Digite o cpf: ")
        telefone = input("Digite o telefone: ")
        nascimento = datetime.strptime(input("Digite a data de nascimenbto: "), '%d/%m/%Y')

        x = Paciente(id, nome, cpf, telefone, nascimento)
        cls.__paciente.append(x)

    @classmethod
    def listar(cls):
        x = Paciente()
        for x in cls.__paciente: print(x, x.idade())

    @classmethod
    def atualizar(cls):
        id = int(input("Digite o seu id: "))
        for x in cls.__paciente: 
            if x.get_id() == id:
                x.set_nome(input("Digite o seu nome para atualizar: "))
                x.set_cpf(input("Digite o seu cpf para atualizar: "))
                x.set_telefone(input("Digite o seu telefone para atualizar: "))
                x.set_nacimento(datetime.strptime(input("Digite a sua data de nascimento para atualizar: "), '%d/%m/%Y'))
                print("Paciente atualizado")

    @classmethod
    def excluir(cls):
        for x in cls.__paciente: print(x)
        id = int(input("Digite o id para excluir: "))
        for x in cls.__paciente: 
            if x.get_id() == id:
                cls.__paciente.remove(x)
    
    @classmethod
    def pesquisar(cls):
        s = int(input("Informa as iniciais do nome: "))
        for x in cls.__paciente: 
            if x.get_nome().startswith(s): print(x)
    
    @classmethod
    def aniversariante(cls):
        m = int(input("Digite o o mes que voce nasceu: "))
        for x in cls.__paciente: 
            if x.get_nascimento().month == m: print(x)

PacienteUI.main()





    