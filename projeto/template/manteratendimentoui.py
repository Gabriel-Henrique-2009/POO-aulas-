import streamlit as st
import pandas as pd
import time
from datetime import datetime
from service import Service

class ManterAtendimentoUI:
    def main():
        st.header("Cadastro de Atendimentos")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterAtendimentoUI.listar()
        with tab2:
            ManterAtendimentoUI.inserir()
        with tab3:
            ManterAtendimentoUI.atualizar()
        with tab4:
            ManterAtendimentoUI.excluir()

    def listar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0:
            st.write("Nenhum atendimento cadastrado")
        else:
            list_dic = []
            for obj in atendimentos:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        data = st.text_input("Informe a data e hora (dd/mm/aaaa hh:mm)", datetime.now().strftime("%d/%m/%Y %H:%M"))
        queixa = st.text_input("Informe a queixa principal")
        historico = st.text_input("Informe o histórico de saúde")
        avaliacao = st.text_input("Informe a avaliação")
        prescricao = st.text_input("Informe a prescrição")
        id_horario = st.number_input("Informe o ID do horário", min_value=0, step=1)

        if st.button("Inserir"):
            data_dt = datetime.strptime(data, "%d/%m/%Y %H:%M")
            Service.atendimento_inserir(data_dt, queixa, historico, avaliacao, prescricao, int(id_horario))
            st.success("Atendimento inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        atendimentos = Service.atendimento_listar()

        if len(atendimentos) == 0:
            st.write("Nenhum atendimento cadastrado")
        else:
            op = st.selectbox("Atualização de Atendimentos", atendimentos)
            data = st.text_input("Nova data e hora (dd/mm/aaaa hh:mm)", op.get_data().strftime("%d/%m/%Y %H:%M"))
            queixa = st.text_input("Nova queixa principal", op.get_queixa_principal())
            historico = st.text_input("Novo histórico de saúde", op.get_historico_saude())
            avaliacao = st.text_input("Nova avaliação", op.get_avaliacao())
            prescricao = st.text_input("Nova prescrição", op.get_prescricao())
            id_horario = st.number_input("Novo ID do horário", value=op.get_id_horario(), min_value=0, step=1)

            if st.button("Atualizar"):
                id_ = op.get_id()
                data_dt = datetime.strptime(data, "%d/%m/%Y %H:%M")
                Service.atendimento_atualizar(id_, data_dt, queixa, historico, avaliacao, prescricao, int(id_horario))
                st.success("Atendimento atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        atendimentos = Service.atendimento_listar()

        if len(atendimentos) == 0:
            st.write("Nenhum atendimento cadastrado")
        else:
            op = st.selectbox("Exclusão de Atendimentos", atendimentos)

            if st.button("Excluir"):
                id_ = op.get_id()
                Service.atendimento_excluir(id_)
                st.success("Atendimento excluído com sucesso")
                time.sleep(2)
                st.rerun()