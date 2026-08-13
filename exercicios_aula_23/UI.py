from service import Service
import streamlit as st

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
        st.header('Paciente Cadastro')
        st.write("1 - Inserir Serviço, 2 - Listar Serviços, 3 - Atualizar Serviço, 4 - Excluir Serviço, 5 - Sair")
        return st.number_input("Informe uma opção: ")

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
# from datetime import datetime
# import streamlit as st
# from exercicios_aula_23.models.paciente import Paciente

# class UI:
#     def main():
#         st.header('Paciente Cadastro')
#         nome = st.text_input("Nome: ")
#         cpf = st.text_input("CPF: ")
#         telefone = st.text_input("Telefone: ")
#         nasc = st.text_input("Nascimento: ")
        
#         if st.button('Calcular'):
#             r = Paciente(str(nome), str(cpf), str(telefone), datetime.strptime(nasc, "%d/%m/%Y"))
#             st.write(r)
#             st.write(f'Idade: {r.idade()} anos')