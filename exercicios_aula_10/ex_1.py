class Time:
    def __init__(self,id,nome,estadofederacao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estadofederacao(estadofederacao)
    def set_id(self, id):
        if id >= 0:
            self.id = id
        else:
            raise ValueError("ID inválido")        
    def set_nome(self, nome):
        if nome != "":
            self.nome = nome
        else:
            raise ValueError("Nome inválido")
    def set_estadofederacao(self,estadofederacao):
        if estadofederacao != "":
            self.estadofederacao = estadofederacao
        else:
            raise ValueError("Estado federativo inválido")
    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_estadofederacao(self):
        return self.estadofederacao
    def __str__(self):
        return f"ID = {self.id} - Nome = {self.nome} - Estado federativo = {self.estadofederacao}"

class Jogador:
    def __init__(self,id,nome,camisa,idtime):
        self.set_id(id)
        self.set_nome(nome)
        self.set_camisa(camisa)
        self.set_idtime(idtime)
    def set_id(self, id):
        if id >= 0:
            self.id = id
        else:
            raise ValueError("ID inválido")
    def set_nome(self,nome):
        if nome != "":
            self.nome = nome
        else:
            raise ValueError("Nome inválido")
    def set_camisa(self,camisa):
        if camisa > 0:
            self.camisa = camisa
        else:
            raise ValueError("Número da camisa inválido")
    def set_idtime(self,idtime):
        if idtime >= 0:
            self.idtime = idtime
        else:
            raise ValueError("ID do time inválido")
    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_camisa(self):
        return self.camisa
    def get_idioma(self):
        return self.idioma
    def __str__(self):
        return f"ID = {self.id} - Nome = {self.nome}" 

class UI:
    times = []   # atributo de classe - é uma lista de contatos
    jogadores = []
    @staticmethod
    def main():
        op_1 = 0
        op_t = 0
        op_j = 0
        while op_1 != 5:
            op_1 = UI.menu()
            if op_1 == 1: UI.time()   # C reate
            if op_1 == 2: UI.jogador()    # R ead
            if op_1 == 3: UI.lista_jogador() # U pdate
            if op_1 == 4: UI.transferencia()   # D elete

            # op_1 = UI.menu()
            # if op_1 == 1: UI.inserir()   # C reate
            # if op_1 == 2: UI.listar()    # R ead
            # if op_1 == 3: UI.atualizar() # U pdate
            # if op_1 == 4: UI.excluir()   # D elete
            # if op_1 == 5: UI.pesquisar()
            
    @staticmethod
    def menu():
        print("1-Times      2-Jogadores     3-listar jogadores      4-Transferencia     5-Fim")
        return int(input("Escolha um opção: "))

    def menu_times():
        print("1-Inserir    2-Listar    3-Atualizar     4-Excluir       5-Fim")
        return int(input("Escolha um opção: "))

    def menu_jogadores():
        print("1-Inserir    2-Listar    3-Atualizar     4-Excluir       5-Fim")
        return int(input("Escolha um opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        x = Contato(id, nome, email, fone)
        cls.contatos.append(x)
        print("Contato inserido com sucesso")      
    @classmethod
    def listar(cls):
        if len(cls.contatos) == 0: print("Nenhum contato na agenda")
        else:
            for x in cls.contatos: print(x)    
    @classmethod
    def listar_id(cls, id):
        # procurar um contato na lista com o id informado
        for x in cls.contatos:
            if x.get_id() == id: return x
        return None    
    @classmethod
    def atualizar(cls):
        ContatoUI.listar()
        id = int(input("Informe o id do contato a ser alterado: "))
        x = ContatoUI.listar_id(id)
        if x != None:
            # remove o contato atual
            cls.contatos.remove(x)
            # insere um novo contato com os dados atualizados
            nome = input("Informe o novo nome: ")
            email = input("Informe o novo e-mail: ")
            fone = input("Informe o novo telefone: ")
            x = Contato(id, nome, email, fone)
            cls.contatos.append(x)            
    @classmethod
    def excluir(cls):
        ContatoUI.listar()
        id = int(input("Informe o id do contato a ser excluído: "))
        x = ContatoUI.listar_id(id)
        if x != None:
            # remove o contato atual
            cls.contatos.remove(x)
    @classmethod
    def pesquisar(cls):
        iniciais = input("Informe as iniciais do contato: ")
        for x in cls.contatos:
            if x.get_nome().startswith(iniciais): print(x)

ContatoUI.main()    