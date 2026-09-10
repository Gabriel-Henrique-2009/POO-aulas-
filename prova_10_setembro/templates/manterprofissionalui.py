import streamlit as st
import pandas as pd
import time
from service import Service


class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionais")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterProfissionalUI.listar()
        with tab2:
            ManterProfissionalUI.inserir()
        with tab3:
            ManterProfissionalUI.atualizar()
        with tab4:
            ManterProfissionalUI.excluir()

    def listar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome", key="prof_ins_nome")
        email = st.text_input("Informe o e-mail", key="prof_ins_email")
        especialidade = st.text_input("Informe a especialidade", key="prof_ins_especialidade")

        if st.button("Inserir", key="btn_prof_inserir"):
            Service.profissional_inserir(nome, email, especialidade)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissionais = Service.profissional_listar()

        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", profissionais, key="sb_prof_atu")
            nome = st.text_input("Novo nome", op.get_nome(), key="prof_atu_nome")
            email = st.text_input("Novo e-mail", op.get_email(), key="prof_atu_email")
            especialidade = st.text_input("Nova especialidade", op.get_especialidade(), key="prof_atu_especialidade")

            if st.button("Atualizar", key="btn_prof_atualizar"):
                id_ = op.get_id()
                Service.profissional_atualizar(id_, nome, email, especialidade)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        profissionais = Service.profissional_listar()

        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionais", profissionais, key="sb_prof_exc")

            if st.button("Excluir", key="btn_prof_excluir"):
                id_ = op.get_id()
                Service.profissional_excluir(id_)
                st.success("Profissional excluído com sucesso")
                time.sleep(2)
                st.rerun()