import streamlit as st
import pandas as pd
from service import Service

class ListarHorariosConfirmadosHojeUI:
    @staticmethod
    def main():
        st.header("Horários Confirmados Hoje")
        horarios = Service.horario_confirmados_hoje_listar()
        
        if len(horarios) == 0:
            st.info("Nenhum horário confirmado para o dia de hoje.")
        else:
            df = pd.DataFrame(horarios)
            st.dataframe(df)