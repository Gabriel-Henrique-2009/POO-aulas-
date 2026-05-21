from datetime import datetime

class Paciente:
    def __init__(self, id, nome, cpf, t, n):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(t)
        self.set_nascimento(n)

    def set_id(self, id):
        if id < 0: raise ValueError("Valor errado")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("Não pode ser vazio")
        self.__nome = nome

    def set_cpf(self, cpf):
        if cpf == "": raise ValueError("Não pode ser vazio")
        self.__cpf = cpf

    def set_telefone(self, t):
        if t == "": raise ValueError("Não pode ser vazio")
        self.__telefone = t

    def set_nascimento(self, n):
        if n > datetime.now() : raise ValueError("Não pode ter nascido no futuro")
        self.__nascimento = n

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def get_nascimento(self):
        return self.__nascimento
    
    def __str__(self):
        return f"- id: {self.__id} -\n- nome: {self.__nome} -\n- cpf: {self.__cpf} -\n- telefone: {self.__telefone} -\n- data de nascimento: {self.__nascimento.strftime('%d/%m/%Y')} -"
    
    def idade(self):
        tempo = datetime.now() - self.__nascimento
        ano = tempo.days // 365
        meses = tempo.days % 365 // 30
        dia = tempo.days % 365 % 30    
        return f"- idade: {ano} -\n- meses: {meses} -\n- dia: {dia} -"

# x = Paciente(1, "Eduardo", "001.002.003.45", "84 1234-5678", datetime(2010, 1, 25))
# print(x)
# print(x.idade())

class PacienteUI:
    __paciente = []

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.atualizar()
            if op == 4: PacienteUI.excluir()
            if op == 5: PacienteUI.pesquisar()
            if op == 6: PacienteUI.aniversariante()

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

PacienteUI.main()





    