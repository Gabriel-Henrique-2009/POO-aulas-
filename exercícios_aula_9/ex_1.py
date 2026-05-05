class Bingo:
    def __init__(self, num_bolas):
        self.set_num_bolas(num_bolas)
        self.set_bolas()

    def set_num_bolas(self, b):
        if b >= 0: self.__num_bolas = b
        else: raise ValueError()

    def set_bolas(self, b):
        if b >= 0: self.__bolas = b
        else: raise ValueError()

    def get_num_bolas(self): return self.__num_bolas
    def get_bolas(self): return self.__bolas

class BingoUI:

    @staticmethod
    def main():
        op = 0 
        while op != 3:
            op = BingoUI.menu()
            if op == 1: BingoUI.iniciar_jogo()
            if op == 2: BingoUI.sortear()
            if op == 3: BingoUI.sorteados()

    @staticmethod
    def menu():
        print("1-Iniciar Jogo")
        print("2-Sortear")
        print("3-Sorteados")
        return int(input("Escolha uma opção: "))
    
    @classmethod 
    def iniciar_jogo(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        x = Bingo(id, nome, email, fone)
        cls.contatos.append(x)
        print("Contato inserido com sucesso")   

BingoUI.main()   