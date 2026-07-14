from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.servico_inserir()
            if op == 2: UI.servico_listar()
            if op == 3: UI.servico_atualizar()
            if op == 4: UI.servico_excluir()
        
    @staticmethod
    def menu():
        print("1 - Inserir Serviço, 2 - Listar Serviços, 3 - Atualizar Serviço, 4 - Excluir Serviço, 5 - Sair")
        return int(input("Informe uma opção: "))

    @staticmethod
    def servico_inserir():
        id = int(input("id: "))
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        Service.servico_inserir(id, descricao, valor)

    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar(): print(obj)

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