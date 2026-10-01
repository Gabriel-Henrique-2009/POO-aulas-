import streamlit as st
import time
from service import Service

class ConfirmarServicoUI:
    @staticmethod
    def main():
        st.header("Confirmar Serviço")
        id_prof = st.session_state["usuario_id"]
        pendentes = Service.horario_listar_pendentes_profissional(id_prof)

        if not pendentes:
            st.info("Não há serviços pendentes de confirmação.")
        else:
            dict_opcoes = {}
            for h in pendentes:
                cli = Service.cliente_listar_id(h.get_id_cliente())
                info_cli = f"{cli.get_id()} - {cli.get_nome()} - {cli.get_email()}" if cli else "Desconhecido"
                label = f"{h.get_id()} - {h.get_data()} - {h.get_confirmado()} ({info_cli})"
                dict_opcoes[label] = h.get_id()

            selecionado = st.selectbox("Informe o horário", list(dict_opcoes.keys()))

            if st.button("Confirmar"):
                id_horario = dict_opcoes[selecionado]
                Service.horario_confirmar(id_horario)
                st.success("Serviço confirmado com sucesso!")
                time.sleep(1.5)
                st.rerun()