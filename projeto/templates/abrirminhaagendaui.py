import streamlit as st
import time
from service import Service

class AbrirMinhaAgendaUI:
    @staticmethod
    def main():
        st.header("Abrir Minha Agenda")
        
        data = st.text_input("Informe a data no formato dd/mm/aaaa", "14/10/2025")
        horario_inicio = st.text_input("Informe o horário inicial no formato HH:MM", "09:00")
        horario_fim = st.text_input("Informe o horário final no formato HH:MM", "12:00")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)", "30")

        if st.button("Abrir Agenda"):
            id_prof = st.session_state["usuario_id"]
            Service.horario_abrir_minha_agenda(data, horario_inicio, horario_fim, intervalo, id_prof)
            st.success("Agenda aberta com sucesso!")
            time.sleep(1.5)
            st.rerun()