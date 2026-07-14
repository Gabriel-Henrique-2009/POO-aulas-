from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_listar_nome()
            if op == 4: UI.cliente_atualizar()
            if op == 5: UI.cliente_excluir()
            if op == 6: UI.servico_inserir()
            if op == 7: UI.servico_listar()
            if op == 8: UI.servico_listar_descricao()
            if op == 9: UI.servico_atualizar()
            if op == 10: UI.servico_excluir()
        
    @staticmethod
    def menu():
        print("1 - Inserir Cliente, 2 - Listar Clientes, 3 - Pesquisar Cliente por Nome, 4 - Atualizar Cliente, 5 - Excluir Cliente")
        print("6 - Inserir Serviço, 7 - Listar Serviços, 8 - Pesquisar Serviço por Descrição, 9 - Atualizar Serviço, 10 - Excluir Serviço")
        print("11 - Sair")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        nome = input("nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(0, nome, email, fone)

    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar(): print(obj)

    @staticmethod
    def cliente_listar_nome():
        iniciais = input("Informe as iniciais do nome para pesquisar: ")
        for obj in Service.cliente_listar_nome(iniciais): print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    @staticmethod
    def servico_inserir():
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        Service.servico_inserir(0, descricao, valor)

    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar(): print(obj)

    @staticmethod
    def servico_listar_descricao():
        iniciais = input("Informe as iniciais da descrição para pesquisar: ")
        for obj in Service.servico_listar_descricao(iniciais): print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service.servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        valor = float(input("Informe o novo valor: "))
        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service.servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser excluído: "))
        Service.servico_excluir(id)

UI.main()