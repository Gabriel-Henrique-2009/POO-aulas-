import streamlit as st
import pandas as pd
from service import Service

class VisualizarMinhaAgendaUI:
    @staticmethod
    def main():
        st.header("Minha Agenda")
        id_prof = st.session_state["usuario_id"]
        agenda = Service.horario_listar_agenda_profissional(id_prof)
        
        if not agenda:
            st.info("Nenhum horário cadastrado na sua agenda.")
        else:
            df = pd.DataFrame(agenda)
            st.dataframe(df, use_container_width=True)